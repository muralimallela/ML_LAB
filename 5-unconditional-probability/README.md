# Credit-Worthiness Analysis

In this program, we are tasked with analyzing credit-worthiness based on descriptions of individuals. The input attributes include income, recreation, job, status, age-group, and home-owner. The goal is to find the unconditional probability of 'golf' and the conditional probability of 'single' given 'medRisk' in the dataset.

## Problem Description

The dataset consists of training examples that map descriptions of individuals onto high, medium, and low credit-worthiness. Each training example contains attributes representing income, recreation, job, status, age-group, and home-owner.

We need to calculate the following probabilities:
1. Unconditional probability of 'golf'.
2. Conditional probability of 'single' given 'medRisk'.

## Implementation

The Python script provided calculates the probabilities based on the given dataset.

## Usage

You can run the provided Python script `credit_analysis.py` to calculate the probabilities. Here's how to run it:

```bash
python credit_analysis.py
```
## Script Explanation
The Python script `credit_analysis.py` contains the following code:

```python
total_Records = 10
numGolfRecords = 4
unConditionalprobGolf = numGolfRecords / total_Records
print("Unconditional probability of golf:=", unConditionalprobGolf)

# conditional probability of 'single' given 'medRisk'
numMedRiskSingle = 2
numMedRisk = 3
probMedRiskSingle = numMedRiskSingle / total_Records
probMedRisk = numMedRisk / total_Records
conditionalProb = probMedRiskSingle / probMedRisk
print("Conditional probability of single given medRisk: =", conditionalProb)
```
This script calculates the unconditional probability of 'golf' and the conditional probability of 'single' given 'medRisk' based on the given dataset.

## Expected Output
Upon running the script, you will see the following output:

The unconditional probability of 'golf'.
The conditional probability of 'single' given 'medRisk'.

```html
Unconditional probability of golf: =0.4
Conditional probability of single given medRisk: = 0.6666666666666667
```
## Explanation
In the given dataset:

- The total number of records are 10.
- The number of records which contain 'golf' are 4.
- Then, the Unconditional probability of golf is calculated as follows:
  -  The number of records which contain 'golf' / total number of records
  - = 4 / 10
  -  = 0.4
- To find the Conditional probability of 'single' given 'medRisk':
  - By the definition of Bayes' rule (conditional probability), we have:
    - P(S | MR) = P(S ∩ MR) / P(MR)
  - Based on the given problem statement:
    - P(S ∩ MR) = The number of 'MedRisk' with 'Single' records / total number of Records
      - = 2 / 10 = 0.2
    - P(MR) = The number of records with 'MedRisk' / total number of Records
      - = 3 / 10 = 0.3
  - Then, the Conditional probability of 'single' given 'medRisk' is calculated as:
    - P(S | MR) = 0.2 / 0.3
    - = 0.66666
