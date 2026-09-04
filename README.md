# Cafe & Wifi API

A Flask REST API that serves data about cafes in Kaunas, Lithuania (wifi
availability, sockets, seating, coffee price, etc.) from a SQLite database.

## Features

- `GET /` - renders a simple welcome page (`templates/index.html`).
- `GET /random` - returns a single random cafe as JSON.
- `GET /all` - returns every cafe in the database as JSON, sorted by name.
- SQLite database (`instance/cafes.db`) accessed through Flask-SQLAlchemy,
  with a `Cafe` model covering name, map URL, image URL, location, seat
  count, wifi/sockets/toilet/call availability, and coffee price.
- `seed_data.py` populates the database with 14 real cafes from Kaunas.

## How to Run

1. Create and activate a virtual environment.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. (Optional, first run only) Seed the database with sample cafes:
   ```
   python seed_data.py
   ```
4. Start the server:
   ```
   python main.py
   ```
5. Visit `http://127.0.0.1:5000/` in a browser, or hit `/random` and `/all`
   directly to get JSON data.

## Known Issues / Limitations

- Only read (`GET`) endpoints are implemented. Create, update, and delete
  routes are stubbed as comments in `main.py` and not yet written.
- No input validation, authentication, or error handling (e.g. `/random`
  will raise an error if the cafes table is empty).
- `requirements.txt` is UTF-16 encoded (artifact of how it was generated),
  which is unusual but still parses fine with `pip install -r`.

## What I Learned

- Setting up Flask-SQLAlchemy with the newer `Mapped`/`mapped_column`
  typed declarative style instead of the older `db.Column` syntax.
- Converting a SQLAlchemy model instance to JSON with a reusable
  `to_dict()` method that iterates over `self.__table__.columns`.
- Using `db.session.execute(db.select(...))` with `.scalars().all()` to
  fetch rows in SQLAlchemy 2.x style, instead of the legacy `Model.query`
  API.
