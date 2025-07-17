# Define threshold for top 10% efficiency
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the uploaded dataset
file_path = "/content/cleaned_ev_battery_data.csv"
df = pd.read_csv(file_path)

# Display basic info to understand the column names and structure
df.info()

high_eff_threshold = df['Efficiency (%)'].quantile(0.9)

# Calculate average charging duration for normal and high-efficiency cases
normal_charging_duration = df['Charging Duration (min)'].mean()
minimized_charging_duration = df[df['Efficiency (%)'] >= high_eff_threshold]['Charging Duration (min)'].mean()

# Scatter plot of Efficiency vs Charging Duration
plt.figure(figsize=(12, 6))

# Full dataset
sns.scatterplot(
    x=df['Efficiency (%)'],
    y=df['Charging Duration (min)'],
    alpha=0.6,
    color='blue',
    label='All Data'
)

# Highlight high-efficiency group
high_eff_data = df[df['Efficiency (%)'] >= high_eff_threshold]
sns.scatterplot(
    x=high_eff_data['Efficiency (%)'],
    y=high_eff_data['Charging Duration (min)'],
    alpha=0.8,
    color='red',
    label='High Efficiency (Top 10%)'
)
# Add this after calculating minimized_charging_duration

plt.axhline(minimized_charging_duration, color='orange', linestyle='--',
            label=f'Minimized Duration: {minimized_charging_duration:.2f} min')

plt.text(
    x=high_eff_data['Efficiency (%)'].min(),
    y=minimized_charging_duration + 1,
    s=f"{minimized_charging_duration:.2f} min",
    color='orange',
    fontsize=12,
    fontweight='bold'
)

# Horizontal line for average minimized charging duration
plt.axhline(minimized_charging_duration, color='orange', linestyle='--',
            label=f'Minimized Charging Duration: {minimized_charging_duration:.2f} min')

# Labels and title
plt.title("Efficiency vs Minimized Charging Duration (Top 10% Efficiency)")
plt.xlabel("Efficiency (%)")
plt.ylabel("Charging Duration (min)")
plt.legend()
plt.tight_layout()
plt.show()
