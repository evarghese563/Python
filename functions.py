def computepay(h,r):
    if h <= 40:
        pay=h*r
    else:
        pay = h*r + ((h-40)*10.5)/2

    return pay

hrs = input("Enter Hours:")
rte = input("Enter Rate:")
hrs=float(hrs)
rte=float(rte)
p = computepay(hrs,rte)
print("Pay",p)
