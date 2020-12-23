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

    def prepend(self, value):
        new_node = Node (value)
        new_node.next = self.head
        self.head = new_node
        return self

def minFront(self):
        # init
        runner = self.head
        minNode = runner
        minVal = runner.value
        prev = runner
        finalPrev = prev

        # loop
        while runner != None:

            # find lowest num
            if runner.value < minVal:

                # set node to previous
                finalPrev = prev

                # grab min value from current node in loop 
                # to check lowest value next time around
                minVal = runner.value

                # set minNode value 
                minNode = runner

            # set prev node -- to track the node before runner update
            prev = runner

            # update runner to next node
            runner = runner.next

        # loop ends 
        # set prev node next to min node next
        finalPrev.next = minNode.next

        # set current head to min node next
        minNode.next = self.head

        # set current head as min head
        self.head = minNode

        # enable chainable
        return self



newSll = SLL()
newSll.append(5).append(8).append(6).prepend(23).display()
minFront()

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
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                                        Class examples
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# EricViera
# def __init__(self):
#     self.head = None

# def placeFront(self, val):

#     # create new node
#     newNode = Node(val)

#     # give new node current self.head
#     newNode.next = self.head

#     # replace self.head new node 
#     self.head = newNode

#     # chain
#     return self        

# def append(self, value):
#     #create a node with the value passed
#     newnode = Node(value)
#     if self.head == None:
#         #add the new node to the SLL
#         self.head = newnode
#     else:
#         runner = self.head
#         #increment runner until we get runner to a node where the node's .next is none (the last node)
#         while runner.next != None:
#             #increment runner by one node
#             runner = runner.next
#         runner.next = newnode
#     return self

# def display(self):
#     runner = self.head
#     # print(runner.next.next.next)
#     while runner != None:
#         print(runner.value)
#         runner = runner.next
#     print(runner)

# def removeFront(self):
#     # print(self.head)
#     # print(self.head.next)
#     self.head = self.head.next
# newSll = SLL()
# newSll.append(5).append(8).append(6).placeFront(28).placeFront(18).display()

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                                        Class examples
#“ List: Add Front
# Rudy isn’t nice: he cuts in line in front of everyone else. Given a pointer to the first ListNode and a value, create a new node, assign it to the list head, and return a pointer to the new head node” Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks. 
# 
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# JerryPerkins

# def addFront(self, value):
#         # make it point to the current first node
#         # make sure the head is pointing to the new node
#         frontNode = Node(value)
#         frontNode.next = self.head
#         self.head = frontNode
#         return self

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                                        Class examples
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#scheider_bertrand..... MAX TO BACK
# def maxToFront(sll):
#     if sll.head == None:
#         print("Nothing to Move")
#         return sll
#     else:
#         maxval = sll.head.value
#         rnr = sll.head
#         while rnr.next != None:
#             if rnr.next.value > maxval:
#                 maxval = rnr.next.value
#                 nodeBeforemax = rnr
#                 maxNode = rnr.next
#             rnr = rnr.next
#         nodeBeforemax.next = maxNode.next
#         maxNode.next = sll.head
#         sll.head = maxNode
#         return sll


# #///////////////////////////////////////////////////////////////////////////////////////////////////// 
# #ahmet_dillice-RobMoore.(working).............MaxtoBack
# def maxBack(self):
# move max num to back
def maxBack(self):

    # nothing in list
    if self.head == None or self.head.next == None:
        return self        

    # init
    runner = self.head
    headValue = runner.value    #head edge case
    maxNode = runner
    maxVal = runner.value
    last = runner
    finalPrev = last

    # loop
    while runner != None:

        # find highest num
        if runner.value > maxVal:

            # set node to previous
            finalPrev = last

            # grab highest value from current node in loop 
            # to check highest value next time around
            maxVal = runner.value

            # set maxNode value 
            maxNode = runner

        # set last node -- to track the node before runner update
        last = runner

        # update runner to next node
        runner = runner.next


    # head edge case
    if(headValue == finalPrev.value):

        # set head to node next
        self.head = maxNode.next

    # set last node next to max node next
    finalPrev.next = maxNode.next

    # set maxNode next to None
    maxNode.next = None


    # # set last node as maxNode
    last.next = maxNode

    # enable chainable
    return self



newSll = SLL()
# newSll.append(1).append(3).append(5).append(99).append(4).append(2).maxBack().display()
newSll.append(3).append(2).maxBack().display()


#///////////////////////////////////////////////////////////////////////////////////////////////////// 
#/jamesravencraft (not working)..............MaxtoBack
# def maxToBack(self):
#     if self.head == None:
#         print(“nothing to move fam”)
#         return self
#     else:
#         maxval = self.head.value
#         rnr = self.head
#         while rnr.next != None:
#             if rnr.next.value > maxval:
#                 maxval = rnr.next.value
#                 nodeBeforemax = rnr
#                 maxNode = rnr.next
#             rnr = rnr.next
#         nodeBeforemax.next = maxNode.next
#         rnr.next = maxNode
#         maxNode.next = None
#     return self









