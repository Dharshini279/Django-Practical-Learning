CURRENT SITUATION

Local:

```
DJANGO/
└── Bakery_Management_System/
    ├── apps
    ├── config
    ├── core
    └── ...
```

GitHub repo:

```
Django-Practical-Learning/
└── Bakery-Management-System/   ← want to push here
```

We will connect only this folder to that repo.

## STEP 1 — Go inside your project folder

```bash
cd Bakery_Management_System
```

## STEP 2 — Initialize git (if not already)

```bash
git init
```

## STEP 3 — Connect to your GitHub repo

Copy repo URL:

```
https://github.com/Dharshini279/Django-Practical-Learning.git
```

Add remote:

```bash
git remote add origin https://github.com/Dharshini279/Django-Practical-Learning.git
```

## STEP 4 — Pull repo first (IMPORTANT)

Because repo already has files.

```bash
git pull origin main --allow-unrelated-histories
```

This merges local + GitHub.

## STEP 5 — Move your folder inside repo structure

If your GitHub repo already has:

```
Django-Practical-Learning/
```

We want:

```
Django-Practical-Learning/
└── Bakery-Management-System/
```

So ensure locally your structure matches:

Inside repo root:

```
Django-Practical-Learning/
└── Bakery-Management-System/
```

If not, move folder:

```bash
mv Bakery_Management_System Bakery-Management-System
```

## STEP 6 — Add & commit

```bash
git add .
git commit -m "Added bakery management project structure"
```

## STEP 7 — Push to GitHub

```bash
git push origin main
```

Now your project appears in that folder.

---

## HOW TO PUSH CHANGES REGULARLY

Every time you code:

```bash
git add .
git commit -m "added models for products"
git push
```

That’s it.

---

## IMPORTANT `.gitignore`

Create `.gitignore` in project root:

```
venv/
bakeryvenv/
__pycache__/
db.sqlite3
.env
*.pyc
```

Then:

```bash
git add .
git commit -m "added gitignore"
git push
```

### What is a Django App?

A **Django app** is a modular component that handles a specific business domain.

Examples:

* accounts → authentication
* products → product catalog
* orders → order management
* notifications → emails/websockets

A project contains multiple apps.

```
Project = container
Apps = features/modules
```

### Why Proper App Structure Matters

Bad structure:

```
views.py → 2000 lines
models.py → 1500 lines
```

Good structure:

* scalable
* testable
* reusable
* interview-ready

### Standard App Structure (Beginner)

When you run:

```
python manage.py startapp products
```

You get:

```
products/
 ├── admin.py
 ├── apps.py
 ├── models.py
 ├── views.py
 ├── tests.py
 ├── migrations/
 └── __init__.py
```

This is fine for small apps.

But **not enough** for real projects.

### Production App Structure

For your showcase project, use this:

```
apps/products/
│
├── models/
│   ├── __init__.py
│   ├── product.py
│   ├── category.py
│   └── inventory.py
│
├── api/
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── routers.py
│
├── services/
│   ├── product_service.py
│   └── inventory_service.py
│
├── selectors/
│   └── product_selector.py
│
├── forms/
│   └── product_form.py
│
├── tasks/
│   └── celery_tasks.py
│
├── templates/products/
├── static/products/
├── signals.py
├── admin.py
├── apps.py
└── migrations/
```

This structure supports:

* Django views
* DRF
* Celery
* Clean architecture

### Explanation of Each Folder

#### models/

Instead of one `models.py`, split models.

```
models/
 ├── product.py
 ├── category.py
```

In `models/__init__.py`:

```python
from .product import Product
from .category import Category
```

Why?

* Large apps have many models
* Easier maintenance

#### api/ (For DRF)

All API logic goes here.

```
api/
 ├── serializers.py
 ├── views.py
 ├── urls.py
```

Keeps API separate from web views.

#### services/ (VERY IMPORTANT)

Business logic should NOT be in views.

Example:

```python
# services/product_service.py
def create_product(data, user):
    product = Product.objects.create(**data, created_by=user)
    return product
```

Views call services.

This is **senior architecture**.

#### selectors/ (Query layer)

All DB queries go here.

```python
def get_active_products():
    return Product.objects.filter(is_active=True)
```

Why?

* Avoid query duplication
* Easier optimization

#### forms/

For Django forms:

```
forms/product_form.py
```

Used in template-based views.

#### tasks/

Celery tasks:

```
tasks/send_email.py
```

Used for:

* background jobs
* async tasks

#### templates/

```
templates/products/list.html
templates/products/detail.html
```

Used for server-rendered pages.

#### static/

```
static/products/css/
static/products/js/
```

#### signals.py

Used for:

* post_save
* pre_delete

Example:

```python
@receiver(post_save, sender=Order)
def create_invoice(sender, instance, created, **kwargs):
    if created:
        generate_invoice(instance)
```

### apps.py Purpose

```
class ProductsConfig(AppConfig):
    name = 'products'

    def ready(self):
        import apps.products.signals
```

Registers signals.

### How Many Apps Should You Create?

Create app when:

* new business domain
* reusable module
* large feature

Example project apps:

```
apps/
 ├── accounts
 ├── products
 ├── orders
 ├── payments
 ├── notifications
 ├── reports
 └── common
```

### Common App

Create shared app:

```
apps/common/
```

Used for:

* base models
* mixins
* utils
* constants

### Naming Conventions

Good:

```
orders
products
accounts
```

Bad:

```
coreapp
main
myapp
```

### App URLs Structure

Inside each app:

```
apps/products/api/urls.py
apps/products/web/urls.py
```

Main urls:

```
path("api/products/", include("apps.products.api.urls"))
path("products/", include("apps.products.web.urls"))
```

### App Dependencies Rule

Apps can depend on:

```
core/
common/
```

But avoid:

```
orders → products → orders
```
No circular imports.

### App Structure for Project

Use this EXACT structure.

```
apps/
├── accounts/
├── products/
├── orders/
├── inventory/
├── notifications/
├── reports/
└── common/
```

Each app:

```
models/
api/
services/
selectors/
admin.py
apps.py
signals.py
```
---


