from linked_list import *

class Test:
    def linkedListTest(self):
        print("""
Output should be like this:
3
1
2
3
4
4
3
2
1
Length = 4
Index of 1 is 0
Index of 2 is 1
Index of 3 is 2
Index of 4 is 3
Index of 20 is False
------------------------------------
Output:""")
        customList = LinkedList()
        customList.insertToStart(Node(2))
        customList.insertToStart(1)
        customList.insertToEnd('3')
        customList.insertToEnd('4')

        print(customList.getIndexOf(2))
        customList.printToConsole()
        customList.reverse()
        customList.printToConsole()
        print('Length = ' + str(customList.length()))
        print('Index of 1 is ' + str(customList.find(1)))
        print('Index of 2 is ' + str(customList.find(2)))
        print('Index of 3 is ' + str(customList.find('3')))
        print('Index of 4 is ' + str(customList.find('4')))

        print('Index of 20 is ' + str(customList.find(20)))

test = Test()
test.linkedListTest()