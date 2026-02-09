class Animal:          # Base class
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):     # Derived class
    def speak(self):   # Overriding method
        print("Dog barks")

# Object creation
a = Animal()
d = Dog()

a.speak()
d.speak()