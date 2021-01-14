from .Node import DoubleLinkNode

class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def size(self):
        """Get the number of nodes in the queue

        Returns
        -------
        int
            number of the nodes in the queue
        """
        return self.__count

    def isEmpty(self):
        """Verify that the queue is empty

        Returns
        -------
        bool
            whether the queue is empty or not
        """
        return self.__count == 0

    def enQueue(self, element):
        """Insert an element to the back of the queue

        Parameters
        -------
        element : any
            The element to be inserted
        """
        if type(element) is not DoubleLinkNode:
            element = DoubleLinkNode(element)

        if self.__tail is not None:
            self.__tail.secondLink = element
            self.__tail.secondLink.firstLink = self.__tail 
            self.__tail = self.__tail.secondLink
        else: 
            self.__head = element
            self.__tail = self.__head 

        self.__count += 1

    def deQueue(self):
        """Remove the element from the beginning of the queue and get its content

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
        if self.__head is not None:
            current = self.__head.data 
            self.__head = self.__head.secondLink
            self.__head.prev=None
            self.__count -= 1
            return current 
        else:
            raise Exception('Queue is empty')


    def front(self):
        """Get the data from the first node of the queue

        Returns
        -------
        any
            The element placed on the specified index

        Raises
        -------
        Exception
            If the stack is empty
        """
        if self.__count != 0:
            return self.__head.data
        else:
            raise Exception('Queue is empty')

    def rear(self):
        """Get the data from the last node of the queue

        Returns
        -------
        any
            The element placed on the specified index

        Raises
        -------
        Exception
            If the stack is empty
        """
        if self.__count != 0:
            return self.__tail.data
        else:
            raise Exception('Queue is empty')

    def printToConsole(self):
        """Print out the current linked list to the console in order"""
        current = self.__head
        while current is not None:
            print(current.data)
            current = current.secondLink