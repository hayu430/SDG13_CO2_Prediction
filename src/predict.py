import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv("../data/worldbank_climate.csv")

# Features & target
feature_cols = ['GDP_per_capita', 'Energy_use_per_capita', 'Urban_pop_pct', 'Renewable_pct']
X = df[feature_cols]
y = df['CO2_per_capita']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Save model
joblib.dump(rf_model, "../model_rf.pkl")
print("Model saved as model_rf.pkl")

# Example prediction using DataFrame
new_country = pd.DataFrame([[20000, 150, 60, 20]], columns=feature_cols)
predicted_co2 = rf_model.predict(new_country)
print("Predicted CO2 emission for new country:", predicted_co2[0])
