def getText(name):
    try:
        file = open(name)
        text = file.read()
        file.close()
        return text
    except FileNotFoundError:
        print("The text could not be found. (FileNotFoundError)")