# Predicting Classification using K-Means Clustering

This Python script predicts a classification for a case where VAR1 and VAR2 are given, using the result of k-means clustering with 3 centroids.

## Problem Description

Given the following data, which specify classifications for nine combinations of VAR1 and VAR2, we need to predict a classification for a case where VAR1=0.906 and VAR2=0.606, using the result of k-means clustering with 3 means (i.e., 3 centroids).

## Implementation

The Python script uses `scikit-learn's KMeans module` to perform k-means clustering. It takes the provided data and class labels as input, fits the KMeans model, and then predicts the classification for the given test case.

## Usage

Before running the script, make sure to install `scikit-learn` module. You can do this via pip:

```bash
pip install scikit-learn
```

You can run the provided Python script kmeans_classification.py to predict the classification. Here's how to run it:
 ```bash
 python kmeans_classification.py
```