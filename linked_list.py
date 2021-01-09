class Node:
    def __init__(self, data=None):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0

    def insertToStart(self, data):
        if type(data) is not Node:
            data = Node(data)
        
        data.link = self.__head
        self.__head = data

        del data
        self.__count += 1

    def insertToEnd(self, data):
        if type(data) is not Node:
            data = Node(data)
        current = self.__head
        if self.__head is None:
            self.insertToStart(data)
        else:
            while current.link is not None:
                current = current.link
        
            current.link = data
            del data

            self.__count += 1

    def remove(self, index=None, data=None):
        if (data != None and index != None) or (data == None and index == None):
            raise Exception('Either "data" or "index" argument should be set.')
        else:
            current = self.__head
            if data != None:
                while current.data is not data:
                    current = current.link
            elif index != None:
                for _ in range(index):
                    current = current.link
            current.data = current.link.data
            current.link = current.link.link
            self.__count -= 1


    def find(self, data):
        current = self.__head
        position = 0

        while current:
            if current.data == data:
                return position
            else:
                position += 1
                current = current.link
        return False
    
    def getDataByIndex(self, index):
        current = self.__head
        if not self.isEmpty():
            for _ in range(index):
                current = current.link
            return current.data
        else:
            raise Exception("The LinkedList is empty")

    def getIndexByData(self, data):
        if self.__head is None:
            return False
        current = self.__head
        index = 0
        while current.data is not data:
            current = current.link
            index += 1
        return index

    def reverse(self):
        previous = None
        current = self.__head
        while(current is not None):
            next = current.link
            current.link = previous
            previous = current
            current = next
        self.__head = previous

    def hardCopyUsing(self, obj):
        if type(obj) is not LinkedList:
            raise Exception("LinkedList object needs to be passed as an argument.")
        else:
            # Clear the current LinkedList
            while self.size() is not 0:
                self.remove(index=0)
            for i in range(obj.size()):
                self.insertToEnd(obj.getDataByIndex(i))
            

    def printToConsole(self):
        current = self.__head
        while current is not None:
            if current.data is not None:
                print(current.data)
            current = current.link
