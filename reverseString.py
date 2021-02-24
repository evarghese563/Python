T = int(input())

for r in range(T):
    x = int(input())
    temp = int(x/10)
    z = 1
    rev = 0
    while (temp != 0):
        temp = int(temp / 10)
        z = z*10
    while x != 0:
        n = (x%10)*z
        rev = rev + n
        z = int(z/10)
        x = int(x/10)
    print(rev)
