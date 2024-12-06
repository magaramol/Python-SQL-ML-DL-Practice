# Revenue Analysis: What is the total revenue generated across all transactions?

df['SaleAmount'].sum()


# Top Customers: Which customer made the highest purchase, and what was the amount?

df.groupby('CustomerName')['SaleAmount'].sum().sort_values(ascending=False).head(1)



# Average Quantity: What is the average quantity of items sold per transaction?


df['Quantity'].mean()

# Category Contribution: What percentage of total sales revenue comes from each category?
(df.groupby('Category')['SaleAmount'].sum()/df['SaleAmount'].sum()*100)


# Date Filtering: How can you filter sales transactions that occurred in February 2024?


df[(df['SaleDate']>'2024-02-01') &  (df['SaleDate']<'2024-02-29')]

# Unique Products: How many unique products were sold?
df['Product'].nunique()


# Cumulative Sales: How can you calculate the cumulative sales amount over time?


df.sort_values('SaleDate',ascending=True,inplace=True)

df['cumsums']=df['SaleAmount'].cumsum()

# Top-Selling Product: Which product generated the most revenue, and how much was it?
df.groupby('Product')['SaleAmount'].sum().sort_values(ascending=False).head(1)

# Average Sales Per Category: What is the average sale amount for each category?


df.groupby('Category')['SaleAmount'].mean()

# Revenue per Item: Create a new column RevenuePerItem that calculates the sale amount per item for each transaction.

df['rev']=df['SaleAmount']/df['Quantity']


