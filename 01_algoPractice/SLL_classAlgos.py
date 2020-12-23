
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def append(self, value):
        # create a node with the value passed
        newnode = Node(value)
        if self.head == None:
            # add the new node to the SLL
            self.head = newnode
        else:
            runner = self.head
            # increment runner until we get runner to a node where the node's .next is none (the last node)
            while runner.next != None:
                # increment runner by one node
                runner = runner.next
            runner.next = newnode
        return self
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
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

    def addFront(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        return self

    # def removeBack(self):
    #     if self.head == None:
    #         return self
    #     elif self.head.next == None:
    #         self.head = None
    #         return self
    #     else:
    #         runner = self.head
    #         while runner.next.next != None:
    #             runner = runner.next
    #         # print(runner.value)
    #         runner.next = None
    #     return self

    # def removeBack2(self):
    #     if self.head == None:
    #         return self
    #     elif self.head.next == None:
    #         self.head = None
    #         return self
    #     else:
    #         runner = self.head
    #         while runner.next.next != None:
    #             runner = runner.next
    #         # print(runner.value)
    #         runner.next = None
    #     return self

# Function which pushes min
# value to front of an array.
    def minToFront(self):
        if self.head == None:
            print("nothing to move here")
            return self
        else:
            minval = self.head.value
            runner = self.head
            while runner.next != None:
                if runner.next.value < minval:
                    minval = runner.next.value
                    nodeBeforemin = runner
                    minNode = runner.next
                runner = runner.next
            nodeBeforemin.next = minNode.next
            minNode.next = self.head
            self.head = minNode
        return self

# Function which pushes max 
# value to end of an array. 
# Only works if more than 2 nodes.
def maxToBack(self):
        if self.head == None or self.head.next == None:
            return self
        elif self.head.next.next == None:
            rnr = self.head
            maxnode = self.head
            while rnr.next != None:
                rnr = rnr.next
            rnr.next = maxnode
            maxnode.next = None
            self.head = rnr
        else:
            maxval = self.head.value
            rnr = self.head
            while rnr.next != None:
                if rnr.next.value > maxval:
                    maxval = rnr.next.value
                    nodeBeforemax = rnr
                    maxNode = rnr.next
                rnr = rnr.next
            if self.head.value == maxval:
                rnr.next = self.head
                newhead = self.head.next
                self.head.next = None
                self.head = newhead
                return self
            nodeBeforemax.next = maxNode.next
            rnr.next = maxNode
            maxNode.next = None
        return self





newSll = SLL()
newSll.append(5).append(6).append(12).addFront(1).append(4).display()
print("*"*100)
newSll.maxToBack().display()