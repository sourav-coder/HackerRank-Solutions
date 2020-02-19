


#coded by ss


a=[]
a.append(1)
a.append(2)
for i in range(2,61):
      if i%2==0:
        a.append(a[i-1]+1)
      else:
        a.append(a[i-1]*2)


for _ in range(int(input())):
  n=int(input())
  print(a[n])
