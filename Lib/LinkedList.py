from .Node import SingleLinkNode

class LinkedList:
    """
    A custom class for a linked list

    Methods
    -------
    size()
        Return the number of nodes that are in the linked list

    isEmpty()
        Return whether the linked list is empty or not

    insertToStart(element)
        Insert an element at the beginning of the linked list

    insertToEnd(element)
        Insert an element at the end of the linked list

    remove(index=None, element=None)
        Remove the element from the linked list either by passing an index, or the element itself
        
    find(element)
        Find the first existing element on the linked list and return it's index

    getElementByIndex(index)
        Return the element by passing its index as an argument

    reverse()
        Reverse the order of the linked list

    hardCopyUsing(obj, printProcess=False)
        Remove all the existing content of the current linked list and replace it with another linked list's content

    printToConsole()
        Print out the contents of the linked list to the console
    """

    def __init__(self, orderedList=[]):
        """If initialized using a list, elements will be added to the linked list in the same order

        Parameters
        ----------
        orderedList : list, optional
            The linked list will be populated using this list
        """
        self.__head = None
        self.__count = 0
        if len(orderedList) != 0:
            for i in range(len(orderedList)-1, -1, -1):
                self.insertToStart(orderedList[i])

    def size(self):
        """Get the number of nodes in the linked list

        Returns
        -------
        int
            number of the nodes in the linked list
        """
        return self.__count

    def isEmpty(self):
        """Verify that the linked list is empty

        Returns
        -------
        bool
            whether the linked list is empty or not
        """
        return self.__count == 0

    def insertToStart(self, element):
        """Insert an element at the beginning of the linked list

        Parameters
        -------
        element : any
            The element to be inserted
        """
        if type(element) is not SingleLinkNode:
            element = SingleLinkNode(element)
        
        element.link = self.__head
        self.__head = element

        del element
        self.__count += 1

    def insertToEnd(self, element):
        """Insert an element at the end of the linked list

        Parameters
        -------
        element : any
            The element to be inserted
        """
        if type(element) is not SingleLinkNode:
            element = SingleLinkNode(element)
        current = self.__head
        if self.__head is None:
            self.insertToStart(element)
        else:
            while current.link is not None:
                current = current.link
        
            current.link = element
            del element

            self.__count += 1

    def remove(self, index=None, element=None):
        """Remove the element from the linked list either by passing an index, or the element itself.
        If the element is passed, only the first found will be removed.

        Parameters
        -------
        index : int
            The index of the Node that is going to be removed
        element : any
            The element that is going to be removed

        Raises
        -------
        Exception
            If the stack is empty
        """
        if (element != None and index != None) or (element == None and index == None):
            raise Exception('Either "element" or "index" argument should be set.')
        else:
            current = self.__head
            if element != None:
                while current.data is not element:
                    current = current.link
            elif index != None:
                for _ in range(index):
                    current = current.link
            current.data = current.link.data
            current.link = current.link.link
            self.__count -= 1

    def find(self, element):
        """Find the first existing element in the linked list and get its index

        Parameters
        -------
        element : any
            The element to be found

        Returns
        -------
        int, bool
            If found, returns the index of the element. If not found, returns False.
        """
        current = self.__head
        position = 0

        while current:
            if current.data == element:
                return position
            else:
                position += 1
                current = current.link
        return False
    
    def getElementByIndex(self, index):
        """Get the specific element from the linked list by using the specified index

        Parameters
        -------
        index : int
            Index of the required element

        Returns
        -------
        any
            The element placed on the specified index
        """
        current = self.__head
        if not self.isEmpty():
            for _ in range(index):
                current = current.link
            return current.data
        else:
            raise Exception("The LinkedList is empty")

    def reverse(self):
        """Reverse the linked list's order"""
        previous = None
        current = self.__head
        while current:
            next = current.link
            current.link = previous
            previous = current
            current = next
        self.__head = previous

    def hardCopyUsing(self, obj, printProcess=False):
        """Remove all the existing content of the current linked list and replace it with another linked list's content

        Parameters
        -------
        obj : Stack
            This stack will copied onto the current stack
        printProcess : bool
            Whether to print every element that is being copied to the console

        Returns
        -------
        element : any
            The top element on the stack before removing it
            
        Raises
        -------
        Exception
            If the passed argument is not a Stack
        """
        if type(obj) is not LinkedList:
            raise Exception("LinkedList object needs to be passed as an argument.")
        else:
            # Clear the current LinkedList
            while self.size() != 0:
                self.remove(index=0)

            for i in range(obj.size()):
                self.insertToEnd(obj.getElementByIndex(i))
            

    def printToConsole(self):
        """Print out the current linked list to the console in order"""
        current = self.__head
        while current is not None:
            if current.data is not None:
                print(current.data)
            current = current.link
