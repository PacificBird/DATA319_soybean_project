# Final Project Proposal:


## Project Idea/Motivation

The idea behind our project is to find which analysis gives the most accurate predictions and how to deal with a dataset with only categorical features. With the categorical data, we wanted a challenge to see who we can analyze using methods that are primarily used for numerical data, but starting with just categorical and converting it to numerical or creating a work around for it not being numerical. We also want to find what factors indicate that the soybean plant will have a disease or whether it will not.


## Description Of The Data

We have chosen to analyze the Soybean (Large) dataset, which is a categorical dataset with 307 lines and 35 features, all of which are observations of the plant characteristics and the conditions that they endure. Most importantly, it distinguishes possible signs of disease, such as leaf spots, lesions, mold growth, shriveling, and other signs. 


## Research Question

1. What approach to analysis gives the most accurate predictive power of whether or not a plant has a disease? 
2. What contributing factor gives the strongest indication that a soybean plant has or will develop a disease? 


## Analysis

Cleaning/exploratory first

Hypothesis testing (the techniques are significantly different from each other, will happen last) 

Classification (Decision tree, multinomial logistic regression)

PCA on dummy variables -> kNN classification


## Justification For Analysis Relevance to Questions

The data has lots of null values and also contains lots of features, many of which have many categories. The cleaning and exploratory step will help to ‘cull the herd’ as it were, making it so there are not so many columns when we eventually use one-hot encoding to turn the categorical data into dummy variables and only keeping the original features which are most likely to provide predictive power to the classification methods we will use later.

The fact that we’re doing classification is obvious. Decision trees were chosen because they’re one of the only ways to do classification natively on exclusively categorical data without dealing with dummy variable encoding. Multinomial logistic regression was chosen as a more standard way of doing classification. Using PCA on the dummy variable data is more of an experiment to see if it’s possible to extract numerical features from categorical data, and then use numerical classification methods on that.

Hypothesis testing will then be necessary to conclude that the different methods are statistically more or less accurate than each other.


## Initial Observations Of Data

Since this dataset contains only categorical data, there are potential challenges associated with the lack of quantitative data in this project. There are several lines that are missing large chunks of data so we will be removing lines that do not contain enough valuable information to be included. 


## Expected Member Contribution

Natalie- [multinomial regression](https://machinelearningmastery.com/multinomial-logistic-regression-with-python/)

Izzy - Classification on dimension-reduced data (turning categorical data into numerical with PCA?)

Cooper- Cleaning/exploratory, Hypothesis testing

Jared- decision tree


## Dataset Source

[https://datahub.io/machine-learning/soybean#data](https://datahub.io/machine-learning/soybean#data)
