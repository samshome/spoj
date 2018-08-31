def numzero(num):
    count=num/5
    while(num>5):
        num/=5
        count+=num/5
    print count
tcases= int(raw_input())

for _ in xrange(tcases):
    num=int(raw_input())
    numzero(num)
    
