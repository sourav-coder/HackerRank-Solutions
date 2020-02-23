
#right rotation


#coded by ss
n,k,q=map(int,input().split())
a=list(map(int,input().split()))
c=[]
for i in range(n):
    c.append(a[(i+(n-k))%n])
while q>0:
    q-=1
    k=int(input())
    print(c[k])
