# date manipulation in pandas

import pandas as pd
import numpy as np

# Creating a raw DataFrame
data = {
    'order_id': [101, 102, 103, 104, 105],
    'order_date': ['2023-05-01', '2023-06-15', '2023-07-20', '2023-08-25', '2023-09-30'],
    'delivery_date': ['2023-05-05', '2023-06-20', '2023-07-25', '2023-08-30', '2023-10-05'],
    'amount': [250, 400, 150, 300, 500]
}
df = pd.DataFrame(data)

# Display the raw DataFrame
df




# Convert the order_date and delivery_date columns to datetime format. Verify their datatypes.

df['order_date']=pd.to_datetime(df['order_date'])
df['delivery_date']=pd.to_datetime(df['delivery_date'])

# Calculate the delivery time (in days) for each order and add it as a new column delivery_time.

df['del_days']=(df['delivery_date']-df['order_date']).dt.days




# # Filter the DataFrame to include orders where the amount is greater than 300.
df[df['amount']>300]

# Extract the month from order_date and delivery_date and add them as new columns order_month and delivery_month.

df['order_month']=df['order_date'].dt.month_name()
df['del_month']=df['delivery_date'].dt.month_name()

# Find the total amount for orders placed in the month of June 2023.
df[
(df['order_date']>'2023-06-01') & 


(
df['order_date']<'2023-06-30' )]['amount'].sum()



# Sort the DataFrame by delivery_date in ascending order.

df.sort_values('delivery_date')


# Identify orders where the delivery took more than 4 days.
df[df['del_days']>4]


# Add 10 days to the delivery_date and create a new column follow_up_date.
df['folow_date']=df['delivery_date']+pd.Timedelta(days=10)
