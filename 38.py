s5=int(input())
a5=""
for i5 in range(1,s5+1):
	if s5%i==0 and i5%2==0:
		a5=a5+str(i5)+" "
print(a5.strip())
