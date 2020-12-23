#Abstract Data Type... Last In, First Out (LIFO)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def display(self):
        runner = self.top
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self
        
# create fx that pushes value to top of LIFO
    def push(self, val):
        newNode = Node(val)
        if self.top == None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode            
        return self

#create fx that pops the last value out            
    def pop(self):
        self.top = self.top.next
        return self

#create fx that peeks to tell me number of items in stack
    def size(self):
        runner = self.top
        count = 0
        while runner != None:
            count += 1
            runner = runner.next
        print("size", count)
        return count






stk1 = Stack()
stk1.push(5).push(8).push(3).display()
print("*"*25)
stk1.pop()