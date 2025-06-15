import cowsay
from colorama import Fore, Style
from jokes_more import get_joke

def tell_joke():
    joke = get_joke()
    print(Fore.CYAN + Style.BRIGHT)
    cowsay.trex(joke)
    print(Style.RESET_ALL)

if __name__ == "__main__":
    tell_joke()