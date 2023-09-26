from fastapi import FastAPI

from firebase import get_app

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/apps/{app_id}")
def read_item(app_id: str):
    return get_app(app_id)
