hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
pay = h*r
opay = (((h-40)*(1.5*r))+(40*r))
if(h<=40):
    print(pay)
else:
    print(opay)
