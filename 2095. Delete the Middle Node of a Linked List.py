class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

head = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

head.next = b
b.next = c
c.next = d
d.next = e 

def middle(head):
    current =  head
    listlen = 0

    while current:
        listlen += 1
        current =  current.next

    middle = listlen // 2

    return middle

def delmiddle(head):
    
    middle = middle(head)
    
    current =  head
    contador = 0

    while contador != middle -1:
        contador += 1
        current = current.next
    
    new_curr = current.next

    current.next = new_curr.next
    new_curr.next = None

    return head

new_head = delmiddle(head)

def pirntlist(head):

    current = head

    while current:
        print (current.value)
        current = current.next

pirntlist(new_head)