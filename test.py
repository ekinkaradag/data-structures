from linked_list import *
from stack import *
import os
import sys
import filecmp

class Test:
        def linkedListTest(self, keepResultFile=False):
                resultFile = "linkedlist_result.txt"
                original_stdout = sys.stdout

                with open(resultFile, "w") as f:
                        sys.stdout = f

                        customList = LinkedList()
                        customList.insertToStart(Node(2))
                        customList.insertToStart(1)
                        customList.insertToEnd('3')
                        customList.insertToEnd('4')
                        customList.insertToEnd(5)

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
                        print('Size = ' + str(customList.size()))
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
            
        def stackTest(self, keepResultFile=False):
                resultFile = "stack_result.txt"
                original_stdout = sys.stdout
                with open(resultFile, "w") as f:
                        sys.stdout = f
                        
                        st = Stack()
                        st.push(0)
                        st.push('1')
                        st.push(Node(2))
                        st.push(Node('3'))

                        print(st.pop())
                        print(st.top())
                        print(st.top())
                        print("----")
                        st2 = Stack()
                        st2.hardCopyUsing(st, printProcess=False)
                        print("Copied Stack is empty = " + str(st2.isEmpty()))
                        print("Copied Stack's top element = " + str(st2.top()))

                        sys.stdout = original_stdout

                print("Stack Test Result: ", end="")
                if filecmp.cmp(resultFile,"test_answer_key/stack_answer_key.txt"):
                        print("PASSED")
                        if not keepResultFile:
                                os.remove(resultFile)
                else:
                        print("FAILED")
                

test = Test()
test.linkedListTest()
test.stackTest()
