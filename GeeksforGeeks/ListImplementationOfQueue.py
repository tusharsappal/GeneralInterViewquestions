# This script is a list implementation of Queue

class Queue(object):

    queue = []

    _DEFAULT_SIZE= 10

    def __init__(self):
        self._data = [None]*Queue._DEFAULT_SIZE
        self._size = 0
        self._front = 0
        self._end = 0

    def __len__(self):
        return len(self.queue)

    def isEmpty(self):
        return self._size == 0

    def first(self):
        if self.isEmpty():
            print "The Queue is Empty , No Front determined"
            return -1
        else:
            return self._data[self._front]

    def enqueue(self,element):

        if self._end == self._front and self._size > 0:
            print "Queue is Full , Cannot put more elements"
            return -1
        else:

            self._data[self._end] = element
            self._end = (self._end + 1) % Queue._DEFAULT_SIZE
            self._size = self._size +1


    def dequeue(self):
        # Removing the first element and increamenting the front

        if self.isEmpty():
            print "The Queue is Empty , cannot dequeu"
            return -1
        else:
            temp = self.first()
            self._data[self._front] = None # To make the element is collected via garbage
            self._front = (self._front+1) % (len(self._data))
            self._size = self._size -1
            return temp

    def printQueue(self):

        for element in self._data:
            if element is not None:
                print element

    def start(self):
        self.enqueue(1)
        self.enqueue(2)
        self.enqueue(3)
        self.enqueue(4)
        self.enqueue(5)
        self.enqueue(6)
        self.enqueue(7)
        self.enqueue(8)
        self.enqueue(9)
        self.enqueue(10)
        # We will try to insert one more element
        # it should fail
        self.enqueue(11)
        # Now we will try to print the element
        self.printQueue()
        print "-------------------"

        # Now we will be dequeing
        self.dequeue()
        self.dequeue()

        self.printQueue()

        print "-------------------"

        # Now we will be trying to insert two element , and it sould insert well
        self.enqueue(11)
        self.enqueue(12)

        self.printQueue()

        # Now if we will try to insert , it should throw errror

        self.enqueue(13)

if __name__=="__main__":
    Queue().start()