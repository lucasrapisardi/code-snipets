# def get_middle_node(head):
#     slow = head
#     fast = head
    
#     while fast:
#         if fast.next is None:
#             return slow
#         fast = fast.next.next
#         slow = slow.next
#     return slow

def get_middle_node(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow