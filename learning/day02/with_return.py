def milk_total(milk1,milk2):
    Total_milk = milk1+milk2
    return Total_milk
milk1=int(input("Milk produced by cow1:"))
milk2=int(input("Milk produced by cow2:"))
total_milk=milk_total(milk1,milk2)
print(f"Total milk produced by cow1 and cow2 is:{total_milk} litres")
