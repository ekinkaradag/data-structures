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
    A node class to hold the data, left subtree and rigth subtree

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
        data
        left
        right
        """
        self.data = data
        self.left = left
        self.right = right

    """
    Method to add value to node.
    if value > root this right subtree, else left.
    """

    def add(self, value) -> None:
        """
        
        Parameters
        ----------
        value

        Returns
        -------

        """
        if self.data == value:
            return

        if self.data > value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.add(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.add(value)
