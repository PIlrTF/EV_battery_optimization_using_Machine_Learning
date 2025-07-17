
 **Project Title: EV Battery Health & Efficiency Analysis using Machine Learning**

This project aims to analyze, visualize, and model electric vehicle (EV) battery performance by focusing on key factors influencing **degradation rate**, **charging efficiency**, and **charging duration**. It involves data preprocessing, feature engineering, exploratory data analysis (EDA), and machine learning to build predictive models that provide actionable insights into battery behavior.

 **Data Preprocessing & Feature Engineering**

The raw dataset, containing real-world EV charging session data, is first cleaned and prepared:

* **Missing values** are inspected and handled.
* **Categorical variables** like *Charging Mode* and *Battery Type* are encoded.
* **New features** are engineered, including:

  * `Charging Power (W)` = Voltage × Current
  * `Temperature Difference (°C)` = Battery Temp – Ambient Temp
* **Numerical columns** are normalized using MinMaxScaler.
* Outliers are detected using the IQR method.

The cleaned dataset is stored as `cleaned_ev_battery_data.csv` for further use.

 **Exploratory Data Analysis (EDA)**

EDA is performed to understand relationships among variables:

* A **correlation heatmap** is generated to identify which features influence battery degradation and efficiency.
* Scatter plots explore the **relationship between efficiency and degradation rate** and also **efficiency vs. charging duration**.
* High-efficiency sessions (top 10%) are analyzed separately to highlight performance differences.

Results show:

* **Higher efficiency leads to reduced degradation**.
* **Charging duration is minimized** for top 10% efficient sessions, reinforcing the value of optimized charging strategies.

 **Machine Learning Modeling**

The project uses **Random Forest Regressor** to predict battery degradation rate from input features. The process includes:

* Splitting the data into training and test sets (80/20).
* Fitting the model to training data.
* Predicting degradation on the test set.

Evaluation metrics:

* **MAE**, **MSE**, and **R² Score** indicate the model performs well in predicting degradation trends.

A **scatter plot of actual vs predicted degradation** is also visualized to assess model accuracy and variance.

 **Key Insights**

* EVs with **higher charging efficiency** tend to have **lower degradation rates** and **faster charging times**.
* These insights help optimize **battery usage**, extend battery life, and improve **energy management** strategies.
* The predictive model can be further enhanced and used in real-time EV systems for **battery health monitoring**.

**Conclusion**

This project provides a robust framework for understanding the impact of charging parameters on EV battery performance. With machine learning and data visualization, it helps stakeholders (manufacturers, fleet operators, researchers) to:

* Optimize charging protocols,
* Predict degradation,
* And promote sustainable battery usage.

