# Plant your day 🪴

This is a simple app to help you keep track of your plants and their care (the real kind, not the ones you buy from the store 🌿)

I'm using this project to learn Python, FastAPI and Vue. It's a work in progress, so expect things to change and break.

## 💥 Tech stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Vue](https://vuejs.org/) with [TypeScript](https://www.typescriptlang.org/)
- [TailwindCSS](https://tailwindcss.com/)

## 👩‍💻 Getting started

### 📦 Prerequisites

- [Docker](https://www.docker.com/)
- Your editor or IDE should have support for [dev containers](https://containers.dev/)
- A database client like [DBeaver](https://dbeaver.io/) is recommended for inspecting the database (optional)

### 🔑 Environment variables

Create a `.env` file in the project root by copying the example file:

```bash
cp .env.example .env
```

Then fill in the values with your own credentials. The `DATABASE_URL` should follow this format:

```
DATABASE_URL=postgresql://DATABASE_USER:DATABASE_PASSWORD@db:5432/DATABASE_NAME
```

Note that `db` is the hostname — it refers to the PostgreSQL Docker service and should not be changed.

### 🚀 Running the app

To get started, first clone this repository and move to the project directory:

```bash
git clone git@github.com:sayheylaura/plant-your-day.git
```

```bash
cd plant-your-day
```

This app is containerized with Docker and uses a dev container. Open the project in your editor or IDE and run the "Reopen/Rebuild in Container" command (or the equivalent command).

Then, to get the FastAPI server up and running, run these commands in your editor's integrated terminal:

1. Move to the backend directory:

```bash
cd backend
```

2. Activate the Python virtual environment:

```bash
source .venv/bin/activate
```

3. Run the FastAPI server:

```bash
fastapi dev app/main.py --host 0.0.0.0 --port 8000
```

You should now be able to access the API at `http://localhost:8000`, and the Swagger UI at `http://localhost:8000/docs`.

4. Seed the database (first time only):

```bash
python seed_db.py
```

This will create some plants in the database for you to play with. This is only necessary the first time you run the app.

If you're using DBeaver or a similar tool, once the app is running, you can connect to the database using the credentials from your `.env` file at `localhost:5432`.

## ✨ Feedback & Suggestions

If you have any suggestions/feedback or find any bugs, feel free to open an issue!

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
