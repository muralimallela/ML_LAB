# Finite Words Classification System using Back-propagation Algorithm

Implement the finite words classification system using the Back-propagation algorithm.

## Requirements:
To run this program, you need to install the `pandas Module`:
```bash
pip install pandas
```
Pandas Module is used to read CSV files.

You also need to install the `scikit-learn Module`:

```bash
pip install scikit-learn
```
Sklearn Module is used for machine learning tasks.

You need to install the `scikit-neuralnetwork Module` as well:

```bash
pip install scikit-neuralnetwork
```

Sklearn Neural Network Module provides neural network models.

Finally, you need to create a dataset called `Statements_data.csv` file.

## Data Description

This dataset `Statements_data.csv` contains labeled English text statements indicating positive (pos) or negative (neg) sentiment.

| Statement                                  | Label |
|--------------------------------------------|-------|
| This is very good place                   | pos   |
| I like this biryani                       | pos   |
| I feel very happy                         | pos   |
| This is my best work                      | pos   |
| I do not like this restaurant             | neg   |
| I am tired of this stuff                  | neg   |
| I can't deal with this                    | neg   |
| What an idea it is                        | pos   |
| My place is horrible                      | neg   |
| This is an awesome place                  | pos   |
| I do not like the taste of this juice     | neg   |
| I love to sing                            | pos   |
| I am sick and tired                       | neg   |
| I love to dance                           | pos   |
| What a great holiday                      | pos   |
| That is a bad locality to stay            | neg   |
| We will have good fun tomorrow            | pos   |
| I hate this food                          | neg   |

## Usage

You can run the provided Python script `back-propagation.py` to Implement the finite words classification system using the Back-propagation algorithm using data from the provided `Statements_data.csv` file. Here's how to run it:

```bash
python back-propagation.py
```
## Script Explanation

The Python script `back-propagation.py` contains the following code:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix,precision_score, recall_score
msglbl_data = pd.read_csv('Statements_data.csv', names=['Message',
'Label'])
print("The Total instances in the Dataset: ", msglbl_data.shape[0])
msglbl_data['labelnum'] = msglbl_data.Label.map({'pos': 1, 'neg':
0})
# place the data in X and Y Vectors
X = msglbl_data["Message"]
Y = msglbl_data.labelnum
# to split the data into train se and test set
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y)
count_vect = CountVectorizer()
Xtrain_dims = count_vect.fit_transform(Xtrain)
Xtest_dims = count_vect.transform(Xtest)
df =pd.DataFrame(Xtrain_dims.toarray(),columns=count_vect.get_feature_names_out())
clf = MLPClassifier(solver='lbfgs', alpha=1e5,hidden_layer_sizes=(5, 2), random_state=1)
# to fit the train data into model
clf.fit(Xtrain_dims, Ytrain)
# to predict the test data
prediction = clf.predict(Xtest_dims)
print('******** Accuracy Metrics *********')
print('Accuracy : ', accuracy_score(Ytest, prediction))
print('Recall : ', recall_score(Ytest, prediction))
print('Precision : ',precision_score(Ytest, prediction))
print('Confusion Matrix : \n', confusion_matrix(Ytest, prediction))
print(10*"-")
# to predict the input statement
test_stmt = [input("Enter any statement to predict :")]
test_dims = count_vect.transform(test_stmt)
pred = clf.predict(test_dims)
for stmt,lbl in zip(test_stmt,pred):
    if lbl == 1:
        print("Statement is Positive")
    else:
        print("Statement is Negative")
```
The script performs the following steps in implementing the finite words classification system using the Back-propagation algorithm:

**Data Loading:** It reads the dataset "Statements_data.csv", which contains statements and their corresponding labels (positive or negative).

**Label Mapping:** The script maps the categorical labels ('pos' for positive and 'neg' for negative) to numerical values (1 for positive and 0 for negative).

**Data Splitting:** The dataset is split into training and testing sets using the train_test_split function from sklearn.model_selection.

**Feature Extraction:** Text data is converted into numerical feature vectors using CountVectorizer. This process converts the text data into a matrix of token counts, which represents the presence of words in the statements.

**Model Initialization:** The script initializes an MLPClassifier model with specific parameters such as solver, alpha, hidden_layer_sizes, and random_state.

**Model Training:** The initialized MLPClassifier model is trained on the training data using the fit method.

**Prediction:** Predictions are made on the test data using the trained model. The model predicts whether each statement in the test set is positive or negative.

**Performance Evaluation:** Accuracy, recall, precision, and confusion matrix metrics are computed and printed to evaluate the performance of the model. These metrics provide insights into how well the model is performing in classifying statements into positive and negative categories.

**User Interaction:** Users can interact with the script by entering a statement for sentiment prediction. The input statement is then vectorized using the same CountVectorizer instance used for training, and the model predicts whether the statement is positive or negative.

**Output Display:** The script displays the predicted sentiment label (positive or negative) for the input statement entered by the user. This allows users to see how the model classifies their input statements.

## Expected Output
This Python script implements a finite words classification system using the Back-propagation algorithm. It reads a dataset from a CSV file, preprocesses the data, trains a Multi-Layer Perceptron (MLP) classifier, and predicts the sentiment of input statements. The accuracy metrics including accuracy, recall, precision, and confusion matrix are computed and printed for evaluation. Users can input statements for sentiment prediction, and the script classifies them as positive or negative.

```html
The Total instances in the Dataset: 18
******** Accuracy Metrics *********
Accuracy : 0.6
Recall : 1.0
Precision : 0.6
Confusion Matrix :
[[0 2]
[0 3]]
----------
Enter any statement to predict :I love biryani
Statement is Positive

```
```html
The Total instances in the Dataset: 18
******** Accuracy Metrics *********
Accuracy : 0.6
Recall : 0.6666666666666666
Precision : 0.6666666666666666
Confusion Matrix :
[[1 1]
[1 2]]
----------
Enter any statement to predict :i do not like summer
Statement is Negative
```
