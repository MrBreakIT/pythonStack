class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None


    def push(self, value):
        #create a new node
        newNode = Node(value)
        if self.top == None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        return self

    def pop(self):
        if self.top == None:
            print('nothing to pop doc')
            return self
        else:
            valToReturn = self.top.value
            self.top = self.top.next
        return valToReturn


    def size(self):
        runner = self.top
        count = 0
        while runner != None:
            count += 1
            runner = runner.next
        # print(count)
        return count

    def display(self):
        runner = self.top
        # print(runner.next.next.next)
        while runner != None:
            print(runner.value)
            runner = runner.next
        print(runner)

# “Given a Stack, create a new second Stack and copy values from first Stack into second Stack, so they pop in same order. Use only one Queue for additional storage”
    def copyStack(stackInput):
        q = Queue
        result = Stack ()
        length = originalStack.size()
        originalrunner = originalStack.top
        for i in range(0, length, 1):
            newNode = Node(originalrunner.value)
            result.push(newNode)
            originalrunner = originalrunner.next
        print("*"*25)
        for i in range (0, length, 1):
            x = result.pop()
            newNode = Node(result.pop())
            q.enqueue(newNode)
        for i in range(0, length, 1):
            newNode = Node(q.dequeue())
            result.push(newNode)
        return result



stk1 = Stack()
stk1.push(5).push(8).push(4).push(1)
# print(stk1.pop())
# stk1.display()
# stk1.push(5).push(8).push(3)
y = copyStack(stk1)