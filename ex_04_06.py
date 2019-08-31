def computepay(hour,rate):
    if(hour<=40):
        reg = hour*rate
        pay = reg
    else:
        over = (((hour-40)*(1.5*rate))+(40*rate))
        pay = over
    return pay
shrs = input("Enter Hours:")
srate = input("Enter Rate:")
h = float(shrs)
r = float(srate)
p = computepay(h,r)
print(p)

#
