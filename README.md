We propose a neuro-symbolic legal judgment prediction framework based on large language models (LLMs) for civil cases. Our framework possesses a certain degree of flexibility, enabling it to be applicable in other legal domains and adaptable to a broader range of legal cases.
## Additional Experiment in other legal domain task

## Content
- [Objective of the Experiment](#objective-of-the-experiment)
- [Dataset and Experimental Details](#dataset-and-experimental-details)
- [The FOL Rules](#the-fol-rules)
- [Results Analysis](#results-analysis)

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

## The FOL rules
In the drunk driving cases, we design two FOL rules in the logic module. These rules are based on the [Meeting Minutes on Several Issues Regarding the Handling of Drunk Driving Cases (2019) from Zhejiang Province] (http://www.fyjc.gov.cn/articleview.do?art\_id=939). Also, we have listed the relevant variable expressions in Table2 that will be used in the FOL rules.
#### Table2 Key Variables in the FOL Rules

| Notation | Details                                                                 |
|----------|-------------------------------------------------------------------------|
| \( Y \)  | Non-prosecution                                                          |
| \( A(x) \) | \( X \) drives under the influence of alcohol.                         |
| \( B(x) \) | \( X \) pleads guilty and shows remorse.                               |
| \( C(x) \) | \( X \)'s blood alcohol concentration (BAC) is below 170mg/100ml (inclusive). |
| \( D(x) \) | \( X \)'s BAC is below 200mg/100ml (inclusive).                       |
| \( E(x) \) | \( X \) drives a motorcycle under the influence of alcohol.           |
| \( N(x) \) | \( X \) does not meet any of the 8 aggravating circumstances (AC).     |
| \( F(x) \) | The AC1, \( X \) causes minor injury or more serious harm to another person. |
| \( G(x) \) | The AC2, \( X \) drives under the influence of alcohol on a highway.   |
| \( H(x) \) | The AC3, \( X \) drives a commercial motor vehicle, a medium or large motor vehicle, or drives while severely overloaded, over capacity, or speeding. |
| \( I(x) \) | The AC4, \( X \) drives without a valid license.                        |
| \( J(x) \) | The AC5, \( X \) drives a vehicle that does not meet safety standards or a vehicle that has been scrapped. |
| \( K(x) \) | The AC6, \( X \) attempts to flee or resist inspection when being stopped by authorities. |
| \( L(x) \) | The AC7, \( X \) refuses to appear in court or flees during the litigation period. |
| \( M(x) \) | The AC8, \( X \) has been prosecuted for drunk driving within the past three years or for driving under the influence within the past five years. |
