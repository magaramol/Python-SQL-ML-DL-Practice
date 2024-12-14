#How can you calculate the total years of experience for each employee?
current_date=pd.Timestamp.now()
current_year=current_date.year
df['JoiningDate']=pd.to_datetime(df['JoiningDate'])
df['exp']=current_year-df['JoiningDate'].dt.year
#What is the average performance score of male employees vs. female employees?
df.groupby('Gender')['PerformanceScore'].mean()

#How can you identify the top 2 employees based on their performance score?
df.sort_values('PerformanceScore',ascending=False).head(2)


# What is the average salary for each department?


df.groupby('Department')['Salary'].mean()


# What percentage of employees earn more than 60,000?

(len(df[df['Salary']>60000]['EmployeeID'])/len(df['Salary']))*100


# Find the employee(s) who worked the most hours in a week.

df.sort_values('WorkHours',ascending=False).head(1)


# Is there any correlation between performance score and salary?


df['Salary'].corr(df['PerformanceScore'])


# Segment employees into Youth (<30), Mid-Aged (30-40),
# and Senior (>40) groups and find the average performance score for each group.

def modes(age):
  if age <30:
    return 'jr'
  elif age <40:
    return 'mid'
  else:
    return 'sr'
df['seg']=df['Age'].apply(modes)

# How many employees have been with the company for more than 5 years?

df[df['exp']>5]

# Create a new column Efficiency as PerformanceScore / WorkHours. Identify the employee with the highest efficiency.

df['efi']=df['PerformanceScore']/df['WorkHours']

df.sort_values('efi',ascending=False).head(1)