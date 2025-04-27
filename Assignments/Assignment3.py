import random
import time

height = int(input("Enter the height of your book pages: "))
width = int(input("Enter the width of each page: "))
symbol = input("Enter a symbol to draw with (like *, #, ~): ")

page_symbols = ['.', ',', '`', ':', ';']
special_words = ["magic", "dream", "story", "adventure", "mystery"]

cover = "=" * (width * 2 + 7)
print(cover)

for row in range(height):
    left_page = ""
    right_page = ""
    for col in range(width):
        if random.randint(1, 7) == 1:
            left_page += symbol
            right_page += symbol
        else:
            left_page += random.choice(page_symbols)
            right_page += random.choice(page_symbols)

    if random.randint(1, height) == row + 1:
        word = random.choice(special_words)
        space_left = " " * ((width * 2 + 3 - len(word)) // 2)
        print(space_left + word + space_left)
    else:
        print(left_page + "     " + right_page)
    time.sleep(0.05)

print(cover)

print("\n📖 You opened a magical book of wonders! 📖")