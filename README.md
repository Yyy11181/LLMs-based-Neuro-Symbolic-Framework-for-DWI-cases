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
In the drunk driving cases, we design two FOL rules in the logic module. These rules are based on the [Meeting Minutes on Several Issues Regarding the Handling of Drunk Driving Cases (2019) from Zhejiang Province] (http://www.fyjc.gov.cn/articleview.do?art\_id=939). Also, we have listed the relevant fact elements extracted by LLMs in Table2, which will be used in the FOL rules.
#### Table2 Key Variables in the FOL Rules
| Notation  | Details                                                                 |
|-----------|-------------------------------------------------------------------------|
| Y         | Non-prosecution                                                          |
| A(x)      | X drives under the influence of alcohol.                                |
| B(x)      | X pleads guilty and shows remorse.                                      |
| C(x)      | X's blood alcohol concentration (BAC) is below 170mg/100ml (inclusive). |
| D(x)      | X's BAC is below 200mg/100ml (inclusive).                              |
| E(x)      | X drives a motorcycle under the influence of alcohol.                  |
| N(x)      | X does not meet any of the eight aggravating circumstances (AC).           |
| F(x)      | The AC1, X causes minor injury or more serious harm to another person.  |
| G(x)      | The AC2, X drives under the influence of alcohol on a highway.         |
| H(x)      | The AC3, X drives a commercial motor vehicle, a medium or large motor vehicle, or drives while severely overloaded, over capacity, or speeding. |
| I(x)      | The AC4, X drives without a valid license.                              |
| J(x)      | The AC5, X drives a vehicle that does not meet safety standards or a vehicle that has been scrapped. |
| K(x)      | The AC6, X attempts to flee or resist inspection when being stopped by authorities. |
| L(x)      | The AC7, X refuses to appear in court or flees during the litigation period. |
| M(x)      | The AC8, X has been prosecuted for drunk driving within the past three years or for driving under the influence within the past five years. |

The first judgment rule is derived from the provision on non-prosecution, which states: ``For drunk driving cases where the blood alcohol concentration (BAC) is below 170mg/100ml, the individual pleads guilty and shows remorse, and none of the following 8 aggravating circumstances apply, the offense is minor, and prosecution may be waived or criminal punishment may be exempted." Based on this provision and practical judicial experience from Chinese prosecutors, we construct the following FOL rule:

<strong>Rule 1:</strong> A(x) ∧ B(x) ∧ C(x) ∧ N(X) → Y

The second judgment rule is derived from the provision: ``For cases where the individual drives a motorcycle under the influence of alcohol, no minor injury or more serious harm is caused to another person, the individual pleads guilty and shows remorse, and the blood alcohol concentration (BAC) is below 200mg/100ml, prosecution may be waived or criminal punishment may be exempted." Similarly, based on practical judicial scenarios, we construct the following FOL rule:

<strong>Rule 2:</strong> E(x) ∧ D(x) ∧ F(x) ∧ B(x) → Y

## Results analysis
Thus, under the same experimental conditions as in private lending dispute cases, we conduct experiments on drunk driving cases. Table3 shows the relevant experimental results.
#### Table3 The Experimental Results

| Method   | Mac.P | Mac.R | Mac.F1 | Mic.F1 |
|----------|-------|-------|--------|--------|
| no_rule  | 94.60 | 93.96 | 94.27  | 95.09  |
| +rule1   | 96.58 | 94.86 | 95.66  | 96.32  |
| +rule2   | 92.03 | 91.27 | 91.63  | 92.84  |
| +all     | 97.14 | 94.83 | 95.87  | 96.52  |


According to the Table3, it can be observed that adding only rule1 results in performance improvements across all metrics compared to the model without any rules, while adding only rule2 leads to declines in all metrics. However, when both rule1 and rule2 are applied together, the model achieves the highest improvement across all metrics, with Mac.P increasing by 2.54%, Mac.R by 0.87%, Mac.F1 by 1.6%, and Mic.F1 by 1.43%. This finding is consistent with our results in private lending cases, further indicating that different rules have a complementary effect. 

Therefore, analyzing the experimental results of this drunk driving case demonstrates that our proposed framework is not limited to a specific case type; it can be adapted based on case characteristics, showing a degree of applicability and scalability.
