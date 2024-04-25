class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
 def printPostOrder(root):
    if root == None:
        return
 
    # left_subtree, right_subtree, root
 
    printPostOrder(root.left)
    printPostOrder(root.right) 
    print(root.data, end = " ")
       
root=TreeNode(11)
b1=TreeNode(7)
b2=TreeNode(15)
b3=TreeNode(5)
b4=TreeNode(9)
b5=TreeNode(13)
b6=TreeNode(20)
b7=TreeNode(3)
b8=TreeNode(8)
b9=TreeNode(10)
b10=TreeNode(12)
b11=TreeNode(14)
b12=TreeNode(18)
b13=TreeNode(25)

root.left=b1
root.right=b2

b1.left=b3
b1.right=b4

b3.left=b7

b4.left=b8
b4.right=b9

b2.left=b5
b2.right=b6

b5.left=b10
b5.right=b11

b6.left=b12
b6.right=b13

printPostOrder(root)
