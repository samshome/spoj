def addsub(usrinput, len1, len2):
    if usrinput[1]=='-':
        diff=int(usrinput[0])-int(usrinput[2])
        len3=len(str(diff))
    if usrinput[1]=='+':
        add=int(usrinput[0])+int(usrinput[2])
        len3=len(str(add))
    maxlen=0
    if len3>=len2 and len3>=len1:
        maxlen=len3
    elif len2>=len1 and len1>=len3:
        maxlen=len2
    elif len1>=len2 and len1>=len3:
        maxlen=len1

    
    if maxlen==len2:
        print (maxlen-len1+1)*' '+usrinput[0]
        print (maxlen-len2)*' '+usrinput[1]+usrinput[2]
        print (maxlen+1)*'-'
        if(usrinput[1]=='-'):
            print ((len1+1)-len3)*' ' + str(diff)
            print
        else:
            print (maxlen-len3+1)*' ' + str(add)
            print
    else:
        print (maxlen-len1)*' '+usrinput[0]
        print (maxlen-len2-1)*' '+usrinput[1]+usrinput[2]
        print maxlen*'-'
        if(usrinput[1]=='-'):
            print ((len1)-len3)*' ' + str(diff)
            print
        else:
            print (maxlen-len3)*' ' + str(add)
            print
    

def mul(usrinput, len1, len2):
    mul=int(usrinput[0])*int(usrinput[2])
    len3=len(str(mul))
    if len3==len2:
        maxlen=len2+1
    else:
        maxlen=len3
    print (maxlen-len1)*' '+usrinput[0]
    print (maxlen-len2-1)*' '+usrinput[1]+usrinput[2]
    if(len1>=len2 and len2!=1):
        print (maxlen-len1-1)*' '+(len1+1)*'-'
    if(len2>len1):
        print (maxlen-len2-1)*' '+(len2+1)*'-'
    
    second=list(usrinput[2])
    if len(second)==1:
        print maxlen*'-'
        print mul
    else:
        plus=0
        str1=''
        for l in reversed(xrange(len2)):
            str1=str(int(usrinput[0])*int(second[l]))
            print (maxlen-len(str1)-plus)*' '+str1+plus*' '
            plus+=1
        print (maxlen-len3)*' ' + len3*'-'
        print (maxlen-len3)*' ' + str(mul)
        print
        
import re
tcase=int(raw_input())
for _ in xrange(tcase):
    ginput=raw_input()
    usrinput=re.split("([+-/*])",ginput)
    
    len1=len(usrinput[0])
    len2=len(usrinput[2])
    
    if usrinput[1]=='+' or usrinput[1]=='-':
        addsub(usrinput, len1, len2)
    elif usrinput[1]=='*':
        mul(usrinput, len1, len2)
        
