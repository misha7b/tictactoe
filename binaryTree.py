class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, data):
        if (data < self.data):
            self.leftChild

    def printNode(self):
        print(self.data)

root = Node(30)
root.printNode()