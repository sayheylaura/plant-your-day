from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Plant(BaseModel):
    id: int
    name: str
    species: str
    notes: str | None = None


class PlantCreate(BaseModel):
    name: str
    species: str
    notes: str | None = None


plants: list[Plant] = [
    Plant(id=1, name="Monstera", species="Monstera deliciosa",
          notes="Loves indirect light"),
    Plant(id=2, name="Fiddle Leaf", species="Ficus lyrata"),
]


@app.get("/plants", response_model=list[Plant])
def get_plants():
    return plants


@app.get("/plants/{plant_id}", response_model=Plant)
def get_plant(plant_id: int):
    plant = next((p for p in plants if p.id == plant_id), None)

    if not plant:
        raise HTTPException(
            status_code=404, detail=f"Plant with ID {plant_id} not found")

    return plant


@app.post("/plants", response_model=Plant, status_code=201)
def create_plant(plant: PlantCreate):
    new_id = max([p.id for p in plants], default=0) + 1

    new_plant = Plant(
        id=new_id,
        name=plant.name,
        species=plant.species,
        notes=plant.notes
    )

    plants.append(new_plant)
    return new_plant


@app.put("/plants/{plant_id}", response_model=Plant)
def update_plant(plant_id: int, updated_plant: Plant):
    # Validate that URL ID matches body ID
    if updated_plant.id != plant_id:
        raise HTTPException(
            status_code=400,
            detail=f"ID in URL ({plant_id}) doesn't match ID in body ({updated_plant.id})"
        )

    for i, p in enumerate(plants):
        if p.id == plant_id:
            plants[i] = updated_plant
            return updated_plant

    raise HTTPException(
        status_code=404, detail=f"Plant with ID {plant_id} not found")


@app.delete("/plants/{plant_id}", status_code=204)
def delete_plant(plant_id: int):
    for i, p in enumerate(plants):
        if p.id == plant_id:
            plants.pop(i)
            return

    raise HTTPException(
        status_code=404, detail=f"Plant with ID {plant_id} not found")
