## Python OOP — Complete Concepts with Simple Explanations

### 1. OOP Basics

#### Class
A **class** is a blueprint/template used to create objects.  
It defines variables (attributes) and functions (methods) that objects will have.

```python
class Car:
    pass
````
---

#### Object

An **object** is an instance of a class.
It is the real usable entity created from the class blueprint.

```python
c1 = Car()   # object of Car class
```
---

#### Attributes

**Attributes** are variables inside a class or object that store data.
They represent the state/data of an object.

```python
class Car:
    def __init__(self):
        self.color = "red"
```
---

#### Methods

**Methods** are functions defined inside a class.
They describe what an object can do (its behavior).

```python
class Car:
    def start(self):
        print("Car started")
```
---

#### self

`self` refers to the **current object instance**.
It is used to access instance variables and methods inside the class.

```python
class Car:
    def show(self):
        print(self)
```
---

#### **init** (Constructor)

`__init__` is a special method that runs automatically when an object is created.
It is used to initialize object data.

```python
class Car:
    def __init__(self, color):
        self.color = color
```
---

#### Instance Variable

An **instance variable** belongs to a specific object.
Each object can have different values.

```python
class Car:
    def __init__(self, color):
        self.color = color

c1 = Car("red")
c2 = Car("blue")
```
---

#### Class Variable

A **class variable** is shared by all objects of the class.
Changing it affects all instances.

```python
class Car:
    wheels = 4   # class variable

c1 = Car()
c2 = Car()
```
---
## 2. Encapsulation

#### What is Encapsulation?
Encapsulation means **bundling data (variables) and methods (functions) inside a class**  
and **controlling how that data is accessed or modified** from outside.

Purpose: Protect data and prevent direct unwanted changes.

---

#### Types of Access

#### 1. Public Variable
Accessible from anywhere (inside or outside class).

```python
class A:
    def __init__(self):
        self.name = "John"   # public

obj = A()
print(obj.name)   # accessible
````
---

#### 2. Protected Variable `_var`

Used internally within class or subclass.
Can be accessed outside, but treated as internal by convention.

```python
class A:
    def __init__(self):
        self._age = 25   # protected

obj = A()
print(obj._age)   # possible but not recommended
```
---

#### 3. Private Variable `__var`

Cannot be accessed directly outside class.
Python uses **name mangling** to protect it.

```python
class A:
    def __init__(self):
        self.__salary = 50000   # private

obj = A()
# print(obj.__salary)  ❌ error
```

Access internally only.

---

#### Getter and Setter

#### Getter → read value safely

Used to access private data.

```python
class A:
    def __init__(self):
        self.__x = 10

    def get_x(self):
        return self.__x
```
---

#### Setter → update value safely

Used to modify private data with control.

```python
class A:
    def __init__(self):
        self.__x = 10

    def set_x(self, value):
        self.__x = value
```
---

#### Property Decorator (Best Practice)

Allows method to be used like a variable.

```python
class A:
    def __init__(self):
        self._x = 10

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
```
Usage:

```python
obj = A()
print(obj.x)   # getter
obj.x = 50     # setter
```
---

#### Purpose of Encapsulation

* Protect sensitive data
* Control access
* Prevent direct modification
* Maintain clean structure
* Add validation logic

---

### 3. Abstraction

#### What is Abstraction?
Abstraction means **hiding internal implementation details**  
and showing only the **necessary functionality** to the user.

The user knows *what a class does*, but not *how it does it*.

Purpose: Reduce complexity and protect internal logic.

---

#### Real-Life Idea
When you drive a car:
- You use steering, brake, accelerator  
- You don’t know engine internals  

That is abstraction.

---

#### How to Implement in Python
Python provides abstraction using the **abc module** (Abstract Base Class).

Tools:
- `abc` module  
- `ABC` class  
- `@abstractmethod` decorator  
---

#### Abstract Class
A class that contains one or more abstract methods.  
Cannot create objects directly from abstract class.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
````
---

#### Abstract Method

Method declared but not implemented in base class.
Child class must implement it.

```python
class Dog(Animal):
    def sound(self):
        print("Bark")
```
Usage:

```python
d = Dog()
d.sound()
```
---

#### Why Use Abstraction?

* Hide complex logic
* Force child classes to implement required methods
* Provide common interface
* Improve code design
* Maintain security
---

#### Key Points

* Cannot create object of abstract class
* Must implement all abstract methods in child
* Used in frameworks (Django, DRF, etc.)

---

### 4. Inheritance (Clear Notes)

#### What is Inheritance?
Inheritance allows a **child class** to use properties and methods of a **parent class**.  
It helps reuse code and extend functionality without rewriting.

Purpose: Code reuse and better structure.

---

