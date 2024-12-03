# this is first code
# Basic Aggregations: What is the average purchase amount across all customers? How can you compute it?
df['PurchaseAmount'].mean()

# Data Filtering: How can you filter customers who purchased items in the "Fashion" category?
df[df['Category']=='Fashion']

# Grouping: What is the total purchase amount for each category?
df.groupby('Category')['PurchaseAmount'].sum()



#Sorting: How can you sort the DataFrame by PurchaseAmount in descending order?
df.sort_values('PurchaseAmount', ascending=False)

# Date Calculations: How many days have passed since the last purchase date for each customer? (Hint: Use datetime operations.)

df['LastPurchaseDate']=pd.to_datetime(df['LastPurchaseDate'])
current_date = pd.Timestamp.now()

df['diff']=(current_date-df['LastPurchaseDate']).dt.days

# Boolean Masking: How can you find all customers from "Delhi" with a purchase amount greater than 100?
a=(df['City']=='Delhi') & (df['PurchaseAmount']>100)
df[a]

# Data Transformation: Create a new column AgeGroup that 
# segments customers into age groups: Youth (<30), Middle-aged (30-50), and Senior (>50).



def bins(age):
  if age <30:
    return 'youth'

  elif age<60:
    return 'mid'

  else:
    return 'old' 
df['bins']=df['Age'].apply(bins)

