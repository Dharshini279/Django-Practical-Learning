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

---

Tell me the exact situation and I’ll give exact commands.

