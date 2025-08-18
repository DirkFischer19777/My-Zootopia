import json

def load_data():
  """ Loads a JSON file """
  with open("animals_data.json", "r") as handle:
        return json.load(handle)


def print_animals(data):
    """Iterates through animals and prints selected info"""
    for animal in data:
        # Name
        if "name" in animal:
            print(f"Name: {animal['name']}")

        # Diet
        diet = animal.get("characteristics", {}).get("diet")
        if diet:
            print(f"Diet: {diet}")

        # Location (first in list)
        locations = animal.get("locations")
        if locations and len(locations) > 0:
            print(f"Location: {locations[0]}")

        # Type
        type_ = animal.get("characteristics", {}).get("type")
        if type_:
            print(f"Type: {type_}")

        print()  # Leerzeile zwischen den Tieren


if __name__ == "__main__":
    animals = load_data()
    if animals:
        print_animals(animals)