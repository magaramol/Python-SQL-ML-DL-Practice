# Basic Aggregations: What is the average price of all products?

df['Price'].mean()



# Data Filtering: How can you filter products with a price greater than 500?
df[df['Price']>500]

# Grouping: What is the total stock available for each category?
df.groupby('Category')['Stock'].sum()

# Sorting: How can you sort the products by their ratings in descending order?
df.sort_values('Rating',ascending=False)

# Date Calculations: How many years have passed since the launch of each product? (Hint: Use the current year.)
current_year=pd.Timestamp.now().year
df['y']=current_year-df['LaunchYear']

# Boolean Masking: How can you find all accessories with a rating greater than 4.5?

df[(df['Rating']>4.5) & (df['Category']=='Accessories')]


# Data Transformation: Create a new column PriceCategory that categorizes products as "Low" (<300), "Medium" (300-600), or "High" (>600).

def tr(price):
  if price <300:
    return 'low'
  elif price <600:
    return 'medium'
  else:
    return 'high'
  


df['range']=df['Price'].apply(tr)


# Correlation Analysis: Is there a correlation between the stock and the price of products?

df['Stock'].corr(df['Price'])


# Pivot Tables: How can you create a pivot table to show the average rating of products for each category?

pd.pivot_table(df,values='Rating',index='Category',aggfunc='mean')



# Top N Analysis: How can you find the top 3 most expensive products?

df.sort_values('Price',ascending=False).head(3)