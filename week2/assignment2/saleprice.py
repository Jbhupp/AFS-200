product = input("Please enter a description of the product: ")
#print(product)

quantity = int(input(f"Please enter a quantity of the {product} being purchased: "))
#print(quantity)

price = float(input(f"Please enter a price for this item: "))
#print(price)

if price> 39.99:
    discountPrice = price * .75
    print('Great news! You get 25 percent off.')
elif price> 19.99:
    discountPrice = price * .85
    print('Great news! You get 15 percent off.')
else:
    discountPrice = price
    
discountTotal = quantity * discountPrice

total = float(quantity * price)
savings = float(total - discountTotal)

tax = float(discountTotal * .065)

finalTotal = float(discountTotal + tax)

print(f"Your Receipt \n {quantity} {product}s at ${discountPrice:,.2f} \n Sales Tax ${tax:,.2f} \n Total amount due ${finalTotal:,.2f} \n You Saved ${savings:,.2f} Today.")
