import matplotlib.pyplot as plt
import seaborn as sns

# Predictions
y_pred = rf_model.predict(X_test)

# Plot
plt.figure(figsize=(8,6))
sns.scatterplot(x=y_test, y=y_pred, color='teal', s=60)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', linewidth=2)
plt.xlabel("Actual Degradation Rate (%)")
plt.ylabel("Predicted Degradation Rate (%)")
plt.title("Actual vs Predicted Degradation Rate")
plt.grid(True)
plt.tight_layout()
plt.show()
