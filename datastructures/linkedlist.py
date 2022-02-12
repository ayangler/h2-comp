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


# LinkedList (array version)

class ALLNode:
    def __init__(self):
        self.data = ""
        self.next = 0


class ALL:
    def __init__(self):
        self.first = 0
        self.nextfree = 1
        self.ALL = [None] + [ALLNode() for i in range(5)]

        for i in range(1, len(self.ALL)):
            self.ALL[i].next = i + 1

    def InsertInOrder(self, new):
        if self.nextfree == 0:
            return

        newIndex = self.nextfree
        self.nextfree = self.ALL[self.nextfree].next
        self.ALL[newIndex].data = new

        if self.first == 0:  # empty
            self.first = newIndex
            self.ALL[newIndex].next = 0
        elif new < self.ALL[self.first].data:
            self.ALL[newIndex].next = self.first
            self.first = newIndex
        else:
            prevIndex = 0
            currIndex = self.first
            while currIndex != 0 and new > self.ALL[currIndex].data:
                prevIndex = currIndex
                currIndex = self.ALL[currIndex].next

            self.ALL[prevIndex].next = newIndex
            self.ALL[newIndex].next = currIndex

    def InOrderTraversal(self):
        if self.first == 0:
            return
        self.InOrder(self.first)

    def InOrder(self, currIndex):
        if currIndex != 0:
            print(self.ALL[currIndex].data)
            self.InOrder(self.ALL[currIndex].next)
