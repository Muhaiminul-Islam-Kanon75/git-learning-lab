# Git Learning Lab

Git Learning Lab is a lightweight browser-based practice tool for learning
common Git commands. It includes:

- An interactive quiz covering repository setup, staging, commits, pulls, and pushes
- A command simulator for `clone`, `init`, `status`, `add`, `commit`, and `push`
- A JSON API that powers the frontend

## Requirements

- Python 3.12 or later

## Install

Create and activate a virtual environment, then install the application
dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

For development and testing dependencies, use:

```bash
pip install -r requirements-dev.txt
```

## Run the Application

```bash
python3 -m app.main
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in a browser. The server
listens on `0.0.0.0:8000`, so it can also be reached from another machine or
container through the host's port 8000.

## Run with Docker

Build and start the application with:

```bash
docker build -t git-learning-lab .
docker run --rm -p 8000:8000 git-learning-lab
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/api/health` | Check that the server is running |
| `GET` | `/api/questions` | Return quiz questions |
| `POST` | `/api/quiz` | Grade answers sent as `{"answers": [...]}` |
| `POST` | `/api/simulate` | Simulate a command sent as `{"command": "status"}` |

## Run Tests

```bash
pytest
```
