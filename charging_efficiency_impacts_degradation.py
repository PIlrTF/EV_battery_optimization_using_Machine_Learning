import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("cleaned_ev_battery_data.csv")

# Define thresholds for high efficiency (top 10%)
high_eff_threshold = df['Efficiency (%)'].quantile(0.9)

# Groupings
normal_degradation = df['Degradation Rate (%)'].mean()
minimized_degradation = df[df['Efficiency (%)'] >= high_eff_threshold]['Degradation Rate (%)'].mean()

# Prepare data for plotting
compare_df = pd.DataFrame({
    "Condition": ["Normal Conditions", "High Efficiency (Top 10%)"],
    "Avg Degradation Rate (%)": [normal_degradation, minimized_degradation]
})

# Plotting efficiency vs minimized degradation rate
plt.figure(figsize=(12, 6))

# Scatter plot of Efficiency vs Degradation Rate for the entire dataset
sns.scatterplot(x=df['Efficiency (%)'], y=df['Degradation Rate (%)'], alpha=0.6, color='blue', label='All Data')

# Scatter plot for high efficiency (top 10%) with minimized degradation rate
high_eff_data = df[df['Efficiency (%)'] >= high_eff_threshold]
sns.scatterplot(x=high_eff_data['Efficiency (%)'], y=high_eff_data['Degradation Rate (%)'], alpha=0.8, color='red', label='High Efficiency')

# Adding average minimized degradation rate as a horizontal line
plt.axhline(minimized_degradation, color='orange', linestyle='--', label=f'Minimized Degradation Rate: {minimized_degradation:.2f}%')

# Adding labels and title
plt.title("Efficiency vs Minimized Degradation Rate (Top 10% Efficiency)")
plt.xlabel("Efficiency (%)")
plt.ylabel("Degradation Rate (%)")
plt.legend()
plt.tight_layout()
plt.show()
