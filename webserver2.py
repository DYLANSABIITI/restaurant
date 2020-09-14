from flask import Flask, render_template, redirect, request, url_for
from fakeMenuItems import restaurant, restaurants, item, items
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///restaurant.db"

db = SQLAlchemy(app)

class restaurants(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique=True, nullable=False)

class items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    course = db.Column(db.String(20), unique=True, nullable=False)
    restaurants_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))






@app.route("/")
@app.route("/restaurants")
def showRestaurants():
    return render_template("restaurants.html", restaurant=restaurant, restaurants=restaurants, items=items, item=item)

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
    return render_template("menu.html", restaurant=restaurant, items=items)

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
    return  render_template("deletemenuitem.html", restaurant_id=restaurant_id, items=items) 



if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000) 