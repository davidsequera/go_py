# prompt: i forgot how oop works in python give me a code example of the basic and advance things i should know

# Basic OOP
class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

  def bark(self):
    print("Woof!")

my_dog = Dog("Fido", "Labrador")
print(my_dog.name)  # Output: Fido
my_dog.bark()  # Output: Woof!

# Advanced OOP (Inheritance, Polymorphism, Encapsulation)
class Animal:
  def __init__(self, name):
    self.__name = name  # Encapsulation: Private attribute

  def speak(self):
    print("Generic animal sound")

class Cat(Animal):
  def __init__(self, name):
    super().__init__(name)  # Inheritance

  def speak(self):  # Polymorphism: Overriding the speak method
    print("Meow!")

my_cat = Cat("Whiskers")
my_cat.speak()  # Output: Meow!
