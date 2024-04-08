def loop_size(node):
    nodes_set = set()
    len_loop = 0
    while node not in nodes_set:
        nodes_set.add(node)
        node = node.next
    head = node
    while True:
        node = node.next
        len_loop += 1
        if node == head:
            break
    return len_loop
