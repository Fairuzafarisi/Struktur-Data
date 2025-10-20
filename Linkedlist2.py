class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insert_before(self, data, value):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
            return
        current = self.head
        while current:
            if current.data == value:
                new_node.next = current
                new_node.previous = current.previous
                if current.previous:
                    current.previous.next = new_node
                else:
                    self.head = new_node
                current.previous = new_node
                return
            current = current.next

    def insert_after(self, data, value):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
            return
        current = self.head
        while current:
            if current.data == value:
                new_node.next = current.next
                new_node.previous = current
                if current.next:
                    current.next.previous = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                return
            current = current.next

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_from_beginning(self):
        if self.is_empty():
            print("Linked list kosong.")
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
        return data

    def delete_at_middle(self, data):
        if self.is_empty():
            print("Linked list kosong.")
            return None
        current = self.head
        while current:
            if current.data == data:
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                return data
            current = current.next
        return None

    def delete_from_end(self):
        if self.is_empty():
            print("Linked list kosong.")
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        return data

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.previous
        print()


# Example usage
dll = DoubleLinkedList()
dll.insert_at_beginning(30)
dll.insert_at_end(10)
dll.insert_at_beginning(20)
dll.insert_at_end(40)

print("Menampilkan data dari depan ke belakang:")
dll.display_forward()   # Output: 20 30 10 40

print("Menampilkan data dari belakang ke depan:")
dll.display_backward()  # Output: 40 10 30 20

dll.insert_before(25, 30)
dll.insert_after(35, 30)

print("\nMenampilkan data setelah penambahan:")
dll.display_forward()   # Output: 20 25 30 35 10 40

dll.delete_from_beginning()
dll.delete_from_end()
dll.delete_at_middle(30)

print("\nMenampilkan data setelah delete:")
dll.display_forward()   # Output: 25 35 10