"""

Reverse Linked List
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?

"""
from Leet.Easy.LinkedList.CreateList import List




# Driver Code
if __name__ == "__main__":
    # Create List
    input = [5,4,3,2,1,6]
    ls = List()
    ls.CreateList(input)


    ls.printList(ls.ReverseList_iterative(ls.head))
    #ls.printList(ls.ReverseList_recursive(ls.head))