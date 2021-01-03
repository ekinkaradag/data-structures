from linked_list import *

customList = LinkedList()
customList.insertToStart(Node(2))
customList.insertToStart(1)
customList.insertToEnd('3')
customList.insertToEnd('4')
customList.printToConsole()
print('Length = ' + str(customList.length()))
print('index of 1 is ' + str(customList.find(1)))
print('index of 2 is ' + str(customList.find(2)))
print('index of 3 is ' + str(customList.find('3')))
print('index of 4 is ' + str(customList.find('4')))

print('index of None is ' + str(customList.find(None)))