k1=int(input())
l1=list(map(int,input().split()))
l1.sort(reverse=True)
for i1 in range(0,k1):
  print(l1[i1],end="")
