import tkinter as tk

# Define the first page
class FirstPage:
    def __init__(self, master):
        self.master = master
        self.button = tk.Button(self.master, text="Open Second Page", command=self.open_second_page)
        self.button.pack()

    def open_second_page(self):
        # Create a new Toplevel window
        self.second_window = tk.Toplevel(self.master)
        self.second_window.title("Second Page")
        self.second_window.geometry("400x300")

        # Add widgets to the new window
        self.label = tk.Label(self.second_window, text="Welcome to the Second Page!")
        self.label.pack()

# Define the second page
class SecondPage:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(self.master, text="Welcome to the Second Page!")
        self.label.pack()

# Create the main application window
root = tk.Tk()

# Create the first page object
first_page = FirstPage(root)

# Run the main event loop
root.mainloop()
