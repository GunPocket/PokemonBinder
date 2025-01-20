from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PokemonCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    serial = db.Column(db.String(20), nullable=False)
    type = db.Column(db.String(20), nullable=False)  # Pokemon, Trainer, Energy
    quantity = db.Column(db.Integer, nullable=False, default=1)
    price_min = db.Column(db.Float, nullable=True)  # Apenas o preço mínimo
    last_updated = db.Column(db.DateTime, nullable=True)  # Data da última alteração
