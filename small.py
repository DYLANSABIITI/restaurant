from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rest.db'


db = SQLAlchemy(app)

class Rest(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(20), nullable=False)
    menu = db.relationship('Item', backref='menu', lazy=True)

    def __repr__(self):
        return f"Restaurant name('{self.name}')"


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.String(8), nullable=False)
    course = db.Column(db.String(250), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('rest.id'), nullable=False)
    

    def __repr__(self):
        return f"item('{self.name}), description({self.description}), price({self.price}), course({self.course})"