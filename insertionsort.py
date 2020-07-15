a=[4,6,2,3,2,8,5,1,0]
for i in range (1,len(a)):
	key=a[i]
	j=i-1
	while (j>=0 and key<a[j]):
		a[j+1]=a[j]
		j-=1;
	a[j+1]=key

for i in a:
	print(i)