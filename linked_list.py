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


# 2.1 Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
def remove_dups(head):
  s = set()
  curr = head
  prev = None
  while curr is not None:
    if curr.data in s:
      prev.next = curr.next
    else:
      s.add(curr.data)
      prev = curr
    curr = curr.next
  return head


def remove_dups_no_buffer(head):
  curr = head
  while curr:
    runner = curr
    while runner.next:
      if runner.next.data == curr.data:
        runner.next = runner.next.next
      else:
        runner = runner.next
    curr = curr.next
my_list = SingleList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(3)
my_list.append(4)
my_list.append(4)

remove_dups_no_buffer(my_list.head)
my_list.show()


# 2.2 Implement an algorithm to find the kth to last element of a singly linked list.

def find_k(head, k):
  curr = head
  count = 0
  res = head
  while curr:
    count += 1
    curr = curr.next
  for i in xrange(count - k):
    res = res.next
  return res.data

my_list = SingleList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(3)
my_list.append(4)
my_list.append(4)

my_list.show()
print find_k(my_list.head, 1)


# 2.3 Implement an algorithm to delete a node in the middle of a singly linked list,
# given only access to that node.
# EXAMPLE
# Input: the node c from the linked list a->b->c->d->e
# Result: nothing is returned, but the new linked list looks like a- >b- >d->e

def delete_middle(node):
  if node or node.next:
    return False
  node.data = node.next.data
  node.next = node.next.next
  return True

my_list = SingleList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(3)
my_list.append(4)
my_list.append(4)

delete_middle(my_list.head.next)
my_list.show()


# 2.4 Write code to partition a linked list around a value x, such that all nodes less than
# x come before all nodes greater than or equal to x.

def partition(head, val):
  curr = head
  left = SingleList()
  right = SingleList()
  while curr:
    if curr.data < val:
      left.append(curr.data)
    else:
      right.append(curr.data)
    curr = curr.next

  temp = left.head
  while temp.next:
    temp = temp.next
  temp.next = right.head
  left.show()

my_list = SingleList()
my_list.append(5)
my_list.append(1)
my_list.append(7)
my_list.append(3)
my_list.append(2)
my_list.append(8)
my_list.append(9)
my_list.append(4)
my_list.append(0)
my_list.append(6)


partition(my_list.head, 5)


# 2.5 You have two numbers represented by a linked list, where each node contains a
# single digit. The digits are stored in reverse order, such that the Ts digit is at the
# head of the list. Write a function that adds the two numbers and returns the sum
# as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.
# Output: 2 -> 1 -> 9.That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295.
# Output: 9 -> 1 -> 2.That is, 912.

def add_reverse(node1, node2, carry):
  if node1 is None and node2 is None and carry == 0:
    return None
  data = carry
  if node1:
    data += node1.data
  if node2:
    data += node2.data
  res = Node(data % 10, None)
  if node1 or node2:
    more = add_reverse(node1.next if node1.next else None,
      node2.next if node2.next else None,
      1 if data > 10 else 0)
  res.next = more
  return res

num1 = SingleList()
num1.append(7)
num1.append(1)
num1.append(6)
num2 = SingleList()
num2.append(5)
num2.append(9)
num2.append(2)
res = add_reverse(num1.head, num2.head, 0)
while res:
  print res.data
  res = res.next

# 2.6 Given a circular linked list, implement an algorithm which returns the node at
# the beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points
# to an earlier node, so as to make a loop in the linked list.
# EXAMPLE
# Input: A - > B - > C - > D - > E - > C [the same C as earlier]
# Output: C


def find_circle(head):
  s = set()
  p1 = head
  while p1:
    if p1.data in s:
      return p1.data
    else:
      s.add(p1.data)
      p1 = p1.next
  return "No cycle"

num1 = SingleList()
num1.append('A')
num1.append('B')
num1.append('C')
num1.append('D')
num1.append('E')
num1.append('C')

num2 = SingleList()
num2.append('A')
num2.append('B')
num2.append('C')
num2.append('D')
num2.append('E')
num2.append('F')

print find_circle(num1.head)
print find_circle(num2.head)

# 2.7 Implement a function to check if a linked list is a palindrome.


def is_palindrome(head):
  slow = head
  fast = head
  s = []
  while fast and fast.next:
    s.append(slow.data)
    slow = slow.next
    fast = fast.next.next
  if fast:
    slow = slow.next
  while slow:
    if slow.data != s.pop():
      return False
    slow = slow.next
  return True

num1 = SingleList()
num1.append('A')
num1.append('B')
num1.append('C')
num1.append('D')
num1.append('E')
num1.append('C')

num2 = SingleList()
num2.append('A')
num2.append('B')
num2.append('C')
num2.append('C')
num2.append('B')
num2.append('A')

num3 = SingleList()
num3.append('A')
num3.append('B')
num3.append('C')
num3.append('B')
num3.append('A')

print is_palindrome(num1.head)
print is_palindrome(num2.head)
print is_palindrome(num3.head)
