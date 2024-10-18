import torch
import torch.nn as nn
import torch.nn.functional as F
import json,pickle

from model.encoder.LSTMEncoder import LSTMEncoder
from model.loss import MultiLabelSoftmaxLoss, log_square_loss,MultiClassCrossEntropyLoss
from model.ljp.Predictor import LJPPredictor
from tools.accuracy_tool import multi_label_accuracy, log_distance_accuracy_function,multi_class_accuracy
from model.logic import Rule



class LSTM(nn.Module):
    def __init__(self, config, gpu_list, *args, **params):
        super(LSTM, self).__init__()

        self.encoder = LSTMEncoder(config, gpu_list, *args, **params)
        self.fc = LJPPredictor(config, gpu_list, *args, **params)
        self.hidden_size = config.getint("model", "hidden_size")

        # self.embedding = nn.Embedding(len(json.load(open(config.get("data", "word2id"),"r",encoding = "utf-8"))),
        #                               config.getint("model", "hidden_size"))
        self.embedding = nn.Embedding(len(pickle.load(open(config.get("data", "word2id"),"rb"))),
                                      config.getint("model", "hidden_size"))
        self.criterion = {
            "zm": MultiClassCrossEntropyLoss()
        }
        self.accuracy_function = {
            "zm": multi_class_accuracy
        }
        self.Logic = Rule(config)

        self.logic_weight = torch.nn.Parameter(torch.tensor(0.5), requires_grad=True) #逻辑模块的自由裁量权 
        
    def init_multi_gpu(self, device, config, *args, **params):
        return
    
    def reset_rule_usage(self):
        """重置规则使用情况统计"""
        self.Logic.reset_rule_usage()  

    def forward(self, data, config, gpu_list, acc_result, mode):
        x = data['text']
        x = self.embedding(x)
        y, _ = self.encoder(x) #y是指pool_max
        
        result = self.fc(y) #y指pool_max
        
        DNNs_loss = self.criterion['zm'](result['zm'], data["zm"])
        
        logic_loss = self.Logic(result['zm'],data['fact_elements'],data['fact'])
        loss = DNNs_loss + torch.sigmoid(self.logic_weight) * logic_loss
        # loss = DNNs_loss
  
        if acc_result is None:
            acc_result = {"zm": None}

        for name in ["zm"]:
            acc_result[name] = self.accuracy_function[name](result[name], data[name], config, acc_result[name])

        return {"loss": loss, "acc_result": acc_result}
