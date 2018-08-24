def palindrome(num, dig):
    left =num[:dig/2]
    if dig%2==1:
        center=num[dig/2]
    else:
        center=''
    right=left[::-1]
    newnum=left+center+right
    if newnum>num:
        return newnum
    else:
        if center:
            if center<'9':
                center=str(int(center)+1)
                newnum=left+center+right
                return newnum
            else:
                center='0'
        if left==len(left)*'9':
            newnum= ('1'+(dig-1)*'0'+'1')
            return newnum
        else:
            numlist=list(left)
            end=len(left)-1
            while numlist[end]=='9':
                numlist[end]='0'
                end-=1
            numlist[end]=str(int(numlist[end])+1)
            left= ''.join(numlist)
            newnum=left+center+left[::-1]
            return newnum

import math
tcase=int(raw_input())
for i in xrange(tcase):
    num=raw_input()
    dig=len(num)
    newnum=palindrome(num, dig)
    print newnum
    


        

