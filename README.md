# Plant your day 🪴

This is a simple app to help you keep track of your plants and their care (the real kind, not the ones you buy from the store 🌿)

I'm using this project to learn Python, FastAPI and Vue. It's a work in progress, so expect things to change and break.

## 💥 Tech stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Vue](https://vuejs.org/) with [TypeScript](https://www.typescriptlang.org/)
- [TailwindCSS](https://tailwindcss.com/)

## 👩‍💻 Getting started

### 📦 Prerequisites

- [Docker](https://www.docker.com/)
- Your editor or IDE should have support for [dev containers](https://containers.dev/)

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

## ✨ Feedback & Suggestions

If you have any suggestions/feedback or find any bugs, feel free to open an issue!

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
