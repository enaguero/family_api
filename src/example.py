class Person:
  # Constructor
  def __init__(self, n, a):
    # Attributes
    self.name = n
    self.age = a

  def increase_age(self): 
    self.age = self.age + 1

p1 = Person("Erwin", 34)
p2 = Person("Andres", 35)
print(p1.name)
print(p2.name)

