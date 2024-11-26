class SortedList:
    def __init__(self, items=None):
        self.items = sorted(items)

    def add(self, item):
        self.items.append(item)
        self.items = sorted(self.items)

    def concat(self, items2):
        self.items = self.items + items2
        self.items = sorted(self.items)