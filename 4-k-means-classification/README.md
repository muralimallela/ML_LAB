# Predicting Classification using K-Means Clustering

This Python script predicts a classification for a case where VAR1 and VAR2 are given, using the result of k-means clustering with 3 centroids.

In this program, we are going to use the following data:

| VAR1  | VAR2  | CLASS |
|-------|-------|-------|
| 1.713 | 1.586 |   0   |
| 0.180 | 1.786 |   1   |
| 0.353 | 1.240 |   1   |
| 0.940 | 1.566 |   0   |
| 1.486 | 0.759 |   1   |
| 1.266 | 1.106 |   0   |
| 1.540 | 0.419 |   1   |
| 0.459 | 1.799 |   1   |
| 0.773 | 0.186 |   1   |

And, we need to apply k-means clustering with 3 means (i.e., 3 centroids). Finally, we need to predict the class for the case where `VAR1=0.906` and `VAR2=0.606`.

## Problem Description

Given the following data, which specify classifications for nine combinations of VAR1 and VAR2, we need to predict a classification for a case where VAR1=0.906 and VAR2=0.606, using the result of k-means clustering with 3 means (i.e., 3 centroids).

## Implementation

The Python script uses `scikit-learn's KMeans module` to perform k-means clustering. It takes the provided data and class labels as input, fits the KMeans model, and then predicts the classification for the given test case.

## Usage

Before running the script, make sure to install `scikit-learn` module. You can do this via pip:

```bash
pip install scikit-learn
```

You can run the provided Python script [!kmeans_classification.py](kmeans_classification.py) to predict the classification. Here's how to run it:
 ```bash
 python kmeans_classification.py
```
## Script Explanation
The Python script kmeans_classification.py contains the following code:

```python
from sklearn.cluster import KMeans
import numpy as np

# Input data
X = np.array([[1.713,1.586], [0.180,1.786], [0.353,1.240], [0.940,1.566], [1.486,0.759],
              [1.266,1.106],[1.540,0.419],[0.459,1.799],[0.773,0.186]])
y = np.array([0,1,1,0,1,0,1,1,1])

# K-means clustering with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=0).fit(X, y)

# Displaying input data
print("The input data is ")
print("VAR1 \t VAR2 \t CLASS")
for val, label in zip(X, y):
    print(val[0],"\t",val[1],"\t", label)

print("="*20)

# Getting test data from the user
print("The Test data to predict ")
VAR1 = float(input("Enter Value for VAR1: "))
VAR2 = float(input("Enter Value for VAR2: "))
test_data = [VAR1, VAR2]
print("="*20)

# Predicting the class
print("The predicted Class is:", kmeans.predict([test_data]))

```
This script performs the following steps:

1. Loads the input data and class labels.
2. Fits a KMeans model with 3 clusters to the input data.
3. Displays the input data.
4. Prompts the user to enter test data for prediction.
5. Predicts the class for the given test data using the fitted KMeans model.

## Expected Output

Upon running the script, you will see the predicted class for the given test data.

```bash
The input data is
VAR1 VAR2 CLASS
1.713 1.586 0
0.18 1.786 1
0.353 1.24 1
0.94 1.566 0
1.486 0.759 1
1.266 1.106 0
1.54 0.419 1
0.459 1.799 1
0.773 0.186 1
====================
The Test data to predict
Enter Value for VAR1 :0.906
Enter Value for VAR2 :0.606
====================
The predicted Class is : [0]

```