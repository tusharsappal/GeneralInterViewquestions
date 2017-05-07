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

    def printInOrderTraversal(self):
        if self.root != None:
            self._printInOrderTraversal(self.root)

    def _printInOrderTraversal(self, node):
        if node != None:
            self._printInOrderTraversal(node.l)
            print str(node.v) + ' '
            self._printInOrderTraversal(node.r)


    def mirrorTree(self):
        if self.root != None:
            self._mirror(self.root)
        else:
            return

    def _mirror(self, node):
        if node is None:
            return 0
        elif node.l is None and node.r is None:
            return 0
        else:
            self._mirror(node.l)
            self._mirror(node.r)
            temp = node.l
            node.l = node.r
            node.r = temp
            # Now calling the the individual tree components / left and right

if __name__=="__main__":
    tree = SumTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    print "Printing the InOrder Traversal Before Mirroring \n"
    tree.printInOrderTraversal()
    print "Printing the InOrder Traversal After Mirroring\n"
    tree.mirrorTree()
    tree.printInOrderTraversal()
