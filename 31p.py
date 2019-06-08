s1=input()
t1=[]
r1=[]
for i1 in s1:
  if i1=='(':
    t1.append(i1)
  elif i1==')':
    r1.append(i1)
if len(t1)==len(r1):
  print("yes")
else:
  print("no")
