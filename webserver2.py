from flask import Flask

# import CRUD Operations from Lesson 1
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

@app.route("/restaurants", methods=["GET"])
def restaurants():
    restaurants = session.query(Restaurant).all()
    output += "<html><body>"
    for restaurant in restaurants:
        output += restaurant.name
        output += "</br>"
        output += "<a href='#'>Edit </a>"
        output += "</br>"
        output += "<a href='#'>Delete</a>"
    output += "</body></html>"


if __name__ == "__main__":
    try:
        app.run(debug=True)
        print('Web server running...open localhost:8080/restaurants in your browser')
    except KeyboardInterrupt:
        print('^C received, shutting down server')