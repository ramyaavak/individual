n=raw_input()
r=len(n)
k=0
for i in range(0,r):
	if(n[i]=='0' or n[i]=='1'):
		k=k+1
	 
if(r==k):
	print("yes")
else:
	print("no")
