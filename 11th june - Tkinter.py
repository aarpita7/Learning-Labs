# Import the Tkinter module
import tkinter as tk
from tkinter import messagebox

# Tkinter is the standard GUI (Graphical User Interface) library for Python.
# It is included with Python and works on Windows, MacOS, and Linux.
# Tkinter provides an easy way to create simple GUI applications.

# Create the main application window
root = tk.Tk()

# The Tk() function initializes the main window of the application.
# This window is the main container for all the widgets.

# Set the title of the main window
root.title("Tkinter App")

# The title() method sets the title of the window, which appears at the top of the window frame.

# Set the dimensions of the main window
root.geometry("300x200")

# The geometry() method sets the size of the window. The format is "widthxheight".

# Define the function that will be called when the button is clicked
def on_button_click():
    # The messagebox.showinfo function displays a simple message box with an OK button.
    # It takes two arguments: the title of the message box and the message to display.
    messagebox.showinfo("Hello!", "Button clicked!")

# Create a label widget
label = tk.Label(root, text="Welcome Arpita!", font=("Helvetica", 16))

# The Label widget is used to display text or images.
# The first argument to Label is the parent widget (in this case, 'root').
# The 'text' parameter sets the text to display, and 'font' sets the font style and size.

# Add the label to the main window
label.pack(pady=20)

# The pack() method adds the widget to the window and manages its placement.
# The pady parameter adds vertical padding (space) around the widget.

# Create a button widget
button = tk.Button(root, text="Click here", command=on_button_click)

# The Button widget is used to create a clickable button.
# The 'command' parameter specifies the function to call when the button is clicked.

# Add the button to the main window
button.pack(pady=10)

# The pack() method is used again to add the button to the window and manage its placement.
# The pady parameter adds vertical padding around the button.

# Start the Tkinter event loop
root.mainloop()

# The mainloop() method starts the Tkinter event loop.
# This loop waits for events (like button clicks) and updates the GUI accordingly.
# The application will remain open and responsive until the user closes the window.
