# Design Patten - Django

## MVC → Django uses MVT

Not theory — understand mapping.

| Classic    | Django                           |
| ---------- | -------------------------------- |
| Model      | Model                            |
| View       | Template                         |
| Controller | View (Django view handles logic) |

**Flow**

```
URL → View → Service/Logic → Model → Template/JSON
```

Know this deeply:

* where logic should live
* where NOT to write logic

Real rule:
**Views should be thin. Business logic should not live in views.**

---

## Fat Model, Thin View Pattern

Django encourages business logic inside models/services.

### Bad

```python
def create_order(request):
    order = Order.objects.create(...)
    send_email()
    calculate_tax()
```

### ✔ Good

```python
class Order(models.Model):
    def create_order(self):
        self.calculate_tax()
        self.send_email()
```

Or even better → service layer (see below).

**Know when NOT to put logic in views.**

---

## Service Layer Pattern

Django doesn’t force this but **real companies use it**.

Why? Views become messy.

### Structure

```
app/
 ├── models.py
 ├── services.py   ⭐ business logic
 ├── selectors.py  ⭐ query logic
 ├── views.py
```

### Example

```python
# services.py
def create_invoice(user, data):
    invoice = Invoice.objects.create(...)
    send_invoice_email(invoice)
    return invoice

# views.py
def create(request):
    invoice = create_invoice(request.user, request.data)
```

Benefits:

* reusable logic
* testable
* clean views

**Real-world Django teams expect this.**

---

## Repository / Selector Pattern (Clear Explanation)

#### What is it?
Repository/Selector pattern means **separating database queries from views/services**  
so queries are written in one place and reused everywhere.

Instead of writing `.filter()` in many files, we keep queries in a dedicated file  
like `selectors.py` or `repositories.py`.

Purpose: Clean code + reusable queries + easy optimization.

#### Basic Example

```python
# selectors.py
from .models import User

def get_active_users():
    return User.objects.filter(is_active=True)
````

Now use it anywhere:

```python
# views.py
from .selectors import get_active_users

def active_users_view(request):
    users = get_active_users()
```

#### Why use this pattern?

##### 1. Avoid query duplication

Without selectors:

```python
User.objects.filter(is_active=True)
```

This might be written in 10 places.

With selectors:

```python
get_active_users()
```

One place → reusable everywhere.

##### 2. Easy optimization later

Suppose you need `select_related` later:

```python
def get_active_users():
    return User.objects.filter(is_active=True).select_related("profile")
```

Only change in one file.
All views automatically optimized.

##### 3. Cleaner views

Views should handle request/response, not heavy queries.

Bad:

```python
def dashboard(request):
    users = User.objects.filter(is_active=True, role="manager")
```

Good:

```python
def dashboard(request):
    users = get_active_managers()
```

##### 4. Helps testing

You can test query logic separately.

```python
def test_active_users():
    users = get_active_users()
    assert users.count() == 5
```

#### Real-world Example

```python
# selectors.py
def get_user_with_orders(user_id):
    return User.objects.select_related("profile").prefetch_related("orders").get(id=user_id)
```

Used in:

* API views
* services
* background jobs

#### When to use?

Use selectors when:

* query used in multiple places
* complex joins
* optimization needed
* large project

Not needed for:

* very small apps
* simple one-time queries

---

## Factory Pattern (Clear Explanation)

#### What is Factory Pattern?
Factory pattern is used when **object creation logic is complex or depends on conditions**.  
Instead of creating objects directly, we use a **factory class/function** to create them.

Purpose: Centralize object creation and keep code clean.

---

#### Basic Example

```python
class UserFactory:
    @staticmethod
    def create_user(role):
        if role == "admin":
            return AdminUser()
        if role == "manager":
            return ManagerUser()
````

Usage:

```python
user = UserFactory.create_user("admin")
```

We don’t create `AdminUser()` directly — factory decides.

#### Why use Factory Pattern?

##### 1. Avoid complex `if-else` everywhere

Without factory:

```python
if role == "admin":
    user = AdminUser()
elif role == "manager":
    user = ManagerUser()
```

This logic may repeat in many files.

With factory:

```python
user = UserFactory.create_user(role)
```

One place → clean code.

##### 2. Easy to extend later

If a new role comes:

```python
if role == "employee":
    return EmployeeUser()
```

Only update factory.
No need to change all views/services.

##### 3. Hides creation logic

Maybe creating user needs:

* setting permissions
* creating profile
* sending email

Factory handles everything.

```python
class UserFactory:
    @staticmethod
    def create_user(role, data):
        if role == "admin":
            user = AdminUser(**data)
            assign_admin_permissions(user)
            return user
```

#### Real Django Use Cases

##### Creating different payment gateways

```python
class PaymentFactory:
    def get_gateway(method):
        if method == "stripe":
            return StripeService()
        if method == "razorpay":
            return RazorpayService()
```

##### Creating notifications

```python
NotificationFactory.create("email")
NotificationFactory.create("sms")
```

##### Test data creation

Factories are heavily used in Django tests.

---

#### When to use?

