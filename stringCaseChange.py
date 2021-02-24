T = int(input())

for i in range(T):

    s = input()
    l = s[0]
    if l.isupper():
        print(s.upper())
    else:
        print(s.lower())
