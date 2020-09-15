from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine



Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


engine = create_engine('sqlite:///restaurantsmenu.db')


Base.metadata.create_all(engine)


 
engine = create_engine('sqlite:///restaurantsmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()

#The cruDdy Crab
restaurant1 = Restaurant(name="The CRUDdy Crab", id=1)
session.add(restaurant1)
session.commit()

menu1 = MenuItem(name="Cheese Pizza", description="made with fresh cheese", price="$5.99", course="Entree", restaurant_id=1)
session.add(item1)
session.commit()

# The Blue Birgers
restaurant2 = Restaurant(name="Blue Burgers", id=2)
session.add(restaurant2)
session.commit()

menu2 = MenuItem(name="Chocolate Cake", description="made with Dutch Chocolate", price="$3.99", course="Dessert", restaurant_id=2)
session.add(item2)
session.commit()

#Taco Hut
restaurant3 = Restaurant(name="Taco Hut", id=3)
session.add(restaurant3)
session.commit()

menu3 = MenuItem(name="Caesar Salad", description="with fresh organic vegetables", price="$5.99", course="Entree", restaurant_id=3)
session.add(item3)
session.commit()


#other items
menu4= MenuItem(name="Iced Tea", description="with lemon", price="$.99", course="Beverage", restaurant_id=4)
session.add(item4)
session.commit()

menu5= MenuItem(name="Spinach Dip", description="creamy dip with fresh spinach", price="$1.99", course="Appetizer", restaurant_id=5)
session.add(item5)
session.commit()



