# Outlier-Detection-Using-IQR
A Python-based mini project that uses the Interquartile Range (IQR) method to detect and remove salary outliers from a 150-employee dataset. The project uses Pandas for data processing and Matplotlib for visualizing salary distributions before and after outlier removal.


# Employee Salary Outlier Detection Using IQR

## Project Overview

This mini project demonstrates how to detect and remove salary outliers from an employee dataset using the **Interquartile Range (IQR)** method.

The dataset contains **150 employee records** with information such as age, department, education, experience, performance, working hours, salary, and bonus.

The main objective is to understand how IQR can be used to identify unusually high or low salary values and visualize the data before and after removing outliers.

## Features

The dataset contains the following columns:

| Feature | Description |
|---|---|
| Employee_ID | Unique employee identifier |
| Age | Age of the employee |
| Department | Employee department |
| Experience_Years | Years of work experience |
| Education | Education level |
| Performance_Score | Performance score from 1 to 10 |
| Working_Hours | Weekly working hours |
| Salary | Employee salary |
| Bonus | Employee bonus |

## Technologies Used

- Python
- Pandas
- Matplotlib
- CSV Dataset
- IQR (Interquartile Range) method

## IQR Method

The Interquartile Range represents the spread of the middle 50% of the data.

### Formulas

**IQR:**

```text
IQR = Q3 - Q1
```

**Lower Limit:**

```text
Lower Limit = Q1 - 1.5 × IQR
```

**Upper Limit:**

```text
Upper Limit = Q3 + 1.5 × IQR
```

Any salary value below the lower limit or above the upper limit is treated as an outlier.

## Results

For this dataset:

```text
Q1 = 46854.25
Q3 = 83051.00
IQR = 36196.75

Lower Limit = -7440.88
Upper Limit = 137346.13
```

Five intentional salary outliers were detected:

```text
150000
175000
200000
225000
250000
```

After removing these values, the cleaned dataset can be saved as:

```text
employee_data_without_outliers.csv
```

## Project Structure

```text
Employee-Salary-Outlier-Detection/
│
├── employee_outlier_dataset_150.csv
├── employee_data_without_outliers.csv
├── outlier_detection.py
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Employee-Salary-Outlier-Detection
```

### 3. Install required libraries

```bash
pip install pandas matplotlib
```

### 4. Run the Python program

```bash
python outlier_detection.py
```

The program will:

1. Load the CSV dataset.
2. Create a Pandas DataFrame.
3. Calculate Q1 and Q3.
4. Calculate IQR.
5. Calculate lower and upper limits.
6. Detect salary outliers.
7. Remove the outliers.
8. Save the cleaned dataset.
9. Display boxplots before and after outlier removal.

## Visualization

The project generates two boxplots:

- **Before Outlier Removal** – shows the salary outliers.
- **After Outlier Removal** – shows the cleaned salary distribution.

## Learning Outcomes

Through this project, you will learn:

- How to read CSV files using Pandas.
- How to work with DataFrames.
- What quartiles are.
- What Q1, Q2, and Q3 represent.
- How to calculate IQR.
- How to calculate outlier limits.
- How to detect and remove outliers.
- How to visualize data using boxplots.

## Conclusion

The IQR method is a simple and effective technique for identifying potential outliers. In this project, it was used to detect unusually high employee salaries and create a cleaner dataset for analysis.


Mini Project – Data Preprocessing / Outlier Detection
