def linked_list_from_string(s):
    if s == 'None':
        return None
    res = Node(int(s.split(' -> ')[0]))
    current = res
    for el in s.split(' -> ')[1:]:
        if el != 'None':
            current.next = Node(int(el))
            current = current.next
        else:
            return res
