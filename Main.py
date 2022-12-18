import random, os, time, ctypes, keyboard, pyfiglet, cursor
from slowprint.slowprint import slowprint as sp
from colorama import Fore, init
init(convert=True)


cursor.hide()


os.system("mode con: cols=70 lines=15")


start = "F9"
cont = "F10"
random_time = [1, 2, 3]
hotkeys = ["w", "a", "s", "d", "space"]
stop = "F8"


def center(var:str, space:int=None):
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())


class ANM():
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        ctypes.windll.kernel32.SetConsoleTitleW("[ANM] ~ Kalju#6942")
        bnum = pyfiglet.figlet_format("ANM", font="sans")
        banner = Fore.LIGHTRED_EX + bnum + Fore.RESET
        print(center(banner))
        sp(" " * 21 + f"Press {Fore.LIGHTRED_EX}{start}{Fore.RESET} To Start Anti-Afk", 0.3)
        keyboard.add_hotkey(start, lambda: self.start_anti_afk())
        keyboard.wait()


    def start_anti_afk(self):
        print("\n")
        sp(" " * 24 + f"Started {Fore.LIGHTRED_EX}Anti-Afk{Fore.RESET}", 0.3)
        keyboard.unhook_all_hotkeys()
        while True:
            if keyboard.is_pressed(stop):
                self.stop_anti_afk()
                break
            key = random.choice(hotkeys)
            keyboard.press_and_release(key)
            time.sleep(random.choice(random_time))
            

    def stop_anti_afk(self):
        keyboard.unhook_all_hotkeys()
        print("\n")
        sp(" " * 24 + f"Stopped {Fore.LIGHTRED_EX}Anti-Afk{Fore.RESET}", 0.3)
        time.sleep(5)
        ANM()


anm = ANM()
