class Node:
    def __init__(self, value=None):
        self.value = value
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def length(self):
        return self.count

    def insertToStart(self, value=Node()):
        if type(value) is not Node:
            value = Node(value)
        
        value.link = self.head
        self.head = value

        del value
        self.count += 1

    def insertToEnd(self, value=Node()):
        if type(value) is not Node:
            value = Node(value)
        current = self.head
        while current.link is not None:
            current = current.link
        current.link = value
        del value

        self.count += 1

    def printToConsole(self):
        current = self.head
        while current is not None:
            if current.value is not None:
                print(current.value)
            current = current.link

    def find(self, value):
        current = self.head
        pos = 0

        while current:
            if current.value == value:
                return pos
            else:
                pos += 1
                current = current.link
        return -1

        


            

