# 🌳 AVL Tree Implementation in Python 🌳
# 🚀 Quick Start
No fancy installation steps here. Just make sure you have Python installed, and you're good to go!
# 📂 Structure
## Node Class
Represents a node in the tree. Each node keeps track of its value, height, and pointers to its left and right children.
```python

class Node:
    def __init__(self, v):
        self.height: int = 1
        self.value = v
        self.left: Node = None
        self.right: Node = None
```
## Tree Class
Handles the insertion and balancing of nodes to maintain that sweet AVL balance.

```python
class Tree:
    def __init__(self):
        self.root: Node = None

    def insert(self, v):
        self.root = self._insert(self.root, v)

    def getHeight(self, r: Node):
        return 0 if r is None else r.height

    def getBalance(self, n: Node):
        return 0 if not n else self.getHeight(n.left) - self.getHeight(n.right)

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
            return self
```
# Example Usage 
``` python
t = Tree()
t.insert(10)
t.insert(5)
t.insert(1)
t.insert(2)
print(t.root.value)  # Should show the root value after balancing
```
## 🔍 How It Works
- Insertion: Adds nodes to the tree while ensuring balance.
- Rotations: Balances the tree using left, right, left-right, and right-left rotations.
