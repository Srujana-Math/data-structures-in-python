class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printTopViewOfBinaryTree(root):
    result = []
 
    Q = [[root, 0]]
    store = dict()
    while len(Q) > 0:
        currPair = Q.pop(0)

        node = currPair[0]
        hd = currPair[1]

        if hd not in store:
            store[hd] = node.data 
 
        if node.left != None:
            Q.append([node.left, hd - 1])
 
        if node.right != None:
            Q.append([node.right, hd + 1])

    allKeys = sorted(store.keys())
    for eachKey in allKeys:
        result.append(store[eachKey])
 
    print("Top view of binary-tree is:")
    print(result)
 
root = TreeNode(18)

obj2 = TreeNode(15)
obj3 = TreeNode(20)
obj4 = TreeNode(25)
obj5 = TreeNode(30)
obj6 = TreeNode(45)
obj7 = TreeNode(80)

root.left = obj2 
root.right = obj3 
 
obj2.left = obj4 
obj2.right = obj5 
 
obj3.left = obj6 
obj3.right = obj7

printTopViewOfBinaryTree(root)
