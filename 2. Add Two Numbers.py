# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]

class ListNode:
    def __init__(self, val = 0, next = None):
            self.val = val
            self.next = next

l1 = ListNode(2)
b = ListNode(4)
c = ListNode(3)

l2 = ListNode(5)
d = ListNode(6)
e = ListNode(4)

l1.next = b
b.next = c

l2.next = d
d.next = e

def addTwoNumbers(l1, l2):

    l3 = ListNode()
    current1 = l1
    current2 = l2
    current3 = l3
    carry = 0
    valor1 = 0
    valor2 = 0

    while current1 or current2:
        if current1:
            valor1 = current1.val
        else:
            valor1 = 0
        if current2:
            valor2 = current2.val
        else:
            valor2 = 0

        resultado = valor1 + valor2
        
        if carry:
            resultado += carry
            carry = 0

        if resultado >= 10:
            last = resultado % 10
            carry = resultado // 10
            current3.val = last

        else:  
            current3.val = resultado

        if current1:
            current1 = current1.next
        if current2:
            current2 = current2.next

        if current1 or current2:
            new_node = ListNode()
            current3.next = new_node
            current3 = current3.next

    if carry:
        new_node = ListNode()
        current3.next = new_node
        current3 = current3.next
        current3.val = carry


    return l3

a = addTwoNumbers(l1, l2)

def printlinkedlist(head):
    
    current = head

    while current:
        print (current.val)
        current = current.next

print (printlinkedlist(a))