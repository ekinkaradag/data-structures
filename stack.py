from linked_list import LinkedList

class Stack:
    def __init__(self):
        self.__linkedList = LinkedList()

    def isEmpty(self):
        return self.__linkedList.isEmpty()

    def push(self, data):
        self.__linkedList.insertToStart(data)

    def top(self):
        if not self.isEmpty():
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
            while self.__linkedList.size() is not 0:
                self.pop(get=printProcess)
            for i in range(obj.__linkedList.size()):
                self.__linkedList.insertToEnd(obj.__linkedList.getDataByIndex(i))