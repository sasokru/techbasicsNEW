my_file = open("week7.py")
content = my_file.read()
print(content)
my_file.close()

def read_fruits():
    dict = {}
    with open("fruits.csv") as f:
        items=line
        name = items