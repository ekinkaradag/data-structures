from .Node import TreeNode


class BinaryTree:
    """
     A custom class for a BinaryTree

    Methods
    -------
    isEmpty()
        Return true if tree is empty else false.

    add(element)
        Add element to tree.

    getRoot()
        Get the root value.

    getMaxValue()
        Get the rightmost subtree.

    getMinValue()
        Get the leftmost subtree.

    preOrder(function)
        Do preorder tree traversal, starting from the root and further from the left subtree followed by the right.

        Algorithm Preorder(tree)
            1. Visit the root.
            2. Traverse the left subtree, i.e., call preOrder(left-subtree)
            3. Traverse the right subtree, i.e., call preOrder(right-subtree)

    inOrder(function)
        Do inorder tree traversal
        Algorithm Inorder(tree)
            1. Traverse the left subtree, i.e., call Inorder(left-subtree)
            2. Visit the root.
            3. Traverse the right subtree, i.e., call Inorder(right-subtree)

    postOrder(function)
        Do postorder tree traversal, starting with the leftmost child and gradually moving to the rightmost child.

        Algorithm Postorder(tree)
           1. Traverse the left subtree, i.e., call Postorder(left-subtree)
           2. Traverse the right subtree, i.e., call Postorder(right-subtree)
           3. Visit the root.

    print()
        Print out the current queue to the console in inOrder traveling.
    """

    def __init__(self, rootValue=None) -> None:
        """If initialized using root, the rest of the descendants will branch out from it.

        Parameters
        ----------
        rootValue : any
            The root value of Tree.
        """
        self.__root = None if rootValue is None else TreeNode(rootValue)

    def isEmpty(self) -> bool:
        """
        Verify that the tree is empty.

        Returns
        -------
        bool :
            whether the tree is empty or not
        """
        return self.__root is None

    def getRoot(self):
        """
        Get the root value.
        
        Returns
        -------
            root value.
        """
        if self.__root is None:
            return None
        return self.__root.data

    def getMaxValue(self):
        """
        Get the value of the rightmost node in the tree.

        Returns
        -------
            maximum value in tree.
        """
        if self.__root is None:
            return None
        return self.__root.getMaxValue()

    def getMinValue(self):
        """
        Get the value of the leftmost node in the tree.

        Returns
        -------
            minimum value in tree.
        """
        if self.__root is None:
            return None
        return self.__root.getMinValue()

    def preOrder(self, function) -> None:
        """
        Do preorder tree traversal, starting from the root and further from the left subtree followed by the right.

        Algorithm Preorder(tree)
            1. Visit the root.
            2. Traverse the left subtree, i.e., call preOrder(left-subtree)
            3. Traverse the right subtree, i.e., call preOrder(right-subtree)

        Parameters
        ----------
        function : 
            Function with one argument to apply on each element of the tree.
        """
        current = self.__root

        if current is None:
            return
        else:
            self.__preOrder(current, function)

    def __preOrder(self, node: TreeNode, function) -> None:
        """
        Do preorder tree traversal, starting from the root and further from the left subtree followed by the right.

        Parameters
        ----------
        node : TreeNode
            current node (subtree) in tree.

        function : 
            function with one argument to apply on each element of the tree.
        """
        if node is None:
            return

        function(node.data)
        self.__preOrder(node.left, function)
        self.__preOrder(node.right, function)

    def inOrder(self, function) -> None:
        """
        Do inorder tree traversal

        Algorithm Inorder(tree)
            1. Traverse the left subtree, i.e., call Inorder(left-subtree)
            2. Visit the root.
            3. Traverse the right subtree, i.e., call Inorder(right-subtree)

        Parameters
        ----------
        function
            function with one argument to apply on each element of the tree.
        """
        current = self.__root

        if current is None:
            return
        else:
            self.__inOrder(current, function)

    def __inOrder(self, node: TreeNode, function) -> None:
        """
        Do inorder tree traversal

        Parameters
        ----------
        node : TreeNode
            current node (subtree) in tree.

        function
            function with one argument to apply on each element of the tree.
        """
        if node is None:
            return

        self.__inOrder(node.left, function)
        function(node.data)
        self.__inOrder(node.right, function)

    def postOrder(self, function) -> None:
        """
        Do postorder tree traversal, starting with the leftmost child and gradually moving to the rightmost child.

        Algorithm Postorder(tree)
           1. Traverse the left subtree, i.e., call Postorder(left-subtree)
           2. Traverse the right subtree, i.e., call Postorder(right-subtree)
           3. Visit the root.

        Parameters
        ----------
        function
            function with one argument to apply on each element of the tree.
        """
        current = self.__root

        if current is None:
            return
        else:
            self.__postOrder(current, function)

    def __postOrder(self, node: TreeNode, function) -> None:
        """
        Do postorder tree traversal, starting with the leftmost child and gradually moving to the rightmost child.

        Parameters
        ----------
        node : TreeNode
            current node (subtree) in tree.

        function
            function with one argument to apply on each element of the tree.
        """
        if node is None:
            return

        self.__postOrder(node.left, function)
        self.__postOrder(node.right, function)
        function(node.data)

    def add(self, element) -> bool:
        """
        Add an element to the tree.

        Parameters
        ----------
        element : any
            element to add to the tree.

        Returns
        -------
        bool
            whether the element is added to tree or not
        """
        if element is None:
            return False
        elif type(element) is not TreeNode:
            element = TreeNode(element)

        if self.__root is None:
            self.__root = element
            return True

        self.__root.add(element)

    def print(self) -> None:
        """
        Print out the current queue to the console in inOrder traveling.
        """

        self.__print(self.__root, 0)

    def __print(self, node, numberChildInTree) -> None:
        """
        Print out the current queue to the console in inOrder traveling.

        Parameters
        ----------
        node : TreeNode
            current node (subtree) in tree.

        numberChildInTree
            node number in the tree to output characters to the console.
        """
        if node is None:
            return

        self.__print(node.left, numberChildInTree + 1)
        for _ in range(numberChildInTree):
            print('-', end='')
        print(node.data)
        self.__print(node.right, numberChildInTree + 1)
