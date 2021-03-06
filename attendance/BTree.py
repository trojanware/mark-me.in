class Node:
  def __init__(self,data=None,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.data)

class Tree:
  def getSubjectList(self,lst):
    self.ans = []
    root = Node()
    for day in lst:      
      newNode = Node(data=day)
      if root.data == None:
        root = Node(data=day)
	continue
      temp = root
      temp1 = root
      while not temp==None and not temp.data == day:
	if temp.data<day:
	  temp1 = temp
	  temp = temp.right
	else:
	  temp1 = temp
	  temp = temp.left
      if temp==None:
	if temp1.data<day:
	  temp1.right = newNode
	else:
	  temp1.left = newNode
      elif temp.data==day:
	pass
	  #print "%s is a dup" % hour

    self.inorder(root)
    return self.ans

  def inorder(self,root):
    if not root==None:
      self.inorder(root.left)
      self.ans.append(root.data)
      self.inorder(root.right)
