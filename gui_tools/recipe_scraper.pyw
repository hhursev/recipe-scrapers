from recipe_scrapers import scrap_me
from tkinter import *
from tkinter import messagebox

# The function called to run download the URL
def download(event):
    url = url_entry.get()   # Get the URL from the box
    try:
        recipie = scrap_me(url) # Attempt to get it
    except KeyError:
        messagebox.showerror("Error", "Invalid URL")   # If it is not supported throw an error 
    # Format the result and save it to a file
    with open('recipie.txt', 'a', encoding='utf-8') as file:
        text = "Title: {}\nTotal Time: {}\nIngredients:\n\t{}\nInstructions:\n{}".format(
            recipie.title(),
            recipie.total_time(),
            "\n\t".join(recipie.ingredients()),
            recipie.instructions())
        result.config(text=text)
        file.write(text)


root = Tk()
root.title("Recipe scraper")

frame = Frame(root, relief='flat', borderwidth=25)

Label(frame, text="URL: ").grid(row=2, column = 1, columnspan=1)
url_entry = Entry(frame, width=50)
url_entry.grid(row=2, column=2, columnspan=3)

run_button = Button(frame, text="Run")
run_button.bind("<Button-1>", download)
run_button.grid(row=4, column = 1, columnspan=4, pady=10)

Label(frame, text="Result: ").grid(row=5, column = 1, columnspan=4, pady=10)
result = Label(frame, text="", justify=LEFT)
result.grid(row=6, column = 1, columnspan=4, pady=10)

frame.pack()

root.mainloop()
