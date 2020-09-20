from flask import Flask, render_template, redirect, request, url_for
#from fakeMenuItems import restaurant, restaurants, item, items
from small import Rest, Item
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurants.db'


db = SQLAlchemy(app)

class Restaurants(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(20), nullable=False)
    menu = db.relationship('MenuItem', backref='menu', lazy=True)

    def __repr__(self):
        return f"Restaurant name('{self.name}')"


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.String(8), nullable=False)
    course = db.Column(db.String(250), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    

    def __repr__(self):
        return f"item('{self.name}), description({self.description}), price({self.price}), course({self.course})"

@app.route("/")
@app.route("/restaurants")
def showRestaurants():
    return render_template("restaurants.html", restaurant=Rest, restaurants=Restaurants, items=MenuItem, item=Item)

@app.route("/restaurants/new")
def newRestaurant():
    return render_template("newRestaurant.html")

@app.route("/restaurants/<int:restaurant_id>/edit")
def editRestaurant(restaurant_id):
    return render_template("editRestaurant.html", restaurant_id=restaurant_id)

@app.route("/restaurants/<int:restaurant_id>/delete")
def deleteRestaurant(restaurant_id):
    return render_template("deleteRestaurant.html", restaurant_id=restaurant_id) 

#Menu item
@app.route("/restaurant/<int:restaurant_id>/menu")
def showMenu(restaurant_id):
    return render_template("menu.html", restaurant=Rest, items=MenuItem)

@app.route("/restaurants/<int:restaurant_id>/menu/new")
def newMenuItem(restaurant_id):
    return render_template("newmenuitem.html", restaurant_id=restaurant_id) 

@app.route("/restaurants/<int:restaurant_id>/menu/menu_id/edit", methods=["POST", "GET"])
def editMenuItem(restaurant_id):
    if request.method == "POST":
        submit = request.form["submit"]
        return redirect(url_for("showMenu", values=submit))
    else:
        return render_template("editmenuItem.html", restaurant_id=restaurant_id) 

@app.route("/restaurants/<int:restaurant_id>/menu/menu_id/delete")
def deleteMenuItem(restaurant_id):
    return  render_template("deletemenuitem.html", restaurant_id=restaurant_id, items=MenuItem) 



if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)