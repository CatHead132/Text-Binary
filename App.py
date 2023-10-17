import tkinter as tk
from PIL import Image, ImageTk
import pyperclip

def text_to_binary():
    text = input_text.get()
    binary_text = ' '.join(format(ord(char), '08b') for char in text)
    output_label.config(text="Copied Binary: " + binary_text)
    pyperclip.copy(binary_text)

def binary_to_text():
    binary_text = input_text.get()
    binary_list = binary_text.split()
    text = ''.join(chr(int(binary, 2)) for binary in binary_list)
    output_label.config(text="Copied Text: " + text)
    pyperclip.copy(text)

def toggle_top_most():
    is_topmost = topmost_var.get()
    window.attributes('-topmost', is_topmost)

# Create the main window
window = tk.Tk()
window.title("Text-Binary Converter")

# Set the icon for the application using a PNG image
img = Image.open('icon.png')
icon = ImageTk.PhotoImage(img)
window.iconphoto(False, icon)

# Create a label and entry (textbox) widget
input_label = tk.Label(window, text="Enter text or binary:")
input_text = tk.Entry(window)

# Create two buttons for conversion
to_binary_button = tk.Button(window, text="To Binary", command=text_to_binary)
to_text_button = tk.Button(window, text="To Text", command=binary_to_text)

# Create a label to display the result
output_label = tk.Label(window, text="Result will be shown here")

# Create a Checkbutton to toggle "always on top"
topmost_var = tk.BooleanVar()
topmost_checkbox = tk.Checkbutton(window, text="Always on Top", variable=topmost_var, command=toggle_top_most)

# Place widgets on the window
input_label.pack()
input_text.pack()
to_binary_button.pack()
to_text_button.pack()
output_label.pack()
topmost_checkbox.pack()

# Start the GUI event loop
window.mainloop()
