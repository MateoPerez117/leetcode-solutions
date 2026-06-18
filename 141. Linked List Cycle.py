class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

def Removenode(node):
    contador = 0
    current = node
    flag = True


    while current or contador <1000:
        if not current:
            flag = False
            break
        
        current = current.next
        contador += 1

    print (flag)

Removenode(head)

