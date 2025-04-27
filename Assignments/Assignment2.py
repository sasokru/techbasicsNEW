quiz_questions = [
    {
        "question": "What would you do if you found a lost wallet?",
        "options": {
            "a": ("Return it to its owner immediately.", "Hufflepuff"),
            "b": ("Keep it. Finders keepers!", "Slytherin"),
            "c": ("Check for ID and decide based on the situation.", "Ravenclaw"),
            "d": ("Ignore it and walk away.", "Gryffindor")
        }
    },
    {
        "question": "At Seminars here at Uni, which role do you like to take in group projects?",
        "options": {
            "a": ("I like to do most of the research to ensure the liability of our sources.", "Ravenclaw"),
            "b": ("I like to make sure that everybody is working and feeling their best.", "Hufflepuff"),
            "c": ("I prefer to take the lead and to manage our tasks.", "Gryffindor"),
            "d": ("I like to do my own part of the project mainly by myself.", "Slytherin"),
        }
    },
    {
        "question": "What is your favorite magical creature?",
        "options": {
            "a": ("Phoenix", "Gryffindor"),
            "b": ("Basilisk", "Slytherin"),
            "c": ("Bowtruckle", "Hufflepuff"),
            "d": ("Hippogriff", "Ravenclaw")
        }
    },
    {
        "question": "Which quality do you value most in yourself?",
        "options": {
            "a": ("Bravery", "Gryffindor"),
            "b": ("Intelligence", "Ravenclaw"),
            "c": ("Ambition", "Slytherin"),
            "d": ("Loyalty", "Hufflepuff")
        }
    },
    {
        "question": "What do you expect will be your favorite magical subject at Hogwarts?",
        "options": {
            "a": ("Defense Against the Dark Arts", "Gryffindor"),
            "b": ("Potions", "Slytherin"),
            "c": ("Herbology", "Hufflepuff"),
            "d": ("Charms", "Ravenclaw")
        }
    },
    {
        "question": "Choose an element.",
        "options": {
            "a": ("Fire", "Slytherin"),
            "b": ("Earth", "Hufflepuff"),
            "c": ("Air", "Ravenclaw"),
            "d": ("Water", "Gryffindor")
        }
    }
]

house_points = {
    "Gryffindor": 0,
    "Ravenclaw": 0,
    "Hufflepuff": 0,
    "Slytherin": 0
}

print("🧙 Welcome to Hogwarts! Yes, Leuphana was indeed just a fever dream. At Hogwarts we started launching our College.")
print("Answer the following questions to find out which Hogwarts house you belong to.\n")

for i, q in enumerate(quiz_questions, 1):
    print(f"Question {i}: {q['question']}")
    for key, value in q["options"].items():
        print(f"{key}) {value[0]}")

    answer = input("Your answer (a/b/c/d): ").strip().lower()

    while answer not in q["options"]:
        answer = input("Invalid choice! Please select a valid option (a/b/c/d): ").strip().lower()

    selected_house = q["options"][answer][1]
    house_points[selected_house] += 1
    print(f"You chose: {q['options'][answer][0]} ({selected_house})\n")

sorted_house = max(house_points, key=house_points.get)

print("🧙 The Sorting Hat has made its decision! 🧙")
print("excited silence")
print("...drumroll...")
print("...almost choking on my butterbeer...")
print("...nervous laughter...")
print(f"Congratulations! You belong to {sorted_house.upper()}!\n")

house_descriptions = {
    "Gryffindor": "You are brave and daring, with a strong sense of justice.",
    "Ravenclaw": "You are wise and creative, always seeking knowledge.",
    "Hufflepuff": "You are loyal and hardworking, with a kind heart.",
    "Slytherin": "You are ambitious and resourceful, striving for greatness."
}
print(house_descriptions[sorted_house])
