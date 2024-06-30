# main_test_script.py
from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity

# Create a State
state = State(name="California")
state.save()

# Create a City
city = City(state_id=state.id, name="San Francisco")
city.save()

# Create a User
user = User(email="john@snow.com", password="johnpwd")
user.save()

# Create 2 Places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()

# Create 3 Amenities
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

# Link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# Link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

storage.save()

# Print places and their amenities
for place in [place_1, place_2]:
    print(f"Place: {place.name}")
    for amenity in place.amenities:
        print(f"  Amenity: {amenity.name}")

# Confirm place_amenity table entries
query = storage._DBStorage__session.query(place_amenity).all()
for row in query:
    print(f"Place ID: {row.place_id}, Amenity ID: {row.amenity_id}")
