import cowsay
from colorama import Fore, Style
from more_jokes import get_programming_joke, get_custom_joke

def tell_joke(joke):
    print(Fore.CYAN + "Here's a joke for you:" + Style.RESET_ALL)
    cowsay.cow(joke)

def main():
    joke1 = get_programming_joke()
    tell_joke(joke1)

    print()  # Leerzeile

    joke2 = get_custom_joke()
    tell_joke(joke2)

if __name__ == "__main__":
    main()