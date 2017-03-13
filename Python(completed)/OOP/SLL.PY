class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None



class SinglyLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def PrintAllVals(self):
		this = self.head
		while(this.next!=None):
			print this.value
			this=this.next
		print this.value

	def AddBack(self, value):
		this = self.head
		while(this.next!=None):
			this=this.next
		this.next = Node(value)
	def AddFront(self, value):
		pointer = self.head
		self.head = Node(value)
		self.head.next = pointer
	def InsertBefore(self, nextValue, value):
		location = self.head
		while(location.value != value):
			location = location.next
			if location.next==None:
				print -1
			location2 = location
			location = location.next
		pointer = location2.next
		location2.next = Node(nextValue)
		location2.next.next = pointer
	def InsertAfter(self, preVal, value):
		location2 = self.head
		while(location2.value != value):
			location2 = location2.next
			if location2.next==None:
				print -1
			location = location2
			location2 = location.next
		pointer = location.next
		location.next = Node(preVal)
		location.next.next = pointer
	def RemoveNode(self, value):
		location = self.head
		while(location.value != value):
			location2 = location
			location = location.next
		temp = location.next
		location.next = None
		location2.next = temp
		



list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')
list.AddBack('Brandon')
list.AddFront('Jeffery')
list.InsertBefore('Shannon', 'Chad')
list.InsertAfter('James', 'Debra')
list.RemoveNode('James')
list.PrintAllVals()
