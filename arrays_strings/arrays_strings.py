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

print all_unique("aaaaaaa")
print all_unique("a")
print all_unique("ab")
print all_unique("")
print all_unique_2("aaaaaaa")
print all_unique_2("a")
print all_unique_2("ab")
print all_unique_2("")


# 1.3 Given two strings, write a method to decide if one is a permutation of the other.

def is_permutation(s1, s2):
  return sorted(s1) == sorted(s2)

print is_permutation("ababa", "aabba")
print is_permutation("aa", "aa")
print is_permutation("", "")
print is_permutation("a", "")

# 1.4 Write a method to replace all spaces in a string with'%20'. You may assume that the string has sufficient space at the end of the string to hold the additional
# characters, and that you are given the "true" length of the string. (Note: if implementing
# in Java, please use a character array so that you can perform this operation
# in place.)
# EXAMPLE
# Input: "Mr John Smith
# Output: "Mr%20Dohn%20Smith"

# 1.5 Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become
# a2blc5a3. If the "compressed" string would not become smaller than the original
# string, your method should return the original string.

# 1.6 Given an image represented by an NxN matrix, where each pixel in the image is
# 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
# place?
