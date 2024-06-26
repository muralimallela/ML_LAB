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
   - The probability of Friday and absent:  $`P(A \cap F) = 0.03`$
   - The probability of Friday: $`P(F) = 0.20`$

2. **Calculation:**
   - Using Bayes' Rule: 
   $$P\left (\frac{A}{F} \right)= \frac{P(A \cap F)}{P(F)} = \frac{ P(A).P\left(\frac{F}{A} \right) }{P(F)} $$

3. **Result:**
   - The probability that a student is absent given that today is Friday: $`P(\frac{A}{F})`$

## Python Code

```python
# The probability that it is Friday and that a student is absent is 3%
pAF = 0.03
print("The probability that it is Friday and that a student is absent:", pAF)

# The probability that it is Friday is 20%
pF = 0.2
print("The probability that it is Friday:", pF)

# The probability that a student is absent given that today is Friday
pResult = (pAF / pF)

# Display the Result
print("The probability that a student is absent given that today is Friday:", pResult * 100, "%")

```
## Output
The output of the script will be:

```bash
The probability that it is Friday and that a student is absent: 0.03
The probability that it is Friday :  0.2
The probability that a student is absent given that today is Friday :  15.0 %

```
This output displays the calculated probabilities and the final result, indicating that the probability of a student being absent given that today is Friday is 15%.
