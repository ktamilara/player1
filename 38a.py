a1=int(input())
b1=''
for i1 in range(2,a1,2):
    if a1%i1==0:
        b1+=str(i1)+" "
print(b1+str(a1))
