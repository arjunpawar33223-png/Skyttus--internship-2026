class Person:
    def __init__(self, name):
        self.__name = name   # private

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

p = Person("Arjun")
print(p.get_name())
p.set_name("Rahul")
print(p.get_name())