from colorprint.printer import uprint
from colorprint.unicolor import *
def printall():
    printfore()
    printback()

def printmode():
    print("Show Mode:")
    uprint("MODE_NORMAL\n", mode=MODE_NORMAL)\
        ("MODE_BLINK\n", mode=MODE_BLINK)\
        ("MODE_BOLD\n", mode=MODE_BOLD)\
        ("MODE_HIDE\n", mode=MODE_HIDE)\
        ("MODE_INVERT\n", mode=MODE_INVERT)\
        ("MODE_UNDERLINE\n", mode=MODE_UNDERLINE)

def printfore():
    print("Show foreground color.")
    uprint("FOREGROUND_BLACK\n", fore=FOREGROUND_BLACK)
    uprint("FOREGROUND_DARKBLUE\n", fore=FOREGROUND_DARKBLUE)
    uprint("FOREGROUND_DARKGREEN\n", fore=FOREGROUND_DARKGREEN)
    uprint("FOREGROUND_DARKSKYBLUE\n", fore=FOREGROUND_DARKSKYBLUE)
    uprint("FOREGROUND_DARKRED\n", fore=FOREGROUND_DARKRED)
    uprint("FOREGROUND_DARKPINK\n", fore=FOREGROUND_DARKPINK)
    uprint("FOREGROUND_DARKYELLOW\n", fore=FOREGROUND_DARKYELLOW)
    uprint("FOREGROUND_DARKWHITE\n", fore=FOREGROUND_DARKWHITE)
    uprint("FOREGROUND_DARKGRAY\n", fore=FOREGROUND_DARKGRAY)
    uprint("FOREGROUND_BLUE\n", fore=FOREGROUND_BLUE)
    uprint("FOREGROUND_GREEN\n", fore=FOREGROUND_GREEN)
    uprint("FOREGROUND_SKYBLUE\n", fore=FOREGROUND_SKYBLUE)
    uprint("FOREGROUND_RED\n", fore=FOREGROUND_RED)
    uprint("FOREGROUND_PINK\n", fore=FOREGROUND_PINK)
    uprint("FOREGROUND_YELLOW\n", fore=FOREGROUND_YELLOW)
    uprint("FOREGROUND_WHITE\n", fore=FOREGROUND_WHITE)

def printback():
    print("Show background color.")
    uprint("BACKGROUND_DARKBLUE\n", back=BACKGROUND_DARKBLUE)
    uprint("BACKGROUND_DARKGREEN\n", back=BACKGROUND_DARKGREEN)
    uprint("BACKGROUND_DARKSKYBLUE\n", back=BACKGROUND_DARKSKYBLUE)
    uprint("BACKGROUND_DARKRED\n", back=BACKGROUND_DARKRED)
    uprint("BACKGROUND_DARKPINK\n", back=BACKGROUND_DARKPINK)
    uprint("BACKGROUND_DARKYELLOW\n", back=BACKGROUND_DARKYELLOW)
    uprint("BACKGROUND_DARKWHITE\n", back=BACKGROUND_DARKWHITE)
    uprint("BACKGROUND_DARKGRAY\n", back=BACKGROUND_DARKGRAY)
    uprint("BACKGROUND_BLUE\n", back=BACKGROUND_BLUE)
    uprint("BACKGROUND_GREEN\n", back=BACKGROUND_GREEN)
    uprint("BACKGROUND_SKYBLUE\n", back=BACKGROUND_SKYBLUE)
    uprint("BACKGROUND_RED\n", back=BACKGROUND_RED)
    uprint("BACKGROUND_PINK\n", back=BACKGROUND_PINK)
    uprint("BACKGROUND_YELLOW\n", back=BACKGROUND_YELLOW)
    uprint("BACKGROUND_WHITE\n", back=BACKGROUND_WHITE)
    uprint("BACKGROUND_WHITE\n", back=BACKGROUND_WHITE)
    uprint("BACKGROUND_WHITE\n", back=BACKGROUND_WHITE)
