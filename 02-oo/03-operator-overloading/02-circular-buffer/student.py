class CircularBuffer:
    def __init__(self, n):
        self.__maximum = n
        self.__items = []
    
    def add(self, item):
        self.__items.append(item) # moet van voor, want anders wordt er niets toegevoegd nadat de condition runt
        if len(self.__items) > self.__maximum:
            # self.__items.pop(0) werkt niet
            del self.__items[0]

    def __getitem__(self, index):
        return self.__items[index]

    def __len__(self):
        return len(self.__items)
    