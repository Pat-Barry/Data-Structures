class Stack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return self.stack_size

    def push(self, value):
        self.stack_size += 1
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        self.stack_size -= 1
        return self.stack_list.pop()

if __name__ == "__main__" :
    stack_obj = Stack()
    print("Pushing 5 items onto stack")
    for i in range(5):
        stack_obj.push(i)

    print(stack_obj.size())
    print(stack_obj.is_empty())
    for i in range(5):
        print(stack_obj.pop())
