T = int(input())

for i in range(T):
    s = input()
    x = len(s)

    if x > 10:
        n = x-2
        print(s[0]+str(n)+s[x-1])
    else:
        print(s)
