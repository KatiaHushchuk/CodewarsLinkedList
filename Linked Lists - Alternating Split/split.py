class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError('single node or node is None')
    current = head.next.next
    head_1 = head
    head_2 = head.next
    tail_1 = head_1
    tail_2 = head_2
    count = 1
    while current:
        if count % 2:
            tail_1.next = current
            tail_1 = tail_1.next
        else:
            tail_2.next = current
            tail_2 = tail_2.next
        count += 1
        current = current.next
    tail_1.next = None
    tail_2.next = None
    return Context(head_1, head_2)
