import tkinter as tk
from tkinter import ttk

class BeautifulInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Beautiful Interface")
        self.root.geometry("400x300")

        # Creating a styled frame
        style = ttk.Style()
        style.configure("My.TFrame", background="#f0f0f0")
        self.frame = ttk.Frame(root, style="My.TFrame")
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Adding labels with custom fonts and colors
        title_label = ttk.Label(self.frame, text="Welcome to the Beautiful Interface", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=(0, 20))

        description_label = ttk.Label(self.frame, text="This is a sample text to demonstrate the design.", font=("Helvetica", 12))
        description_label.pack()

        # Creating a styled button
        style.configure("My.TButton", background="#4CAF50", foreground="white")
        self.button = ttk.Button(self.frame, text="Click Me", style="My.TButton")
        self.button.pack(pady=20)

        # Creating an entry with custom border color
        style.configure("My.TEntry", fieldbackground="#f0f0f0", bordercolor="#4CAF50")
        self.entry = ttk.Entry(self.frame, style="My.TEntry")
        self.entry.pack(pady=20)

        # Adding a separator
        separator = ttk.Separator(self.frame, orient="horizontal")
        separator.pack(fill=tk.X, pady=20)

        # Creating a custom-themed combobox
        self.combo_var = tk.StringVar()
        self.combo_var.set("Select an option")
        self.combobox = ttk.Combobox(self.frame, textvariable=self.combo_var, values=["Option 1", "Option 2", "Option 3"])
        self.combobox.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = BeautifulInterface(root)
    root.mainloop()