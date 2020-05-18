from price import total

amount_tendered=float(input("enter the money tendered :"))
change=float((amount_tendered-total).__round__(2))
print(change)