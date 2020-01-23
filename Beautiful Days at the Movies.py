

i, j, k = map(int, input().split())
c=0
for p in range(i, j + 1):
    
    #reverse each element
    r=list(reversed(str(p)))  
    r=''.join(r)
    r=int(r)
    if abs(p-r)%k==0:
        c+=1


    #print(r)

print(c)













