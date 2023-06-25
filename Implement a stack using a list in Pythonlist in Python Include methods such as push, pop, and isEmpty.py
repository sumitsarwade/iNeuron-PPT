class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty. Cannot perform pop operation.")

    def isEmpty(self):
        return len(self.stack) == 0


# Create a stack object
my_stack = Stack()

# Check if the stack is empty
print(my_stack.isEmpty())  # Output: True

# Push elements to the stack
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Check if the stack is empty
print(my_stack.isEmpty())  # Output: False

# Pop elements from the stack
print(my_stack.pop())  # Output: 30
print(my_stack.pop())  # Output: 20
print(my_stack.pop())  # Output: 10

# Try popping from an empty stack
print(my_stack.pop())  # Output: IndexError: Stack is empty. Cannot perform pop operation.
