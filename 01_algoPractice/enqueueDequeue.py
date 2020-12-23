#First In, First Out.... (FIFO)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail =None

    def display(self):
        runner = self.head
        # print(runner.next.next.next)
        while runner != None:
            print(runner.value)
            runner = runner.next
        print(runner)
        return self

    def enqueue(self, value):
        #create new Node
        newNode = Node(value)
        #check if queue is empty, if empty-> set self.head and til to point to it
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next            
        return self

    def dequeue(self):
        if self.head == None:
            print('nothing to remove here')
        else:
            self.head = self.head.next  
            if self.head == None:
                self.tail = None      
        return self


    def size(self):
        runner = self.head
        count = 0
        while runner != None:
            count += 1
            runner = runner.next
        print(count)
        return count

# “Create method contains(val) to return whether given value is found within our queue.”
    def contain(self, value):
        runner = self.head
        if runner.value == value:
            return print('This is:', True)
        while runner.next != None:
            if runner.value == value:
                return print('This is:', True)
            else:
                runner = runner.next
        if self.tail.value == value:
            return  print('This is:', True)
        return print('This is:', False)

# “ Queue: Is Palindrome
# Given a Queue, return true if its values are a palindrome (if they are same in reverse order), else return false. Restore Queue to original state before exiting. For storage, use one additional Stack”    
# below is ShawnLockharts class example including addition Stack
q1 = Queue()
q1.enqueue('h').enqueue('a').enqueue('n').enqueue('n').enqueue('a').enqueue('h')

# def palindrome(queueInput):
#     stk = Stack()
#     length = queueInput.size()
#     for i in range(length):
#         t = queueInput.dequeue()
#         queueInput.enqueue(t)
#         stk.push(t)
#     # print('-' * 40)
#     # stk.display()
#     # queueInput.display()
#     # print('-' * 40)
#     rnr = queueInput.head
#     rnr2 = stk.top
#     while rnr is not None:
#         if rnr.value is not rnr2.value:
#             print(False)
#             return False
#         rnr = rnr.next
#         rnr2 = rnr2.next
#     print(True)

# palindrome(q1)
# ///////////////////////////////////////////////////////////////
from collections import deque

def QIsPalindrome(char):
    char_deque = deque(char)
    while len(char_deque) > 1:
        first = char_deque.popleft()
        last = char_deque.pop()
        if first != last:
            return False

    return True



q1 = Queue()
QIsPalindrome.append(c).append(i).append(v).append(i).append(c)
# q1.enqueue(5).enqueue(6).enqueue(-7).enqueue(9).display()
print('*'*50)
print('*'*50)
# q1.size()
# q1.dequeue().size()
# q1.contain(-7)
print('*'*50)
print('*'*50)


