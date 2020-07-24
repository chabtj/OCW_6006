class Node:
	def __init__(self,value):
		self.value=value
		self.next=None





class llist:
	def __init__(self):
		self.head=None

	def addelement(self,value):
		newnode=Node(value)
		if self.head is None:
			self.head=newnode
		else :
			ptr=self.head
			while ptr.next is not None:
				ptr=ptr.next 
			ptr.next=newnode
	
	def addbeg(self,value):
		newnode=Node(value)
		if(self.head is None):
			self.head=newnode
		else:
			tmp=self.head
			self.head=newnode
			self.head.next=tmp

	def deletebeg(self):
		tmp=self.head
		del(tmp)
		self.head=self.head.next

	def deleteend(self):
		tmp=self.head
		tmp1=self.head.next
		while(tmp1.next is not None):
			tmp=tmp.next
			tmp1=tmp1.next
		tmp.next=None
		del(tmp1)

	

	def printlist(self):


		ptr=self.head
		
		while ptr is not None:
			print (ptr.value)
			ctr=1
			ptr=ptr.next



l1=llist()
l1.addelement("mon")
l1.addelement("tue")
l1.addelement("wed")
l1.addbeg("hello")
l1.addbeg("bye")
l1.addelement("hello")
l1.deleteend()
l1.deletebeg()
l1.printlist()



