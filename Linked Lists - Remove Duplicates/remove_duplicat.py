class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None
    current = head
    dup = {current.data}
    while current.next:
        if current.next.data in dup:
            current.next = current.next.next
        else:
            dup.add(current.next.data)
            current = current.next
    return head
