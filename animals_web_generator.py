import json

def load_data():
  """ Loads a JSON file """
  with open("animals_data.json", "r") as handle:
        return json.load(handle)


def print_animals(data):
    """Iterates through animals and prints selected info"""
    output = ""
    for animal in data:
        # Name
        if "name" in animal:
            #print(f"Name: {animal['name']}")
            output += f"Name: {animal['name']}\n"

        # Diet
        diet = animal.get("characteristics", {}).get("diet")
        if diet:
            #print(f"Diet: {diet}")
            output += f"Diet: {diet}\n"

        # Location (first in list)
        locations = animal.get("locations")
        if locations and len(locations) > 0:
            #print(f"Location: {locations[0]}")
            output += f"Location: {locations[0]}\n"

        # Type
        type_ = animal.get("characteristics", {}).get("type")
        if type_:
            #print(f"Type: {type_}")
            output += f"Type: {type_}\n\n"
        if not type_:
            output += f"\n"


    return output

def read_html():
    # HTML-Datei einlesen
    with open("animals_template.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return html_content

def replace_placeholder(data):
    return html_input.replace("__REPLACE_ANIMALS_INFO__", data)

def save_data(data):
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(data)

if __name__ == "__main__":
    animals = load_data()
    output_string = print_animals(animals)
    html_input = read_html()
    html_output = replace_placeholder(output_string)
    save_data(html_output)
    print(html_output)
    print(output_string)