class Node:
    def __init__(self, key):
        # Initialize the node with a value (key), and set left and right children to None
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    # If the tree is empty, create a new node and return it
    if root is None:
        return Node(key)
    
    # If the key is smaller than the root, insert it into the left subtree
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        # If the key is greater than the root, insert it into the right subtree
        root.right = insert(root.right, key)
    
    # Return the unchanged root node
    return root

def inorder_traversal(root):
    if root:
        # Recursively traverse the left subtree
        inorder_traversal(root.left)
        # Print the value of the current node
        print(root.val, end=' ')
        # Recursively traverse the right subtree
        inorder_traversal(root.right)

# Example Usage:
if __name__ == "__main__":
    # Create the root node with value 1
    root = Node(1)
    
    root.left = Node(2)          # Create left child of root (value 2)
    root.right = Node(3)         # Create right child of root (value 3)
    
    root.left.left = Node(4)     # Create left child of node 2 (value 4)
    root.left.right = Node(5)    # Create right child of node 2 (value 5)
    
    root.right.left = Node(6)    # Create left child of node 3 (value 6)
    root.right.right = Node(7)   # Create right child of node 3 (value 7)
    
    # Perform inorder traversal of the tree
    # This will print the nodes in the following order: 4 2 5 1 6 3 7
    print("Inorder traversal of the full binary tree:")
    inorder_traversal(root)