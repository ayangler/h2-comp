"""
Q3
"""


# -------------------------------------------------------------------------
class Node:
    def __init__(self, Left=0):
        self.LeftP = Left
        self.Data = ""
        self.RightP = 0


# -------------------------------------------------------------------------
class Tree:
    def __init__(self):

        self.ThisTree = [None] * 21  # array[0..20] of tree nodes

        # set up an empty tree 	
        self.Root = 0
        self.NextFreePosition = 1

        for i in range(1, 19 + 1):
            self.ThisTree[i] = Node(i + 1)

        self.ThisTree[20] = Node(0)  # last node with left pointer 0

    def OutputData(self):
        print('Root:', self.Root)
        print('NextFreePosition:', self.NextFreePosition)
        print()
        print('Index'.ljust(8), 'LeftP'.ljust(8), 'Data'.ljust(12), 'RightP')
        print('=' * 36)
        for i in range(1, 20 + 1):
            print(str(i).ljust(8), str(self.ThisTree[i].LeftP).ljust(8), self.ThisTree[i].Data.ljust(12),
                  str(self.ThisTree[i].RightP))

    def AddItemToBinaryTree(self, NewTreeItem):
        if self.NextFreePosition == 0:
            print('No space available!')
        else:
            # get next free node
            NewNodePosition = self.NextFreePosition
            self.NextFreePosition = self.ThisTree[self.NextFreePosition].LeftP

            self.ThisTree[NewNodePosition].LeftP = 0
            self.ThisTree[NewNodePosition].RightP = 0
            self.ThisTree[NewNodePosition].Data = NewTreeItem

            # perform insertion
            LastMove = ''  # direction of the previous traversal move
            if self.Root == 0:
                self.Root = NewNodePosition
            else:
                CurPosition = self.Root  # start from the root

                while CurPosition != 0:
                    PrevPosition = CurPosition
                    if NewTreeItem < self.ThisTree[CurPosition].Data:  # move left
                        LastMove = 'L'
                        CurPosition = self.ThisTree[CurPosition].LeftP
                    else:  # move right
                        LastMove = 'R'
                        CurPosition = self.ThisTree[CurPosition].RightP

                if LastMove == 'R':
                    self.ThisTree[PrevPosition].RightP = NewNodePosition
                elif LastMove == 'L':
                    self.ThisTree[PrevPosition].LeftP = NewNodePosition

    def InOrder(self):
        self.InOrderTraversal(self.Root)

    def InOrderTraversal(self, index):
        if index != 0:
            self.InOrderTraversal(self.ThisTree[index].LeftP)
            print(self.ThisTree[index].Data, end=' ')
            self.InOrderTraversal(self.ThisTree[index].RightP)

    def getRoot(self):
        return self.Root


def main():
    tree = Tree()  # create a tree object

    # input data  
    print()
    inp = input("Enter data item (XXX to end): ")
    while inp != 'XXX':
        tree.AddItemToBinaryTree(inp)
        inp = input("Enter data item (XXX to end): ")

    #  print tree structure
    print()
    print('Non-EmptyTree:\n==============')
    tree.OutputData()

    # Inorder traversal
    # print ( '\nIN-ORDER TRAVERSAL\n==================' )
    # tree.InOrder()

    #  or

    print('\nIN-ORDER TRAVERSAL\n==================')
    root = tree.getRoot()
    tree.InOrderTraversal(root)


main()
