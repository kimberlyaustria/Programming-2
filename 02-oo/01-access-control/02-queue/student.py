class Queue:
    def __init__(self):
        self.__queue = []

    def add(self, item):
        self.__queue.append(item)
    
    def next(self): 
        ''' (fout)
        while len(self.list) > 1:
            self.list.pop(0)
            return self.list[0]
        '''
        item = self.__queue[0]
        del self.__queue[0]
        return item

    def is_empty(self):
        if len(self.__queue) == 0:
            return True
        