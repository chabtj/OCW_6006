a=[0,2,5,43,3,5,6,4,8,9,5,76]
for i in range (len(a)):
	
	pos=i
	for j in range(i+1,len(a)):
		if (a[j]<a[i]):
			pos=j
	tmp=a[i]
	a[i]=a[pos]
	a[pos]=tmp


print (a)
