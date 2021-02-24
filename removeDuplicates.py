T = int(input())

for i in range(T):

    n = int(input())         ###
    arr = []                 ###
    for j in range(0, n):    ###  Inputtinng into the array
        a = int(input())     ###
        arr.append(a)        ###
    #print(arr)


    for k in range(0, n):               ###travesing through the list
        print()
        #print(k,",", n)
        if k < n:
            #print("in if")
            for l in range(k, n):         ###
                #print(k,",", l, ",", n)
                if arr[k] == arr[l]:
                    #print(k,",", l, ",", n)
                    del arr[l]
                    n=n-1
    print(arr)
