# Python OOP — Complete Concepts with Simple Explanations

## 1. OOP Basics
- **Class** → Blueprint for creating objects  
- **Object** → Instance of a class  
- **Attributes** → Variables inside class/object  
- **Methods** → Functions inside class  
- **self** → Refers to current object  
- **__init__** → Constructor called when object created  
- **Instance variable** → Unique per object  
- **Class variable** → Shared across all objects  

---

## 2. Encapsulation
- Bundling data + methods together  
- Controls access to variables  

Types:
- Public → accessible anywhere  
- Protected `_var` → internal use  
- Private `__var` → name-mangled  

Tools:
- Getter → get value  
- Setter → set value  
- `@property` → access method like variable  

Purpose: Data protection

---

## 3. Abstraction
- Hide internal logic  
- Show only required functionality  
- Use abstract classes  

Modules:
- `abc`
- `ABC`
- `@abstractmethod`

Purpose: Hide complexity

---

## 4. Inheritance
- Child class gets parent features  

Types:
- Single  
- Multiple  
- Multilevel  
- Hierarchical  
- Hybrid  

Concepts:
- Method overriding  
- `super()` → call parent method  
- MRO → method lookup order  

Purpose: Code reuse

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
