class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
        p = Node(data)        
        if head==None:
            head=p
        elif head.next==None:
            head.next=p
        else:
            start=head
            while(start.next!=None):
                 start=start.next
            start.next=p
        return head 
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next

    def removeDuplicates(self, head):
        # If the list is empty or has only one node, no need to remove duplicates
        if head == None or head.next == None:
            return head

        current = head
        while current != None and current.next != None:
            if current.data == current.next.data:
                # Skip the duplicate node
                current.next = current.next.next
            else:
                # Move to the next distinct node
                current = current.next
        return head
        
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)   
head=mylist.removeDuplicates(head)
mylist.display(head);
