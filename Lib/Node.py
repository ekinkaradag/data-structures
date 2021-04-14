class SingleLinkNode:
    """
    A node class to hold the data and its linked node

    Attributes
    -------
    data : any
        The data to be held

    link : Node
        Next linked node
    """

    def __init__(self, data=None):
        self.data = data
        self.link = None


class DoubleLinkNode:
    """
    A node class to hold the data and its two linked nodes

    Attributes
    -------
    data : any
        The data to be held

    firstLink : Node
        First linked node

    secondLink : Node
        Second linked node
    """

    def __init__(self, data=None):
        self.data = data
        self.firstLink = None
        self.secondLink = None


class TreeNode:
    """
    A node class to hold the data, left subtree and right subtree

    Attributes
    -------
    data : any
        The data to be held

    left : TreeNode
        Left subtree

    right : TreeNode
        Right subtree

    """

    def __init__(self, data, left=None, right=None) -> None:
        """
        Parameters
        ----------
        data : any

        left : TreeNode

        right : TreeNode
        """
        self.data = data
        self.left = left
        self.right = right

    def add(self, element) -> bool:
        """
        Add element to left node or right.
        Parameters
        ----------
        element
            element to left node or right.

        Returns
        -------
        bool
            true if element is added else false
        """
        if self.data == element.data:
            return False

        if self.data > element.data:
            if self.left is None:
                self.left = element
                return True
            else:
                return self.left.add(element)
        else:
            if self.right is None:
                self.right = element
                return True
            else:
                return self.right.add(element)

    def getMaxValue(self):
        """
        Get the rightmost subtree.

        Returns
        -------
            Max value in tree
        """
        if self.right is None:
            return self.data
        return self.right.getMaxValue()

    def getMinValue(self):
        """
        Get the leftmost subtree.
        
        Returns
        -------
            Min value in tree.
        """
        if self.left is None:
            return self.data
        return self.left.getMinValue()
