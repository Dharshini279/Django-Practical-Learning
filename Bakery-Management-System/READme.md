Product App Structure

apps/products/
│
├── __init__.py
├── admin.py
├── apps.py
├── urls.py                 ← web (template) urls
│
├── models/
│   ├── __init__.py
│   ├── category.py
│   ├── product.py
│   └── product_variant.py
│
├── views/                  ← template views
│   ├── __init__.py
│   ├── product_views.py
│   └── category_views.py
│
├── forms/
│   └── product_forms.py
│
├── templates/
│   └── products/
│       ├── product_list.html
│       ├── product_detail.html
│       ├── product_create.html
│       └── category_list.html
│
├── static/
│   └── products/
│       ├── css/
│       └── js/
│
├── services/               ← business logic
│   └── product_service.py
│
├── selectors/              ← DB queries
│   └── product_selectors.py
│
├── api/                    ← DRF
│   ├── __init__.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── routers.py
│   └── permissions.py
│
├── tasks/                  ← celery tasks
│   ├── __init__.py
│   └── product_tasks.py
│
├── signals.py              ← model signals
├── tests/                  ← tests later
│   └── test_products.py
│
└── migrations/
