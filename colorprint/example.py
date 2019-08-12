from colorprint.printer import uprint
from colorprint.unicolor import *
def printall():
    printmode()
    printfore()
    printback()

def printmode():
    print("Show Mode:")
    uprint("MODE_NORMAL", mode=MODE_NORMAL,end="\n")\
        ("MODE_BLINK",mode=MODE_BLINK)\
        ("MODE_BOLD",mode=MODE_BOLD)\
        ("MODE_HIDE",mode=MODE_HIDE)\
        ("MODE_INVERT",mode=MODE_INVERT)\
        ("MODE_UNDERLINE",mode=MODE_UNDERLINE)

def printfore():
    print("Show foreground color.")
    uprint("FOREGROUND_BLACK", fore=FOREGROUND_BLACK,end="\n")\
        ("FOREGROUND_DARKBLUE", fore=FOREGROUND_DARKBLUE)\
        ("FOREGROUND_DARKGREEN", fore=FOREGROUND_DARKGREEN)\
        ("FOREGROUND_DARKSKYBLUE", fore=FOREGROUND_DARKSKYBLUE)\
        ("FOREGROUND_DARKRED", fore=FOREGROUND_DARKRED)\
        ("FOREGROUND_DARKPINK", fore=FOREGROUND_DARKPINK)\
        ("FOREGROUND_DARKYELLOW", fore=FOREGROUND_DARKYELLOW)\
        ("FOREGROUND_DARKWHITE", fore=FOREGROUND_DARKWHITE)\
        ("FOREGROUND_DARKGRAY", fore=FOREGROUND_DARKGRAY)\
        ("FOREGROUND_BLUE", fore=FOREGROUND_BLUE)\
        ("FOREGROUND_GREEN", fore=FOREGROUND_GREEN)\
        ("FOREGROUND_SKYBLUE\n", fore=FOREGROUND_SKYBLUE,end="")\
        ("FOREGROUND_RED\n", fore=FOREGROUND_RED)
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


if __name__ == "__main__":
    printall()