# 3.2 How would you design a stack which, in addition to push and pop, also has a
# function min which returns the minimum element? Push, pop and min should
# all operate in O(1) time.


class StackItem(object):
  def __init__(self, data):
    self.data = data
    self.min = None


class Stack(object):
  def __init__(self):
    self.res = []

  def push(self, data):
    item = StackItem(data)
    item.min = data if self.is_empty() else min(data, self.peek().min)
    self.res.append(item)

  def pop(self):
    return self.res.pop()

  def peek(self):
    return self.res[-1]

  def is_empty(self):
    return len(self.res) == 0

  def min(self):
    return self.peek().min

  def size(self):
    return len(self.res)

s = Stack()
s.push(1)
s.push(6)
s.push(2)
s.push(5)
s.push(0)
s.push(2)

print s.min()


# 3.3 Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack
# exceeds some threshold. Implement a data structure SetOf Stacks that mimics
# this. SetOf Stacks should be composed of several stacks and should create a
# new stack once the previous one exceeds capacity. SetOf Stacks. push() and
# SetOf Stacks. pop() should behave identically to a single stack (that is, popO
# should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on
# a specific sub-stack.

class SetOfStacks(object):
  def __init__(self, max_height):
    self.stacks = []
    self.max = max_height

  def push(self, item):
    if self.is_empty() or self.stacks[-1].size() >= self.max:
      stack = Stack()
      stack.push(item)
      self.stacks.append(stack)
    else:
      self.stacks[-1].push(item)

  def pop(self):
    if self.stacks[-1].is_empty():
      self.stacks.pop()
    return self.stacks[-1].pop()

  def pop_at(self, index):
    return self.stacks[index].pop()

  def is_empty(self):
    return len(self.stacks) == 0

  def size(self):
    return len(self.stacks)


s = SetOfStacks(3)
s.push(1)
s.push(6)
s.push(3)
s.push(5)
s.push(0)
s.push(2)
s.push(21)

print s.pop().data
print s.pop_at(1).data


# 3.4 In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
# different sizes which can slide onto any tower. The puzzle starts with disks sorted
# in ascending order of size from top to bottom (i.e., each disk sits on top of an
# even larger one). You have the following constraints:
# (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto the next tower.
# (3) A disk can only be placed on top of a larger disk.
# Write a program to move the disks from the first tower to the last using stacks.

def tower_hanoi(n, source, helper, target):
  if n > 0:
    tower_hanoi(n - 1, source, target, helper)
    if source:
      target.append(source.pop())
    tower_hanoi(n - 1, helper, source, target)

source = [4, 3, 2, 1, 0]
target = []
helper = []
tower_hanoi(len(source), source, helper, target)
print source
print helper
print target

# 3.5 Implement a MyQueue class which implements a queue using two stacks.


class MyQueue(object):
  def __init__(self):
    self.queue = Stack()
    self.helper = Stack()

  def enqueue(self, item):
    self.helper.push(item)

  def deque(self):
    if self.queue.is_empty():
      while not self.helper.is_empty():
        self.queue.push(self.helper.pop().data)
    return self.queue.pop().data


q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print q.deque()
print q.deque()


# 3.6 Write a program to sort a stack in ascending order (with biggest items on top).
# You may use at most one additional stack to hold items, but you may not copy
# the elements into any other data structure (such as an array). The stack supports
# the following operations: push, pop, peek, and isEmpty.

def sort_stack(s):
  temp = Stack()
  while not s.is_empty():
    elem = s.pop().data
    while (not temp.is_empty()) and temp.peek().data > elem:
      s.push(temp.pop().data)
    temp.push(elem)
  return temp

s = Stack()
s.push(2)
s.push(5)
s.push(8)
s.push(-1)
s.push(1)
s.push(7)
s.push(4)
s.push(9)
s.push(0)
s.push(3)

res = sort_stack(s)
while not res.is_empty():
  print res.pop().data

# 3.7 An animal shelter holds only dogs and cats, and operates on a strictly "first in,
# first out" basis. People must adopt either the "oldest" (based on arrival time) of
# all animals at the shelter, or they can select whether they would prefer a dog or
# a cat (and will receive the oldest animal of that type). They cannot select which
# specificanimal they would like. Create the data structures to maintain this system
# and implement operations such as enqueue, dequeueAny, dequeueDog and
# dequeueCat.You may use the built-in LinkedList data structure

import time


class Node(object):

    def __init__(self, data, next):
        self.data = data
        self.next = next


class SingleList(object):

    head = None
    tail = None

    def show(self):
        print "Showing list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.data, " -> ",
            current_node = current_node.next
        print None

    def append(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node

    def remove_head(self):
      curr = self.head
      self.head = self.head.next
      return curr.data


class Animal(object):
  def __init__(self, animal):
    self.type = animal
    self.timestamp = time.time()


class ShelterQueue(object):
  def __init__(self):
    self.dog_queue = SingleList()
    self.cat_queue = SingleList()

  def enqueue(self, animal):
    if animal == 'dog':
      self.dog_queue.append(Animal('dog'))
    else:
      self.cat_queue.append(Animal('cat'))

  def dequeue(self):
    res = self.dequeue_cats().type if self.cat_queue.head.data.timestamp < self.dog_queue.head.data.timestamp else self.dequeue_dogs().type
    return res.type

  def dequeue_cats(self):
    return self.cat_queue.remove_head()

  def dequeue_dogs(self):
    return self.dog_queue.remove_head().type
