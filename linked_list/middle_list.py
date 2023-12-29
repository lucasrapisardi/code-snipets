"""
Could be also used for:
  Detect a cycle in a linked list
  Rotate a linked list by k places
"""
def find_middle(linked_list):
  fast = linked_list.head_node
  slow = linked_list.head_node

  while fast:
    fast = fast.get_next_node()
    if fast:
      fast = fast.get_next_node()
      slow = slow.get_next_node()
  return slow

# half the time 
def find_middle_alt(linked_list):
  count = 0
  fast = linked_list.head_node
  slow = linked_list.head_node
  while fast:
    fast = fast.get_next_node()
    if count % 2 != 0:
      slow = slow.get_next_node()
    count += 1
  return slow