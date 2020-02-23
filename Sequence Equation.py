
#coded by ss




n=int(input())
a=list(map(int,input().split()))
for i in range(1,n+1):
    c=i
    j=a.index(c)+1
    print(a.index(j)+1)
