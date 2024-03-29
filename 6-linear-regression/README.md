# Age and Income Regression Analysis

This script performs a simple linear regression analysis on the relationship between age and income using data from the provided `Age_Income.csv` file.


## Requirements

Before running the script, make sure you have the following Python libraries installed:

- pandas
- numpy
- matplotlib

You can install these libraries using pip:

```bash
pip install pandas numpy matplotlib
```

## Data Description

The `Age_Income.csv` file contains two columns: Age and Income. Each row represents a data point with the age and income of an individual.

Here is a sample of the data:

| Age | Income |
|-----|--------|
| 25  | 25000  |
| 23  | 22000  |
| 24  | 26000  |
| 28  | 29000  |
| 34  | 38600  |
| 32  | 36500  |
| 42  | 41000  |
| 55  | 81000  |
| 45  | 47500  |

## Script Explanation

1. The script uses pandas to read the data from the `Age_Income.csv` file into a DataFrame.
2. It extracts the Age and Income columns from the DataFrame into separate arrays.
3. It calculates the mean of the Age and Income vectors.
4. The script then calculates the regression coefficients using simple linear regression formulas.
5. After computing the regression coefficients, it prints them.
6. Next, it plots the actual data points as a scatter plot and the regression line.
7. Finally, it displays the plot.

## Running the Script

Before running the script, make sure you have installed the necessary Python libraries: pandas, numpy, and matplotlib.

You can run the script using any Python environment or IDE.

```bash
python regression_analysis.py
```