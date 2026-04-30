# %%
!pip install pandas
!pip install numpy
!pip install matplotlib
!pip install seaborn
!pip install scikit-learn

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# %%
df = pd.read_csv("climate_change_dataset.csv")
print(df.head())
print(df.info())


# %%
df.isnull().sum()

# Drop missing values (if any)
df.dropna(inplace=True)


# %%
print(df.describe())


# %%
plt.figure()
sns.lineplot(x="Year", y="Avg Temperature (°C)", data=df)
plt.title("Average Temperature Trend")
plt.show()


# %%
plt.figure()
sns.lineplot(x="Year", y="CO2 Emissions (Tons/Capita)", data=df)
plt.title("CO2 Emissions Trend")
plt.show()


# %%
plt.figure()
sns.scatterplot(x="CO2 Emissions (Tons/Capita)", y="Avg Temperature (°C)", data=df)
plt.title("CO2 vs Temperature")
plt.show()


# %%
plt.figure()
sns.scatterplot(x="Avg Temperature (°C)", y="Extreme Weather Events", data=df)
plt.title("Temperature vs Extreme Weather Events")
plt.show()


# %%
country_temp = df.groupby("Country")["Avg Temperature (°C)"].mean()

plt.figure(figsize=(10,5))
country_temp.sort_values().plot(kind="bar")
plt.title("Average Temperature by Country")
plt.show()


# %%
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()


# %%
X = df[["CO2 Emissions (Tons/Capita)"]]
y = df["Avg Temperature (°C)"]

model = LinearRegression()
model.fit(X, y)

print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)


# %%
sample = [[10]]  # CO2 emissions
prediction = model.predict(sample)
print("Predicted Temperature:", prediction[0])



