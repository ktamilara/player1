p1,q1=map(int,input().split())
l1=list(map(int,input().split()))
res1=0
for i1 in range(len(l1)):
  if (l1[i1]==q):
    res1+=1
    print("Yes")
    break
else:
  print("No")
