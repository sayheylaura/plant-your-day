import os

from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import Field, SQLModel, create_engine


class Plant(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    species: str
    notes: str | None = None


database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
