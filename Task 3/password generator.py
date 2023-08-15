import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=5)

        self.length_entry = tk.Entry(root, font=("Helvetica", 14))
        self.length_entry.pack(pady=5)

        self.complexity_label = tk.Label(root, text="Password Complexity:")
        self.complexity_label.pack(pady=5)

        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Medium")

        self.complexity_menu = tk.OptionMenu(root, self.complexity_var, "Low", "Medium", "High")
        self.complexity_menu.pack(pady=5)

        self.generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12), command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.password_display = tk.Label(root, text="", font=("Helvetica", 16))
        self.password_display.pack(pady=10)

    def generate_password(self):
        password_length = int(self.length_entry.get())
        complexity = self.complexity_var.get()

        if complexity == "Low":
            characters = string.ascii_letters
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits
        else:
            characters = string.ascii_letters + string.digits + string.punctuation

        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        self.password_display.config(text=generated_password)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
