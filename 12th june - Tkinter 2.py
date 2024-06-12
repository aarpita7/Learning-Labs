import tkinter as tk

def click():
    text= entry.get()
    global stext
    stext = text
    print(f'Text from textbox: {stext}')


root = tk.Tk()
root.title("Tkinter Text Entry ")

label = tk.Label(root, text="Enter text:")
label.pack(pady=10)


entry = tk.Entry(root, width=40)
entry.pack(pady=10)


button = tk.Button(root, text="Submit", command=click)
button.pack(pady=10)


root.mainloop()
