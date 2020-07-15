def peak1D(a):
	l=0
	h=len(a)
	mid=(l+h)//2
	print (mid)
	print(a)
	if(mid-1<len(a) and mid+1<len(a) and a[mid]>a[mid-1]and a[mid]>a[mid+1] ):
		return a[mid]
	elif (len(a)>1 and a[mid+1]>a[mid]):
		peak1D(a[mid:])
	elif (len(a)>1 and a[mid-1]>a[mid]):
		peak1D(a[:mid])

peak1D([0,2,3,4,5,6,1,2])

# def peak2D(b):
# 	while (True):
# 		x=len()



