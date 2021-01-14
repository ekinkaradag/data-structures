from Lib.Node import SingleLinkNode
from Lib.LinkedList import LinkedList
from Lib.Stack import Stack
from Lib.Queue import Queue
import os
import sys
import filecmp

class bcolors:
        GREEN = '\033[92m'
        RED = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'

class Test:
        def linkedListTest(self, keepResultFile=False):
                resultFile = "linkedlist_result.txt"
                original_stdout = sys.stdout

                with open(resultFile, "w") as f:
                        sys.stdout = f

                        customList = LinkedList()
                        customList.insertToStart(SingleLinkNode(2))
                        customList.insertToStart(1)
                        customList.insertToEnd('3')
                        customList.insertToEnd('4')
                        customList.insertToEnd(5)

                        print(customList.getElementByIndex(2))
                        print('----')
                        customList.printToConsole()
                        print('----')
                        customList2 = LinkedList()
                        customList2.hardCopyUsing(customList)
                        customList2.printToConsole()
                        print("----")
                        customList.remove(element='4')
                        customList.reverse()
                        customList.printToConsole()
                        print('Size = ' + str(customList.size()))
                        print('Index of 1 is ' + str(customList.find(1)))
                        print('Index of 2 is ' + str(customList.find(2)))
                        print('Index of 3 is ' + str(customList.find('3')))
                        print('Index of 4 is ' + str(customList.find('4')))
                        print('Index of 5 is ' + str(customList.find(5)))
                        print('Index of 20 is ' + str(customList.find(20)))
                        print("----")
                        customList3 = LinkedList([0,1,2,3,4,5,6,7,8,9])
                        customList3.printToConsole()
                        

                        sys.stdout = original_stdout

                print("Linked List Test Result: ", end="")
                if filecmp.cmp(resultFile,"test_answer_key/linkedlist_answer_key.txt"):
                        print(bcolors.GREEN + bcolors.BOLD + "PASSED" + bcolors.ENDC)
                        if not keepResultFile:
                                os.remove(resultFile)
                else:
                        print(bcolors.RED + bcolors.BOLD + "FAILED" + bcolors.ENDC)
            
        def stackTest(self, keepResultFile=False):
                resultFile = "stack_result.txt"
                original_stdout = sys.stdout
                with open(resultFile, "w") as f:
                        sys.stdout = f
                        
                        st = Stack()
                        st.push(0)
                        st.push('1')
                        st.push(SingleLinkNode(2))
                        st.push(SingleLinkNode('3'))

                        print(st.pop())
                        print(st.top())
                        print(st.top())
                        print("----")
                        st2 = Stack()
                        st2.hardCopyUsing(st, printProcess=False)
                        print("Copied Stack is empty = " + str(st2.isEmpty()))
                        print("Copied Stack's top element = " + str(st2.top()))
                        print("----")
                        st3 = Stack([0,1,2,3,4,5])
                        print(st3.top())
                        print(st3.pop())
                        print(st3.top())
                        

                        sys.stdout = original_stdout

                print("Stack Test Result: ", end="")
                if filecmp.cmp(resultFile,"test_answer_key/stack_answer_key.txt"):
                        print(bcolors.GREEN + bcolors.BOLD + "PASSED" + bcolors.ENDC)
                        if not keepResultFile:
                                os.remove(resultFile)
                else:
                        print(bcolors.RED + bcolors.BOLD + "FAILED" + bcolors.ENDC)

        def queueTest(self, keepResultFile=False):
                resultFile = "queue_result.txt"
                original_stdout = sys.stdout
                with open(resultFile, "w") as f:
                        sys.stdout = f
                        
                        # While the queue is empty
                        q = Queue()
                        try:
                                q.deQueue()
                        except Exception as e:
                                print(str(e))
                        try:
                                q.front()
                        except Exception as e:
                                print(str(e))
                        print(q.size())
                        print(q.isEmpty())
                        q.enQueue(0)
                        q.enQueue(1)
                        q.enQueue(2)
                        q.enQueue(3)
                        print(q.size())
                        print(q.deQueue())
                        print(q.isEmpty())
                        print(q.front())
                        print(q.rear())
                        q.printToConsole()
                        
                        sys.stdout = original_stdout

                print("Stack Test Result: ", end="")
                if filecmp.cmp(resultFile,"test_answer_key/queue_answer_key.txt"):
                        print(bcolors.GREEN + bcolors.BOLD + "PASSED" + bcolors.ENDC)
                        if not keepResultFile:
                                os.remove(resultFile)
                else:
                        print(bcolors.RED + bcolors.BOLD + "FAILED" + bcolors.ENDC)
                

test = Test()
test.linkedListTest()
test.stackTest()
test.queueTest()