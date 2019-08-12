def sums(st):
	k=0
	for j in range(0,len(st)):
		k+= int(st[j])

n= int(input())
a=[]
for i in range(0,n):
	a.append(str(input()))
	
a.sort()
a.reverse()
a.append("0")
s=""
x=""
t=""
y=""
for i in range(0,n):
	x=""
	y=""
	if(sums(a[i]) != sums(a[i+1])):
		s=s+a[i]
	elif(sums(a[i])==sums(a[i+1])):
		x=a[i]+a[i+1]
		y=a[i+1]+a[i]
		if(x>y):
			s+=a[i]
		else:
			t=a[i]
			a[i]=a[i+1]
			a[i+1]=t
			s+=a[i]
print(s)
#print(a[:-1])
