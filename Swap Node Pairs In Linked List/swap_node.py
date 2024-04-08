from preloaded import Node

def swap_pairs(head):
    if head is None:
        return None
    prev = None
    current = head
    if current.next is None:
        return current
    while current and current.next:
        next = current.next
        if prev is None:
            head = next
        else:
            prev.next = next
        current.next = next.next
        next.next = current
        prev = current
        current = current.next
    return head
