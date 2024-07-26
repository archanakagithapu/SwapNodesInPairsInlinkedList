class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes_in_pairs(head):
    if head is None or head.next is None:
        return head

    new_head = head.next
    prev = None
    current = head
    while current and current.next:
        next_node = current.next
        next_next_node = next_node.next

        # Swap current and next nodes
        next_node.next = current
        if prev is not None:
            prev.next = next_node
        else:
            head = next_node

        prev = current
        current = next_next_node

    prev.next = current
    return new_head

def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

# Example usage:
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original list:")
print_list(head)

head = swap_nodes_in_pairs(head)

print("Swapped list:")
print_list(head)

