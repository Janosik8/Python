class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def increment_all(self, increment_value):
        current = self.head
        while current:
            current.data += increment_value
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create a linked list
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Display the initial list
print("Initial list:")
my_list.display()

# Increment all nodes by 10
my_list.increment_all(10)

# Display the updated list
print("\nAfter incrementing all nodes by 10:")
my_list.display()
