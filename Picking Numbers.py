
n=int(input())
a=list(map(int,input().split()))
b=set(a)
# print(b)
l=0
for i in b:
    c=0
    d=0
    
    if i+1 in b :
        c+=a.count(i+1)
        
    if abs(i-1) in b :
        d+=a.count(abs(i-1))
    
        


    
    m=max(c,d)+a.count(i)
    l=max(l,m)
    
    

print(l)

