
class Car:
    wheels = 4
    steering = 1
    headlights = 2
    backlights = 2

    # Constructor
    def __init__(self, name: str, model: int, make: str, year: int):
        self.name = name
        self.model = model
        self.make = make
        self.year = year

    # Method without parameters
    def drive(self):
        print(f"{self.name} is driving")

    # Method with one attribute
    def engine_capacity(self, capacity):
        self.capacity = capacity

    # Method with multiple attributes
    def mileage(self, km: float, avg: float):
        mileage = km * avg
        return mileage


# Child class (inherits from Car)
class SportsCar(Car):
    def __init__(self, name: str, model: int, make: str, year: int, door: int, roof: bool, spoiler: bool):
        super().__init__( name, model, make, year)  # Inherit properties from Car
        self.door = door
        self.roof = roof
        self.spoiler = spoiler

    def info(self):
        return (
            f'{self.name} is a sports car designed by {self.make} in {self.year}, '
            f'with {self.door} doors, roof: {self.roof}, spoiler: {self.spoiler}'
        )


# Creating an object of SportsCar
ferrari = SportsCar("Ferrari", 488, "Ferrari", 2022, 2, True, True)


class family_car(Car):
    def __init__(self, name: str, model: int, make: str, year: int, door: int, roof: bool, spoiler: bool):
        super().__init__( name, model, make, year) 
        self.door = door
        self.roof = roof
        self.spoiler = spoiler

    def info(self):
        return (
            f'{self.name} is a family car designed by {self.make} in {self.year}, '
            f'with {self.door} doors, roof: {self.roof}, spoiler: {self.spoiler}'
        )

details = family_car("Ferrari", 488, "Ferrari", 2022, 2, True, True)

print(details.info())

# # Printing the car info
# print(ferrari.info())

# # Demonstrating method from parent class
# ferrari.drive()

# # Setting and checking engine capacity
# ferrari.engine_capacity("3.9L V8")
# print(f"Engine Capacity: {ferrari.capacity}")

# # Mileage calculation example
# print(f"Mileage: {ferrari.mileage(100, 12)} km")



# class myClass:
#     x = 5

# p1 = myClass()
# print(p1.x)


# class myClass: 
#     def __init__(self, name, subject, num):
#         self.name = name
#         self.subject = subject
#         self.num = num

# details = myClass("Cloud Engineering", "10", 20)

# print(details.name , details.subject)

# class Person :
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}({self.age})"
    
# p1 = Person("Umair", 20)

# print(p1.name, p1.age)


# class Person :
#     def __init__(self, name, age, height: int):
#         self.name = name
#         self.age = age
#         self.height = height

#     def myFunc(self):
#         print("Hello my name is " + self.name)

# p1 = Person("Umair", 21, 16)
# p1.name = "Hammad"
# del p1.height

# del p1

# print(p1.myFunc())

# class Person :
#     pass
        
        

# class Person :
#     def __init__(self, firstName, lastName):
#         self.firstName = firstName
#         self.lastName = lastName
    
#     def printName(self):
#         print(f'Hello my name is {self.firstName} {self.lastName}')

# p1 = Person("Umair", "Ahmed")

# p1.printName()


# class Student(Person):
#     def __init__(self, firstName, lastName, StudentID):
#         Person.__init__(self, firstName, lastName)
#         self.StudentID = StudentID
    
#     def displayID(self):
#         print(f'Hello my name is {self.firstName} {self.lastName} and my ID is {self.StudentID}')

# x = Student("Umair", "Ahmed", 1234)

# x.displayID()
        


# class Car :
#     def __init__(self, name, model, maker):
#         self.name = name
#         self.model = model
#         self.maker = maker

#     def showDetails(self):
#         print(f'Hey, these are the details of the car {self.name} {self.model} {self.maker}')
        

# p1 = Car("Honda", "2010","Honda wale")

# print(p1.showDetails())


# class Child(Car):
#     def __init__(self, name, model, maker, wheels: bool, steering: bool, isActive: bool):
#         Car.__init__(self, name, model, maker)
#         self.wheels = wheels
#         self.steering = steering
#         self.isActive = isActive
    
#     def childDetails(self):
#         print(f'Hey everyOne looks here {self.name} {self.model} {self.wheels} {self.steering} {self.isActive}')

# p2 = Child("Honda", "2013","Honda walle ", True, True, False)

# print(p2.childDetails())


# myTuple = ["Banana","Orange","Apple"]

# myItr = iter(myTuple)

# print(next(myItr))
# print(next(myItr))
# print(next(myItr))


# class Bags :
#     def __init__(self, name, price, color):
#         self.name = name
#         self.price = price
#         self.color = color

#     def bagDetails(self):
#         print(f'Hey, these are the details of the bag {self.name} {self.price} {self.color}')
        

# p1 = Bags("Bag1", "1000", "Blue")

# print(p1.bagDetails())

# class Child(Bags):
#     def __init__(self, name, price, color, isSold: bool):
#         Bags.__init__(self, name, price, color)
#         self.isSold = isSold

#     def childDetails(self):
#         print(f'Hey everyOne looks here {self.name} {self.price} {self.color} {self.isSold}')

# p2 = Child("Bag2", "2000","Red", True)

# print(p2.childDetails())

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius

# rectangle = Rectangle(5, 3)
# circle = Circle(2)

# print(rectangle.area())
# print(circle.area())

def sum():
    name = "Umair"

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # This method overrides Animal's speak()
        print("Dog barks")

# Usage
animal = Animal()
animal.speak()  # Output: Animal speaks

dog = Dog()
dog.speak()     # Output: Dog barks


name = "Umair"

name = "faiz"


def Person():
    console.log("Hlelo")
    

