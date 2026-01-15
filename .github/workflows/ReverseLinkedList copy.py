from operator import ne
from tkinter import N


class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def reverse(head: Node) -> Node:
  
    dummy_node = Node()
    curr = head

    while curr:
        next_node = curr.next
        curr.next = dummy_node.next
        dummy_node = curr

        curr = next_node

    return dummy_node.next


print(reverse(Node(1, Node(2, Node(3)))))

   
    


