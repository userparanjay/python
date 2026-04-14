from fastapi import FastAPI
from db.database import Base,engine
from routes.products_routes import router as products_routes
from routes.users_routes import user_routes
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from middlewares.logger_middleware import logger_middleware
from middlewares.error_handling import global_exception_handler

app=FastAPI(
    title="Product API",
    description="API for managing products",
    version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.exception_handler(Exception) (global_exception_handler)
app.middleware("http")(logger_middleware)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return RedirectResponse(url="/docs")
app.include_router(products_routes)
app.include_router(user_routes)
