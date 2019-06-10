# -*- coding: utf-8 -*-

class animal:

    def __init__(self, name):
        self.name = name
        print(name)

    def test(self):
        print('test', self.name)

class cat(animal):

    def __init__(self, name):
        super(cat, self).__init__(name)
        print('cat', name)

    def test2(self):
        print('test2', self.name)

if __name__=='__main__':
    a: animal = cat('rrrrr')
    a.test()
    a.test2()