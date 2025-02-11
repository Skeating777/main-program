import sys
import random
import os
import shutil


def create_path(directory, chord_type="r"):
    if chord_type == "r":
        chord_type = random.randint(0, 2)
    if chord_type == 0:
        chord_type = "Major"
    elif chord_type == 1:
        chord_type = "Minor"
    elif chord_type == 2:
        chord_type = "Maj7"
    key = random.randint(97, 103)
    path = "Text/" + directory + "/" + chord_type + "/" + (chr(key))
    try:
        path = "Text/" + directory + "/" + chord_type + "/" + (chr(key))
    except FileNotFoundError:
        create_path(directory, chord_type)
    return path


def random_chord(directory):
    command = input("Press Enter to begin or specify chord by type (ex: major, minor, major7). Use r to "
                    " return to home.  ")
    if command == "":
        while True:
            chord_type = random.randint(0, 2)
            if chord_type == 0:
                chord_type = "Major"
            elif chord_type == 1:
                chord_type = "Minor"
            elif chord_type == 2:
                chord_type = "Maj7"
            key = random.randint(97, 103)
            path = create_path(directory, chord_type)
            path = "Text/Library/" + chord_type + "/" + (chr(key))
            prompt = path + "/prompt.txt"
            diagram = path + "/diagram.txt"
            text = open(prompt, "r")
            print(text.read())
            text.close()
            command = input("Press Enter for diagram.")
            if command == "":
                text = open(diagram, "r")
                print(text.read())
                text.close()
            command = input("Press Enter for next chord, s to save this chord (can be deleted later), or use r to "
                            "return to home. ")
            if command.lower() == "r":
                return False
            elif command.lower() == "s":
                new_name = chr(key) + chord_type + "diagram.txt"
                save_path = "Text/Saved/" + new_name
                if os.path.exists(save_path):
                    print("Chord is already saved!")
                else:
                    with open(save_path, "w") as file:
                        shutil.copyfile(diagram, save_path)

    elif command.lower() == "major":
        chord_type = "Major"
        while True:
            key = random.randint(97, 103)
            path = "Text/Library/" + chord_type + "/" + (chr(key))
            prompt = path + "/prompt.txt"
            diagram = path + "/diagram.txt"
            text = open(prompt, "r")
            print(text.read())
            text.close()
            command = input("Press Enter for diagram.")
            if command == "":
                text = open(diagram, "r")
                print(text.read())
                text.close()
            command = input("Press Enter for next chord, s to save this chord (can be deleted later), or use r to "
                            "return to home.")
            if command.lower() == "r":
                return False
            elif command.lower() == "s":
                new_name = chr(key) + chord_type + "diagram.txt"
                save_path = "Text/Saved/" + new_name
                if os.path.exists(save_path):
                    print("Chord is already saved!")
                else:
                    with open(save_path, "w") as file:
                        shutil.copyfile(diagram, save_path)

    elif command.lower() == "minor":
        chord_type = "Minor"
        while True:
            key = random.randint(97, 103)
            path = "Text/Library/" + chord_type + "/" + (chr(key))
            prompt = path + "/prompt.txt"
            diagram = path + "/diagram.txt"
            text = open(prompt, "r")
            print(text.read())
            text.close()
            command = input("Press Enter for diagram.")
            if command == "":
                text = open(diagram, "r")
                print(text.read())
                text.close()
            command = input("Press Enter for next chord, s to save this chord (can be deleted later), or use r to "
                            "return to home. ")
            if command.lower() == "r":
                return False
            elif command.lower() == "s":
                new_name = chr(key) + chord_type + "diagram.txt"
                save_path = "Text/Saved/" + new_name
                if os.path.exists(save_path):
                    print("Chord is already saved!")
                else:
                    with open(save_path, "w") as file:
                        shutil.copyfile(diagram, save_path)
                        print("Chord saved!")

    elif command.lower() == "major7":
        chord_type = "Maj7"
        while True:
            key = random.randint(97, 103)
            path = "Text/Library/" + chord_type + "/" + (chr(key))
            prompt = path + "/prompt.txt"
            diagram = path + "/diagram.txt"
            text = open(prompt, "r")
            print(text.read())
            text.close()
            command = input("Press Enter for diagram.")
            if command == "":
                text = open(diagram, "r")
                print(text.read())
                text.close()
            command = input("Press Enter for next chord, s to save this chord (can be deleted later), or use r to "
                            "return to home. ")
            if command.lower() == "r":
                return False
            elif command.lower() == "s":
                new_name = chr(key) + chord_type + "diagram.txt"
                save_path = "Text/Saved/" + new_name
                if os.path.exists(save_path):
                    print("Chord is already saved!")
                else:
                    with open(save_path, "w") as file:
                        shutil.copyfile(diagram, save_path)
    if command.lower() == "r":
        return False


