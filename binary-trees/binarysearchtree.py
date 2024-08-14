class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert_bst(root, key):
    if root is None:
        return BSTNode(key)
    else:
        if key < root.val:
            root.left = insert_bst(root.left, key)
        else:
            root.right = insert_bst(root.right, key)
    return root

def inorder_bst(root):
    if root:
        inorder_bst(root.left)
        print(root.val, end=' ')
        inorder_bst(root.right)

# Example of usage
bst_root = BSTNode(50)
insert_bst(bst_root, 30)
insert_bst(bst_root, 20)
insert_bst(bst_root, 40)
insert_bst(bst_root, 70)
insert_bst(bst_root, 60)
insert_bst(bst_root, 80)

inorder_bst(bst_root)
