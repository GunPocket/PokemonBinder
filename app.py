from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokemon_cards.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)


class PokemonCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    serial = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(20), nullable=False)  # Pokémon, Trainer, Energy
    quantity = db.Column(db.Integer, default=1)
    price_min = db.Column(db.Float, nullable=True)
    last_updated = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<PokemonCard {self.name} ({self.serial})>"


@app.route('/')
def index():
    type_filter = request.args.get('type')
    search_query = request.args.get('search')
    sort_by = request.args.get('sort_by')

    query = PokemonCard.query

    if type_filter:
        query = query.filter_by(type=type_filter)
    if search_query:
        query = query.filter(PokemonCard.name.contains(search_query))

    # Adicionando lógica de ordenação
    if sort_by == 'type':
        query = query.order_by(PokemonCard.type)
    elif sort_by == 'name':
        query = query.order_by(PokemonCard.name)
    elif sort_by == 'price_min_asc':
        query = query.order_by(PokemonCard.price_min)
    elif sort_by == 'price_min_desc':
        query = query.order_by(PokemonCard.price_min.desc())

    cards = query.all()
    return render_template('index.html', cards=cards)


@app.route('/add_card', methods=['GET', 'POST'])
def add_card():
    if request.method == 'POST':
        name = request.form['name']
        serial = request.form['serial']
        card_type = request.form['type']
        quantity = int(request.form['quantity'])
        price_min = request.form.get('price_min')

        if price_min:
            price_min = float(price_min)
        else:
            price_min = None

        new_card = PokemonCard(
            name=name,
            serial=serial,
            type=card_type,
            quantity=quantity,
            price_min=price_min,
            last_updated=datetime.now()
        )

        db.session.add(new_card)
        db.session.commit()
        flash('Card added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_card.html')


@app.route('/delete_card/<int:card_id>', methods=['POST'])
def delete_card(card_id):
    card = PokemonCard.query.get_or_404(card_id)
    db.session.delete(card)
    db.session.commit()
    flash('Card deleted successfully!', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
