from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Import routers
from api.routers import food

# Include routers
app.include_router(food.router)
app.mount("/static", StaticFiles(directory="static"), name="static")
