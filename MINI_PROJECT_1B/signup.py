

import tkinter as tk

# Create the tkinter window
window = tk.Tk()
window.title('Sign Up')

# Create a frame for the sign-up form
signup_frame = tk.Frame(window, bd=2, relief='groove')
signup_frame.pack(padx=20, pady=20)

# Create labels and entry fields for the username and password
username_label = tk.Label(signup_frame, text='Username:')
username_label.grid(row=0, column=0, sticky='e')
username_entry = tk.Entry(signup_frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)
password_label = tk.Label(signup_frame, text='Password:')
password_label.grid(row=1, column=0, sticky='e')
password_entry = tk.Entry(signup_frame, show='*')
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Define the available colors
colors = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple']

# Create a frame for the password display
password_frame = tk.Frame(signup_frame, bd=2, relief='groove')
password_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create a canvas to display the password
password_canvas = tk.Canvas(password_frame, width=500, height=100)
password_canvas.pack()

# Define a function to add a color to the password
def add_color(color):
    password_list.clear()
    password_list.append(color)
    update_password()

# Define a function to update the password display
def update_password():
    # Clear the current password display
    password_canvas.delete('all')
    # Draw the colors in the password
    x, y = 10, 10
    for color in password_list:
        if color == 'Red':
            password_canvas.create_rectangle(x, y, x+100, y+80, fill='#ff0000')
        elif color == 'Green':
            password_canvas.create_rectangle(x, y, x+100, y+80, fill='#00ff00')
        elif color == 'Blue':
            password_canvas.create_rectangle(x, y, x+100, y+80, fill='#0000ff')
        elif color == 'Yellow':
            password_canvas.create_rectangle(x, y, x+100, y+80, fill='#ffff00')
        elif color == 'Orange':
            password_canvas.create_rectangle(x, y, x+100, y+80, fill='#ffa500')
        elif color == 'Purple':
            password_canvas.create_rectangle(x, y, x+100, y+80, fill='#800080')
        x += 120

# Define a function to clear the password
def clear_password():
    password_list.clear()
    update_password()

# Create buttons for each color
for i, color in enumerate(colors):
    button = tk.Button(signup_frame, width=20, height=20, command=lambda c=color: add_color(c))
    if color == 'Red':
        button.config(bg='#ff0000')
    elif color == 'Green':
        button.config(bg='#00ff00')
    elif color == 'Blue':
        button.config(bg='#0000ff')
    elif color == 'Yellow':
        button.config(bg='#ffff00')
    elif color == 'Orange':
        button.config(bg='#ffa500')
    elif color == 'Purple':
        button.config(bg='#800080')
    button.grid(row=3, column=i, padx=5, pady=5)


def submit_form():
    # Get the entered username and password
    username = username_entry.get()
    password = ''.join(password_list)
    # Print the values to the console (for testing purposes)
    print(f'Username: {username}')
    print(f'Password: {password}')
    # Clear the form
    username_entry.delete(0, tk.END)
    clear_password()

#Create a button to submit the form
submit_button = tk.Button(signup_frame, text='Submit', command=submit_form)
submit_button.grid(row=4, column=0, columnspan=6, padx=5, pady=5)

#Create a list to hold the password colors
password_list = []

#Run the main loop
window.mainloop()