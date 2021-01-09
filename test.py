from linked_list import *
from stack import *
import os
import sys
import filecmp

class Test:
        def linkedListTest(self, keepResultFile=False):
                resultFile = "linkedlist_result.txt"
                customList = LinkedList()
                customList.insertToStart(Node(2))
                customList.insertToStart(1)
                customList.insertToEnd('3')
                customList.insertToEnd('4')
                customList.insertToEnd(5)

                original_stdout = sys.stdout
                with open(resultFile, "w") as f:
                        sys.stdout = f

                        print(customList.getDataByIndex(2))
                        print('----')
                        customList.printToConsole()
                        print('----')
                        customList2 = LinkedList()
                        customList2.hardCopyUsing(customList)
                        customList2.printToConsole()
                        print("----")
                        customList.remove(data='4')
                        customList.remove(index=customList.getIndexByData(2))
                        customList.reverse()
                        customList.printToConsole()
                        print('Length = ' + str(customList.size()))
                        print('Index of 1 is ' + str(customList.find(1)))
                        print('Index of 2 is ' + str(customList.find(2)))
                        print('Index of 3 is ' + str(customList.find('3')))
                        print('Index of 4 is ' + str(customList.find('4')))
                        print('Index of 5 is ' + str(customList.find(5)))
                        print('Index of 20 is ' + str(customList.find(20)))

                        sys.stdout = original_stdout

                print("Linked List Test Result: ", end="")
                if filecmp.cmp(resultFile,"test_answer_key/linkedlist_answer_key.txt"):
                        print("PASSED")
                        if not keepResultFile:
                                os.remove(resultFile)
                else:
                        print("FAILED")
            


test = Test()
test.linkedListTest()
"""

st = Stack()
st.push(0)
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st2 = Stack()
st2.hardCopyUsing(st,False)

st.printToConsole()
print()
st2.printToConsole()
"""
