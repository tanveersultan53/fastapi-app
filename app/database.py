from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session
