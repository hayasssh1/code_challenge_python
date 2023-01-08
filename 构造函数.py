
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __sub__(self, person):
        return Person('undefined name', self.age - person.age)

    def __add__(self,person):
        return Person('undefined name', self.age + person.age)

lin = Person('linqiqi', 25)
liu = Person('liuyingyue', 30)
wang = Person('wanglong', 30)

print(abs((lin-liu).age))
print(abs((lin+wang).age))
