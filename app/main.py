from fastapi import FastAPI, Depends
from . import models, crud, database
from sqlmodel import Session

app = FastAPI()

# Create database tables
models.SQLModel.metadata.create_all(database.engine)

@app.post("/items/", response_model=models.Item)
def create_item(item: models.Item, session: Session = Depends(database.get_session)):
    return crud.create_item(session, item)

@app.get("/")
def read_root():
    return {"Hello": "World"}
