## Django Project Setup — Clean & Company Standard

### Step 1 — Create Django Project

Run this inside your root folder:

```bash
django-admin startproject config .
````

**Folder structure:**

```
bakery_system/
├── venv/
├── config/
├── manage.py
```

> We use `config` as the project core (company standard).

### Step 2 — Create Main Folders

Run:

```bash
mkdir apps
mkdir core
mkdir requirements
mkdir scripts
```

**Updated structure:**

```
bakery_system/
├── venv/
├── config/
├── apps/
├── core/
├── requirements/
├── scripts/
├── manage.py
```

### Why These Folders?

### `apps/`

All Django apps go here:

* `accounts`
* `orders`
* `products`
* `inventory`

> Keeps root clean.

### `core/`

Reusable logic:

* `services`
* `utils`
* `base models`
* `mixins`
* `permissions`

> Used in advanced architecture.

### `requirements/`

Split dependencies:

* `base.txt`
* `dev.txt`
* `prod.txt`

> Real companies split dependencies.

### `scripts/`

Custom scripts for later:

* Seed data
* Cron jobs
* Management helpers

### Step 3 — Tell Django About `apps/`

Open `config/settings.py` and add at top:

```python
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
```

> Now Django can detect apps inside `apps/`.

### Step 4 — Create Requirements File

```bash
pip freeze > requirements/base.txt
```

### Step 5 — Initialize Git

```bash
git init
```

Create `.gitignore`:

```
venv/
__pycache__/
db.sqlite3
.env
*.pyc
```

Commit:

```bash
git add .
git commit -m "Initial project structure"
```

> Push to GitHub if a repo exists.

### Final Structure (Memorize This)

```
bakery_system/
│
├── config/          → settings & urls
├── apps/            → all apps
├── core/            → shared logic
├── requirements/    → dependencies
├── scripts/         → custom scripts
├── manage.py
└── venv/
```

> This is company-level Django structure.