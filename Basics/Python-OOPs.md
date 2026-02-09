## Python OOP — Complete Concepts with Simple Explanations

### 1. OOP Basics

#### Class
A **class** is a blueprint/template used to create objects.  
It defines variables (attributes) and functions (methods) that objects will have.

```python
class Car:
    pass
````

#### Object

An **object** is an instance of a class.
It is the real usable entity created from the class blueprint.

```python
c1 = Car()   # object of Car class
```

#### Attributes

**Attributes** are variables inside a class or object that store data.
They represent the state/data of an object.

```python
class Car:
    def __init__(self):
        self.color = "red"
```

#### Methods

**Methods** are functions defined inside a class.
They describe what an object can do (its behavior).

```python
class Car:
    def start(self):
        print("Car started")
```

#### self

`self` refers to the **current object instance**.
It is used to access instance variables and methods inside the class.

```python
class Car:
    def show(self):
        print(self)
```

#### **init** (Constructor)

`__init__` is a special method that runs automatically when an object is created.
It is used to initialize object data.

```python
class Car:
    def __init__(self, color):
        self.color = color
```

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

### 2. Encapsulation

#### What is Encapsulation?
Encapsulation means **bundling data (variables) and methods (functions) inside a class**  
and **controlling how that data is accessed or modified** from outside.

Purpose: Protect data and prevent direct unwanted changes.

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

#### Setter → update value safely

Used to modify private data with control.

```python
class A:
    def __init__(self):
        self.__x = 10

    def set_x(self, value):
        self.__x = value
```

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

#### Real-Life Idea
When you drive a car:
- You use steering, brake, accelerator  
- You don’t know engine internals  

That is abstraction.

#### How to Implement in Python
Python provides abstraction using the **abc module** (Abstract Base Class).

Tools:
- `abc` module  
- `ABC` class  
- `@abstractmethod` decorator  

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

#### Why Use Abstraction?

* Hide complex logic
* Force child classes to implement required methods
* Provide common interface
* Improve code design
* Maintain security

#### Key Points

* Cannot create object of abstract class
* Must implement all abstract methods in child
* Used in frameworks (Django, DRF, etc.)

---

### 4. Inheritance

#### What is Inheritance?
Inheritance allows a **child class** to use properties and methods of a **parent class**.  
It helps reuse code and extend functionality without rewriting.

Purpose: Code reuse and better structure.

#### Basic Example
```python
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

d = Dog()
d.eat()   # inherited method
```

#### Types of Inheritance

#### 1. Single Inheritance

One child inherits from one parent.

```python
class A:
    pass

class B(A):
    pass
```

#### 2. Multiple Inheritance

Child inherits from multiple parents.

```python
class A: pass
class B: pass

class C(A, B):
    pass
```

#### 3. Multilevel Inheritance

Chain of inheritance (grandparent → parent → child).

```python
class A: pass
class B(A): pass
class C(B): pass
```

#### 4. Hierarchical Inheritance

Multiple children inherit from one parent.

```python
class A: pass

class B(A): pass
class C(A): pass
```

#### 5. Hybrid Inheritance

Combination of multiple types.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
```

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

#### Why Use Inheritance?

* Reuse existing code
* Avoid duplication
* Extend functionality
* Maintain clean structure
* Easy maintenance

---

### 5. Polymorphism

#### What is Polymorphism?
Polymorphism means **same method or operator behaves differently** depending on the object.  
In simple terms: one interface → many forms.

Purpose: Flexibility and reusable code.

##### Example Idea
The `+` operator:
- Adds numbers  
- Joins strings  

```python
print(2 + 3)        # 5
print("a" + "b")    # ab
````
Same operator, different behavior → polymorphism.

#### Types of Polymorphism

##### 1. Method Overriding

Child class changes parent class method behavior.

```python
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")
```

##### 2. Operator Overloading

Custom behavior for operators using dunder methods.

```python
class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x
```

##### 3. Duck Typing

If an object behaves like required, Python accepts it.
Type doesn't matter, behavior matters.

```python
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def make_sound(animal):
    animal.speak()
