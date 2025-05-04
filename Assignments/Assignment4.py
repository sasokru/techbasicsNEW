print('This is a quiz of a different kind! :) ')


QUIZ_QUESTIONS = [
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
            "a": ("I like to do most of the research.", "Ravenclaw"),
            "b": ("I make sure everyone’s doing well.", "Hufflepuff"),
            "c": ("I like taking the lead.", "Gryffindor"),
            "d": ("I prefer to work alone.", "Slytherin")
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
        "question": "What do you think would be your favorite magical subject?",
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

HOUSE_DESCRIPTIONS = {
    "Gryffindor": "You are brave and daring, with a strong sense of justice.",
    "Ravenclaw": "You are wise and creative, always seeking knowledge.",
    "Hufflepuff": "You are loyal and hardworking, with a kind heart.",
    "Slytherin": "You are ambitious and resourceful, striving for greatness."
}

def ask_question(q_data, number):
    print(f"Question {number}: {q_data['question']}")
    for key, (text, _) in q_data["options"].items():
        print(f"{key}) {text}")

    answer = input("Your answer (a/b/c/d): ").strip().lower()

    while answer not in q_data["options"]:
        answer = input("Invalid input. Please choose a, b, c, or d: ").strip().lower()

    selected_house = q_data["options"][answer][1]
    print(f"You chose: {q_data['options'][answer][0]} ({selected_house})\n")
    return selected_house

def main():
    print("🧙 Welcome to Hogwarts! (Yes, Leuphana was just a fever dream.)")
    print("Answer the questions to see which house you belong to!\n")

    points = {
        "Gryffindor": 0,
        "Ravenclaw": 0,
        "Hufflepuff": 0,
        "Slytherin": 0
    }

    for i, question in enumerate(QUIZ_QUESTIONS, start=1):
        house = ask_question(question, i)
        points[house] += 1

    final_house = max(points, key=points.get)

    print("🧙 The Sorting Hat is thinking...")
    print("...almost choking on my butterbeer...")
    print("...nervous laughter...")
    print(f"\n🎉 Congratulations! You belong to {final_house.upper()}!")
    print(HOUSE_DESCRIPTIONS[final_house])


if __name__ == "__main__":
    main()
