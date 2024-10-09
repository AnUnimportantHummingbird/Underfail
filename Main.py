
print('''
┏┓╋┏┓╋╋╋╋┏┓╋╋╋╋╋┏━┓╋╋╋┏┓
┃┃╋┃┃╋╋╋╋┃┃╋╋╋╋╋┃┏┛╋╋╋┃┃
┃┃╋┃┣━┓┏━┛┣━━┳━┳┛┗┳━━┳┫┃
┃┃╋┃┃┏┓┫┏┓┃┃━┫┏┻┓┏┫┏┓┣┫┃
┃┗━┛┃┃┃┃┗┛┃┃━┫┃╋┃┃┃┏┓┃┃┗┓
┗━━━┻┛┗┻━━┻━━┻┛╋┗┛┗┛┗┻┻━┛
''')
#*Menu
print("Options:")
print("Play")
print("Story Mode")
print("Load")
print("Controls")
#
MenuChoice = []
#Prevents any error messages from occurring
while True:
    MenuChoice = input("What would you like to select: ")
    if MenuChoice == "Play" or MenuChoice == "play":
        print("This area is a possible work in progress.")
        break
    elif MenuChoice == "Story Mode" or MenuChoice == "story mode" or MenuChoice == "Story mode":
        print("This area is a work in progress.")
        break
    elif MenuChoice == "Load" or MenuChoice == "load":
        print("This feature has not been implemented yet.")
        break
    elif MenuChoice == "Load" or MenuChoice == "load":
        print("This area is a work in progress")
        break
    else:
        print("That option is not available. Try again.")