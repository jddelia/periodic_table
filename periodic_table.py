''' This program prints a version of the Periodic
    Table of Elements. '''

import sys

class Element:
    def __init__(self, name, symbol, number, weight):
        self.name = name
        self.symbol = symbol
        self.number = number
        self.weight = weight

    def __repr__(self):
        return 'Element(%s, %s, %d, %d)' %(self.name, self.symbol,
                                           self.number, self.weight)

    def __str__(self):
        return ('Element: %s\nSymbol: %s\n' +
        'Atomic Number: %d\nAtomic Weight: %d') %(self.name, self.symbol,
                                                  self.number, self.weight)

class AllElements:
    def __init__(self):
        self.collect_elements()

    def collect_elements(self):
        self.elements = [0]
        fin = open('elements.txt')
        lines = [i.split() for i in fin.readlines()]
        lines.sort(key=lambda x: int(x[2]))
        for i in lines:
            name = i[1].lower()
            name = Element(i[1], i[0], int(i[2]), int(i[2])*2)
            self.elements.append(name)

    def __repr__(self):
        return 'Table contains %d elements' %(len(self.elements[1:]))

class PTable:
    def __init__(self, name):
        self.name = name

elements_1 = AllElements()

print(elements_1.elements[int(sys.argv[1])])
