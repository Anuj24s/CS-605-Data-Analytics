import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# -------- Linear Regression --------
print("\n===== Simple Linear Regression =====")

# Dataset
data_lr = {
    'X': [1, 2, 3, 4, 5],
    'Y': [2, 4, 5, 4, 5]
}

df_lr = pd.DataFrame(data_lr)

X_lr = df_lr[['X']]
Y_lr = df_lr['Y']

# Model
model_lr = LinearRegression()
model_lr.fit(X_lr, Y_lr)

# Prediction
input_value = 6
pred_lr = model_lr.predict(pd.DataFrame([[input_value]], columns=['X']))

# Output
print(f"Input Feature (X): {input_value}")
print(f"Predicted Output (Y): {pred_lr[0]:.2f}")
print(f"Model Equation: Y = {model_lr.coef_[0]:.2f}*X + {model_lr.intercept_:.2f}")


# -------- Multiple Linear Regression --------
print("\n===== Multiple Linear Regression =====")

# Dataset
data_mlr = {
    'X1': [1, 2, 3, 4, 5],
    'X2': [2, 1, 3, 5, 4],
    'Y': [3, 4, 5, 6, 7]
}

df_mlr = pd.DataFrame(data_mlr)

X_mlr = df_mlr[['X1', 'X2']]
Y_mlr = df_mlr['Y']

# Model
model_mlr = LinearRegression()
model_mlr.fit(X_mlr, Y_mlr)

# Prediction
input_values = [6, 3]
pred_mlr = model_mlr.predict(pd.DataFrame([input_values], columns=['X1', 'X2']))

# Output
print(f"Input Features: X1 = {input_values[0]}, X2 = {input_values[1]}")
print(f"Predicted Output (Y): {pred_mlr[0]:.2f}")

print("Model Equation:")
print(f"Y = {model_mlr.coef_[0]:.2f}*X1 + {model_mlr.coef_[1]:.2f}*X2 + {model_mlr.intercept_:.2f}")
