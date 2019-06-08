n1,m=map(int,input().split())
a11=[int(n1) for n1 in input().split()]
b11=[int(m1) for m1 in input().split()]
cu1=0
for i1 in range(0,len(b11)):
    for j1 in range(0,len(a11)):
        if b11[i1]==a11[j1]:
            cu1 +=1
if cu1==len(b11):
    print("YES")
else:
    print("NO")
