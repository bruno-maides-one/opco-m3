import os.path
from fastapi import FastAPI
from pydantic import BaseModel
from models import Pret, Client, Region, Niveau_etude, Base
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
app = FastAPI()

# Init de la base
DATABASE_FILE = os.path.join('data', 'database.db')
DATABASE_URI = f'sqlite:///./{DATABASE_FILE}'

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(bind=engine)
session = sessionmaker(bind=engine)()

# async def get_db():
#     db_session = sessionmaker(bind=engine)
#     try:
#         yield db_session
#     finally:
#         close_all()




@app.get("/clients")
async def clients():
    # Assuming you have a database session set up (db)
    # client_list = session.scalars(select(Client).limit(3)).all()
    client_list = session.scalars(select(Client).limit(5)).all()
    print(client_list)
    return {"status": "success", "data": [c.__dict__ for c in client_list]}

@app.post("/client")
async def create_client(client: Client):
    session.add(client)
    session.commit()
    session.refresh(client)
    return {"status": "success", "data": client.__dict__}
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/prets")
async def prets():
    pass

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}