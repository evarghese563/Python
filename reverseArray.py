x = int(input())

while  x > 0 :

    n = int(input())
    #l = list()
    l = list(map(int, input().rstrip().split()))

    print(l)
    j = len(l)
    start = 0
    end = j - 1

    while start > end:
        l[start], l[end] = l[end], l[start]
        start = start + 1
        end = end - 1

    print(l)
