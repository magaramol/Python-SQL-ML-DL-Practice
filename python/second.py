#     Basic Aggregations: What is the average salary of employees in the company? How can you compute it?
df['Salary'].mean()

# Data Filtering: How can you filter employees with a PerformanceScore greater than 85?
df[df['PerformanceScore']>85]


#     Grouping: What is the total salary paid to employees in each department?
df.groupby('Department')['Salary'].sum()


#     Sorting: How can you sort the DataFrame by PerformanceScore in ascending order?
df.sort_values('PerformanceScore')


#     Year Calculations: How many years have passed since each employee's last promotion? (Hint: Use the current year.)
df['LastPromotionYear']=pd.to_datetime(df['LastPromotionYear'],format='%Y')
current_days=pd.Timestamp.now().year
df['difdf']=current_days-df['LastPromotionYear'].dt.year

# Boolean Masking: How can you find all employees in the "IT" department with ExperienceYears greater than 5?
df[(df['ExperienceYears']>5) &(df['Department']=='IT')]

# Data Transformation: Create a new column, SalaryLevel, that categorizes employees'
#  salaries into Low (<55,000), Medium (55,000-60,000), and High (>60,000).

def sal(salary):
  if salary<55000:
    return 'low'
  elif salary<60000:
    return 'mid'
  else:
    return 'high'
  

df['sal_range']=df['Salary'].apply(sal)

# Correlation Analysis: How can you find the correlation between ExperienceYears and PerformanceScore?
df['ExperienceYears'].corr(df['PerformanceScore'])


#     Pivot Table: Create a pivot table showing the average PerformanceScore for each Department.


piv_table=pd.pivot_table(df,values='PerformanceScore',index='Department',aggfunc='mean')


