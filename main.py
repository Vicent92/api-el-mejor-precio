from fastapi import FastAPI
from app.routes import item_routes

app = FastAPI(
    title="API El Mejor Precio",
    description="Una API básica con FastAPI usando MVC",
    version="1.0.0"
)

# Incluir las rutas
app.include_router(item_routes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
