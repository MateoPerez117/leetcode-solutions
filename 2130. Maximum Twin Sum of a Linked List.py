class ListNode:
    def __init__(self, val):
        self.val = val
        self.next =  None
        self.previous = None

head = ListNode(1)
b = ListNode(100000)

head.next = b

def max_twinsum(head):
    current = head
    contador = 0
    lenlist = 0
    maximo = float('-inf')
    contador2 = 0
    current2 = head
    
    while current:
        contador += 1
        current = current.next
    
    lenlist = contador

    stack = []
    flag = True

    while current2:
        if contador2 == lenlist/2:
            flag = False
        if flag == False:
            maximo = max(current2.val + stack[-1], maximo)
            stack.pop(-1)
            current2 = current2.next

        if flag == True:
            stack.append(current2.val)
            contador2 += 1
            current2 = current2.next

    return maximo

maximo = max_twinsum(head)

print(maximo)
