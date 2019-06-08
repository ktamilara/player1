nu11=int(input())
nu21=input().split()
l1=[]
for i1 in range(0,nu11):
  if(int(nu21[i1])==i1):
    l1.append(nu21[i1])
if(l1==[]):
  print("-11")
else:
  l1.sort()
  for j1 in range(0,len(l)):
    print(l1[j1],end=" ")
