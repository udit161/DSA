class stack:
    def __init__(self):
        self.stack = []
    
    def lenght(self):
        return len(self.stack)

    def push(self, value):
        self.stack.insert(0, value)   

    def pop(self):
        self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def peek(self):
        if len(self.stack) == 0:
            raise Exception("Stack is empty")
        return self.stack[0]    


    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            for i in self.stack:
                print(i)

obj = stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.display()
print("-" * 10)
obj.pop()
obj.display()