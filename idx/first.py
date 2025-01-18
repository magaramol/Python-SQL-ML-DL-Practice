# first code on idx machine

import pandas as pd


# Creating a raw DataFrame
data = {
    'order_id': [101, 102, 103, 104, 105],
    'order_date': ['2023-05-01', '2023-06-15', '2023-07-20', '2023-08-25', '2023-09-30'],
    'delivery_date': ['2023-05-05', '2023-06-20', '2023-07-25', '2023-08-30', '2023-10-05'],
    'amount': [250, 400, 150, 300, 500]
}
df = pd.DataFrame(data)