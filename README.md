# Python Workspace: FastAPI + Next.js + Practice Scripts

This repo mixes a full-stack FastAPI + Next.js project with smaller Python learning exercises. The main app lives under `fast/new_project`, and there is an earlier FastAPI demo in `fast/` plus assorted practice scripts at the repo root and in `numpy/`.

## Project Map
- `fast/new_project`: Full-stack “Product Console” app (FastAPI backend + Next.js frontend).
- `fast/new_project/forntend`: Next.js UI (note the folder name is `forntend`).
- `fast/new_project/alembic`: Database migrations.
- `fast/new_project/uploads`: User profile pictures saved by the backend.
- `fast/`: Simple in-memory FastAPI products API demo.
- `numpy/`, `class.py`, `loops.py`, etc.: Python practice exercises and notes.

## Backend (FastAPI)
**Location:** `fast/new_project`

**What it does**
- Product CRUD with pagination and search.
- User signup/login with JWT access tokens.
- Profile updates (username + profile picture upload).
- Password change and reset via email flow.
- Email templates for welcome + password reset.
- Simple request logging and a global error handler.

**Key endpoints**
- `POST /signup` and `POST /login`
- `GET /products`, `POST /products`, `GET /products/{id}`
- `PUT /products/{id}`, `DELETE /products/{id}` (delete requires admin role)
- `GET /user/me`, `PUT /user/update`
- `POST /change-password`
- `POST /reset-password` and `POST /reset-password/confirm`

**Notes from code**
- JWT is required for create/update product and profile routes.
- Delete product uses a role check (`admin`).
- Profile images are saved to `uploads/profile_pictures` and served at `/uploads`.
- Reset password flow generates a short-lived token and emails a link.

## Frontend (Next.js)
**Location:** `fast/new_project/forntend`

**Pages included**
- `/` overview
- `/login` and `/signup`
- `/products` list with pagination + search
- `/products/new` create product
- `/products/[id]` detail + update + delete
- `/profile` update username/profile picture, change password
- `/forgot-password` and `/reset-password`

**Notes from code**
- The UI stores the access token in `localStorage`.
- API base defaults to `http://localhost:8000` via `NEXT_PUBLIC_API_BASE_URL`.
- Profile images are fetched from the backend `/uploads` path.

## Environment Variables
Create a `.env` inside `fast/new_project` (do not commit it). These are referenced in code:
- `DATABASE_URL`
- `SECRET_KEY`
- `ALGORITHM`
- `ACCESS_TOKEN_EXPIRE_MINUTES`
- `MAIL_USERNAME`
- `MAIL_PASSWORD`
- `MAIL_FROM`
- `MAIL_PORT`
- `MAIL_SERVER`
- `APP_URL` (frontend base URL, e.g. `http://localhost:3000`)

For the frontend, optionally set:
- `NEXT_PUBLIC_API_BASE_URL` (defaults to `http://localhost:8000`)

## How to Run
**Backend**
1. `cd fast/new_project`
2. Create `.env` with the values above.
3. Install deps (example): `pip install -r requirements.txt`
4. Run: `uvicorn main:app --reload`

**Frontend**
1. `cd fast/new_project/forntend`
2. `npm install`
3. `npm run dev`

## Extra Notes
- `fast/main.py` is a simpler FastAPI demo that uses an in-memory product list.
- The `uploads/` folder is user-generated content and should stay out of git.
- Practice scripts at repo root are small Python exercises and utilities.