```

#### Why Use Polymorphism?

* Write flexible code
* Reuse same method names
* Support different object types
* Cleaner design

---

### 6. Dunder (Magic) Methods

#### What are Dunder Methods?
Dunder (double underscore) methods are **special built-in methods** in Python  
that let you **customize how objects behave** with operators and built-in functions.

They start and end with `__`.

Purpose: Make custom objects behave like built-in Python objects.

#### Common Dunder Methods

### `__init__`
Constructor called when object is created.  
Used to initialize object data.

```python
class A:
    def __init__(self, x):
        self.x = x
````

##### `__str__`

Controls what prints when using `print(object)`.
Gives user-friendly output.

```python
class A:
    def __str__(self):
        return "Hello"
```

##### `__repr__`

Used for debugging and developer view.
Shows detailed representation of object.

```python
class A:
    def __repr__(self):
        return "A()"
```

##### `__len__`

Defines behavior of `len(object)`.

```python
class A:
    def __len__(self):
        return 5
```

##### `__add__`

Defines behavior of `+` operator for objects.

```python
class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x
```

##### `__eq__`

Defines behavior of `==` comparison.

```python
def __eq__(self, other):
    return self.x == other.x
```

##### `__call__`

Makes object behave like a function.

```python
class A:
    def __call__(self):
        print("Called")

a = A()
a()   # works like function
```

##### `__iter__` and `__next__`

Used to make object iterable (loopable).

```python
def __iter__(self):
    return self

def __next__(self):
    return 1
```

#### Why Use Dunder Methods?

* Customize operators
* Make objects iterable
* Improve printing
* Support built-in functions
* Make classes behave like native types

---

### 7. Method Types

#### 1. Instance Method
An instance method works with **object data** and uses `self`.  
It can access and modify instance variables.

```python
class A:
    def show(self):
        print("Instance method")

obj = A()
obj.show()
````

#### 2. Class Method

A class method works with the **class itself**, not a specific object.
It uses `cls` and can access class variables.

Decorator: `@classmethod`

```python
class A:
    count = 0

    @classmethod
    def show_count(cls):
        print(cls.count)
```

Call:

```python
A.show_count()
```

#### 3. Static Method

A static method is a **utility function** inside a class.
It does not use `self` or `cls`.

Decorator: `@staticmethod`

```python
class A:
    @staticmethod
    def add(a, b):
        return a + b
```

Call:

```python
A.add(2, 3)
```
---

### 8. Attributes Handling
- `getattr()` → get attribute  
- `setattr()` → set attribute  
- `hasattr()` → check attribute  
- `delattr()` → delete attribute  
- `__dict__` → object data  

---

### 9. Composition vs Inheritance

#### Inheritance (is-a relationship)
Inheritance means a child class **is a type of** parent class.  
Used when classes share common behavior and structure.

```python
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):   # Dog is an Animal
    pass
````

#### Composition (has-a relationship)

Composition means a class **contains another class object** inside it.
Used when one object needs another to function.

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()   # Car has an Engine
```

#### Key Difference

* Inheritance → **is-a** relationship
* Composition → **has-a** relationship

#### Why Composition is Preferred

* More flexible
* Less tightly coupled
* Easier to modify
* Avoids deep inheritance chains
* Better for large projects

---

### 10. Dataclasses (Clear Notes)

#### What is a Dataclass?
A dataclass is a special class used mainly to store data.  
It automatically creates common methods like `__init__`, `__repr__`, and comparisons.

Purpose: Write cleaner and shorter model classes.

#### Basic Example
```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
````

Python automatically creates:

* `__init__`
* `__repr__`
* `__eq__`

Usage:

```python
u = User("Ram", 25)
print(u)
```

#### Default Values

You can set default values easily.

```python
@dataclass
class User:
    name: str
    age: int = 18
```

#### Frozen Dataclass (Immutable)

Prevents modification after creation.

```python
@dataclass(frozen=True)
class User:
    name: str
    age: int
```

Now values cannot be changed.

#### Why Use Dataclasses?

* Less boilerplate code
* Cleaner models
* Auto methods
* Easy comparison
* Good for APIs, Django-like models, configs

---

### 11. `__slots__`

####  What is `__slots__`?
`__slots__` is used to **limit the attributes** an object can have.  
It saves memory and makes attribute access slightly faster.

Purpose: Optimize memory when creating many objects.

