def color(color,text):
    if color == "red":
        return "\033[31m"+text+"\033[0m"
    elif color == "green":
        return "\033[32m"+text+"\033[0m"
    elif color == "yellow":
        return "\033[33m"+text+"\033[0m"
    elif color == "blue":
        return "\033[34m"+text+"\033[0m"
    elif color == "magenta":
        return "\033[35m"+text+"\033[0m"
    elif color == "cyan":
        return "\033[31m"+text+"\033["
    else:
        return None