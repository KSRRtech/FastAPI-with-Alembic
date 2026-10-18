# FastAPI with Alembic: Notes API

A beginner-friendly Notes API built with **FastAPI**, **SQLAlchemy** and **SQLite**, with database changes managed by **Alembic**. This is the companion code for the CodeTickle tutorials below.

## Read the tutorials

- [FastAPI, SQLAlchemy and Alembic: The Quick Guide](https://codetickle.wordpress.com/2026/10/19/fastapi-sqlalchemy-and-alembic-the-quick-guide/): the short version, in four steps
- [Build Your First Notes App with FastAPI, SQLAlchemy and Alembic](https://codetickle.wordpress.com/2026/10/17/build-your-first-notes-app-with-fastapi-sqlalchemy-and-alembic/): the full walkthrough, with every line explained

## What's inside

| File | What it is |
| --- | --- |
| `main.py` | The Notes API, saving notes to a SQLite database |
| `CRUD.py` | The first version, which keeps notes in a Python list (lost on restart) |
| `database.py` | The database connection, sessions and the `Base` class |
| `models.py` | The `Note` table: `id`, `title`, `content` and an optional `category` |
| `alembic/`, `alembic.ini` | Alembic setup and migration files |
| `hello.py` | A first Python warm-up script |

## Endpoints

| Method | Path | What it does |
| --- | --- | --- |
| GET | `/notes` | List all notes |
| POST | `/notes` | Create a note |
| GET | `/notes/{note_id}` | Get one note |
| PUT | `/notes/{note_id}` | Update a note |
| DELETE | `/notes/delete/{note_id}` | Delete a note |

## Run it locally

You need Python 3.10 or newer.

```bash
git clone https://github.com/KSRRtech/FastAPI-with-Alembic.git
cd FastAPI-with-Alembic
python -m venv .venv
.venv\Scripts\activate
pip install "fastapi[standard]" sqlalchemy alembic
alembic upgrade head
fastapi dev main.py
```

On Mac or Linux, activate the environment with `source .venv/bin/activate` instead.

`alembic upgrade head` creates the `notes.db` file and its table. Then open http://127.0.0.1:8000/docs to try every endpoint in your browser.

## Changing the database

Whenever you change `models.py`, create and apply a migration:

```bash
alembic revision --autogenerate -m "describe your change"
alembic upgrade head
```

Read the new file in `alembic/versions/` before you apply it. To undo the last migration, run `alembic downgrade -1`.

## Author

Sai K, [CodeTickle](https://codetickle.wordpress.com)
