class Node:
    def __init__(self, data, color="RED"):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(data=None, color="BLACK")
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k != self.root and k.parent.color == "RED":
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == "RED":
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == "RED":
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.left_rotate(k.parent.parent)
        self.root.color = "BLACK"

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = "BLACK"
            return

        if new_node.parent.parent is None:
            return

        self.fix_insert(new_node)

    def inorder_helper(self, node):
        if node != self.NIL:
            self.inorder_helper(node.left)
            if node.data is not None:
                print(node.data, end=' ')
            self.inorder_helper(node.right)

    def inorder(self):
        self.inorder_helper(self.root)
        print()

    def search_helper(self, node, data):
        if node == self.NIL or data == node.data:
            return node
        if data < node.data:
            return self.search_helper(node.left, data)
        return self.search_helper(node.right, data)

    def search(self, data):
        result = self.search_helper(self.root, data)
        return result if result != self.NIL else None

    def print_tree(self, node, level=0, prefix="Root: "):
        if node != self.NIL:
            print(" " * (level * 4) + prefix + f"{node.data}({node.color})")
            if node.left != self.NIL:
                self.print_tree(node.left, level + 1, "L--- ")
            if node.right != self.NIL:
                self.print_tree(node.right, level + 1, "R--- ")

# Example Usage
if __name__ == "__main__":
    rbt = RedBlackTree()

    # Inserting elements
    rbt.insert(10)
    rbt.insert(20)
    rbt.insert(30)
    rbt.insert(15)

    # Display the Red-Black Tree
    print("Red-Black Tree structure:")
    rbt.print_tree(rbt.root)

    # Inorder traversal
    print("\nInorder traversal:")
    rbt.inorder()  # Output: 10 15 20 30

    # Search for a node
    search_15 = rbt.search(15)
    search_25 = rbt.search(25)
    print("\nSearch for 15:", search_15 is not None)  # Output: True
    print("Search for 25:", search_25 is not None)  # Output: False

