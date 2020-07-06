class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def insert(self, data):
        if self.key:
            if data < self.key:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.key:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.key = data

    def search(self, data):
        if self.key is None or self.key == data:
            return self.key
        if data < self.key: return self.left.search(data)
        else: return self.right.search(data)
    
    def minValueNode(self):
        cur = self
        while (cur.left is not None):
            cur = cur.left
        return cur.key

    def maxValueNode(self):
        cur = self
        while (cur.right is not None):
            cur = cur.right
        return cur.key

    def PrintTreeInOrder(self):
        if self.left:
            self.left.PrintTree()
        print(self.key)
        if self.right:
            self.right.PrintTree()

if __name__ == "__main__":
    root = Node(50)
    root.insert(30)
    root.insert(20)
    root.insert(40)
    root.insert(70)
    root.insert(60)
    root.insert(80)
    
    print(root.maxValueNode())
    #root.PrintTreeInOrder()