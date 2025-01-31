# psudocode


a=[1,3,5,7,2]


# find lowest value while going right
# find highest value while going right
# and take diffrence

lowest=float('inf')
max_profit=0

for price in a:
    if price<lowest:
        lowest=price

        profit=price-lowest

    if profit>max_profit:
        max_profit=profit

return max_profit