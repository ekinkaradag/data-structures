from linked_list import *
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

                original_stdout = sys.stdout
                with open(resultFile, "w") as f:
                        sys.stdout = f

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
