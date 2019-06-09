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

    def ReverseList_iterative(self,Head = None):
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


    def ReverseList_recursive(self, Head = None):
        if Head == None:
            return

        if Head.next == None:
            self.head = Head
            return self.head

        self.ReverseList_recursive(Head.next)
        Head.next.next = Head
        Head.next = None

    def isPalindrome_twoPointer(self,Head = None):
        if Head != None:
            Curr = Head
        else:
            Curr = self.head

        Slow, Fast = Curr, Curr
        MidNode = None
        Prev_to_Slow = None
        while Fast and Fast.next:
            Fast = Fast.next.next
            Prev_to_Slow = Slow
            Slow = Slow.next


        if Fast is not None:
            MidNode = Slow
            Slow = Slow.next

        # Prepare the list for comparison
        Second_half = Slow
        Prev_to_Slow.next = None


        ls.printList("Second Half", Second_half)
        ls.printList("First Half",Curr)

        reverseList = ls.ReverseList_iterative(Slow)
        ls.printList( reverseList)

    def isPalindrome_checkwithStack(self, Head=None):
        if Head != None:
            Curr = Head
        else:
            Curr = self.head
        Val_stack = []
        while Curr:
            Val_stack.append(Curr.val)
            Curr = Curr.next
        print(Val_stack)

        Curr = self.head
        while Curr:
            #print("Stack:%s, CurrentVal: %s" % (Val_stack.pop(), Curr.val))
            if Val_stack.pop() != Curr.val:
                print("Not a Palindrome! ")
                return False
            Curr = Curr.next
        return True

    def printList(self,text = None, Head = None):
        if Head == None:
            current_node = self.head
        else:
            current_node = Head
        if text != None:
            print(text, ":")
        while current_node is not None:
            print("[%s]->" % current_node.val )
            current_node = current_node.next



# Driver Code
if __name__ == "__main__":
    listelment = [1,2,3,2,1]
    #listelment = []
    ls = List()
    ls.CreateList(listelment)
    #ls.printList()
    #print(ls.isPalindrome_checkwithStack(ls.head))
    print(ls.isPalindrome_twoPointer(ls.head))