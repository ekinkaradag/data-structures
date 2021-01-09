from linked_list import LinkedList

class Stack:
    def __init__(self):
        self.__linkedList = LinkedList()

    def size(self):
        return self.__linkedList.size()

    def isEmpty(self):
        return self.__linkedList.isEmpty()

    def push(self, data):
        self.__linkedList.insertToStart(data)

    def top(self):
        length = self.__linkedList.size()
        if length > 0:
            return self.__linkedList.getDataByIndex(0)
        else:
            raise Exception('Stack does not have any data.')

    def pop(self, get=True):
        if get is False:
            self.__linkedList.remove(index=0)
        else:
            data = self.__linkedList.getDataByIndex(0)
            self.__linkedList.remove(index=0)
            return data

    def hardCopyUsing(self, obj, printProcess=True):
        if type(obj) is not Stack:
            raise Exception("Stack object needs to be passed as an argument.")
        else:
            # Clear the current Stack
            while self.size() is not 0:
                self.pop(get=printProcess)
            for i in range(obj.size()):
                self.__linkedList.insertToEnd(obj.stack.getDataByIndex(i))

    def printToConsole(self):
        self.__linkedList.printToConsole()