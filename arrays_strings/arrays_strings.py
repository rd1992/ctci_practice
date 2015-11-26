# 1.1 Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?


def all_unique(string):
  s = set()
  for c in string:
    if c not in s:
      s.add(c)
  return len(s) == len(string)


# sort the strings
def all_unique_2(string):
  for i in xrange(len(sorted(string)) - 1):
    if string[i] == string[i + 1]:
      return False
  return True

print "Ans for Q 1.1"
print all_unique("aaaaaaa")
print all_unique("a")
print all_unique("ab")
print all_unique("")
print all_unique_2("aaaaaaa")
print all_unique_2("a")
print all_unique_2("ab")
print all_unique_2("")
print


# 1.3 Given two strings, write a method to decide if one is a permutation of the other.

def is_permutation(s1, s2):
  return sorted(s1) == sorted(s2)

print "Ans for Q 1.3"
print is_permutation("ababa", "aabba")
print is_permutation("aa", "aa")
print is_permutation("", "")
print is_permutation("a", "")
print

# 1.4 Write a method to replace all spaces in a string with'%20'. You may assume that the string has sufficient space at the end of the string to hold the additional
# characters, and that you are given the "true" length of the string. (Note: if implementing
# in Java, please use a character array so that you can perform this operation
# in place.)
# EXAMPLE
# Input: "Mr John Smith
# Output: "Mr%20Dohn%20Smith"


def space_replace(string):
  return string.replace(" ", "%20")

print "Ans for Q 1.4"
print space_replace("Mr John Smith")
print space_replace("Mr JohnSmith")
print space_replace("")
print


# 1.5 Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become
# a2blc5a3. If the "compressed" string would not become smaller than the original
# string, your method should return the original string.
def string_compress(string):
  if len(string) <= 1:
    return string
  res = list()
  count = 1
  last = string[0]
  for i in xrange(1, len(string)):
    if string[i] == last:
      count += 1
    else:
      res.append(last)
      res.append(str(count))
      last = string[i]
      count = 1

  res.append(last)
  res.append(str(count))

  if len(string) <= len("".join(res)):
    return string
  else:
    return "".join(res)

print "Ans for Q 1.5"
print string_compress("aabcccccaaa")
print string_compress("a")
print string_compress("aa")
print string_compress("")
print string_compress("abcd")
print


# 1.6 Given an image represented by an NxN matrix, where each pixel in the image is
# 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
# place?

def rotate_matrix_90(matrix):
  n = len(matrix)
  res = []
  for i in xrange(n):
    row = []
    for j in xrange(n):
      row.append(matrix[n - 1 - j][i])
    res.append(row)
  return res


def rotate_matrix_90_in_place(matrix):
  # to be done
  return matrix

print "Ans for Q 1.6"
print rotate_matrix_90([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print rotate_matrix_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print rotate_matrix_90_in_place([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print rotate_matrix_90_in_place([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print


# 1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row
# and column are set to 0.

def set_zeros(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  zero_rows = []
  zero_cols = []
  for i in xrange(rows):
    for j in xrange(cols):
      if matrix[i][j] == 0:
        zero_rows.append(i)
        zero_cols.append(j)
  for i in xrange(rows):
    for j in xrange(cols):
      if (i in zero_rows or j in zero_cols):
        matrix[i][j] = 0
  return matrix

print "Ans for Q 1.7"
print set_zeros([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print set_zeros([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print set_zeros([[1, 2, 0, 4], [5, 6, 7, 8], [9, 10, 11, 12], [0, 14, 15, 16]])
