p=float(input("enter the amount:"))
t=float(input("enter the time period in year:"))
r=float(input("enter the rate of interest:"))
si=(p*t*r)/100
total_amount=p+si
print("simple interest:",si)
print("total amount:",total_amount)