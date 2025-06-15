from pyjokes.jokes_cs import jokes_cs
import pyjokes
import cowsay
from termcolor import colored
import pyfiglet

title = pyfiglet.figlet_format("Dev Joke", font="slant")
print(colored(title, 'cyan'))

joke = pyjokes.get_joke(language='en', category='all')

print(colored("Here's a joke for you:", 'green'))
print()

cowsay.dragon(colored(joke, 'yellow'))