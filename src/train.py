import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("../data/worldbank_climate.csv")
print(df.columns)

# Define features and target (use correct column names)
X = df[[
    "GDP_per_capita",
    "Energy_use_per_capita",
    "Urban_pop_pct",
    "Renewable_pct"
]]

# Correct target column name
y = df["CO2_per_capita"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open("../model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")
