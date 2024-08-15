from tkinter import *
from main import get_recipes

root = Tk(className="button_click_label")
root.geometry("400x400")

message = StringVar()
message.set('You can check the list of recipes here')

l1 = Label(root, text="You can check the list of recipes here")

# Метка для отображения состава рецепта
structure_label = Label(root, text="")
structure_label.pack()

# Вывод списка рецептов
def press():
    recipes = get_recipes()
    l1.config(text="This is the list of recipes:\n" + "\n".join([f"ID: {recipe['id']}, Name: {recipe['name']}" for recipe in recipes]))
    b1.pack_forget()  # Удаляем кнопку из интерфейса

b1 = Button(root, text="clickhere", command=press)
b1.pack()

l1.pack()

root.mainloop()