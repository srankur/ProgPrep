"""

Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?

"""


import LinkedList



# Create List


if __name__ == "__main__":
    input = [5, 4, 3, 2, 1]
    ls = List()
    ls.CreateList(input)
    ls.isPalindrome_checkwithStack(ls.head)
