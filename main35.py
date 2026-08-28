import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("employee_outlier_dataset_150.csv")


print("Original Data:")
print(df.head())


Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)


IQR = Q3 - Q1


lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower)
print("Upper Limit:", upper)


outliers = df[
    (df["Salary"] < lower) |
    (df["Salary"] > upper)
]

print("\nOutliers:")
print(outliers)


df_clean = df[
    (df["Salary"] >= lower) &
    (df["Salary"] <= upper)
]

print("\nData After Removing Outliers:")
print(df_clean)


df_clean.to_csv("employee_data_without_outliers.csv", index=False)


plt.figure()
plt.boxplot(df["Salary"])
plt.title("Salary - Before Outlier Removal")
plt.ylabel("Salary")
plt.show()


plt.figure()
plt.boxplot(df_clean["Salary"])
plt.title("Salary - After Outlier Removal")
plt.ylabel("Salary")
plt.show()