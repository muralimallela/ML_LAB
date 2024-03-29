# K-Nearest Neighbors Classification with Python

This Python script implements k-nearest neighbors (KNN) classification using the scikit-learn library. KNN is a simple and effective classification algorithm that assigns a class label to an input based on the majority class among its k nearest neighbors in the feature space.

## Installation

Before running the script, make sure to install the `scikit-learn module`. You can do this via pip:

```bash
pip install scikit-learn
```
# Usage
You can run the provided Python script `knn_classification.py` to perform k-nearest neighbors classification. Here's how to run it:

```bash
python knn_classification.py
```
# Script Explanation
The Python script `knn_classification.py` contains the following code:

```python
# Import necessary modules
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import random

# Loading data
data_iris = load_iris()

# To get list of target names
label_target = data_iris.target_names

print("Sample Data from Iris Dataset")
print("*" * 30)

# to display the sample data from the iris dataset
for i in range(10):
    rn = random.randint(0, 120)
    print(data_iris.data[rn], "===>", label_target[data_iris.target[rn]])

# Create feature and target arrays
X = data_iris.data
y = data_iris.target

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

print("The Training dataset length: ", len(X_train))
print("The Testing dataset length: ", len(X_test))

try:
    nn = int(input("Enter number of neighbors: "))
    knn = KNeighborsClassifier(nn)
    knn.fit(X_train, y_train)

    # to display the score
    print("The Score is:", knn.score(X_test, y_test))

    # To get test data from the user
    test_data = input("Enter Test Data: ").split(",")
    for i in range(len(test_data)):
        test_data[i] = float(test_data[i])

    print()
    v = knn.predict([test_data])
    print("Predicted output is:", label_target[v])
except:
    print("Please supply valid input......")
```
This script performs the following steps:

1. Loads the Iris dataset from scikit-learn.
2. Displays a sample of the dataset.
3. Splits the dataset into training and testing sets.
4. Asks the user to input the number of neighbors (k) for KNN.
5. Fits the KNN classifier on the training data.
6. Calculates and displays the classification score on the test data.
7. Accepts test data from the user and predicts the output class label.

# Expected Output

Upon running the script, you will see the following output:

- A sample of the data from the Iris dataset.
- The lengths of the training and testing datasets.
- The classification score on the test data.
- A prompt to enter test data for prediction, followed by the predicted output class label.

```bash
Sample Data from Iris Dataset
******************************
[5.7 2.6 3.5 1. ] ===> versicolor
[5.1 3.8 1.6 0.2] ===> setosa
[6. 2.2 5. 1.5] ===> virginica
[5.7 4.4 1.5 0.4] ===> setosa
[6.6 2.9 4.6 1.3] ===> versicolor
[4.4 3.2 1.3 0.2] ===> setosa
[6. 2.9 4.5 1.5] ===> versicolor
[5.7 4.4 1.5 0.4] ===> setosa
[6.4 2.7 5.3 1.9] ===> virginica
[6.6 3. 4.4 1.4] ===> versicolor
The Training dataset length: 105
The Testing dataset length: 45
Enter number of neighbors :10
The Score is : 0.9777777777777777
Enter Test Data :6.2, 2.6, 3.4, 0.6
Predicted output is : ['versicolor']
```