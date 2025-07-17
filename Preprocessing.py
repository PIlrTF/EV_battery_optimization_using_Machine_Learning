import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('ev_battery_charging_data.csv')

# 1. Check for missing values
print("Missing values per column:")
print(df.isnull().sum())

# 2. Check data types
print("\nData types:")
print(df.dtypes)

# 3. Handle missing values (none found in this dataset)
# If there were missing values, we might:
# - Drop rows with missing values
# - Impute with mean/median for numerical columns
# - Use mode for categorical columns

# 4. Convert categorical variables to numerical (if needed for modeling)
df['Charging Mode'] = df['Charging Mode'].astype('category')
df['Battery Type'] = df['Battery Type'].astype('category')

# 5. Feature engineering (example)
# Create a new feature: Charging Power (V * A)
df['Charging Power (W)'] = df['Voltage (V)'] * df['Current (A)']

# Create temperature difference feature
df['Temp Difference (°C)'] = df['Battery Temp (°C)'] - df['Ambient Temp (°C)']

# 6. Normalize numerical features (example for columns that might need it)
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
cols_to_normalize = ['SOC (%)', 'Voltage (V)', 'Current (A)', 'Battery Temp (°C)',
                    'Ambient Temp (°C)', 'Charging Duration (min)', 'Charging Cycles']
df[cols_to_normalize] = scaler.fit_transform(df[cols_to_normalize])

# 7. Encode categorical variables
df = pd.get_dummies(df, columns=['Charging Mode', 'Battery Type'], drop_first=True)

# 8. Check for outliers (example using IQR)
def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] < lower_bound) | (df[column] > upper_bound)]

print("\nOutliers in Current (A):")
print(detect_outliers(df, 'Current (A)').shape[0])

# 9. Save cleaned dataset
df.to_csv('cleaned_ev_battery_data.csv', index=False)
