class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
b1=Node(10)
b2=Node(20)
b3=Node(30)
b4=Node(40)
b5=Node(50)
b6=Node(60)
b7=Node(70)
b8=Node(80)
b9=Node(90)
b10=Node(100)

b1.next=b2
b2.next=b3
b3.next=b4
b4.next=b5
b5.next=b6
b6.next=b7
b7.next=b8
b8.next=b9
b9.next=b10
curr=b1
while curr!=None:
    print(curr.data,end="-->")
    curr=curr.next
