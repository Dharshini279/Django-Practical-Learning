# Manage.py Commands

### AUTH COMMANDS

#### `createsuperuser`

Create admin login.

**Real use:**
When you set up project first time.

```bash
python manage.py createsuperuser
```

Then login:

```
/admin
```

Used for:

* admin panel
* managing products/orders/users

#### `changepassword`

Change user password from terminal.

```bash
python manage.py changepassword username
```

**Real use:**

* Reset admin password on server
* Dev forgot password

### CONTENT TYPES

#### `remove_stale_contenttypes`

Removes deleted model references from DB.

```bash
python manage.py remove_stale_contenttypes
```

**Real use:**
You delete a model like `OldProduct`
Django still keeps content type entry.
This cleans it.

Used during:

* refactoring
* model deletion

### DJANGO CORE COMMANDS

#### `check`

Checks project for issues.

```bash
python manage.py check
```

**Real use:**
Run before deployment.

Finds:

* wrong settings
* model errors
* URL issues

#### `compilemessages`

Used for translations.

```bash
python manage.py compilemessages
```

**Real use:**
Multi-language apps (Tamil/English sites).

#### `createcachetable`

Creates DB table for caching.

```bash
python manage.py createcachetable
```

**Real use:**
When using DB caching:

```python
CACHES = {"default": {"BACKEND": "django.core.cache.backends.db.DatabaseCache"}}
```

#### `dbshell`

Open DB terminal.

```bash
python manage.py dbshell
```

**Real use:**

* Check tables
* Run SQL
* Debug DB

SQLite → opens sqlite
Postgres → opens psql

#### `diffsettings`

Shows modified settings.

```bash
python manage.py diffsettings
```

**Real use:**
Compare with default Django settings.

Very useful in debugging production issues.

#### `dumpdata`

Export database data.

```bash
python manage.py dumpdata > data.json
```

**Real use:**

* backup DB
* move data to another server
* create demo data

#### `flush`

Deletes all data but keeps tables.

```bash
python manage.py flush
```

**Real use:**
Reset dev database.

Deletes everything.

#### `inspectdb`

Convert existing DB → Django models.

```bash
python manage.py inspectdb
```

**Real use:**
When company already has DB.

You generate models automatically.

#### `loaddata`

Load JSON data.

```bash
python manage.py loaddata data.json
```

**Real use:**

* seed demo products
* import backup

#### `makemessages`

Create translation files.

```bash
python manage.py makemessages -l ta
```

**Real use:**
Multi-language websites.

#### `makemigrations`

Create migration file.

```bash
python manage.py makemigrations
```

**Real use:**
After editing models.

#### `migrate`

Apply migrations to DB.

```bash
python manage.py migrate
```

Creates tables.

#### `optimizemigration`

Optimizes migration files.

Rarely used.

Used in large projects.

#### `sendtestemail`

Send test email.

```bash
python manage.py sendtestemail your@email.com
```

**Real use:**
Check email config.

#### `shell`

Open Django shell.

```bash
python manage.py shell
```

**Real use:**
Test queries quickly.

```python
from products.models import Product
Product.objects.all()
```

#### `showmigrations`

Show migration status.

```bash
python manage.py showmigrations
```

Shows applied migrations.

#### `sqlflush`

Shows SQL for flush.

```bash
python manage.py sqlflush
```

Used for debugging.

#### `sqlmigrate`

Show SQL for migration.

```bash
python manage.py sqlmigrate products 0001
```

Used when debugging migration errors.

#### `sqlsequencereset`

Reset auto increment IDs.

```bash
python manage.py sqlsequencereset products
```

Used when:
IDs messed up.

#### `squashmigrations`

Combine migrations.

```bash
python manage.py squashmigrations products 0001 0010
```

Used in large apps.

#### `startapp`

Create new app.

```bash
python manage.py startapp products
```

Used at project start.

#### `startproject`

Create project.

```bash
django-admin startproject config
```

#### `test`

Run tests.

```bash
python manage.py test
```

Used in CI/CD.

#### `testserver`

Run server with test DB.

```bash
python manage.py testserver
```

Used for debugging fixtures.

---

### SESSIONS

#### `clearsessions`

Delete expired sessions.

```bash
python manage.py clearsessions
```

**Real use:**
Cron job in production.

---

### STATIC FILES

#### `collectstatic`

Collect static files.

```bash
python manage.py collectstatic
```

Used in production before deployment.

#### `findstatic`

Find static file path.

```bash
python manage.py findstatic css/style.css
```

Used for debugging static issues.

#### `runserver`

Start dev server.

```bash
python manage.py runserver
```

Daily use.

---
### REAL PROJECT WORKFLOW

Daily developer commands:

```
runserver
makemigrations
migrate
shell
```

Deployment:

```
collectstatic
check --deploy
```

Debug:

```
showmigrations
sqlmigrate
dbshell
```

Data migration:

```
dumpdata
loaddata
```

---
### Most important to master

Focus on these first:

```
runserver
makemigrations
migrate
shell
createsuperuser
collectstatic
showmigrations
dumpdata
loaddata
check
```

---