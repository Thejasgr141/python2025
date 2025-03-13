class Person:
 def __init__(self, name, age):
  self.name = name
  self.age = age
 def greet(self):
  print(f"Hiiii, my name is {self.name} and I am {self.age} years old.")
person1 = Person("Thejas", 18)
person1.greet()
