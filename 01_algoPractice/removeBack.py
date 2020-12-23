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

    def removeBack(self):
        if self.head == None:
            return self
        elif self.head.next == None:
            self.head = None
            return self
        else:
            runner = self.head
            while runner.next.next != None:
                runner = runner.next
            # print(runner.value)
            runner.next = None
            return self


def removeBack2(sllInput):
    if sllInput.head == None:
        return sllInput
    elif sllInput.head.next == None:
        sllInput.head = None
        return sllInput
    else:
        runner = sllInput.head
        while runner.next.next != None:
            runner = runner.next
        # print(runner.value)
        runner.next = None
        return sllInput


newSll = SLL()
newSll.append(5).append(8).append(6).addFront(23).display()
print("*****")
# anotherOne = SLL()
# anotherOne.append(2).removeBack().display()

removeBack2(newSll)
newSll.display()
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


# ////////////////////////////////////////////////////////////////////////////////removeBack
#                                                                                 JonathanKohen
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class SLL:
#     def __init__(self):
#         self.head = None

#     def append(self, value):
#         newNode = Node(value)
#         if self.head == None:
#             self.head = newNode
#         else:
#             runner = self.head
#             while runner.next != None:
#                 runner = runner.next
#             runner.next = newNode
#         return self

#     def display(self):
#         runner = self.head
#         while runner != None:
#             print(runner.value)
#             runner = runner.next
#         print(runner)

#     def removeFront(self):
#         self.head = self.head.next


# def lastNode(self):
#     if self.head == None:
#         return None
#     if self.head.next == None:
#         self.head = None
#         return None
#     second_last = self.head
#     while(second_last.next.next):
#         second_last = second_last.next
#     second_last.next = None
#     return self.head


# newSLL = SLL()
# newSLL.append(5).append(8).append(12)
# lastNode(newSLL)
# newSLL.display()

# ////////////////////////////////////////////////////////////////////////////////removeBack
#                                                                                  Rob-instructor*******
# def removeBack(self):
#     runner = self.head
#     while runner.next.next != None:
#         runner = runner.next
#     print(runner.value)


# newSll = SLL()
# newSll.append(5).append(8).append(6).prepend(23).display()

# ////////////////////////////////////////////////////////////////////////////////removeBack
#                                                                                  JerryPerkins
# def removeLast(self):
#     runner = self.head
#     while runner.next != None:
#         if runner.next.next == None:
#             runner.next = None
#             return self
#         else:
#             runner = runner.next

# ////////////////////////////////////////////////////////////////////////////////removeBack
#                                                                                  my group attempt
# def removeLastNode(self):
#     if self.head == None:
#         return None
#     if self.head.next == None:
#         self.head = None
#         return None
#     second_last = self.head
#     while(second_last.next.next):
#         second_last = second_last.next
#     second_last.next = None
#     return self.head


# newSLL = SLL()
# newSLL.append(5).append(8).append(12)
# removeLastNode(newSLL)
# removeLastNode.display()
