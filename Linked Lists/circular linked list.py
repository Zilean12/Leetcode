class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        self.append(data)

    def delete(self, key):
        if self.head is None:
            return
        
        current = self.head
        previous = None

        # If the node to be deleted is the head node
        if current.data == key:
            if current.next == self.head:  # Only one node in the list
                self.head = None
            else:
                # Find the last node
                while current.next != self.head:
                    current = current.next
                # Set last node's next to the second node
                current.next = self.head.next
                # Update head
                self.head = self.head.next
            return

        # If the node to be deleted is not the head node
        previous = self.head
        current = self.head.next
        while current != self.head:
            if current.data == key:
                previous.next = current.next
                return
            previous = current
            current = current.next

    def delete_at_beginning(self):
        if self.head is None:
            return

        current = self.head
        if current.next == self.head:  # Only one node in the list
            self.head = None
        else:
            # Find the last node
            while current.next != self.head:
                current = current.next
            # Set last node's next to the second node
            current.next = self.head.next
            # Update head
            self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            return

        current = self.head
        previous = None

        # If there's only one node in the list
        if current.next == self.head:
            self.head = None
            return

        # Traverse to the second last node
        while current.next != self.head:
            previous = current
            current = current.next

        # Remove the last node by updating the second last node's next pointer
        previous.next = self.head

    def display(self):
        nodes = []
        current = self.head
        if self.head is not None:
            while True:
                nodes.append(current.data)
                current = current.next
                if current == self.head:
                    break
        print(" -> ".join(map(str, nodes)))

cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
print("display Circular Linked List")
cll.display()
cll.insert_at_beginning(0)
print("added value in beginning")
cll.display() 
cll.insert_at_end(4)
print("added value in end")
cll.display()  # Output: 0 -> 1 -> 2 -> 3 -> 4
cll.delete_at_end()
print("delete value from the End")
cll.display()  # Output: 0 -> 1 -> 2 -> 3
cll.delete_at_beginning()
print("delete value from the Beginning")
cll.display() 