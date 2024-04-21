class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None 

def addNodeAtTailOfLinkedList(head, val):
    newBlock = Node(val)
 
    if head == None:
        return newBlock
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = newBlock 
    newBlock.prev = tail 
    return head

 
def printLeftToRightManner(head):
    print("Left to Right")
    curr = head 
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
def printRightToLeftManner(head):
    print("Right to Left")
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    curr = tail
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.prev 
    print()
 
def deleteAtTailNode(head):
    if head==None or head.next==None:
        return None

    curr=head
    previous=None
    while curr.next!=None:
        previous=curr
        curr=curr.next
    previous.next=None
    curr.prev=None
    return head

def deleteNodeAtHead(head):
    if head==None or head.next==None:
        return None
    secondnode=head.next
    head.next=None
    secondnode.prev=None
    return secondnode
def deleteAtSpecificPosition(head,position):
    if position==1:
        return deleteNodeAtHead(head)
    curr=head
    index=1
    while index != position-1:
        curr=curr.next
        index+=1
    
    nodeToBeDeleted = curr.next 
    nextNode = nodeToBeDeleted.next 
    curr.next = nextNode 
    nextNode.prev = curr 
    return head
    
l = [11, 22, 33, 44, 55, 66, 77, 88, 99]
head = None 
for ele in l:
    head = addNodeAtTailOfLinkedList(head, ele)
head=deleteNodeAtHead(head)
printLeftToRightManner(head)
printRightToLeftManner(head)   
