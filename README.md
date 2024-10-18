We propose a neuro-symbolic legal judgment prediction framework based on large language models (LLMs) for civil cases. Our framework possesses a certain degree of flexibility, enabling it to be applicable in other legal domains and adaptable to a broader range of legal cases.
## Additional Experiment in other legal domain task

## Content
- [Objective of the experiment]
- [Dataset and experimental details]
- [The FOL rules]
- [Results analysis]



## Objective of the experiment
To validate the scalability of our proposed framework, we apply it to the prosecution phase of drunk driving cases, aiming to assist prosecutors in identifying offenses related to dangerous driving due to intoxication. Therefore, based on the fact descriptions of the drunk driving cases, we utilize this framework to automatically predict whether a public prosecution should be initiated against the suspect.
## Dataset and experimental details
We construct a new drunk driving cases dataset in Zhejiang Province, China, which contains a total of 4886 entries. All personal information in the dataset has been replaced with special characters. The proportions of the training set, validation set, and test set are 0.8:0.1:0.1, respectively. The statistics of the dataset are shown in Table1.
#### Table1 Statistics of the Drunk Driving Cases Dataset
| Item                              | Total |
|-----------------------------------|-------|
| Training Set Cases                | 3908  |
| Validation Set Cases              | 489   |
| Test Set Cases                    | 489   |
| Non-prosecution                   | 3536  |
| Prosecution                       | 1350  |
| Average Length of Fact Description | 172   |

To better align with the characteristics of the current task, we simplify the DNNs module in our proposed framework. Specifically, we use an LSTM to encode the fact descriptions, followed by a fully connected layer to predict whether a case should proceed to prosecution. The maximum length for fact descriptions is set to 200, with a hidden layer dimension of 50. Additionally, when extracting fact elements using LLMs, we employed the latest [GPT-4o model ](https://openai.com/index/hello-gpt-4o/) from OpenAI, with other parameter settings kept consistent with those used in private lending cases.


