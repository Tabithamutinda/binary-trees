"""Perfect Binary Tree
Definition: A full binary tree where all internal nodes have two children, and all leaves are at the same level.
Explanation: Every level of the tree is fully filled, making it perfectly balanced.
Use Case:
Complete Decision Processes: Ensures every possible outcome is represented, which is critical in decision trees used for AI and machine learning."""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example Perfect Binary Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)





"""Skewed Binary Tree
Definition: A binary tree in which all nodes have only one child, either left or right, making the tree resemble a linked list.
Explanation: A special case where the tree has the worst-case height, which is equal to the number of nodes.
Use Case:
Edge Case Analysis: Used in algorithm testing to examine performance in worst-case scenarios."""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example of Left Skewed Binary Tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.left = Node(4)


"""Degenerate (or Pathological) Tree
Definition: A tree where each parent node has only one child, resembling a linked list.
Explanation: It’s the same as a skewed binary tree but emphasizes that such a structure can lead to poor performance in operations like search and insertion.
Use Case:
Testing Algorithm Efficiency: Used to simulate worst-case scenarios for operations like search, insertion, and deletion."""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example  of a Right Skewed Degenerate Binary Tree
root = Node(1)
root.right = Node(2)
root.right.right = Node(3)
root.right.right.right = Node(4)

