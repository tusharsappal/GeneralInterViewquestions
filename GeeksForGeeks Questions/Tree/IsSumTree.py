#!/usr/bin/python

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class SumTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l != None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r != None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root != None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printPostOrderTraversal(self):
        if self.root != None:
            self._printPostOrderTraversal(self.root)

    def _printPostOrderTraversal(self, node):
        if node != None:
            self._printPostOrderTraversal(node.l)
            self._printPostOrderTraversal(node.r)
            print str(node.v) + ' '

    def isSumTree(self):
        if self.root != None:
            self._isSumTree(self.root)

    def _sum(self,node):
        if node is None:
            return 0
        else:
            return self._sum(node.l) + node.v + self._sum(node.r)

    def _isSumTree(self, node):

        if node is None or ( node.l is None and node.r is None):
            # This is done to check if the node is null or if it is leaf node
            return 1
        else:
            ls = self._sum(node.l)
            rs = self._sum(node.r)

            if node.v == (ls+rs) and self._isSumTree(node.l)!= None and self._isSumTree(node.r) != None:
                return 1

        return 0



if __name__=="__main__":
    tree = SumTree()
    tree.add(26)
    tree.add(10)
    tree.add(3)
    tree.add(4)
    tree.add(6)
    tree.add(3)
    # print "Printing the PostOrder Traversal \n"
    # tree.printPostOrderTraversal()

    isSumTree = tree.isSumTree()
    if isSumTree != 1:
        print "Not a SumTree"
    else:
        print "A Sum Tree"

    # print "Printing PostOrder Traversal \n"
    # tree.printPostOrderTraversal()

# print (tree.find(3)).v
# print tree.find(10)
# tree.deleteTree()
# tree.printInOrderTree()