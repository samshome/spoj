def palindrome(num, ndig):
    count=0
    if ndig%2==1:
        ptl=ndig/2+1
        ptr=ndig/2-1
        for o in xrange(ndig/2):
            if(dig[ptl]>dig[ptr]):
                for k in range(ptl, ndig):
                    dig[ptr]=dig[k]
                    ptl=ptl+1
                    ptr=ptr-1
                return dig
            elif(dig[ptr]>dig[ptl]):
                dig[ndig/2]=dig[ndig/2]+1
                for k in range(ptl, ndig):
                    dig[ptr]=dig[k]
                    ptl=ptl+1
                    ptr=ptr-1
                return dig
            count=count+1
            ptl=ptl+1
            ptr=ptr-1
            if count==ndig/2:
                dig[ndig/2]=dig[ndig/2]+1
                return dig
    elif ndig%2==0:
        ptl=ndig/2
        ptr=ndig/2-1
        for o in xrange(ndig/2):
            if(dig[ptl]>dig[ptr]):
                for k in range(ptl, ndig):
                    dig[ptr]=dig[k]
                    ptr=ptr-1
                    ptl=ptl+1
                return dig
            elif(dig[ptr]>dig[ptl]):
                dig[ndig/2]=dig[ndig/2]+1
                for k in range(ptl, ndig):
                    dig[ptr]=dig[k]
                    ptl=ptl+1
                    ptr=ptr-1
                return dig
            count=count+1
            ptl=ptl+1
            ptr=ptr-1
            if count==ndig/2:
                dig[ndig/2-1]=dig[ndig/2-1]+1
                dig[ndig/2]=dig[ndig/2]+1
                return dig
    
    
import math
tcase=int(raw_input())
for i in xrange(tcase):
    knum=raw_input()
    ndig=len(knum)
    num=int(knum)
    dig=range(0, ndig)
    gnum=num
    nine=0
    for k in xrange(ndig):
        dig[k]=num%10
        num/=10
        if dig[k]==9:
            nine+=1
    if ndig==1 and num!=9:
        print 11
        continue
    if nine==ndig:
        gnum+=2
        print gnum
        continue
    rdig=palindrome(dig, ndig)
    k=ndig/2
    for l in range(ndig/2, ndig):
        if rdig[l]==10:
            rdig[l+1]=rdig[l+1]+1
            rdig[k-1]=rdig[k-1]+1
            rdig[l]=0
            rdig[k]=0
        k-=1
    finale=""
    for h in xrange(ndig):
        finale = finale+str(rdig[h])
    print finale

        

