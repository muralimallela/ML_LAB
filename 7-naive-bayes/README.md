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

