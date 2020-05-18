price=float(input("Enter or scan price of the product : "))
tax=float(input("applicable tax : "))
total=float(price+(float((price*tax)/100)))
print('Total :',total.__round__(2))

