# Customer Lifetime Value (CLV) Prediction

## Overview
This project focuses on estimating Customer Lifetime Value (CLV) using historical transaction data.
The objective is to identify high-value customers and support data-driven retention and revenue strategies.

## Dataset
The project uses a transactional retail dataset containing customer purchases over time.
The raw dataset is not included in this repository due to file size limitations.
It can be downloaded from the Online Retail Dataset available on Kaggle or the UCI Machine Learning Repository.

## Feature Engineering
Customer-level features were created using the RFM framework:
- Recency: Days since the most recent purchase
- Frequency: Number of unique transactions
- Monetary: Total spending per customer

## Modeling Approach
CLV was framed as a regression problem.
A Linear Regression model was trained using Recency and Frequency as predictors and Monetary value as the target variable.

## Model Evaluation
The model was evaluated using:
- RMSE to measure average prediction error
- R² score to assess explained variance

The focus was on interpretability and business relevance rather than over-optimizing accuracy.

## Customer Segmentation
Predicted CLV values were used to segment customers into three groups:
- Low Value
- Medium Value
- High Value

Quantile-based segmentation ensured balanced and interpretable customer groups.

## Business Insights
- High Value customers contribute a disproportionate share of predicted revenue
- Medium Value customers represent strong upsell and engagement opportunities
- Low Value customers may require cost-efficient retention strategies

## Project Links
GitHub Repository:
https://github.com/NiDHiN-1908/customer-lifetime-value-prediction

Portfolio:
https://nidhin-1908.github.io/
