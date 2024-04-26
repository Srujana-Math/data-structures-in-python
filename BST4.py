n=int(input())
num=list(map(int,input().split()))
k=int(input())
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

def fillInOrder(inorder,root):
    if root ==None:
        return

    fillInOrder(inorder,root.left)
    inorder.append(root.data)
    fillInOrder(inorder,root.right)



root=None
for ele in num:
    root=insertIntoBST(root,ele)
    
inorder=[]
fillInOrder(inorder,root)
inorder=inorder[::-1]
print(inorder[k-1])
