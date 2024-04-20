class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next
    print()
 
def insertAtEndOfTail(head, ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    curr = head 
    while curr.next != None:
        curr = curr.next 
    curr.next = newBlock
    return head
def deleteAtEnd(head):
    curr = head
    previous = None
    while curr.next != None:
        previous = curr
        curr = curr.next
    previous.next = None
    return head

def deleteHeadNode(head):
    if head==None:
        return None
    secondNode=head.next
    head.next=None
    return secondNode
def deleteAtSpecificPosition(head,position):
    if position==1:
        return deleteHeadNode(head)
    curr=head
    index=1
    while index!=position-1:
        curr=curr.next
        index+=1
    mainNode=curr.next
    nextNode=mainNode.next
    mainNode.next=None
    curr.next=nextNode
    return head

l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
    head = insertAtEndOfTail(head, ele) 
head = deleteAtEnd(head)
printLinkedList(head) 

l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
    head = insertAtEndOfTail(head, ele) 
head = deleteHeadNode(head)  
printLinkedList(head)  

l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
    head = insertAtEndOfTail(head, ele) 
head = deleteAtSpecificPosition(head,6)
printLinkedList(head)
