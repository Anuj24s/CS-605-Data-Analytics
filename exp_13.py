import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# -------- Linear Regression --------
# Dataset (single feature)
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
pred_lr = model_lr.predict([[6]])
print("Linear Regression Prediction:", pred_lr)


# -------- Multiple Linear Regression --------
# Dataset (multiple features)
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
pred_mlr = model_mlr.predict([[6, 3]])
print("Multiple Linear Regression Prediction:", pred_mlr)