import os

from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Plant(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    species: str
    notes: str | None = None


class PlantCreate(SQLModel):
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


def get_session():
    with Session(engine) as session:
        yield session


@app.get("/plants", response_model=list[Plant], tags=["plants"])
def get_all_plants(session: Session = Depends(get_session)):
    plants = list(session.exec(select(Plant).order_by(Plant.id)).all())
    return plants


@app.get("/plants/{plant_id}", response_model=Plant, tags=["plants"])
def get_plant_by_id(plant_id: int, session: Session = Depends(get_session)):
    plant = session.get(Plant, plant_id)
    if not plant:
        raise HTTPException(
            status_code=404, detail=f"Plant with ID {plant_id} not found"
        )
    return plant


@app.post("/plants", response_model=Plant, status_code=201, tags=["plants"])
def create_plant(plant: PlantCreate, session: Session = Depends(get_session)):
    new_plant = Plant(name=plant.name, species=plant.species, notes=plant.notes)
    session.add(new_plant)
    session.commit()
    session.refresh(new_plant)
    return new_plant


@app.put("/plants/{plant_id}", response_model=Plant, tags=["plants"])
def update_plant(plant_id: int, plant: PlantCreate, session: Session = Depends(get_session)):
    existing = session.get(Plant, plant_id)
    if not existing:
        raise HTTPException(
            status_code=404, detail=f"Plant with ID {plant_id} not found"
        )
    existing.name = plant.name
    existing.species = plant.species
    existing.notes = plant.notes
    session.add(existing)
    session.commit()
    session.refresh(existing)
    return existing


@app.delete("/plants/{plant_id}", status_code=204, tags=["plants"])
def delete_plant(plant_id: int, session: Session = Depends(get_session)):
    plant = session.get(Plant, plant_id)
    if not plant:
        raise HTTPException(
            status_code=404, detail=f"Plant with ID {plant_id} not found"
        )
    session.delete(plant)
    session.commit()
