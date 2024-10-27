class Node:
    def __init__(self, v):
        self.height: int = 1
        self.value = v
        self.left: Node = None
        self.right: Node = None

class Tree:
    def __init__(self):
        self.root: Node = None

    def insert(self, v):
        self.root = self._insert(self.root, v)

    def getHeight(self, r: Node):
        if r is None:
            return 0
        else:
            return r.height

    def getBalance(self, n: Node):
        if not n:
            return 0
        return self.getHeight(n.left) - self.getHeight(n.right)

    def leftRotate(self, z: Node):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = max(self.getHeight(z.left), self.getHeight(z.right)) + 1
        y.height = max(self.getHeight(y.left), self.getHeight(y.right)) + 1
        return y

    def rightRotate(self, z: Node):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = max(self.getHeight(z.left), self.getHeight(z.right)) + 1
        y.height = max(self.getHeight(y.left), self.getHeight(y.right)) + 1
        return y

    def _insert(self, r: Node, v):
        if r is None:
            return Node(v)
        if v < r.value:
            r.left = self._insert(r.left, v)
        else:
            r.right = self._insert(r.right, v)

        r.height = max(self.getHeight(r.left), self.getHeight(r.right)) + 1

        balance = self.getBalance(r)

        if balance > 1 and v < r.left.value:
            return self.rightRotate(r)
        if balance < -1 and v > r.right.value:
            return self.leftRotate(r)
        if balance > 1 and v > r.left.value:
            r.left = self.leftRotate(r.left)
            return self.rightRotate(r)
        if balance < -1 and v < r.right.value:
            r.right = self.rightRotate(r.right)
            return self.leftRotate(r)
        
        return r


t = Tree()
t.insert(10)
t.insert(5)
t.insert(1)
t.insert(2)
print(t.root.value)