#### Basic Example
```python
class User:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age
````

Now only `name` and `age` are allowed.

#### Prevents Dynamic Attributes

You cannot add new attributes not listed in `__slots__`.

```python
u = User("Ram", 25)
u.city = "Chennai"   # ❌ Error
```

#### Why Use `__slots__`?

* Reduces memory usage
* Faster attribute access
* Prevents accidental attributes
* Useful in large-scale systems with many objects

---

### 12. Metaclasses (Advanced — Clear Notes)

#### What is a Metaclass?
A metaclass is a **class that creates other classes**.  
Just like classes create objects, metaclasses create classes.

In Python, the default metaclass is `type`.

#### Basic Idea
When you write a class, Python internally uses `type` to build it.

```python
class A:
    pass

print(type(A))   # <class 'type'>
````

Here, `type` created class `A`.

#### Why Use Metaclasses?

Metaclasses let you **control how classes are created**.
Used in frameworks like Django ORM, DRF, etc.

Common uses:

* Validate class structure
* Auto-register classes
* Modify class attributes
* Enforce rules

#### Simple Custom Metaclass

```python
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print("Creating class:", name)
        return super().__new__(cls, name, bases, attrs)

class A(metaclass=MyMeta):
    pass
```

When class `A` is created → metaclass runs first.

#### Key Points

* `type` is default metaclass
* Metaclass controls class creation
* Advanced feature
* Mostly used in frameworks and libraries

---

### 13. Object Lifecycle
- `__new__` → create object  
- `__init__` → initialize  
- `__del__` → destroy  

---

### 14. Context Managers (Clear Notes)

#### What is a Context Manager?
A context manager is used with the `with` statement to **manage resources automatically**.  
It ensures setup happens before use and cleanup happens after use.

Purpose: Proper resource handling (files, DB connections, locks, etc.).

#### How it Works
A context manager class uses two special methods:
- `__enter__()` → runs at start of `with`
- `__exit__()` → runs at end of `with`

#### Basic Example
```python
class FileManager:
    def __enter__(self):
        print("Open resource")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("Close resource")

with FileManager():
    print("Using resource")
````

Output order:

* enter runs
* block executes
* exit runs

#### Real Example (File Handling)

```python
with open("test.txt", "w") as f:
    f.write("Hello")
```

Python automatically:

* opens file
* closes file after block

#### Why Use Context Managers?

* Auto cleanup
* Prevent resource leaks
* Cleaner code
* Safe error handling

---

### 15. Descriptors (Advanced — Clear Notes)

#### What is a Descriptor?
A descriptor is a class that **controls how attributes are accessed, set, or deleted**.  
It works using special methods and is used internally by features like `@property` and Django models.

Purpose: Add custom logic when reading or writing attributes.

#### Descriptor Methods
- `__get__(self, obj, cls)` → runs when attribute is accessed  
- `__set__(self, obj, value)` → runs when value is assigned  
- `__delete__(self, obj)` → runs when attribute is deleted  

#### Simple Example
```python
class MyDescriptor:
    def __get__(self, obj, cls):
        print("Getting value")
        return obj._x

    def __set__(self, obj, value):
        print("Setting value")
        obj._x = value
````

Use inside another class:

```python
class A:
    x = MyDescriptor()

a = A()
a.x = 10     # calls __set__
print(a.x)   # calls __get__
```

#### Where Descriptors Are Used

* `@property`
* Django model fields
* ORM frameworks
* Validation systems

#### Key Idea

Whenever you access or set an attribute,
descriptor methods automatically run and control the behavior.

---

### 16. Copying Objects (Clear Notes)

#### Why Copy Objects?
Copying creates a new object from an existing one.  
Important when working with lists, dicts, or nested objects.

Python provides shallow and deep copy.

#### Shallow Copy
Creates a new object, but **inner objects are shared**.  
Changes inside nested objects affect both copies.

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)

b[0][0] = 99
print(a)   # also changes
````

#### Deep Copy

Creates a completely independent copy.
All nested objects are copied too.

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 99
print(a)   # unchanged
```

#### copy Module

Python provides built-in module for copying.

```python
import copy

copy.copy(obj)      # shallow copy
copy.deepcopy(obj)  # deep copy
```

#### Key Difference

* Shallow copy → copies outer object only
* Deep copy → copies everything recursively

---
