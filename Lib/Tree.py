from Lib.Node import TreeNode


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
        Method for traversing a tree starting from the root and further from the left subtree followed by the right.
        This method using to create copy of tree.

        Algorithm Preorder(tree)
            1. Visit the root.
            2. Traverse the left subtree, i.e., call preOrder(left-subtree)
            3. Traverse the right subtree, i.e., call preOrder(right-subtree)

    inOrder(function)
        Algorithm Inorder(tree)
            1. Traverse the left subtree, i.e., call Inorder(left-subtree)
            2. Visit the root.
            3. Traverse the right subtree, i.e., call Inorder(right-subtree)

    postOrder(function)
        Method for traversing the tree, starting with the leftmost child and gradually moving to the rightmost child.
        Postorder traversal is used to delete the tree

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
        rootValue
            The root value of Tree.
        """
        self.__root = None if rootValue is None else TreeNode(rootValue)

    def isEmpty(self) -> bool:
        """
        Verify that the tree is empty.
        Returns
        -------
        bool
            true if tree is empty else false.
        """
        return self.__root is None

    def getRoot(self):
        """
        Get root value.
        Returns
        -------
            root value.
        """
        if self.__root is None:
            return None
        return self.__root.data

    def getMaxValue(self):
        """
        Get the rightmost subtree.

        Returns
        -------
            max value in tree.
        """
        if self.__root is None:
            return None
        return self.__root.getMaxValue()

    def getMinValue(self):
        """
        Get the leftmost subtree.

        Returns
        -------
            min value in tree.
        """
        if self.__root is None:
            return None
        return self.__root.getMinValue()

    def preOrder(self, function) -> None:
        """
        Method for traversing a tree starting from the root and further from the left subtree followed by the right.
        This method using to create copy of tree.

        Algorithm Preorder(tree)
            1. Visit the root.
            2. Traverse the left subtree, i.e., call preOrder(left-subtree)
            3. Traverse the right subtree, i.e., call preOrder(right-subtree)
        Parameters
        ----------
        function
            Function with one argument to apply on each element tree.
        """
        current = self.__root

        if current is None:
            return
        else:
            self.__preOrder(current, function)

    def __preOrder(self, node: TreeNode, function) -> None:
        """
        Method for traversing a tree starting from the root and further from the left subtree followed by the right.
        This method using to create copy of tree. This method uses a recursive approach to traverse the tree.

        Parameters
        ----------
        node
            current node (subtree) in tree.
        function
            function with one argument to apply on each element tree.
        """
        if node is None:
            return

        function(node.data)
        self.__preOrder(node.left, function)
        self.__preOrder(node.right, function)

    def inOrder(self, function) -> None:
        """
        This method uses a recursive approach to traverse the tree.
        Algorithm Inorder(tree)
            1. Traverse the left subtree, i.e., call Inorder(left-subtree)
            2. Visit the root.
            3. Traverse the right subtree, i.e., call Inorder(right-subtree)

        Parameters
        ----------
        function
            function with one argument to apply on each element tree.
        """
        current = self.__root

        if current is None:
            return
        else:
            self.__inOrder(current, function)

    def __inOrder(self, node: TreeNode, function) -> None:
        """
        Parameters
        ----------
        node
            current node (subtree) in tree.
        function
            function with one argument to apply on each element tree.
        """
        if node is None:
            return

        self.__inOrder(node.left, function)
        function(node.data)
        self.__inOrder(node.right, function)

    def postOrder(self, function) -> None:
        """
        Method for traversing the tree, starting with the leftmost child and gradually moving to the rightmost child.
        Postorder traversal is used to delete the tree

        Algorithm Postorder(tree)
           1. Traverse the left subtree, i.e., call Postorder(left-subtree)
           2. Traverse the right subtree, i.e., call Postorder(right-subtree)
           3. Visit the root.
        Parameters
        ----------
        function
            function with one argument to apply on each element tree.
        """
        current = self.__root

        if current is None:
            return
        else:
            self.__postOrder(current, function)

    def __postOrder(self, node: TreeNode, function) -> None:
        """
        Method for traversing the tree, starting with the leftmost child and gradually moving to the rightmost child.
        Postorder traversal is used to delete the tree. This method uses a recursive approach to traverse the tree.
        Parameters
        ----------
        node
            current node (subtree) in tree.
        function
            function with one argument to apply on each element tree.
        """
        if node is None:
            return

        self.__postOrder(node.left, function)
        self.__postOrder(node.right, function)
        function(node.data)

    def add(self, value) -> bool:
        """
        Add element to tree.
        Parameters
        ----------
        value
            value to add in tree.
        Returns
        -------
            true if element added to tree else false.
        """
        if self.__root is None:
            self.__root = TreeNode(value)
            return True

        if value is None:
            return False

        self.__root.add(value)

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
        node
            current node (subtree) in tree.
        numberChildInTree
            node number in the tree to output characters to the console.
        """
        if node is None:
            return

        self.__print(node.left, numberChildInTree + 1)
        for i in range(numberChildInTree):
            print('-', end='')
        print(node.data)
        self.__print(node.right, numberChildInTree + 1)
