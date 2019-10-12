class person:
    
    def __init__(self):
        self.name = ""
        self.age = 0
        
    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def getInfo(self):
        print(self.name)
        print(self.age)


class stack:
    
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item);

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False
        # return self.stack == []

    def getSize(self):
        size = 0
        for i in self.stack:
            size += i

        return size
        # return len(self.stack)

class queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
