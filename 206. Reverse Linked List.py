class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c

head = a

def print_list(head):

    current = head

    while current:
        print(current.val)
        current = current.next
        
def reverse_list(head):

    current = head
    pre = None

    while current:
        next_node = current.next
        current.next = pre
        pre = current
        current = next_node
    
    return pre

head = reverse_list(head)


print_list(head)