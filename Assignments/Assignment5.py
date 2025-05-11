
trainer_name = "y/n"
pokemon_team = ["Panflam", "Igellaver", "Glumanda"]
inventory = []
inventory_limit = 5

locations = {
    "Pallet Town": {
        "description": "Your hometown. Professor Oak lives here.",
        "items": [{"name": "Poké Ball", "type": "tool"}, {"name": "Potion", "type": "healing", "uses": 1}],
        "east": "Route 1"
    },
    "Route 1": {
        "description": "A grassy path where wild Pokémon appear.",
        "items": [{"name": "Berry", "type": "food"}, {"name": "Antidote", "type": "healing", "uses": 1}],
        "west": "Pallet Town",
        "north": "PokéCenter",
        "east": "Viridian Forest"
    },
    "PokéCenter": {
        "description": "A place to heal your Pokémon and rest.",
        "items": [{"name": "Super Potion", "type": "healing", "uses": 2}],
        "south": "Route 1"
    },
    "Viridian Forest": {
        "description": "A dark forest full of bug-type Pokémon.",
        "items": [{"name": "Rare Candy", "type": "boost"}],
        "west": "Route 1"
    }
}

current_location = "Pallet Town"

def show_location():
    loc = locations[current_location]
    print(f"\nYou are at {current_location}.")
    print(loc["description"])

    directions = [d for d in ["north", "south", "east", "west"] if d in loc]
    if directions:
        print("You can go: " + ", ".join(directions))

    if loc["items"]:
        print("Items here:")
        for item in loc["items"]:
            print(f" - {item['name']}")
        print("You can type: pickup [item], examine [item]")
    else:
        print("No items are visible here.")

def show_inventory():
    print("\nYour inventory:")
    if not inventory:
        print(" - It's empty.")
    else:
        for item in inventory:
            uses = f" (uses: {item['uses']})" if "uses" in item else ""
            print(f" - {item['name']}{uses}")
        print("You can type: use [item], drop [item], examine [item]")

def show_team():
    print(f"\n{trainer_name}'s Pokémon Team:")
    for poke in pokemon_team:
        print(f" - {poke}")

def help_menu():
    print("\nAvailable commands:")
    print("- inventory       → show items in your bag")
    print("- team            → show your Pokémon")
    print("- pickup [item]   → pick up an item")
    print("- drop [item]     → drop an item")
    print("- use [item]      → use an item")
    print("- examine [item]  → learn about an item")
    print("- go [direction]  → move to another place")
    print("- help            → show commands again")
    print("- quit            → exit game")

def pick_up(item_name):
    loc = locations[current_location]
    for item in loc["items"]:
        if item["name"].lower() == item_name.lower():
            if len(inventory) >= inventory_limit:
                print("Your bag is full. Drop something first.")
                return
            inventory.append(item)
            loc["items"].remove(item)
            print(f"You picked up the {item['name']}.")
            return
    print("That item isn’t here.")

def drop(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            inventory.remove(item)
            locations[current_location]["items"].append(item)
            print(f"You dropped the {item['name']}.")
            return
    print("You don’t have that item.")

def use(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            if item["type"] == "healing":
                print(f"You used {item['name']} to heal your Pokémon.")
                item["uses"] -= 1
                if item["uses"] <= 0:
                    inventory.remove(item)
                    print(f"{item['name']} is now used up.")
            elif item["type"] == "boost":
                print(f"You used {item['name']}. Your Pokémon feel stronger.")
                inventory.remove(item)
            else:
                print(f"You used the {item['name']}, but nothing happened.")
            return
    print("You don’t have that item.")

def examine(item_name):
    for item in inventory + locations[current_location]["items"]:
        if item["name"].lower() == item_name.lower():
            print(f"{item['name']} is a {item['type']} item.")
            return
    print("You don’t see that item.")

def move(direction):
    global current_location
    if direction in locations[current_location]:
        current_location = locations[current_location][direction]
        show_location()
    else:
        print("You can’t go that way.")

print("Welcome to the Pokémon Text Adventure!")
print(f"You are Trainer {trainer_name}.")
show_team()
show_location()
help_menu()

while True:
    command = input("\nWhat would you like to do? > ").strip().lower()
    if command == "quit":
        print("Game exited. See you next time!")
        break
    elif command == "inventory":
        show_inventory()
    elif command == "team":
        show_team()
    elif command.startswith("pickup "):
        pick_up(command[7:])
    elif command.startswith("drop "):
        drop(command[5:])
    elif command.startswith("use "):
        use(command[4:])
    elif command.startswith("examine "):
        examine(command[8:])
    elif command.startswith("go "):
        move(command[3:])
    elif command == "help":
        help_menu()
    else:
        print("Unknown command. Type 'help' to see a list of available commands.")

