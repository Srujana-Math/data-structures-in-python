n=int(input())
num=list(map(int,input().split()))
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insertIntoBST(root,ele):
    newblock=TreeNode(ele)
    if root== None:
        return newblock

    if root.data<ele:
        root.right=insertIntoBST(root.right,ele)
    else:
        root.left=insertIntoBST(root.left,ele)
    return root

def printInOrder(root):
    if root ==None:
        return

    printInOrder(root.left)
    print(root.data,end=" ")
    printInOrder(root.right)

root=None
for ele in num:
    root=insertIntoBST(root,ele)

printInOrder(root)
