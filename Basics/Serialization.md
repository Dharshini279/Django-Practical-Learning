# Serialization

**Serialization = converting a Python object → storable/transmittable format**
So you can:

* save to file
* send over network
* store in DB
* cache
* send via API

Reverse process = **Deserialization**

### Why serialization matters (real life)

In Django/DRF:

* Model instance → JSON → API response
* Cache objects → Redis
* Send tasks → Celery
* Store sessions

Frameworks do this *constantly*.

### JSON Serialization

Human readable. Used in APIs.

##### Object → JSON

```python
import json

data = {"name": "Ram", "age": 25}
json_str = json.dumps(data)
```

##### JSON → Object

```python
obj = json.loads(json_str)
```

##### Problem: custom objects

```python
class User:
    def __init__(self, name):
        self.name = name

u = User("Ram")

json.dumps(u)   # ERROR
```

JSON doesn't understand custom classes.

##### Solution: convert to dict

```python
class User:
    def __init__(self, name):
        self.name = name

u = User("Ram")

json.dumps(u.__dict__)
```

##### Advanced: custom encoder

```python
class User:
    def __init__(self, name):
        self.name = name

class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return obj.__dict__
        return super().default(obj)

json.dumps(User("Ram"), cls=UserEncoder)
```
Django REST Framework serializers do exactly this internally.

### Pickle Serialization (Python internal)

Pickle converts Python objects → binary format.

Supports:

* classes
* functions
* complex objects

```python
import pickle

data = {"a": 1}

binary = pickle.dumps(data)
obj = pickle.loads(binary)
```

### Pickle Warning (VERY IMPORTANT)

Never unpickle untrusted data.

```python
pickle.loads(data_from_user)   # DANGEROUS
```

Why?
Pickle can execute code.
Pickle is powerful but unsafe for external data.

### JSON vs Pickle

| Feature                 | JSON      | Pickle |
| ----------------------- | --------- | ------ |
| Readable                | Yes       | No     |
| Language independent    | Yes       | No     |
| Secure                  | Yes       | No     |
| Supports custom objects | Limited   | Yes    |
| Used in APIs            | Yes       | No     |
| Used in caching         | Sometimes | Yes    |

**Rule:**

* API → JSON
* Python internal → Pickle

### Serialization in Django/DRF

DRF Serializer = structured serialization system.

```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
```

Flow:

```
Model instance → serializer → JSON → API
```

Reverse:

```
JSON → serializer → Python → DB save
```

This is **controlled serialization**.

### Advanced concept

#### Serialization vs Copy

| Concept       | Purpose             |
| ------------- | ------------------- |
| copy()        | duplicate in memory |
| serialization | store/send          |


#### Serialization vs Marshaling

Python internal low-level serialization:

```python
import marshal
```

Used for `.pyc` files.

#### When to use what (real scenarios)

##### Use JSON when:

* API
* frontend communication
* logging
* config files

##### Use Pickle when:

* caching Python objects
* ML models
* background jobs

#### Performance concept

Pickle is faster than JSON for Python objects.

But:

* not portable
* not safe

So production APIs use JSON.

### Real-world deep example

Celery task queue:

```
Django → serialize task → send to worker → deserialize → run
```

Redis cache:

```
object → pickle → store → unpickle → retrieve
```

### One-line memory trick

**Serialization = object → transferable format**
**Deserialization = format → object**

---
