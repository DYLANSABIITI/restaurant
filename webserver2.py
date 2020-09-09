from flask import Flask, render_template
from fakeMenuItems import restaurant

app = Flask(__name__)

@app.route("/")
@app.route("/restaurants")
def showRestaurants():
    return render_template("restaurants.html",  restaurant=restaurant)

@app.route("/restaurants/new")
def newRestaurant():
    return render_template("newRestaurant.html")

@app.route("/restaurants/restaurant_id/edit")
def editRestaurant():
    return render_template("editRestaurants.html", restaurants=restaurant_id) 

@app.route("/restaurants/restaurant_id/delete")
def deleteRestaurant():
    return render_template("deleteRestaurants.html", restaurants=restaurant_id) 

#Menu item
@app.route("/restaurants/restaurant_id/restaurants/restaurant_id/menu")
def showMenu():
    return render_template("menu.html")

@app.route("/restaurants/restaurant_id/menu/new")
def newMenuItem():
    return render_template("newmenuitem.html", restaurants=restaurant_id) 

@app.route("/restaurants/restaurant_id/menu/menu_id/edit")
def editMenuItem():
    return render_template("editmenuItem.html", restaurants=restaurant_id) 

@app.route("/restaurants/restaurant_id/menu/menu_id/delete")
def deleteMenuItem():
    return  render_template("deletemenuitem.html", restaurants=restaurant_id) 



if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)