"""

Creating a list to support the operation in the list

"""

# Definition for singly-linked list.
class ListNode:
 def __init__(self, x):
     self.val = x
     self.next = None


class List:
    def __init__(self):
        self.head = None


    def CreateList(self, list_element = None):

        if list_element is None or len(list_element) == 0:
            return

        if self.head is None :
            self.head = self.addNode(list_element[0])

        current_node = self.head
        for i in range(1, len(list_element)):
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next= self.addNode(list_element[i])

        # Finally Print the updated list
        self.printList()


    def addNode(self, element ): # Pass list of element to create a list
        return(ListNode(element))


    def printList(self, Head = None):
        if Head == None:
            current_node = self.head
        else:
            current_node = Head

        print("Current List::\n")
        while current_node is not None:
            print("[%s]->" % current_node.val )
            current_node = current_node.next

    def deleteNode(self,node):
        current_node = self.head
        if current_node == node:
            current_node.val = current_node.next.val
            current_node.next = current_node.next.next

        # Finally Print the updated list
        self.printList()

    def removeNthFromEnd(self,  n):
        slow = self.head
        fast = self.head

        # Moving the fast pointer n steps ahead.
        for i in range(n):
            if fast.next:
                fast = fast.next
            else:
                print("List Exhausted")
                return

        while fast.next:
            if fast.next:
                slow = slow.next
                fast = fast.next

        slow.next = slow.next.next

        # Finally Print the updated list
        self.printList()

    def ReverseList_iterative(self,Head):
        Prev = None
        Curr = None
        Next = None

        if Head is not None:
            Curr = Head
        else:
            Curr = self.head

        while Curr:
            Next = Curr.next
            Curr.next = Prev
            Prev = Curr
            Curr = Next
        return Prev


    def ReverseList_recursive(self, Head):
        if Head == None:
            return

        if Head.next == None:
            self.head = Head
            return self.head

        self.ReverseList_recursive(Head.next)
        Head.next.next = Head
        Head.next = None




# Driver Code

if __name__ == "__main__":
    #listelment = [1,2,3,4,5]
    listelement = []
    ls = List()
    ls.CreateList(listelement)
    ls.printList()