def add_chord():
    key = input("Please enter the key of the chord (Case Sensitive: A, B, C, etc.)")
    type = input("Please enter the chord type (Case Sensitive: Minor, Major, Maj7)")
    path = "Text/Library/" + type + "/" + key
    diagram = path + "/diagram.txt"
    text = open(diagram, "r")
    print(text.read())
    text.close()
    command = input("This one? (Y/N)")
    if command.lower() == "n":
        add_chord()
    elif command.lower() == "y":
        new_name = key + type + "diagram.txt"
        save_path = "Text/Saved/" + new_name
        if os.path.exists(save_path):
            print("Chord is already saved!")
        else:
            with open(save_path, "w") as file:
                shutil.copyfile(diagram, save_path)


def saved():
    while True:
        command = input("Press Enter to begin. Press a and Enter to manually add a chord. Use r to"
                        " return to home.  ")
        if command.lower() == "a":
            while True:
                add_chord()
                command = input("Add another? (Y/N)")
                if command.lower() == "n":
                    saved()
                saved_list = os.listdir(path="Text/Saved")
        elif command == "":
            saved_list = os.listdir(path="Text/Saved")
            if len(saved_list) == 0:
                print("")
                print("No chords saved!")
                command = input("Press a and Enter to manually add a chord. Use r to"
                                " return to saved options.  ")
                if command.lower() == "a":
                    add_chord()
                elif command.lower() == "r":
                    saved()
            while True:
                index = 0
                while index <= len(saved_list):
                    if index < 0:
                        command = input("Beginning of list! Continue? (Y/N)  ")
                        if command.lower() == "y":
                            index = 0
                        elif command.lower() == "n":
                            saved()
                    elif index >= len(saved_list):
                        command = input("End of list! Continue? (Y/N)  ")
                        if command.lower() == "y":
                            index = len(saved_list) - 1
                        elif command.lower() == "n":
                            saved()
                    text = open("Text/Saved/" + saved_list[index], "r")
                    print(text.read())
                    text.close()
                    command = input("Enter + or - to see next or previous. Enter d to delete chord. Use r to return "
                                    "to saved options.  ")
                    if command == "+":
                        index += 1
                    elif command == "-":
                        index -= 1
                    elif command.lower() == "r":
                        saved()
                    elif command.lower() == "d":
                        command = input("Are you sure you want to delete this chord? (Chord will need to be re-added "
                                        "manually or by chance in random feature) (Y/N)  ")
                        if command.lower() == "y":
                            directory = "Text/Saved/"
                            file = saved_list[index]
                            if index == len(saved_list):
                                index -= 1
                            path = os.path.join(directory, file)
                            os.remove(path)
                            saved_list = os.listdir(path="Text/Saved")
                            if len(saved_list) == 0:
                                command = input("No more chords! Continue? (Y/N)  ")
                                if command.lower() == "y":
                                    saved()
                                elif command.lower() == "n":
                                    return False
                        elif command.lower() == "n":
                            saved()
        elif command.lower() == "r":
            home()



def info():
    text = open("Text/Example.txt", "r")
    print(text.read())
    text.close()
    command = input("Use r to return to home.")

def home():
    while True:
        text = open("Text/Banner.txt", "r")
        print(text.read())
        text.close()
        print("")
        print("Practice at your own pace and create your own study materials with this interactive chord library!")
        print("")
        command = input("Enter 1 to access random chords/2 for saved chords/3 for help and info/q to exit  ")
        if command == '1':
            random_chord("Library")
        elif command == '2':
            saved()
        elif command == '3':
            info()
        elif command.lower() == 'q':
            sys.exit()

home()

