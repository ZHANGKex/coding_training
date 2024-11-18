class Student(object):
    __slot__ = ('name', 'score')

s = Student()
s.name = 'Michel'
s.age = 3