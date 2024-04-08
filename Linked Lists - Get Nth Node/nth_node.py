from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    current = node
    count = 0
    while current:
        if count != index:
            current = current.next
            count += 1
        else:
            return current
    raise ValueError('incorrect index')
