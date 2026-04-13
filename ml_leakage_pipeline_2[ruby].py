import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Create synthetic data
np.random.seed(42)
n = 50

data = pd.DataFrame({
    'area_sqft': np.random.randint(500, 2000, n),
    'num_bedrooms': np.random.randint(1, 5, n),
    'age_years': np.random.randint(0, 30, n)
})

# Target variable (price)
data['price_lakhs'] = (
    data['area_sqft'] * 0.05 +
    data['num_bedrooms'] * 5 -
    data['age_years'] * 0.3 +
    np.random.randn(n) * 2
)

# Features & target
X = data[['area_sqft', 'num_bedrooms', 'age_years']]
y = data['price_lakhs']

# Model
model = LinearRegression()
model.fit(X, y)

# Output
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Predictions
predictions = model.predict(X)

# First 5 actual vs predicted
print(pd.DataFrame({
    "Actual": y[:5],
    "Predicted": predictions[:5]
}))



 # TASK 2
 from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y, predictions)
rmse = np.sqrt(mean_squared_error(y, predictions))
r2 = r2_score(y, predictions)

print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)

# MAE shows average error in predictions.
# RMSE gives higher weight to large errors.
# R2 score shows how well the model explains variance (closer to 1 is better).


#TASK 3
import matplotlib.pyplot as plt

# Residuals
residuals = y - predictions

# Plot
plt.hist(residuals, bins=10)
plt.title("Residuals Distribution")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.show()

# Residual = actual value - predicted value.
# A good model has residuals centered around zero.
# If the histogram is symmetric, the model fits well.