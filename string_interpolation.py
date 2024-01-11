# Homework
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
price_item = {
    "Purse": 189.00,
    "Watch": 979.00,
    "Tie": 9.00
}

def price_formatter(price_obj):
    formatted_prices = ''
    for item in price_obj:
        formatted_price = f'{item} {price_obj[item]:>8}\n'
        formatted_prices += formatted_price
            

    total = 0
    for price in price_obj:
            unadded_price = price_obj[price]
            total += unadded_price
            

    total_price = f'{formatted_prices}\nTotal price: ${total:,.2f}'
        
    return total_price 


print(price_formatter(price_item))
