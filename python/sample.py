"""
Here is a sample DataFrame that is comprehensive enough to suit all the questions previously discussed. Each column represents key attributes for employees, transactions, and products:

### Columns:
1. **EmployeeID**: Unique identifier for employees.
2. **EmployeeName**: Names of the employees.
3. **Gender**: Gender of the employees (Male/Female).
4. **Age**: Age of the employees.
5. **Department**: Department they belong to (IT, HR, Sales, Finance).
6. **Salary**: Salary of the employees.
7. **WorkHours**: Weekly work hours of employees.
8. **PerformanceScore**: Performance scores of employees (on a scale of 0-100).
9. **JoiningDate**: The date the employee joined the company.
10. **Product**: Names of products sold.
11. **Category**: Category of the products (Electronics, Fashion, Accessories).
12. **Price**: Price of each product.
13. **Quantity**: Quantity of products sold in each transaction.
14. **SaleDate**: Date of each sale.
15. **Stock**: Stock availability for each product.
16. **LaunchYear**: Year each product was launched.
17. **SaleAmount**: Total sale amount for each transaction (calculated as `Price * Quantity`).

You can now proceed to apply any analysis or questions to this dataset. Let me know if you need specific examples or further modifications!

"""




import pandas as pd
import numpy as np

# Creating a DataFrame that suits all the questions
data = {
    'EmployeeID': range(1, 21),
    'EmployeeName': [f'Employee_{i}' for i in range(1, 21)],
    'Gender': np.random.choice(['Male', 'Female'], size=20),
    'Age': np.random.randint(22, 60, size=20),
    'Department': np.random.choice(['IT', 'HR', 'Sales', 'Finance'], size=20),
    'Salary': np.random.randint(40000, 80000, size=20),
    'WorkHours': np.random.randint(35, 60, size=20),
    'PerformanceScore': np.random.uniform(60, 100, size=20),
    'JoiningDate': pd.date_range(start='2010-01-01', periods=20, freq='365D'),
    'Product': np.random.choice(['Product_A', 'Product_B', 'Product_C'], size=20),
    'Category': np.random.choice(['Electronics', 'Fashion', 'Accessories'], size=20),
    'Price': np.random.randint(200, 1000, size=20),
    'Quantity': np.random.randint(1, 10, size=20),
    'SaleDate': pd.date_range(start='2024-01-01', periods=20, freq='15D'),
    'Stock': np.random.randint(10, 100, size=20),
    'LaunchYear': np.random.randint(2000, 2023, size=20),
}

df = pd.DataFrame(data)

# Calculating SaleAmount as the product of Price and Quantity
df['SaleAmount'] = df['Price'] * df['Quantity']

df.head()


# questiosn
"""
### Gist of Unique Data Science Interview Questions

1. **Basic Aggregations:**
   - What is the total revenue generated across all transactions?
   - What is the average quantity of items sold per transaction?

2. **Grouping and Aggregations:**
   - What is the average salary for each department?
   - What is the total stock available for each category?
   - What is the average performance score of male employees vs. female employees?
   - What is the average sale amount for each category?

3. **Filtering and Boolean Masking:**
   - How can you filter products with a price greater than 500?
   - How can you filter sales transactions that occurred in February 2024?
   - How can you find all employees in the "IT" department with ExperienceYears greater than 5?

4. **Sorting:**
   - How can you sort the products by their ratings in descending order?
   - Which customer made the highest purchase, and what was the amount?
   - Which employee worked the most hours in a week?

5. **Date Calculations:**
   - How many years have passed since the launch of each product?
   - How many years of experience does each employee have?
   - How many employees have been with the company for more than 5 years?

6. **Unique Values:**
   - How many unique products were sold?

7. **Category Analysis:**
   - What percentage of total sales revenue comes from each category?
   - What percentage of employees earn more than 60,000?

8. **Top N Analysis:**
   - What are the top 3 most expensive products?
   - Identify the top 2 employees based on their performance score.
   - Which product generated the most revenue, and how much was it?

9. **Data Transformation:**
   - Create a new column, `SalaryLevel`, that categorizes employees' salaries into Low (<55,000), Medium (55,000-60,000), and High (>60,000).
   - Create a new column, `PriceCategory`, that categorizes products as "Low" (<300), "Medium" (300-600), or "High" (>600).
   - Create a new column, `Efficiency`, as `PerformanceScore / WorkHours`. Identify the employee with the highest efficiency.
   - Create a new column, `RevenuePerItem`, that calculates the sale amount per item for each transaction.

10. **Correlation Analysis:**
    - Is there a correlation between performance score and salary?
    - Is there a correlation between stock and the price of products?

11. **Segmentations:**
    - Segment employees into Youth (<30), Mid-Aged (30-40), and Senior (>40) groups and find the average performance score for each group.

12. **Pivot Tables:**
    - How can you create a pivot table to show the average rating of products for each category?

13. **Cumulative Analysis:**
    - How can you calculate the cumulative sales amount over time?

14. **Revenue Analysis:**
    - What is the total revenue generated across all transactions?
    - Which product generated the most revenue?

15. **Performance Analysis:**
    - Which employee has the highest performance score?

This list avoids duplicate questions and provides a comprehensive set of queries that cover a wide range of data science concepts.

"""