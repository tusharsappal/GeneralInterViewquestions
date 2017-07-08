#!/usr/bin/python
'''
Inorder travesal traverses first the left child , then parent element and then the right subchild

Using the iteration it can be done as following
1. Create am empty Stack
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
'''


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class InOrderTraversalUsingIteration:
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
        stk = []
        current = node
        done = 0

        while not done:
            if current != None:
                stk.append(current)
                current = current.l

            elif len(stk) > 0 :
                current = stk.pop()
                print current.v
                current = current.r

            else:
                done = 1



if __name__=="__main__":
    tree = InOrderTraversalUsingIteration()
    tree.add(5)
    tree.add(4)
    tree.add(3)
    tree.add(2)
    tree.add(1)
    print "Printing Inorder Traversal \n"
    tree.printInOrderTree()