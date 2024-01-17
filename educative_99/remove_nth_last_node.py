# from linked_list import LinkedList
# # Seta dois ponteiros
# # o primeiro é nulo
# # O segundo é o head
# # Enquanto o segundo não for nulo
# # o segundo avança a quantidade de n
# #  1  2   3  4 5  6  7  8
# # |23|28|10|05|67|39|70|28| 
# # o primeiro recebe o valor de head
# # os dois ponteiros avançam
# # se o segundo for nulo, o valor a ser removido é o primeiro
# # pega o valor do proximo
# # seta o proximo para o  atual
# # valor do primeiro vira 0
# # retorna o head

# def remove_nth_last_node(linked_list, n):
#   # Seta dois ponteiros
#   # o primeiro é nulo
#   left = None
#   # O segundo é o head
#   right = linked_list.head_node
#   count = 0
#   # Enquanto o segundo não for nulo
#   while right is not None:
#     # o segundo avança a quantidade de n
#     right = right.get_next_node()
#     # o primeiro recebe o valor de head
#     if count >= n + 1:
#       if left is None:
#         left = linked_list.head_node
#       else:
#     # os dois ponteiros avançam
#         left = left.get_next_node()
#     count += 1
#   current_node = left.get_next_node()
#   left.set_next_node(current_node.get_next_node())
#   current_node = 0
#   return linked_list.stringify_list()

# ll = LinkedList()
# ll.insert_beginning(28)
# ll.insert_beginning(70)
# ll.insert_beginning(39)
# ll.insert_beginning(67)
# ll.insert_beginning(5)
# ll.insert_beginning(10)
# ll.insert_beginning(28)
# ll.insert_beginning(23)
# print(remove_nth_last_node(ll, 2))

from linked_list import LinkedList
from linked_list import Node

def remove_nth_last_node(linked_list, n):
    right = linked_list.head_node
    left = linked_list.head_node

    for i in range(n):
        right = right.get_next_node()
    
    if not right:
      return right.get_next_node()
    
    while right.get_next_node():
      right = right.get_next_node()
      left = left.get_next_node()
    
    left.set_next_node(left.get_next_node().get_next_node())
    
    return linked_list.stringify_list()


ll = LinkedList()
ll.insert_beginning(28)
ll.insert_beginning(70)
ll.insert_beginning(39)
ll.insert_beginning(67)
ll.insert_beginning(5)
ll.insert_beginning(10)
ll.insert_beginning(28)
ll.insert_beginning(23)
print(remove_nth_last_node(ll, 2))