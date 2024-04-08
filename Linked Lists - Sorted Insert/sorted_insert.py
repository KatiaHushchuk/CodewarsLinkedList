""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    if head is None:
        return Node(data)
    current = head
    if current.data > data:
        n = Node(data)
        n.next = head
        return n
    while not(current.data < data and current.next is None) and \
        not(current.data < data and current.next.data > data):
        current = current.next
    new_node = Node(data)
    new_node.next = current.next
    current.next = new_node
    return head