Use factory when:

* object creation has conditions
* setup logic is complex
* multiple object types
* avoid repeated `if-else`

Not needed when:

* simple object creation

---

## Singleton Pattern

Used for:

* settings
* config
* cache clients
* logging

Example:

```python
from django.conf import settings
```

Settings object behaves like singleton.

Also:

* Redis connection
* service clients

---

## Strategy Pattern (VERY COMMON)

Switch logic dynamically.

### Example: payment methods

```python
class PaymentStrategy:
    def pay(self): pass

class StripePayment(PaymentStrategy):
    def pay(self): ...

class RazorpayPayment(PaymentStrategy):
    def pay(self): ...
```

Use:

* payment gateways
* notifications
* pricing logic
* tax logic

In Django:

```
select strategy → execute
```

---

## Signals Pattern (Observer Pattern in Django)

#### What is it?
Django signals follow the **Observer pattern**.

Meaning:
When an event happens → other functions (listeners) automatically run.

Example flow:
```

User saved → signal triggered → send email/log/audit

````

You don’t call the function manually. Django triggers it.

---

#### Basic Example

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        print("Send email to", instance.email)
````

Whenever a User is created → email logic runs automatically.

#### Why signals are useful?

Used for side-effects:

* send notifications
* create audit logs
* update analytics
* background jobs
* auto-create profile

They keep code decoupled:
Model save does not directly call email function.

#### Real-world uses

✔ Send welcome email
✔ Create profile on user creation
✔ Log changes
✔ Push events to queue
✔ Cache invalidation

#### Problem with signals (IMPORTANT)

Signals are **hidden logic**.

When you save a model:

```python
user.save()
```

You don’t see:

* email sending
* logging
* tasks running

This makes debugging harder.

#### When NOT to use signals?

##### 1. Critical business logic

If logic must always run and be predictable.

Bad:

```python
Order.save() → signal → create payment
```

If signal fails → system breaks silently.

Better:
Use service layer:

```python
create_order()
create_payment()
```

##### 2. When order matters

Signals run in unpredictable order if multiple exist.

##### 3. Complex workflows

If logic has:

* multiple steps
* transactions
* validations

Use services instead.

#### Best Practice Rule

Use signals only for:

* notifications
* logging
* analytics
* non-critical side effects

Avoid for:

* core business logic
* payments
* order creation
* important workflows

#### Signals vs Service Layer

| Signals               | Service                 |
| --------------------- | ----------------------- |
| Automatic             | Explicit                |
| Hidden                | Clear                   |
| Hard to debug         | Easy                    |
| Good for side effects | Good for business logic |

---

## Serializer Pattern (Django REST Framework)

#### What is it?
DRF Serializer is a pattern used to **convert data between Python objects and JSON**  
while also handling **validation and object creation/update**.

It acts like a middle layer between:
```

Request data (JSON) ↔ Python objects ↔ Database models

````

Purpose:
- validate input data  
- transform data  
- create/update objects  
- convert objects → JSON response  

---

#### Basic Example

```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email"]
````

Usage:

```python
serializer = UserSerializer(data=request.data)
serializer.is_valid()
serializer.save()
```

`serializer.save()` internally creates or updates model instance.

#### Why it's a design pattern?

Serializer hides multiple patterns inside:

##### 1. Validation pattern

Validates data before saving.

```python
def validate_email(self, value):
    if "admin" in value:
        raise serializers.ValidationError("Invalid email")
    return value
```

##### 2. Transformation pattern

Transforms data format.

Example:
DB → JSON response.

```python
def to_representation(self, instance):
    data = super().to_representation(instance)
    data["full_name"] = instance.first_name + instance.last_name
    return data
```

##### 3. Factory pattern

Serializer decides how object is created.

```python
def create(self, validated_data):
    return User.objects.create(**validated_data)
```

You don’t manually create object → serializer does it.

#### Important internal methods

#### `validate()`

Runs overall validation.

```python
def validate(self, data):
    if data["start"] > data["end"]:
        raise serializers.ValidationError("Invalid dates")
    return data
```

##### `to_internal_value()`

Converts request JSON → Python data.

```
JSON input → Python dict
```

Rarely overridden but important internally.

##### `to_representation()`

Converts model instance → response JSON.

```
Model → JSON output
```

Used when customizing API response.

#### Real-world flow

```
request.data
   ↓
serializer(data=...)
   ↓
is_valid()
   ↓
validated_data
   ↓
save()
   ↓
model instance
   ↓
serializer.data → response JSON
```

#### Why serializers are powerful?

They combine:

* validation
* transformation
* creation logic
* representation

All in one place.

This keeps views clean:

```python
serializer = UserSerializer(data=request.data)
serializer.is_valid(raise_exception=True)
serializer.save()
return Response(serializer.data)
```
---

## Middleware Pattern (Django)

##### What is Middleware?
Middleware is a **request–response pipeline pattern**.  
Every request passes through middleware before reaching the view,  
and the response passes through middleware again before going back to the user.

Flow:
```

request → middleware → view → middleware → response

````

