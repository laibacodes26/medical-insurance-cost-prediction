# Medical Insurance Cost Prediction

## Problem
Predicting a person's medical insurance charges based on personal and 
lifestyle factors, since costs vary a lot between individuals depending 
on things like smoking status and BMI.

## Dataset
Medical Cost Personal Dataset, 1338 records, 7 columns: age, gender, 
bmi, children, smoker, region, charges (target).

## Preprocessing
- Checked for missing values (none found) and duplicates (removed if present)
- Encoded gender and smoker as 0/1
- One-hot encoded region

## Exploratory Data Analysis
- Smoking status has the strongest correlation with charges (~0.79)
- Age and BMI also show positive relationships with charges
- Gender and number of children have little effect

## Model
Multiple Linear Regression, trained with an 80/20 train-test split.

## Evaluation
- MAE: ~4181
- MSE: ~33,596,915
- RMSE: ~5796
- R² Score: ~0.78

## Prediction App
A Streamlit web app takes age, gender, BMI, children, smoker status, 
and region as input, and returns an estimated insurance cost using the 
trained model.

## Limitations
Linear Regression assumes straight-line relationships and can't fully 
capture interactions like smoking combined with high BMI. A more 
advanced model (like Random Forest) could improve accuracy.
