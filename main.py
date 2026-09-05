from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from dotenv import load_dotenv
import random
import os

load_dotenv()

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")

TRUTHY_FORM_VALUES = {"true", "1", "yes", "on"}


def parse_form_bool(field_name):
    """Return True if the named form field's value is one of TRUTHY_FORM_VALUES (case-insensitive)."""
    value = request.form.get(field_name, "")
    return value.strip().lower() in TRUTHY_FORM_VALUES

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"])
def random_cafe_finder():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all", methods=["GET"])
def all_cafe_finder():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search", methods=["GET"])
def search_cafe():
    location = request.args.get("location")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    all_cafes_in_location = result.scalars().all()
    if all_cafes_in_location:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes_in_location])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location!"}), 404

# HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=parse_form_bool("sockets"),
        has_toilet=parse_form_bool("toilet"),
        has_wifi=parse_form_bool("wifi"),
        can_take_calls=parse_form_bool("calls"),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    price_to_update = db.session.get(Cafe, cafe_id)
    if price_to_update is None:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    price_to_update.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"success": "Successfully updated the price."})

# HTTP DELETE - Delete Record

@app.route("/report-closed/<cafe_id>", methods=["GET","DELETE"])
def report_closed(cafe_id):
    cafe_to_delete = db.session.get(Cafe, cafe_id)
    if cafe_to_delete is None:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    user_api_key = request.args.get("api_key")
    if user_api_key != API_KEY:
        return jsonify(error={"Wrong API Key": "Make sure you used the correct API key."}), 404
    else:
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the cafe."})

if __name__ == '__main__':
    app.run(debug=True)
