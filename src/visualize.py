import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("../data/worldbank_climate.csv")

# Features & target
X = df[['GDP_per_capita', 'Energy_use_per_capita', 'Urban_pop_pct', 'Renewable_pct']]
y = df['CO2_per_capita']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predict
y_pred = rf_model.predict(X_test)

# Plot Actual vs Predicted
plt.figure(figsize=(6,4))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([0,20],[0,20], 'r--')  # reference line for perfect prediction
plt.xlabel('Actual CO2 Emissions')
plt.ylabel('Predicted CO2 Emissions')
plt.title('Actual vs Predicted CO2 Emissions')
plt.show()

# Optional: Feature importance
importances = rf_model.feature_importances_
for f, i in zip(X.columns, importances):
    print(f"{f}: {i:.3f}")
