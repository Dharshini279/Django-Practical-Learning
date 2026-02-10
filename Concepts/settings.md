# What is `settings.py`?

`settings.py` is the **central configuration file** of a Django project.

It controls:

* apps
* database
* templates
* static files
* security
* middleware
* environment configs
* production settings

Think of it like:

> **Control panel of Django**

Every Django project has one.

### How Django uses `settings.py`

When you run:

```bash
python manage.py runserver
```

Django:

1. Loads `settings.py`
2. Reads configurations
3. Loads apps
4. Connects DB
5. Starts server

If settings wrong → project won’t start.

#### Typical structure

```
project/
    manage.py
    project/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

---
## BASIC SECTION (Must understand first)

### BASE_DIR

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
```

This gives root project folder.

Used for:

* database path
* static files
* templates

Without this → paths break.

---
### SECRET_KEY

```python
SECRET_KEY = "django-insecure-xxxxx"
```

Used for:

* sessions
* password hashing
* tokens
* CSRF

Never expose in production.

Advanced practice later:

```
.env file
```

---
### DEBUG

```python
DEBUG = True
```

* True → development
* False → production

If False:

* errors hidden
* security strict

---
### ALLOWED_HOSTS

```python
ALLOWED_HOSTS = []
```

Defines which domains can access app.

Development:

```python
ALLOWED_HOSTS = ["*"]
```

Production:

```python
ALLOWED_HOSTS = ["example.com"]
```

---
## CORE DJANGO CONFIG

---
### INSTALLED_APPS

Most important section.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

This tells Django:

> Which apps exist in project

If app not added:

* models won’t migrate
* admin won’t detect
* views won’t work

Adding custom app:

```python
INSTALLED_APPS += ["blog"]
```

#### Built-in apps explained

| App         | Purpose             |
| ----------- | ------------------- |
| admin       | admin panel         |
| auth        | users & permissions |
| sessions    | login sessions      |
| messages    | flash messages      |
| staticfiles | CSS/JS              |

---
### MIDDLEWARE (Request pipeline)

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]
```

Middleware runs:

```
Request → Middleware → View → Middleware → Response
```

Examples:

* authentication check
* CSRF protection
* session handling

Advanced later:
You can create custom middleware.

---
### URL Configuration

```python
ROOT_URLCONF = 'project.urls'
```

Main URL file Django uses.

---
### Templates

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
    },
]
```

Explanation:

| Key      | Meaning                 |
| -------- | ----------------------- |
| DIRS     | global templates folder |
| APP_DIRS | templates inside apps   |

---
### DATABASE CONFIG

Default SQLite:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Other DB examples:

#### PostgreSQL

```python
DATABASES = {
 'default': {
  'ENGINE': 'django.db.backends.postgresql',
  'NAME': 'dbname',
  'USER': 'postgres',
  'PASSWORD': '123',
  'HOST': 'localhost',
  'PORT': '5432',
 }
}
```

---
### Password validators

```python
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
]
```

Ensures strong passwords.

---
### Internationalization

```python
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_TZ = True
```

Change timezone:

```python
TIME_ZONE = 'Asia/Kolkata'
```
---
### Static files (CSS/JS)

```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
```

For production:

```python
STATIC_ROOT = BASE_DIR / "staticfiles"
```
---
### Media files (uploads)

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Used for:

* profile images
* product images

---
## INTERMEDIATE LEVEL SETTINGS

Now we move deeper.
### Custom user model

```python
AUTH_USER_MODEL = "accounts.User"
```

Used when creating custom user.
### Login redirects

```python
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/"
```
### Email config

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "email@gmail.com"
EMAIL_HOST_PASSWORD = "password"
```
### Caching

```python
CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
 }
}
```

Used for performance.
### Logging

```python
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'},
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
```

Used in production debugging.

---

## ADVANCED SETTINGS

### Environment variables (.env)

Best practice:

```python
import os

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG") == "True"
```

Use library:

```
python-decouple
django-environ
```
### Split settings (professional way)

Instead of one file:

```
settings/
    base.py
    dev.py
    prod.py
```
### Security settings

```python
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
```

Production only.
### Installed apps grouping

```python
DJANGO_APPS = [...]
THIRD_PARTY_APPS = [...]
LOCAL_APPS = [...]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
```

Professional structure.