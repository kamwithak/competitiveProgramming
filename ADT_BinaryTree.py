class BSTNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def insert(self, data):
        if self.key:
            if data < self.key:
                if self.left is None:
                    self.left = BSTNode(data)
                else:
                    self.left.insert(data)
            elif data > self.key:
                if self.right is None:
                    self.right = BSTNode(data)
                else:
                    self.right.insert(data)
        else:
            self.key = data

    def search(self, data):
        if self.key is None or self.key == data:
            return self.key
        if data < self.key: return self.left.search(data)
        else: return self.right.search(data)
    
    def minValueNodeIterative(self):
        cur = self
        while (cur.left):
            cur = cur.left
        print(cur.key)

    def minValueNodeRecursive(self, root):
        if (not root.left):
            print(root.key)
        else:
            self.minValueNodeRecursive(root.left)

    def maxValueNodeIterative(self):
        cur = self
        while (cur.right):
            cur = cur.right
        print(cur.key)
    
    def maxValueNodeRecursive(self, root):
        if (not root.right):
            print(root.key)
        else:
            self.maxValueNodeRecursive(root.right)

    def PrintTreeInOrder(self, root):
        if root.left:
            self.PrintTreeInOrder(root.left)
        print(root.key)
        if root.right:
            self.PrintTreeInOrder(root.right)

    def PrintTreePreOrder(self, root):
        print(root.key)
        if (root.left):
            self.PrintTreePreOrder(root.left)
        if (root.right):
            self.PrintTreePreOrder(root.right)
    
    def PrintTreePostOrder(self, root):
        if (root.left):
            self.PrintTreePreOrder(root.left)
        if (root.right):
            self.PrintTreePreOrder(root.right)
        print(root.key)
#!
if __name__ == "__main__":
    root = BSTNode(50)
    root.insert(30)
    root.insert(20)
    root.insert(40)
    root.insert(70)
    root.insert(60)
    root.insert(80)
    
    root.minValueNodeRecursive(root)

