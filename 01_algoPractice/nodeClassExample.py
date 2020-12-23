class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def append(self, value):
        #create a node with the value passed
        newnode = Node(value)
        if self.head == None:
            #add the new node to the SLL     
            self.head = newnode
        else:
            runner = self.head
            #increment runner until we get runner to a node where the node's .next is none (the last node)
            while runner.next != None:
                #increment runner by one node
                runner = runner.next
            runner.next = newnode
        return self


    def display(self):
        runner = self.head
        # print(runner.next.next.next)
        while runner != None:
            print(runner.value)
            runner = runner.next
        print(runner)

    def removeFront(self):
        # print(self.head)
        # print(self.head.next)
        self.head = self.head.next




newSll = SLL()
newSll.append(5).append(8).append(6).display()

# node1 = Node(5)
# node2= Node(8)
# node3 = Node(12)
# node1.next = node2
# node2.next = node3

# newSll.head = node1

# newSll.display()
# newSll.removeFront()
# print('removed the front')
# newSll.display()