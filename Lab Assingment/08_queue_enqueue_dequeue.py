# Program to Perform ENQUEUE and DEQUEUE Operations on a Queue

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
        else:
            item = self.queue.pop(0)
            print(f"Dequeued: {item}")

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue (front -> rear):", self.queue)

    def is_empty(self):
        return len(self.queue) == 0


q = Queue()

print("=== Queue Operations ===")
while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        val = input("Enter value to enqueue: ")
        q.enqueue(val)
    elif choice == '2':
        q.dequeue()
    elif choice == '3':
        q.display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

