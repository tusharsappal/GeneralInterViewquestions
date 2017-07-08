#!/usr/bin/python

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
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

    def printInOrderTree(self):
        if(self.root != None):
            self._printInOrderTree(self.root)

    def _printInOrderTree(self, node):
        if(node != None):
            self._printInOrderTree(node.l)
            print str(node.v) + ' '
            self._printInOrderTree(node.r)

    def printPreOrderTraversal(self):
        if self.root != None:
            self._printPreOrderTraversal(self.root)

    def _printPreOrderTraversal(self, node):
        if node != None:
            print str(node.v) + ' '
            self._printPreOrderTraversal(node.l)
            self._printPreOrderTraversal(node.r)

    def printPostOrderTraversal(self):
        if self.root != None:
            self._printPreOrderTraversal(self.root)

    def _printPostOrderTraversal(self, node):
        if node != None:
            self._printPostOrderTraversal(node.l)
            self._printPostOrderTraversal(node.r)
            print str(node.v) + ' '



if __name__=="__main__":
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    print "Printing Inorder Traversal \n"
    tree.printInOrderTree()
    print "Printing PreOrder Traversal \n"
    tree.printPreOrderTraversal()
    print "Printing the PostOrder Traversal \n"
    tree.printPostOrderTraversal()
    # print "Printing PostOrder Traversal \n"
    # tree.printPostOrderTraversal()

# print (tree.find(3)).v
# print tree.find(10)
# tree.deleteTree()
# tree.printInOrderTree()