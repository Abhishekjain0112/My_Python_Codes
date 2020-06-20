class Array():

    def __init__(self):
        self.length = 0
        self.data = []

    def get(self, index):
        return self.data[index]

    def insertEnd(self, value):
        self.data.append(value)
        self.length += 1
        return self.data

    def insertatindex(self, index, value):

        if self.length == 0:
            self.data.append(value)
            self.length += 1
            return self.data
        else:
            self.data = self.data[:index] + [value] + self.data[index + 1:]
            self.length += 1
            return self.data

    def traverse(self):
        for i in self.data:
            print(i, end=",")


a = Array()
a.insertEnd(1)
a.insertEnd(2)
a.insertEnd(4)
a.insertEnd(3)
a.traverse()
print("\n data ")
print(a.get(1))
print(a.get(1))
print(a.get(2))
a.get(1)
a.get(2)
a.insertatindex(1, 9)
a.insertatindex(10, 9)

a.traverse()