Middleware sits between server and view.

#### Why use Middleware?
Used for logic that must run on **every request**.

Common uses:
- authentication checks  
- logging  
- request tracking  
- tenant detection  
- performance timing  
- modifying request/response  

Purpose: Handle cross-cutting concerns globally.

#### Basic Example

```python
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Before view")

        response = self.get_response(request)

        print("After view")
        return response
````

Add in `settings.py`:

```python
MIDDLEWARE = [
    "myapp.middleware.SimpleMiddleware"
]
```

Now it runs on every request.

#### Real-world examples

##### ✔ Authentication middleware

Checks logged-in user.

##### ✔ Logging middleware

Logs every request URL and time.

```python
print(request.path)
```

##### ✔ Tenant middleware

Sets current company/tenant.

##### ✔ Performance tracking

Measures response time.

#### Middleware vs View

| Middleware            | View                       |
| --------------------- | -------------------------- |
| Runs for all requests | Runs for specific endpoint |
| Global logic          | Business logic             |
| Auth/logging          | Data processing            |


#### Middleware vs Decorator

| Middleware         | Decorator         |
| ------------------ | ----------------- |
| Global             | Per-view          |
| Runs automatically | Applied manually  |
| Auth/logging       | Permission checks |

Use middleware when logic must apply to **every request**.

#### Execution order

Request:

```
Middleware 1
Middleware 2
View
```

Response:

```
Middleware 2
Middleware 1
```

Order matters in `settings.py`.

#### When to use?

Use middleware for:

* auth/session handling
* request logging
* tenant handling
* rate limiting
* tracking

Do NOT use for:

* heavy business logic
* DB operations
* complex workflows

---

## Dependency Injection (DI) in Django

#### What is Dependency Injection?
Dependency Injection means **passing required objects (dependencies) into a class/function**  
instead of creating them inside the class.

Purpose: Make code flexible, testable, and reusable.

Instead of this:
```python
class OrderService:
    def __init__(self):
        self.payment_service = StripeService()   # tightly coupled
````

Use DI:

```python
class OrderService:
    def __init__(self, payment_service):
        self.payment_service = payment_service
```

Now payment service is injected from outside.

#### Why DI is important?

##### 1. Loose coupling

Your class does not depend on a specific implementation.

You can switch easily:

```python
OrderService(StripeService())
OrderService(RazorpayService())
```

##### 2. Easy testing

You can inject a fake service in tests.

```python
class FakePayment:
    def pay(self): return True

service = OrderService(FakePayment())
```

Testing becomes simple.

##### 3. Flexible architecture

Used in large apps where services change:

* payment gateways
* email providers
* notification systems

#### Django doesn't have full DI framework

Unlike some frameworks, Django doesn't enforce DI.

But we manually use DI in:

* services
* class-based views
* managers
* background tasks

#### Real-world Django example

```python
class InvoiceService:
    def __init__(self, email_service):
        self.email_service = email_service

    def send_invoice(self, user):
        self.email_service.send(user.email)
```

Usage:

```python
service = InvoiceService(EmailService())
service.send_invoice(user)
```

#### Where DI is used in Django projects?

* service layer
* payment integrations
* external APIs
* testing
* large-scale systems

#### DI vs Hardcoding

Hardcoded:

```python
self.email = EmailService()
```

Injected:

```python
service = InvoiceService(EmailService())
```

Injected version is better.

---

## Template Method Pattern (Django CBVs & DRF)

#### What is Template Method Pattern?
Template Method pattern defines a **fixed workflow**, but allows you to  
override specific steps without changing the entire process.

Meaning:
Framework controls the main flow → you customize only parts.

Purpose: Reuse common flow while allowing customization.

#### Simple idea
Parent class defines steps:
```

step1 → step2 → step3

````

Child class overrides only needed step.

You don’t rewrite whole logic.

---

#### Example in DRF

```python
class CreateAPIView:
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()
````

Here:

* `post()` = full workflow (template)
* `perform_create()` = customizable step

You override only:

```python
class MyView(CreateAPIView):
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

You changed one step, not whole process.

#### Why it's powerful?

You don’t rewrite:

* validation
* response
* serializer handling

Framework already defines flow.

You only customize:

* save logic
* querysets
* permissions
* hooks

#### Django CBV example

```python
class ListView:
    def get(self, request):
        data = self.get_queryset()
        return self.render_to_response(data)

    def get_queryset(self):
        return Model.objects.all()
```

Override:

```python
class MyListView(ListView):
    def get_queryset(self):
        return Model.objects.filter(active=True)
```

Again:
Template flow fixed → step overridden.

#### Where used in Django?

* CBVs (`get_queryset`, `form_valid`)
* DRF views (`perform_create`, `perform_update`)
* authentication classes
* serializers
* generic views

You override hooks, not full logic.

---

## How real Django projects are structured

```
project/
 ├── apps/
 │   ├── users/
 │   │   ├── models.py
 │   │   ├── services.py
 │   │   ├── selectors.py
 │   │   ├── views.py
 │   │   ├── serializers.py
```
---
