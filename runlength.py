s = input()
count = 0
final = ""
x = len(s)
i=0
flag= 0


for i in range(x):  #first for loop to going the entire length
    l = s[i]
    if not final:
        final = final + l
    else:
        for j in final:
            if l != j:
                flag=1
            else:
                flag = 0
        if(flag == 1):
            final = final + l

    for k in range(i+1,x):

        if l == s[k]:  # if state ment to start counting
            count = count + 1
        else:
            print("in here")
            count = count + 1
            count = str(count)
            final = final + count
            count = 0
print(final)
