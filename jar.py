K = int(input())
N=10
if K <= 5:
    print('NUMBER OF CANDIES SOLD : ', str(K))
    remaining = N-K
    print('NUMBER OF CANDIES AVAILABLE : '+ str(remaining))
else:
    print('INVALID INPUT')
    print('NUMBER OF CANDIES REMAINING : '+ str(N))
