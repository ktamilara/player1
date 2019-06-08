a11=int(input())
b1=input().split()
c1=[]
d1=''
for i1 in b1:
    if b1.count(i1)>1 and i1 not in c1:
        c1.append(i1)
if len(c1)>0:
    for i1 in range(len(c1)-1):
        d1+=c1[i1]+" "
    print(d1+c1[-1])
else:
    print("unique")
