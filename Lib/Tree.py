from Lib.Node import TreeNode


class BinaryTree:
    """
    
    """

    def __init__(self, rootValue=None) -> None:
        """
        
        Parameters
        ----------
        rootValue
        """
        self.__root = None if rootValue is None else TreeNode(rootValue)

    """
    
    """

    def preOrder(self, value, function) -> None:
        """
        
        Parameters
        ----------
        value
        function

        Returns
        -------

        """
        current = self.__root

        if current is None:
            return
        else:
            self.__preOrder(value, current, function)

    """
    
    """

    def __preOrder(self, value, node: TreeNode, function) -> None:
        """
        
        Parameters
        ----------
        value
        node
        function

        Returns
        -------

        """
        if node is None:
            return

        function(node.data)
        self.__preOrder(value, node.left, function)
        self.__preOrder(value, node.right, function)

    """
    
    """

    def inOrder(self, function) -> None:
        """
        
        Parameters
        ----------
        function

        Returns
        -------

        """
        current = self.__root

        if current is None:
            return
        else:
            self.__inOrder(current, function)

    """
    
    """

    def __inOrder(self, node: TreeNode, function) -> None:
        """
        
        Parameters
        ----------
        node
        function

        Returns
        -------

        """
        if node is None:
            return

        self.__inOrder(node.left, function)
        function(node.data)
        self.__inOrder(node.right, function)

    """
    """

    def postOrder(self, value: TreeNode, function) -> None:
        """
        
        Parameters
        ----------
        value
        function

        Returns
        -------

        """
        current = self.__root

        if current is None:
            return
        else:
            self.__postOrder(value, current, function)

    """
    """

    def __postOrder(self, value, node: TreeNode, function) -> None:
        """
        
        Parameters
        ----------
        value
        node
        function

        Returns
        -------

        """
        if node is None:
            return

        self.__postOrder(value, node.left, function)
        self.__postOrder(value, node.right, function)
        function(node.data)

    """
    """

    def add(self, value) -> None:
        """
        
        Parameters
        ----------
        value

        Returns
        -------

        """
        if self.__root is None:
            self.__root = TreeNode(value)
            return

        if value is None:
            return

        self.__root.add(value)

    """
    """

    def print(self) -> None:
        """
        
        Returns
        -------

        """
        self.__print(self.__root)

    """
    """

    def __print(self, node, count=0) -> None:
        """
        
        Parameters
        ----------
        node
        count

        Returns
        -------

        """
        if node is None:
            return

        for i in range(count):
            print('-', end='')

        self.__print(node.left, count + 1)
        print(node.data)
        self.__print(node.right, count + 1)


def main():
    tree = BinaryTree()
    tree.add(5)
    tree.add(6)
    tree.add(4)
    tree.print()


if __name__ == '__main__':
    main()
