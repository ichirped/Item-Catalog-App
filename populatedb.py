from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Category, Base, Item, User
 
engine = create_engine('sqlite:///catalogwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

user1 = User(name="Bhoomi", email="bhoomipvyas@gmail.com", picture="myimage.jpg", id=1)
session.add(user1)
session.commit()

#Snowboarding
snowboarding = Category(name = "Snowboarding", user = user1)

session.add(snowboarding)
session.commit()


item1 = Item(title = "Snowboard", description = "Best for any terrain and conditions", category = snowboarding, user = user1)

session.add(item1)
session.commit()


#Soccer
soccer = Category(name = "Soccer", user = user1)

session.add(soccer)
session.commit()


item1 = Item(title = "Soccer Cleats", description = "The shoes", category = soccer, user = user1)

session.add(item1)
session.commit()

item2 = Item(title = "Jersey", description = "The shirt", category = soccer, user = user1)

session.add(item2)
session.commit()


#Baseball
bball = Category(name = "Baseball", user = user1)

session.add(bball)
session.commit()

item1 = Item(title = "Bat", description = "The bat", category = bball, user = user1)

session.add(item1)
session.commit()

item2 = Item(title = "Jersey", description = "The shirt", category = bball, user = user1)

session.add(item2)
session.commit()


#Rock Climbing
rclimb = Category(name = "Rock Climbing", user = user1)

session.add(rclimb)
session.commit()


#Hockey
hockey = Category(name = "Hockey", user = user1)

session.add(hockey)
session.commit()

item1 = Item(title = "Hockey Stick", description = "The stick", category = hockey, user = user1)

session.add(item1)
session.commit()

print "added items to catalog!"