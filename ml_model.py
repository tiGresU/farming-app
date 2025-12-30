# =========================================
# File: ml_model.py
# Purpose: Machine Learning Model
# =========================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# -----------------------------
# Load Dataset (ABSOLUTE PATH)
# -----------------------------
df = pd.read_csv("pesticides.csv"
)

# -----------------------------
# Data Preparation
# -----------------------------
df_ml = df[["Area", "Year", "Value"]].copy()
df_ml.loc[:, "Area"] = df_ml["Area"].astype("category").cat.codes

# -----------------------------
# Features and Target
# -----------------------------
X = df_ml[["Area", "Year"]]
y = df_ml["Value"]

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# Evaluation
# -----------------------------
X_test = pd.DataFrame(X_test, columns=X_train.columns)
y_pred = model.predict(X_test)

rmse = mean_squared_error(y_test, y_pred) ** 0.5

print("R2 Score:", r2_score(y_test, y_pred))
print("RMSE:", rmse)

# -----------------------------
# Prediction Function
# -----------------------------
def predict_pesticide_usage(area_code, year):
    sample = pd.DataFrame({
        "Area": [area_code],
        "Year": [year]
    })
    return model.predict(sample)[0]

# -----------------------------
# User Input
# -----------------------------
if __name__ == "__main__":
    print("\n--- Pesticide Usage Prediction ---")
    area_code = int(input("Enter Area code (numeric): "))
    year = int(input("Enter Year: "))

    prediction = predict_pesticide_usage(area_code, year)
    print("Predicted Pesticide Usage:", round(prediction, 2))



def predict_pesticide_usage(area_code, year):
    sample = pd.DataFrame({
        "Area": [area_code],
        "Year": [year]
    })
    return model.predict(sample)[0]

