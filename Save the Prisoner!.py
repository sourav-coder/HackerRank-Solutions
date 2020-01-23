
#----coded by sourav sarkar----#

t=int(input())
while(t>0):
    t-=1
    n,m,s=map(int,input().split())

    s-=1
    #if the sweets are divided completely
    if(m+s)%n==0:
        print(n)
    else:
        print((m+s)%n)
    
