# Using AI to Predict CO₂ Emissions for Climate Action (SDG13)

## Problem Statement
Climate change is one of the greatest challenges facing humanity. CO₂ emissions are a primary driver of global warming, and understanding factors that influence emissions can help policymakers and researchers take informed action. This project focuses on predicting CO₂ emissions per capita using socio-economic and energy-related features.

## Machine Learning Solution
We used **supervised learning** with a **Random Forest Regressor** to model the relationship between features and CO₂ emissions. Features include GDP per capita, energy use per capita, urban population percentage, and renewable energy percentage. A small dataset of 50 countries was used to demonstrate the workflow.

The model was trained, tested, and evaluated using standard metrics:  
- **R² score:** measures model fit  
- **Mean Absolute Error (MAE):** average absolute difference between predicted and actual values  
- **Root Mean Squared Error (RMSE):** standard deviation of prediction errors

Predictions for new countries can be generated quickly using the trained model.

## Results & Impact
- The Random Forest model successfully captured patterns in the data, providing accurate CO₂ emission predictions.
- Visualizations like Actual vs Predicted CO₂ emissions help interpret the model and understand key factors.
- Feature importance analysis shows which factors most influence CO₂ emissions, aiding policy insights.

## Ethical & Sustainability Considerations
- Predictions are based on available data; missing or biased data could affect outcomes.
- The model is intended for analysis and education, not as a replacement for scientific or policy decisions.
- Using AI to analyze environmental data supports sustainable planning and climate action.

## Conclusion
This project demonstrates that AI can be a **bridge between innovation and sustainability**, supporting SDG13 by providing insights into CO₂ emissions patterns. The approach can be scaled to larger datasets for real-world impact, helping governments, researchers, and organizations make data-driven decisions to combat climate change.

**Author:** Hayu Yonatan
