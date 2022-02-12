# Linked list(Node version)

class NLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class NLL:
    def __init__(self):
        self.first = None

    def InsertFront(self, newData):
        newNode = NLLNode(newData)
        newNode.next = self.first
        self.first = newNode

    def InsertBack(self, newData):
        newNode = NLLNode(newData)
        if self.first is None:
            self.first = newNode
        else:
            prevNode = self.first
            while prevNode.next is not None:
                prevNode = prevNode.next
            prevNode.next = newNode

    def InsertInOrder(self, newData):
        newNode = NLLNode(newData)
        if self.first is None:
            self.first = newNode
        elif newData < self.first.data:
            newNode.next = self.first
            self.first = newNode
        else:
            prevNode = None
            currNode = self.first
            while currNode is not None and newData > currNode.data:
                prevNode = currNode
                currNode = currNode.next

            prevNode.next = newNode
            newNode.next = currNode  # covers both middle and end cases

    def InOrderTraversal(self):
        if self.first is None:
            return
        self.InOrder(self.first)

    def InOrder(self, curr):
        if curr is not None:
            print(curr.data)
            self.InOrder(curr.next)
