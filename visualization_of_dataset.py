# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the dataset
file_path = "/content/cleaned_ev_battery_data.csv"
df = pd.read_csv(file_path)

# ---------------------- #
# Correlation Heatmap    #
# ---------------------- #
sns.set(style="whitegrid", palette="muted", font_scale=1.1)

correlation_matrix = df.select_dtypes(include=['float64', 'int64']).corr()
plt.figure(figsize=(12, 12))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

