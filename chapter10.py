# object oriented programming 
# we have already leaned this concept in c++


# classes and objects
"""
Object-oriented programming (OOP) is a programming paradigm that uses "objects" to represent data and methods to manipulate that data.
It is based on several key concepts including classes, objects, inheritance, encapsulation, and polymorphism.
"""
# Defining a class
class Dog:
    # Constructor
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    # Method
    def bark(self):
        print(f"{self.name} says Woof!")
# Creating an object (instance) of the class
my_dog = Dog("Buddy", 3)
# Accessing attributes and methods
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")
my_dog.bark()





# INHERITANCE
"""
Inheritance is a mechanism in OOP that allows a new class (derived class) to inherit attributes and methods from an existing class (base class).
This promotes code reusability and establishes a hierarchical relationship between classes.
"""
# Base class
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")
# Derived class
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__("Cat")  # Call the constructor of the base class
        self.name = name
        self.age = age

    def make_sound(self):  # Overriding method
        print(f"{self.name} says Meow!")
# Creating an object of the derived class
my_cat = Cat("Whiskers", 2)
print(f"My cat's name is {my_cat.name}, she is a {my_cat.species} and is {my_cat.age} years old.")
my_cat.make_sound()








# ENCAPSULATION
""" 
Encapsulation is the concept of restricting access to certain components of an object and bundling the data (attributes) and methods (functions) that operate on the data into a single unit or class.
This is typically done by making attributes private and providing public methods to access and modify them.
"""
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance                  # Private attribute

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    # Public method to get the current balance
    def get_balance(self):
        return self.__balance
# Creating a bank account object
my_account = BankAccount("123456789")
my_account.deposit(500)
my_account.withdraw(200)
print("Current balance:", my_account.get_balance())






# POLYMORPHISM
"""
Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface.
It allows methods to do different things based on the object it is acting upon, even if they share the same name.
"""
class Bird:
    def make_sound(self):
        print("Chirp Chirp")
class Cow:
    def make_sound(self):
        print("Moo Moo")
def animal_sound(animal):
    animal.make_sound()
# Creating objects
sparrow = Bird()
bessie = Cow()
# Using polymorphism
animal_sound(sparrow)  # Output: Chirp Chirp
animal_sound(bessie)   # Output: Moo Moo

#