class ReverseList:
    def __init__(self, items):
        self.items = sorted(items, reverse=True)

    def add(self, item):
        self.items.append(item)
        self.items = sorted(self.items, reverse=True)

    def reverse(self):
       self.items = list(reversed(self.items))

    def __str__(self):
        return str(self.items)


# 测试代码
r1 = ReverseList([3, 1, 2])
print(r1)  # 应该输出 [3, 2, 1]

r1.add(4)
print(r1)  # 应该输出 [4, 3, 2, 1]

r1.reverse()
print(r1)  # 应该输出 [1, 2, 3, 4]

class UniqueList:
    def __init__(self, items):
        self.items = sorted(set(items))

    def add(self, item):
        if item not in self.items:
            self.items.append(item)
            self.items.sort()

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def __str__(self):
        return str(self.items)



# 测试代码
ul1 = UniqueList([3, 1, 2])
print(ul1)  # 应该输出 [1, 2, 3]

ul1.add(4)
print(ul1)  # 应该输出 [1, 2, 3, 4]

ul1.add(2)
print(ul1)  # 应该仍然输出 [1, 2, 3, 4]，因为 2 已经在列表中

ul1.remove(3)
print(ul1)  # 应该输出 [1, 2, 4]
