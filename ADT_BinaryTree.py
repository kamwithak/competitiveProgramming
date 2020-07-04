class Node:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    def insert(self, data):
        if self.root:
            if data < self.root:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.root:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.root = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.root)
        if self.right:
            self.right.PrintTree()

if __name__ == "__main__":
    root = Node(5)
    root.insert(1)
    root.insert(2)
    root.insert(3)
    root.insert(4)
    root.PrintTree()