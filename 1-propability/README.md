# Probability Calculation using Bayes' Rule

This Python script calculates the probability that a student is absent given that today is Friday using Bayes' Rule.

## Problem Statement

The problem states that the probability that it is Friday and that a student is absent is 3%. Since there are 5 school days in a week, the probability that it is Friday is 20%. We need to find the probability that a student is absent given that today is Friday.

## Bayes' Rule Application

Bayes' Rule states that the probability of an event A given that event B has occurred is calculated as:
```css
P(A/B) = (P(B/A) * P(A)) / P(B)
```
where:
- P(A/B) is the probability of A given B
- P(B/A) is the probability of B given A
- P(A) is the probability of A
- P(B) is the probability of B

In this problem:
- A: Student is absent
- B: Today is Friday

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