# Probability Calculation using Bayes' Rule

This Python script calculates the probability that a student is absent given that today is Friday using Bayes' Rule.

## Problem Statement

The problem states that the probability that it is Friday and that a student is absent is 3%. Since there are 5 school days in a week, the probability that it is Friday is 20%. We need to find the probability that a student is absent given that today is Friday.

## Problem Description

The problem statement provides the following probabilities:
- The probability that it is Friday and that a student is absent is 3%.
- The probability that it is Friday is 20%.

We need to find the probability that a student is absent given that today is Friday.

## Bayes' Rule Application

Bayes' Rule is applied as follows:
1. **Given Information:**
   - The probability of Friday and absent: p(A ∩ F) = 0.03
   - The probability of Friday: p(F) = 0.20

2. **Calculation:**
   - Using Bayes' Rule: **P(A | F) = P(A ∩ F) / P(F)**

3. **Result:**
   - The probability that a student is absent given that today is Friday: P(A | F)


## Python Code

```python
pAF = 0.03  # Probability of a student being absent
pF = 0.2    # Probability of today being Friday

# Applying Bayes' Rule to calculate the probability of a student being absent given that today is Friday
result = (pAF / pF) * 100

print("The probability is", result, "%")
```
## Output
The output of the script will be:

```bash
The probability is 15.0 %
```