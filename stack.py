from linked_list import LinkedList

class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def size(self):
        return self.stack.size()

    def isEmpty(self):
        return self.stack.isEmpty()

    def push(self, data):
        self.stack.insertToStart(data)

    def top(self):
        length = self.stack.size()
        if length > 0:
            return self.stack.getDataByIndex(0)
        else:
            raise Exception('Stack does not have any data.')

    def pop(self, get=True):
        if get is False:
            self.stack.remove(index=0)
        else:
            data = self.stack.getDataByIndex(0)
            self.stack.remove(index=0)
            return data

    def hardCopyUsing(self, obj, printProcess=True):
        if type(obj) is not Stack:
            raise Exception("Stack object needs to be passed as an argument.")
        else:
            # Clear the current Stack
            while self.size() is not 0:
                self.pop(get=printProcess)
            for i in range(obj.size()):
                self.stack.insertToEnd(obj.stack.getDataByIndex(i))

    def printToConsole(self):
        self.stack.printToConsole()