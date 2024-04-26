n=int(input())
num=list(map(int,input().split()))
target=int(input())
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

def searchInBST(root,target):
    if root==None:
        return False
    if root.data==target:
        return True
     
    elif root.data<target:
        return searchInBST(root.right,target)
    else:
        return searchInBST(root.left,target)

root=None
for ele in num:
    root=insertIntoBST(root,ele)

if searchInBST(root,target):
    print("Target element is found")
else:
    print("Target element is not found")
