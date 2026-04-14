# Learning Notes (Repo Summary)

This file summarizes what you have learned based on the code in this repo. I grouped topics by area and listed the key files that show each topic.

## Python Basics
- Variables, input/output, `None`, booleans: `firstmessage.py`
- String operations, `len`, `count`, user input, conditional logic: `strings.py`
- Lists and slicing, list length, mutability: `list_tuples.py`
- Tuples and immutability (attempted mutation error): `list_tuples.py`
- Dictionaries: create, update, keys/values/items, length: `dictionary.py`
- Sets, uniqueness, union/intersection: `set.py`

## Control Flow and Loops
- `while` loops, list building, search with `break`: `loops.py`
- `for` loops, `range` variants, `for-else`: `loops.py`
- Simple logic exercises (palindrome list, counting): `questions.py`

## Functions
- Function with default parameters: `functions.py`
- Iterative factorial: `functions.py`

## File Handling
- Read/write text files with `open`, `read`, `write`: `filesystem.py`
- Sample files used for I/O: `demo.txt`, `demo1.txt`

## Object-Oriented Programming (OOP)
- Class, constructor, instance attributes, static method: `class.py`
- Basic encapsulation (name-mangled private attribute): `class.py`
- Inheritance and `super()`: `class1.py`

## NumPy (Numerical Computing)
- Array creation, shapes, dtype, indexing/slicing, zeros/ones/full/eye, arange/linspace, random arrays: `numpy/num.py`
- Array operations, reshape, flatten, dot product, boolean filtering, math functions: `numpy/questions.py`

## Pandas (Data Analysis)
- DataFrame creation, head/tail, columns, describe, shape: `numpy/test_pandas.py`
- Rename columns, selection with `loc`/`iloc`, filtering, `where`: `numpy/test_pandas.py`
- Add/update rows and columns, drop rows/columns: `numpy/test_pandas.py`
- Sorting, datetime parsing, extracting date parts: `numpy/test_pandas.py`
- Missing values (`NaN`), `isnull`, `fillna`: `numpy/test_pandas.py`
- Groupby + aggregation, value counts: `numpy/test_pandas.py`
- Concat, merge, query: `numpy/test_pandas.py`
- CSV write/read: `numpy/test_pandas.py`, `numpy/data.csv`

## Matplotlib (Data Visualization)
- Line plot styling, multiple lines, bar chart, histogram, pie chart, scatter: `numpy/mplot.py`
- Subplots and figure sizing: `numpy/mplot.py`
- Pandas + Matplotlib charting: `numpy/mplot.py`

## FastAPI (Basics)
- Simple API with in-memory data and CRUD routes: `fast/main.py`, `fast/product_model.py`
- FastAPI demo with Pydantic model + basic routes: `fastapi/fastapi-demo/main.py`, `fastapi/fastapi-demo/models.py`

## FastAPI (Full Project: Product Console)
- App setup, CORS, static files, router include: `fast/new_project/main.py`
- SQLAlchemy setup, session handling, env-based DB URL: `fast/new_project/db/database.py`
- Pydantic schemas for validation/response: `fast/new_project/schemas/products_schema.py`, `fast/new_project/schemas/users_schema.py`
- Models for products and users: `fast/new_project/models/products_models.py`, `fast/new_project/models/user_model.py`
- Controllers + service layer separation: `fast/new_project/controllers/*.py`, `fast/new_project/services/*.py`
- JWT auth and role checks: `fast/new_project/middlewares/jwt_checker.py`, `fast/new_project/middlewares/role_checker.py`
- Logger and global error handler: `fast/new_project/middlewares/logger_middleware.py`, `fast/new_project/middlewares/error_handling.py`
- Password hashing: `fast/new_project/utils/password_utils.py`
- Email sending (FastAPI Mail) and templates: `fast/new_project/utils/email_service.py`, `fast/new_project/templates/*.html`
- JWT utilities + reset token flow: `fast/new_project/utils/jwt_utils.py`
- Alembic migrations: `fast/new_project/alembic/*`
- File uploads (profile pictures): `fast/new_project/uploads/`

## Frontend (Next.js)
- Next.js app pages and routing: `fast/new_project/forntend/src/app/*`
- Auth UI, products CRUD UI, profile updates, password reset flow: `fast/new_project/forntend/src/app/**/*`
- API helpers + token storage: `fast/new_project/forntend/src/lib/api.ts`, `fast/new_project/forntend/src/lib/token.ts`
- Shared navigation component: `fast/new_project/forntend/src/components/TopNav.tsx`

## Extra Notes
- There are practice scripts at the repo root (`class.py`, `loops.py`, `strings.py`, etc.)
- The folder name for the frontend is spelled `forntend` in this repo.
