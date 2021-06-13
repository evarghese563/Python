def poix(m1,c1,m2,c2):
    num = (-c1*1) - (-c2*1)
    den = (1*(-m2)) - (1*(-m1))
    xval = round(num/den)
    return xval

def poiy(m1,c1,m2,c2):
    num = (-m1*-c2) - (-m2*-c1)
    den = (1*(-m2)) - (1*(-m1))
    yval = round(num/den)
    return yval


print('Slope formula: y=mx+b')
m1 = float(input("Enter m1: \n"))
c1 = float(input("Enter c1: \n"))

m2 = float(input("Enter m2: \n"))
c2 = float(input("Enter c1: \n"))

if m1 == m2:
    print("Line segments do not intersect")
else:
    x = poix(m1,c1,m2,c2)
    y = poiy(m1,c1,m2,c2)
    print("The point of intersection is (" , x , "," , y , ")")
