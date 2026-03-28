class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


list1 = ListNode(1)
b = ListNode(2)
c = ListNode(4)


list2 = ListNode(1)
d = ListNode(3)
e = ListNode(4)


list1.next = b
b.next = c


list2.next = d
d.next = e


def print_List(head):


    current = head


    while current:
        print (current.val)
        current = current.next


print(print_List(list2))




def merge_arrs(list1, list2):


    if not list1 and not list2:
        return None
    elif not list1:
        return list2
    elif not list2:
        return list1


    current = list1
    lala = list2
       
    if current.val <= lala.val:
        guardado = current
        current = current.next
    else:
        guardado = lala
        lala = lala.next


    new_head = guardado


    while current and lala:
        if current.val <= lala.val:
            guardado.next = current
            guardado = guardado.next
            current = current.next
        else:
            guardado.next = lala
            guardado = guardado.next
            lala = lala.next
       
    if current:
        while current:
            guardado.next = current
            current = current.next
            guardado = guardado.next
    if lala:
        while lala:
            guardado.next = lala
            lala = lala.next
            guardado = guardado.next


    return new_head




a =merge_arrs(list1, list2)


print(print_List(a))