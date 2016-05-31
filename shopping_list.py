from os.path import isfile

def remove_item(idx):
    try:
        index = int(idx) - 1
        item = shopping_list.pop(index)
    except:
        item = idx
        try:
            shopping_list.remove(item)
        except:
            print("This isn't in your list.")
            show_list()
            return
    print("Removed: {}.".format(item))

def show_help():
    print("\nSeparate each item with a comma.")
    print("Type DONE to quit, SHOW to see the current list, REMOVE to delete an d item and HELP to get this message")

def load_list():
    if isfile(file_name):
        print("Grocery list found.")
        for f in tuple(open(file_name, 'r')):
            f = f.split(": ")
            if len(f) > 1:
                f.pop(0)
                f[-1] = f[-1][:-1]
                shopping_list.append(": ".join(f))
        return show_list(return_only=True)

def show_list(return_only=False):
    if return_only:
        display = ""
    else:
        display = "\nHere's your list:\n"

    if len(shopping_list) > 0:
        for count, item in enumerate(shopping_list):
            display += "{}: {}\n".format(count + 1, item)
    else:
        display = "Your shopping list is empty right now."

    if return_only:
        return display
    else:
        print(display)

def save_list():
    show_list()
    with open(file_name, "w") as text_file:
        text_file.write(show_list(return_only=True))
    print("It has been saved.")

shopping_list = []
file_name = "grocery_list" + ".txt"

current_list = load_list()
if current_list:
    print(current_list, end="")
else:
    print("Give me a list of things you want to shop for.")
show_help()

while True:
    new_stuff = input("> ")
    command = new_stuff.upper()

    if command == "DONE":
        save_list()
        break
    elif command == "HELP":
        show_help()
    elif command == "SHOW":
        show_list()
    elif command.startswith("REMOVE"):
        if not new_stuff[7:]:
            show_list()
            idx = input("Which item? Tell me the number.")
        else:
            idx = new_stuff[7:]
        remove_item(idx)
    else:
        new_list = new_stuff.split(",")
        index = ""
        if len(shopping_list) > 0:
            index = input("Add this at a certain spot? Press enter for the end of the list, "
                          "or give me a number. This is the current list:\n" + show_list(return_only=True))
        if index:
            spot = int(index) - 1
            for item in new_list:
                shopping_list.insert(spot, item.strip())
                spot += 1
        else:
            for item in new_list:
                shopping_list.append(item.strip())
