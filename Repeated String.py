

#coded by ss

s=input()
n=int(input())
# if len(s)==1:print(n)
print(s.count('a')*(n//len(s))+s[:n%len(s)].count('a'))



