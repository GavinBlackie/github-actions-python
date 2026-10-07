
def calculate_total(price, quantity):
    return price * quantity

def apply_taxes(price):
    return price * 1.13

price = 25
quantity = 4
total = calculate_total(price, quantity)
print(f"Price: ${price}")
print(f"Quantity: ${quantity}")
print(f"Total: ${total}")
totalWithTax = apply_taxes(total)
print(f"Total with Taxes: ${round(totalWithTax, 2)}")