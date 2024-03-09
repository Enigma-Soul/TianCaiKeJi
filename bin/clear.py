from os import system
def clear():
    ok = False
    try:
        system("cls")
        ok = True
    except :
        pass
    if not ok:
        system("clear")