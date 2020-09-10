from flask import Flask, render_template, redirect
from fakeMenuItems import restaurant, restaurants, item, items

app = Flask(__name__)

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
@app.route("/restaurants/<int:restaurant_id>/restaurants/restaurant_id/menu")
def showMenu(restaurant_id):
    return render_template("menu.html")

@app.route("/restaurants/<int:restaurant_id>/menu/new")
def newMenuItem(restaurant_id):
    return render_template("newmenuitem.html", restaurant_id=restaurant_id) 

@app.route("/restaurants/<int:restaurant_id>/menu/menu_id/edit")
def editMenuItem(restaurant_id):
    return render_template("editmenuItem.html", restaurant_id=restaurant_id) 

@app.route("/restaurants/<int:restaurant_id>/menu/menu_id/delete")
def deleteMenuItem(restaurant_id):
    return  render_template("deletemenuitem.html", restaurant_id=restaurant_id) 



if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)