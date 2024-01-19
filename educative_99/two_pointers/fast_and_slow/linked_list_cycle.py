from linked_list import LinkedList

def detect_cycle(head):
   fast = head
   slow = head

   while fast.next:
      fast = fast.next.next
      slow = slow.next

      if fast == slow:
         return True
   
   return False