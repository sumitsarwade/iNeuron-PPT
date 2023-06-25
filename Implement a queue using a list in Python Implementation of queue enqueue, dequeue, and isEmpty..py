class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty. Cannot perform dequeue operation.")

    def isEmpty(self):
        return len(self.queue) == 0


# Create a queue object
my_queue = Queue()

# Check if the queue is empty
print(my_queue.isEmpty())  # Output: True

# Enqueue elements to the queue
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

# Check if the queue is empty
print(my_queue.isEmpty())  # Output: False

# Dequeue elements from the queue
print(my_queue.dequeue())  # Output: 10
print(my_queue.dequeue())  # Output: 20
print(my_queue.dequeue())  # Output: 30

# Try dequeueing from an empty queue
print(my_queue.dequeue())  # Output: IndexError: Queue is empty. Cannot perform dequeue operation.
