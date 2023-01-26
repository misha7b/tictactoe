class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        
    def addChild(self, data):
        self.children.append(data)
    
    def traverse(self):
        nodesToVisit = self
        while len(nodesToVisit) > 0:
            currentNode = nodesToVisit.pop()
            print(currentNode.data)
            nodesToVisit += currentNode.children







 