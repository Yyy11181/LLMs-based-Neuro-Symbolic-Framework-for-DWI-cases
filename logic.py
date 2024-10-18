import torch.nn as nn
import torch
import re



class Rule(nn.Module):
    def __init__(self,config):
        super(Rule, self).__init__()
        self.config = config
        # self.weights = nn.Parameter(torch.zeros(1, 2))  # 初始化权重为0，sigmoid后为0.5的权重,每个规则的权重,会随着模型参数进行更新
        self.rule_usage_count = torch.zeros(2)  # 初始化规则使用次数计数器 这个不是要更新的
        self.one_tensor = torch.tensor([1]) #不起诉
        # self.zero_tensor = torch.tensor([0]) #起诉
        self.loss_fn = torch.nn.CrossEntropyLoss()
    
    def calculate_loss(self, logits, target_tensor):
        
        return self.loss_fn(logits.unsqueeze(0), target_tensor)

    def reset_rule_usage(self):
        """重置规则使用情况统计"""
        self.rule_usage_count.zero_()
 
 
    def forward(self,result,fact_element,fact):
        loss = 0.0
        count = 0
        for i in range(len(fact_element)):
            device = result.device
            one_tensor = self.one_tensor.to(device)
            # zero_tensor = self.zero_tensor.to(device)
            tools = fact_element[i].get('驾驶类型')["值"]
            #从fact中提取酒精含量
            pattern_jiu = r'(\d+)\s*mg\s*/\s*100\s*ml|(\d+)\s*毫克\s*/\s*100\s*毫升'
            match = re.search(pattern_jiu, fact[i])
            mg_pattern = r"(\d+\.\d+|\d+)(mg/ml)"

            if match:
                if match.group(1):  # 如果匹配的是 mg/ml 格式
                    alcohol_content_value = float(match.group(1))
                elif match.group(2):  # 如果匹配的是 毫克/毫升 格式
                    alcohol_content_value =  float(match.group(2))
            else:
                alcohol_content = fact_element[i]["酒精含量"]["值"]
                mg_ml = re.search(r'(\d+)\s*mg\s*/\s*100\s*ml', alcohol_content)
                match_mg = re.search(mg_pattern, alcohol_content, re.IGNORECASE)
                if match_mg:
                    alcohol_content_value = float(match_mg.group(1))*100
                if mg_ml:
                    alcohol_content_value = float(mg_ml.group(1))

            bx = fact_element[i]["认罪悔罪"]["是否"]=="是"  #认罪悔罪
            #8种从重情节
            fx =  fact_element[i]["从重情节1"]["是否"]=="否" #轻伤及以上后果
            gx =  fact_element[i]["从重情节2"]["是否"]=="否" 
            hx = fact_element[i]["从重情节3"]["是否"]=="否"
            Ix =  fact_element[i]["从重情节4"]["是否"]=="否"
            jx =  fact_element[i]["从重情节5"]["是否"]=="否"
            kx = fact_element[i]["从重情节6"]["是否"]=="否"
            lx = fact_element[i]["从重情节7"]["是否"]=="否"
            mx = fact_element[i]["从重情节8"]["是否"]=="否"
            #torch.sigmoid(self.weights[0,0]) *  这个是规则前面的系数
            # if tools == '汽车':
            #     if alcohol_content_value <= 170 and bx and fx and gx and hx and Ix and jx and kx and lx and mx:
            #         loss +=  self.calculate_loss(result[i], one_tensor)
            #         count += 1
            #         self.rule_usage_count[0] += 1
            if tools == '摩托车':
                if alcohol_content_value <= 200 and fx and bx:
                    loss +=  self.calculate_loss(result[i], one_tensor)
                    count += 1
                    self.rule_usage_count[1] += 1
            
        if count > 0:
            loss /= count
        
        return loss