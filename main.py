from fastapi import FastAPI

from app.routes import routes

app = FastAPI()

app.include_router(routes.router, prefix="/produtor-rural", tags=["Produtores"])

@app.get("/")
def read_root():
    return {"message": "API com arquitetura limpa funcionando!"}
