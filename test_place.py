#!/usr/bin/python3
from models import storage
from models.place import Place

# Create a new Place
new_place = Place()
new_place.city_id = "4b457e66-c7c8-4f63-910f-fd91c3b7140b"
new_place.user_id = "4f3f4b42-a4c3-4c20-a492-efff10d00c0b"
new_place.name = "Lovely place"
new_place.number_rooms = 3
new_place.number_bathrooms = 1
new_place.max_guest = 6
new_place.price_by_night = 120
new_place.latitude = 37.773972
new_place.longitude = -122.431297
storage.new(new_place)
storage.save()
print(f"New Place: {new_place.id}")

# Retrieve all Place objects
all_places = storage.all(Place)
print(f"All Places: {len(all_places.keys())}")
for place in all_places.values():
    print(place)
