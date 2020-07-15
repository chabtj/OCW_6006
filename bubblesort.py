a=[0,1,5,2,34,2,1,345,3]
for i in range (0,len(a)):
	for j in range (0,len(a)-i-1):
		if a[j]>a[j+1]:
			a[j],a[j+1]=a[j+1],a[j]
for i in a:
	print (i)
