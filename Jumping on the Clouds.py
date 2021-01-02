# Coded by Sourav Sarkar 
n=int(input())
a=list(map(int,input().split()))
c=0
f=0
i=0
try:

    while i<len(a)-1:
        if  a[i]==0 and   a[i+2]==0 :
            c+=1
            i+=2
        elif a[i]==0 and a[i+1]==1:
            c+=1
            i+=2
        else:
            c+=1
            i+=1
        # print(c,i)
        
except: IndexError
if i==len(a)-2:print(c+1)
else:
    print(c)
    
