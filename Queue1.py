class Queue:
    def __init__(self):
        self.Queue = list()
    def addtoq(self, dataval):
        if dataval not in self.Queue:
            self.Queue.insert(0,dataval)
            return True
        return False
    def size(self):
        return len(self.Queue)
    def show(self):
        return self.Queue
    def pop(self):
        return self.Queue.pop(0)
    def add1(self, value):
        return self.Queue.insert(0, value)
TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
TheQueue.add1("Fri")
print(TheQueue.show())
TheQueue.pop()
print(TheQueue.size())