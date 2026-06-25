# Program to Create a Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        print(f"Inserted: {data}")

    def delete_node(self, data):
        if self.head is None:
            print("List is empty!")
            return
        if self.head.data == data:
            self.head = self.head.next
            print(f"Deleted: {data}")
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                print(f"Deleted: {data}")
                return
            current = current.next
        print(f"{data} not found in list.")

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        print("Linked List: ", end="")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = SinglyLinkedList()

print("=== Singly Linked List ===")
while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        val = int(input("Enter value: "))
        ll.insert_at_end(val)
    elif choice == '2':
        val = int(input("Enter value to delete: "))
        ll.delete_node(val)
    elif choice == '3':
        ll.display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

