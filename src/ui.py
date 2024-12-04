import sys
import time
from colorama import Fore, Style


def print_centered(text, width=40):
    print()
    print("=" * width)
    print(text.center(width))
    print("=" * width)


def print_text_centered(text, width=100):
    print(text.center(width))


def print_line(width):
    print("=" * width)

def print_header(text):
    print(Fore.YELLOW + Style.BRIGHT + f"{text}" + Style.RESET_ALL)

def print_success(text):
    print(Fore.GREEN + f"{text}" + Style.RESET_ALL)

def print_error(text):
    print(Fore.RED + "\033[4m" + f"{text}" + "\033[0m" + Style.RESET_ALL)


def get_dish_name():
    return input(Fore.CYAN + "\nEnter the name of the dish: " + Fore.RESET).strip()

def loading_animation():
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.25)


def progress_bar(iterable, total, prefix='', length=50):
    for i, _ in enumerate(iterable, 1):
        percent = (i / total) * 100
        filled_length = int(length * i // total)
        bar = '█' * filled_length + '-' * (length - filled_length)
        sys.stdout.write(f'\r{prefix} |{bar}| {percent:.1f}%')
        sys.stdout.flush()
        time.sleep(0.05)  
    sys.stdout.write('\n')  