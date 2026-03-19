class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

head = ListNode(1)
b = ListNode(2) 
c = ListNode(3) 
d = ListNode(-5)

head.next =  b
b.next = c
c.next = d

def oddeven(head):
    if not head or not head.next:
        print ("head")

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next
    
    odd.next = even_head

    return head

def print_linked_list(head):

    current = head
    nexthead = current.next

    while current:
        contador += 1
        current = current.next

    return contador

print(print_linked_list(head))
