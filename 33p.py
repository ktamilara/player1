n11=int(input())
l1=[]
c1=0 
for i1 in range(n11):
    l1.append(list(map(int,input().split())))
if n11==1 and  l1[0]==[1]:
     print('11')
else:
    for i1 in range(n11):
        for j1 in range(n11):
            if l1[i1][j1]==1:
                if i1==0 and j1==n11-1:
                    if(l1[i1][j1-1]==0 and l1[i1+1][j1]==0):
                            c1=c1+1
                elif i1==0 and j1==0:
                    if l1[i1][j1+1]==0 and l1[i1+1][j1]==0:
                        c1=c1+1
                elif i1==0 and l1[i1][j1-1]==0 and l1[i1][j1+1]==0 and l1[i1+1][j1]==0:
                    c1=c1+1
                elif i1==n11-1 and j1==n11-1:
                    if l1[i1-1][j1]==0 and l1[i1][j1-1]==0:
                        c1=c1+1
                elif i1==n11-1 and l1[i1][j1-1]==0 and l1[i1][j1+1]==0 and l1[i1-1][j1]==0:
                    c1=c1+1
                elif i1!=0 or i1!=n11-1 and (l1[i1][j1+1]==0 and l1[i1+1][j]==0 and l1[i1-1][j1]==0 and l1[i1][j1-1]==0):
                    c1=c1+1
    print(c1)    
