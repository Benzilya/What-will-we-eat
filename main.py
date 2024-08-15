import sys
sys.path.append('G:/Programming/What will we eat')

import keyboard
import json
from configs import config

print(f"Password: {config.password}")

# end
main_arr = []
# Подключение к файлу со списком рецептов и чтение строк

try:
    with open("What will we eat/data/recipes.txt", "r", encoding="UTF-8") as f:
        recipes_read = json.loads(f.read())
        main_arr = recipes_read
except (json.JSONDecodeError, FileNotFoundError) as e:
    # Обработка ошибок
    print(f"Error: {e}")
# end

#Добавление рецепта в список/файл
def add_new_recipe(name, id):
    with open("What will we eat/data/recipes.txt","a+") as f:
        global main_arr
        this_recipe = {
            "id": id,
             "name": name,
             "structure" : []
        }
        main_arr.append(this_recipe)
        print(f"Recipe '{name}' added with ID: {id}")
        open_to_write()

def open_to_write():
    with open ("What will we eat/data/recipes.txt", "w", encoding="UTF-8") as f:
        json.dump(main_arr, f, ensure_ascii=False, indent=4)

# Отрисовка списка рецептов
def render_recipes_list():
    if len(main_arr) == 0:
        print("No recipes in the list. Add a new one please.")
        return
    else:
        print("Recipes list: ")
        for recipe in main_arr:
            print(f"ID: {recipe['id']}, Name: {recipe['name']}")
            if recipe['structure']:
                print(f"  Structure: {', '.join(recipe['structure'])}")

def add_structure(recipe):
    recipe_structure = []
    print('Please add the structure of the dish! To stop, type "stop" or press Esc.')
    while True:
        new_component = input("Add component: ").strip()
        if keyboard.is_pressed('esc'):
            print("You pressed Esc. Stopping the structure addition.")
            break
        if new_component.lower() == "stop":
            print('Adding structure is stopped')
            break
        recipe_structure.append(new_component)

    recipe['structure'] = recipe_structure
    print(f"Structure for recipe ID {recipe['id']}: {recipe_structure}")
    open_to_write()
    
# Вернуть все рецепты с их составами
def get_recipes():
    return main_arr

if __name__ == "__main__":

    greetings = print("""
    ******************************************************************************
    Hello, you can watch all the recipes in this program.                      *
    * If you want to want to start adding new recipes press 's' or 'start'.      *
    * If you want to see all the functions please add 'h' or 'help'.             *
    ******************************************************************************""")
    help_message = """
    _____________________________________HELP_____________________________________
    |'exit' - stop addind recipes                                                 |
    |'start', 's' - start adding recipes                                          |
    |'recipes', 'r' - show recipes list                                           |
    |'clear', 'c' - clear all recipes                                             |
    |'add structure', '+' - add structure of choosed recipe                       |
    |'clear structure', '-' - clear structure of choosed recipe                   |
    |_____________________________________________________________________________|
    """

    check = True
    while check == True:
        command = (input("Choose your action: ")).lower()
        if command.lower() in ["start", "s"]:
            break
        elif command.lower() in ["help", "h"]:
            print(help_message)
        elif command.lower() in ["clear", "c"]:
            id = 0
            main_arr = []
            open_to_write()
            print("All recipes cleared.")
            render_recipes_list()
        elif command.lower() == "exit":
            print("Goodbye!")
            sys.exit()
        elif command.lower() in ["recipes", "r"]:
            render_recipes_list()
        else:
            print("Unknown command. Please try again.")

    # Добавление нового рецепта
    reserved_commands = ["exit", "clear", "c", "start", "s", "help", "h", "recipes", "r"]
    id = len(main_arr)
    dish_structure = []
    control = True
    while control == True:
        recipe_name = (input("Input name of the dish: (If you want to exit input 'exit') -> ")).lower()
        if recipe_name in ["exit"]:
            control = False
            break
        elif recipe_name in ["clear", 'c']:
            id = 0
            main_arr = []
            open_to_write()
            print("All recipes cleared.")
            render_recipes_list()
            continue
        if recipe_name in reserved_commands:
            print("This name is reserved for a command. Please choose a different name.")
            continue
        else:
            add_new_recipe(recipe_name, id)
            current_recipe = main_arr[-1]
            id += 1
            add_structure(current_recipe)
            print(main_arr)

    render_recipes_list()