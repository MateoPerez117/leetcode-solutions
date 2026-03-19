class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

head = ListNode(1)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
e = ListNode(3)

head.next = b
b.next = c
c.next = d
d.next = e

def remove_ahora_si(head):

    if not head or not head.next:
        return head

    current = head

    while current and current.next:
        if current.val == current.next.val:
            if current.next.next:
                current.next = current.next.next
            else:
                current.next = None
        else:
            current = current.next
    
    return head

remove_ahora_si(head)

def pirntlist(head):

    current = head

    while current:
        print (current.val)
        current = current.next

pirntlist(head)
