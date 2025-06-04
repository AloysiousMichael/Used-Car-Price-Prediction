# Used Car Price Prediction

This project predicts the **selling price of used cars** using machine learning models trained on the CarDekho dataset. It includes data preprocessing, exploratory data analysis (EDA), model training, evaluation, and a **Streamlit-based web interface** for interactive predictions.

---

## Features Used

- Year: Year of purchase
- Kms_Driven: Kilometers the car has been driven
- Fuel_Type: CNG / Diesel / Petrol
- Transmission: Manual / Automatic
- Owner: Number of previous owners

---

## Models Trained

1. **Linear Regression**
2. **Support Vector Regression (SVR)** with GridSearchCV
3. **Random Forest Regressor** with hyperparameter tuning (final model)

---

## Model Evaluation Metrics

Used:
- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**

Final model: `RandomForestRegressor` performed best and was saved for deployment.

---

##  Streamlit Web App

An interactive interface for users to input car features and predict the price.

###  How to Run

1. Install required libraries:
   ```bash
   pip install pandas numpy matplotlib scikit-learn streamlit joblib
   streamlit run app.py

