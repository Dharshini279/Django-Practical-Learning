# Django Installation in Separate Virtual Environment

### Create a folder (anywhere)

```bash
mkdir django_env_test
cd django_env_test
```

---

### Create virtual environment

#### Linux / Mac

```bash
python3 -m venv venv
```

#### Windows

```bash
python -m venv venv
```

This creates:

```
django_env_test/
   venv/
```

### Activate virtual environment

#### Linux / Mac

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

You should now see:

```
(venv) $
```

That means environment is isolated.

### Upgrade pip (recommended)

```bash
pip install --upgrade pip
```

### Install Django

```bash
pip install django
```

### Verify installation

```bash
python -m django --version
```

Example output:

```
5.0.3
```

Now Django is installed **only inside this env**.

### Check installed packages

```bash
pip list
```

You should see:

```
Django
asgiref
sqlparse
```

### Deactivate environment

```bash
deactivate
```

Environment will close.

### Reactivate later

Whenever you return to project:

```bash
cd django_env_test
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

---
