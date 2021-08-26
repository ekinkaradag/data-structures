from .LinkedList import LinkedList

class Stack:
    """
    A custom class for a stack

    Methods
    -------
    isEmpty()
        Return whether the stack is empty or not

    push(element)
        Push an element to the stack

    top()
        Get the top element of the stack

    pop(get=True)
        Get the top element, and remove it from the stack
        
    hardCopyUsing(obj, printProcess=False)
        Remove all the existing content of the current stack and replace it with another stack's content
    """

    def __init__(self, orderedList=[]):
        """If initialized using a list, elements will be added to the stack one by one in order.

        Parameters
        ----------
        orderedList : list, optional
            The stack will be populated using this list
        """
        self.__linkedList = LinkedList()
        if len(orderedList) != 0:
            for item in orderedList:
                self.push(item)

    def isEmpty(self):
        """Verify that the stack is empty

        Returns
        -------
        bool
            whether the stack is empty or not
        """
        return self.__linkedList.isEmpty()

    def push(self, element):
        """Push an element to the stack

        Parameters
        -------
        element : any
            The element to be pushed
        """
        self.__linkedList.insertToStart(element)

    def top(self):
        """Get the top element of the stack

        Returns
        -------
        top : any
            The top element of the stack

        Raises
        -------
        Exception
            If the stack is empty
        """
        if not self.isEmpty():
            return self.__linkedList.getElementByIndex(0)
        else:
            raise Exception('Stack is empty.')

    def pop(self, get=True):
        """Get the top element, and remove it from the stack

        Parameters
        -------
        get : bool
            Whether to return to top element before removing (default is True)

        Returns
        -------
        element : any
            The top element on the stack before removing it

        Raises
        -------
        Exception
            If the stack is empty
        """
        if not self.isEmpty():
            if get is False:
                self.__linkedList.remove(index=0)
            else:
                element = self.top()
                self.__linkedList.remove(index=0)
                return element
        else:
            raise Exception('Stack is empty.')

    def hardCopyUsing(self, obj, printProcess=False):
        """Remove all the existing content of the current stack and replace it with another stack's content

        Parameters
        -------
        obj : Stack
            This stack will be copied onto the current stack
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
        if type(obj) is Stack:
            # Clear the current Stack
            while self.__linkedList.size() != 0:
                self.pop(get=printProcess)
            for i in range(obj.__linkedList.size()-1, -1, -1):
                self.__linkedList.insertToStart(obj.__linkedList.getElementByIndex(i))
        else:
            raise Exception("Stack object needs to be passed as an argument.")
