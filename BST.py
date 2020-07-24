class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  

def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 

def BSTsort(root): 
    if root: 
        BSTsort (root.left) 
        print(root.val) 
        BSTsort(root.right) 



root=Node(50)
insert(root,Node(10))
insert(root,Node(65))
insert(root,Node(40))
BSTsort(root)


                #     50
                #  /      \
                # 10       65
                #         /
                #       40

