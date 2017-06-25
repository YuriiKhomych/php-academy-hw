class ListIterator(object):

    def __init__(self, items):
        self.items = items
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.item = self.items[self.count]
            self.count += 1
            return self.item
        except IndexError:
            raise StopIteration


class FileIterator(object):

    def __init__(self, filename):
        self.my_file = open(filename, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.my_file.readline()
        if line != '':
            line = line.rstrip('\n')
            return line.upper()
        raise StopIteration

# CAN`T
class DictIterator(object):

        def __init__(self, values):
            self._values = values
            self.count = 0

        def __getitem__(self, name):
            return self._values[name]

        def __iter__(self):
            return self

        def keys(self):
            return self._values.keys()

        def values(self):
            return self._values.values()

        def items(self):
            return self._values.items()

        def __next__(self):
            for attr, value in self._values:
                return attr, value

#file_data = ListIterator(["first", "second", "third"])
file_data = DictIterator({"first key": "first value",
                          "second key":"second value",
                          "third key": "third value"})
# file_data = FileIterator("test.txt")

#print(file_data.items())
# print(file_data.__next__())

def my_generation(start):
    for item in range(0, start):
        if item % 3 == 0:
            yield item
my_gener = my_generation(100)

# for g in my_gener:
#     print(g)

gen = [ran for ran in range(100) if ran % 3 == 0]
# print(gen)
