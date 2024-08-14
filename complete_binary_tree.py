class Node:
    def __init__(self, key):
        # Initialize a node with a given value and set left and right children to None
        self.left = None
        self.right = None
        self.val = key

def insert_level_order(arr, root, i, n):
    # Base case for recursion
    if i < n:
        # Create a new node with the current element of the array
        temp = Node(arr[i])
        root = temp

        # Insert the left child
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

        # Insert the right child
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    
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
    # Array representing a complete binary tree
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = len(arr)
    root = None

    # Create a complete binary tree from the array
    root = insert_level_order(arr, root, 0, n)
    
    # Perform inorder traversal of the tree
    # This will print the nodes in the following order: 4 2 5 1 6 3 7
    print("Inorder traversal of the complete binary tree:")
    inorder_traversal(root)