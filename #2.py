from math import sqrt
tcase=int(raw_input())

for i in range (0, tcase):
    num=map(int, raw_input().split())
    for n in range(num[0], num[1]+1):
        isprime=True
        for k in range(2, int(sqrt(n))+1):
            if n%k==0:
                isprime=False
                break
        if isprime==True and n!=1:
            print n
                
    
