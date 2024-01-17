def customer_receipt():

  meals_ordered = True

  sub_total = 250.87

  tip = sub_total * 0.10

  total = sub_total + tip

  

  if meals_ordered:

    return f'Your total is ${total:.2f}'

    



print(customer_receipt())


# - - - - - - - - - - - - - - - - - - - -



# meals_ordered = True

# sub_total = 250.87

# tip = sub_total * 0.10

# total = sub_total + tip

# receipt = "Your total is " + "$" + str(total)

# print(receipt)

