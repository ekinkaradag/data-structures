from .Node import DoubleLinkNode

class Queue:
    """
    A custom class for a queue

    Methods
    -------
    size()
        Returns the number of nodes that are in the queue

    isEmpty()
        Returns whether the queue is empty or not

    enQueue(element)
        Insert an element to the back of the queue

    deQueue()
        Remove the element from the beginning of the queue and get its content

    front()
        Get the data from the first node of the queue

    rear()
        Get the data from the last node of the queue
        
    printToConsole()
        Print out the contents of the queue to the console
    """

    def __init__(self, orderedList=[]):
        """If initialized using a list, elements will be added to the queue in the same order

        Parameters
        ----------
        orderedList : list, optional
            The queue will be populated using this list
        """
        self.__head = None
        self.__tail = None
        self.__count = 0

        if len(orderedList) != 0:
            for i in range(len(orderedList)):
                self.enQueue(orderedList[i])

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

        Raises
        -------
        Exception
            If the stack is empty
        """
        if self.__head is not None:
            current = self.__head.data 
            self.__head = self.__head.secondLink
            self.__head.firstLink=None
            self.__count -= 1
            return current 
        else:
            raise Exception('Queue is empty')

    def front(self):
        """Get the data from the first node of the queue

        Returns
        -------
        any
            The first element in the queue

        Raises
        -------
        Exception
            If the queue is empty
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
            The last element in the queue

        Raises
        -------
        Exception
            If the stack is empty
        """
        if self.__count != 0:
            return self.__tail.data
        else:
            raise Exception('Queue is empty')
    
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
                current = current.secondLink
        return False

    def printToConsole(self):
        """Print out the current queue to the console in order"""
        current = self.__head
        while current is not None:
            print(current.data)
            current = current.secondLink