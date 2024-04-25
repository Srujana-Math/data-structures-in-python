class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=TreeNode(2)
l1=TreeNode(7)
r1=TreeNode(5)
l2=TreeNode(2)
r2=TreeNode(6)
r3=TreeNode(9)
l4=TreeNode(5)
r4=TreeNode(11)
r5=TreeNode(4)

root.left=l1
root.right=r1

l1.left=l2
l1.right=r2

r1.right=r3

r2.left=l4
r2.right=r4

r3.left=r5

def printLevelOrder(root):
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
     
            curr = Q.pop(0)
            subResult.append(curr.data)

            if curr.left != None:
                Q.append(curr.left)

            if curr.right != None:
                Q.append(curr.right)
 
        result.append(subResult)
 
    print(result)
  printLevelOrder(root)
