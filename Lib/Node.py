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
    
