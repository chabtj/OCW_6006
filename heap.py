import math
import numpy as np
def createheap(a):
	
	for i in range ( 1,len(a)+1 ):
		
		x=i//2
		j=i
		
		while(x>=1 and a[j-1]>a[x-1]):
		
			a[j-1],a[x-1]=a[x-1],a[j-1]
			j=x
			x=x//2
	return(a)




# def deleteheap(a):
# 		j=i=1
# 		#for i in range (1,len(a))
# 		#if oen of the two childs is greater then swap 
# 		heapsize=len(a)
# 		while ( heapsize!=0):
		
# 			element=a[0]
# 			print ( heapsize)
# 			print ((math.log(heapsize,2)))
# 			a[i-1]=a[heapsize-1]
# 			for ctr in range (1,(int)(math.log(heapsize,2))):
# 				if (j*2+1<heapsize):
# 					child1=a[i*2-1]
# 					child2=a[i*2]
# 					if (child1>=child2):
# 						a[j-1],a[j*2-1]=a[j*2-1],a[j-1]
# 						j=j*2
# 					else:
# 						a[j-1],a[j*2]=a[j*2],a[j-1]
# 						j=(j*2)+1
# 				print (a)

# 			a[heapsize-1]=element
# 			heapsize-=1
			
		




def delheap(a):
	
	for heapsize in range (len(a),0,-1):
		i=j=1
		element=a[0]
		a[0]=a[heapsize-1]
		#heapify
		while( j*2+1<=heapsize):
			if(a[j*2-1]>a[j*2]):
				a[j-1],a[j*2-1]=a[j*2-1],a[j-1]
				j=j*2
			else:
				a[j-1],a[j*2]=a[j*2],a[j-1]
				j=(j*2)+1
		a[heapsize-1]=element
		print(a)



