class ListNode:
    def __init__(self, val=0,next=None):
        self.val =val
        self.next = next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

val = 6

def showlinkedlist(head):
    if head == None:
        return 
    
    current = head
    last = head

    while current.val == val and current:
        current = current.next
    
    newhead = current

    while current and last:
        current = current.next

        if current == None:
            break

        if current.val == val and current.next == None:
            last.next = None
            current == None

        if current == None:
            break

        if current.val == val:
            last.next = current.next

        if current == None:
            break

        if current.val != val:
            last = last.next
            
    return newhead


a = showlinkedlist(head)

def printlist(node):
    current = node

    while current:

        print(current.val)
        current = current.next

printlist(a)