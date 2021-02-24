x = input()
l = x.split(' ')
x = l[0]
y = l[1]

for i in range(1,y+1):
    print(x,'x',i,'=',x*i)
