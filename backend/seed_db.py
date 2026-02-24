from sqlmodel import Session

from app.main import engine, Plant


def seed_db():
    with Session(engine) as session:
        plant_1 = Plant(
            name="Monstera", species="Monstera deliciosa", notes="Loves indirect light")
        plant_2 = Plant(name="Fiddle Leaf", species="Ficus lyrata")
        plant_3 = Plant(name="Pothos", species="Epipremnum aureum")

        session.add(plant_1)
        session.add(plant_2)
        session.add(plant_3)
        session.commit()


if __name__ == "__main__":
    seed_db()
