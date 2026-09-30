def revenue(milk,price):
    total_revenue = milk * price
    return total_revenue
milk=float(input("Milk produced:"))
price=float(input("Price per litre:"))
total_revenue=revenue(milk,price)
print(f"Total revenue from milk is : {total_revenue} rupees")