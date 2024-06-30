main_arr = []

def add_new_recipe(name):
    import random
    hash = random.getrandbits(128)
    print("hash value: %010x" % hash)
    global this_recipe
    this_recipe = []
    this_recipe.append(name)
    this_recipe.append(hash)
    main_arr.append(this_recipe)
    print(f"Recipe '{name}' added with ID: {hash}")
    # print(this_recipe)

def render_recipes_list():
    print("Recipes list: ")
    for recipe in main_arr:
        print(f"ID: {recipe[1]}, Name: {recipe[0]}")

control = True
while control == True:
    recipe_name = input("Input name of the dish: (is you want to exit input 'STOP' or 'EXIT') ")
    if recipe_name == "STOP":
        control = False
        break
    else:
        add_new_recipe(recipe_name);
        print(main_arr)

# render_recipes_list()