#### Basic Example
```python
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

d = Dog()
d.eat()   # inherited method
````
---

#### Types of Inheritance

#### 1. Single Inheritance

One child inherits from one parent.

```python
class A:
    pass

class B(A):
    pass
```
---

#### 2. Multiple Inheritance

Child inherits from multiple parents.

```python
class A: pass
class B: pass

class C(A, B):
    pass
```
---

#### 3. Multilevel Inheritance

Chain of inheritance (grandparent → parent → child).

```python
class A: pass
class B(A): pass
class C(B): pass
```
---

#### 4. Hierarchical Inheritance

Multiple children inherit from one parent.

```python
class A: pass

class B(A): pass
class C(A): pass
```
---

#### 5. Hybrid Inheritance

Combination of multiple types.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
```
---

#### Method Overriding

Child class provides its own version of a parent method.

```python
class A:
    def show(self):
        print("Parent")

class B(A):
    def show(self):
        print("Child")
```
---

#### super()

Used to call parent class method from child class.

```python
class A:
    def show(self):
        print("Parent")

class B(A):
    def show(self):
        super().show()
        print("Child")
```
---

#### MRO (Method Resolution Order)

MRO defines the **order in which Python looks for methods and attributes** in a class hierarchy.  
It becomes very important when using **multiple inheritance**, because Python must decide which parent class method to run first.

```python
class A: pass
class B(A): pass

print(B.mro())
````
Output order shows:
`B → A → object`
Python searches methods in this exact order.

---

#### Why Use Inheritance?

* Reuse existing code
* Avoid duplication
* Extend functionality
* Maintain clean structure
* Easy maintenance

---

## 5. Polymorphism
Same function → different behavior  

Types:
- Method overriding  
- Operator overloading  
- Duck typing  

Example:
`+` works for numbers and strings  

Purpose: Flexibility

---

## 6. Dunder (Magic) Methods
Special methods with `__`

Common:
- `__init__` → constructor  
- `__str__` → print friendly  
- `__repr__` → debug view  
- `__len__` → length  
- `__add__` → + operator  
- `__eq__` → ==  
- `__call__` → object callable  
- `__iter__`, `__next__` → iteration  

Purpose: Customize behavior

---

## 7. Method Types
- Instance method → uses self  
- Class method → uses cls  
- Static method → no self/cls  

Decorators:
- `@classmethod`
- `@staticmethod`

---

## 8. Attributes Handling
- `getattr()` → get attribute  
- `setattr()` → set attribute  
- `hasattr()` → check attribute  
- `delattr()` → delete attribute  
- `__dict__` → object data  

---

## 9. Composition vs Inheritance
- Inheritance → is-a relationship  
- Composition → has-a relationship  

Example:
Car has Engine → composition  

Preferred: Composition

---

## 10. Dataclasses
Auto-generate class methods  

Features:
- `@dataclass`  
- Auto `__init__`  
- Auto `__repr__`  
- Default values  
- Frozen class  

Purpose: Cleaner models

---

## 11. __slots__
- Saves memory  
- Prevents dynamic attributes  
- Faster access  

Used in large object systems

---

## 12. Metaclasses (Advanced)
Class that creates classes  

- `type` is default metaclass  
- Control class creation  
- Used in frameworks (Django, ORM)

---

## 13. MRO (Method Resolution Order)
Order Python searches for methods  
- Important in multiple inheritance  
- Check using:  
`Class.mro()`

---

## 14. Operator Overloading
Define behavior for operators  

Examples:
- `__add__`  
- `__lt__`  
- `__eq__`  

Used in custom objects

---

## 15. Object Lifecycle
- `__new__` → create object  
- `__init__` → initialize  
- `__del__` → destroy  

---

## 16. Callable Objects
Object behaves like function  

Use:
`__call__`

---

## 17. Iterators
Make class iterable  

Methods:
- `__iter__`  
- `__next__`  

---

## 18. Context Managers
Used with `with`  

Methods:
- `__enter__`  
- `__exit__`  

Purpose: resource handling

---

## 19. Design Patterns
- Singleton → one instance  
- Factory → object creator  
- Builder → step creation  
- Strategy → change behavior  
- Observer → event system  
- Decorator → extend behavior  

---

## 20. SOLID Principles
- Single Responsibility  
- Open/Closed  
- Liskov Substitution  
- Interface Segregation  
- Dependency Inversion  

Purpose: Clean architecture

---

## 21. Descriptors (Advanced)
Control attribute access  

Methods:
- `__get__`  
- `__set__`  
- `__delete__`  

Used in:
- Django models  
- Properties  

---

## 22. Copying Objects
- Shallow copy  
- Deep copy  
- `copy` module  

---

## 23. Serialization
Convert object → storable format  

Tools:
- JSON  
- Pickle  

---

## 24. Immutability
Objects that cannot change  

Examples:
- tuple  
- frozen dataclass  
