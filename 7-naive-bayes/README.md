# Implement Naive Bayes Theorem for English Text Classification

This program is to implement Naive Bayes Theorem for classifying English text as positive or negative sentiment.

## Requirements

To run this program, you need to have the following modules installed:

1. **pandas Module**: Used for reading CSV files.
   - To install pandas, open Command Prompt and execute the following command:
     ```bash
     pip install pandas
     ```

2. **scikit-learn (sklearn) Module**: Required for implementing Naive Bayes classifier.
   - To install sklearn, open Command Prompt and execute the following command:
     ```bash
     pip install scikit-learn
     ```

Finally, you need to create a dataset called `Statements_data.csv` with labeled English text statements.


### Data Description

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

You can run the provided Python script `naive-bayes-theorem.py` to implement Naive Bayes Theorem for classifying English text as positive or negative sentiment using data from the provided `Statements_data.csv` file. Here's how to run it:

```bash
python naive-bayes-theorem.py
```
## Script Explanation

The Python script `naive-bayes-theorem.py` contains the following code:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
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
df = pd.DataFrame(Xtrain_dims.toarray(),columns=count_vect.get_feature_names_out())
clf = MultinomialNB()
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

1. The script reads the dataset Statements_data.csv containing statements and their corresponding labels (positive or negative).
2. It maps the labels to numeric values.
3. The data is split into training and testing sets.
4. Text data is converted to vectors using CountVectorizer.
5. A Multinomial Naive Bayes classifier is trained on the training data.
6. Predictions are made on the test data.
7. Accuracy, recall, precision, and confusion matrix metrics are printed.
8. Users can input a statement for sentiment prediction, and the script will classify it as positive or negative.

## Expected Output


The output of the sentiment analysis Python script provides information about the dataset, model performance metrics, and prediction results.


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
Enter any statement to predict :I hate juice
Statement is Negative
```

