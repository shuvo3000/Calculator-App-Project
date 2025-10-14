import tkinter as tk
from math import sqrt

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("700x800")
        self.root.configure(bg="#0A0A0A")
        self.root.resizable(False, False)

        self.expression = ""
        self.memory = 0
        self.input_text = tk.StringVar()
        self.result_shown = False

        self.create_display()
        self.create_buttons()

    # --- Display ---
    def create_display(self):
        entry = tk.Entry(
            self.root,
            textvariable=self.input_text,
            font=("Segoe UI", 24),
            bg="#5E6468",
            fg="white",
            bd=0,
            justify="right",
        )
        entry.pack(ipady=20, pady=10, fill="x")

    # --- Buttons ---
    def create_buttons(self):
        buttons = [
            ["MC", "MR", "M+", "M−", "MS"],
            ["%", "CE", "C", "⌫"],
            ["1/x", "x²", "√x", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["+/-", "0", ".", "="],
        ]


        for row in buttons:
            frame = tk.Frame(self.root, bg="#1E1E1E")
            frame.pack(expand=True, fill="both")

            for btn in row:
                action = lambda x=btn: self.click(x)

                # --- Color Logic ---
                if btn in ["+", "-", "×", "÷"]:
                    bg_color = "#FF9500"     # Orange (operator buttons)
                    fg_color = "white"
                    active_bg = "#FFA733"
                elif btn in ["="]:
                    bg_color = "#0CEE63"     # Light gray top buttons
                    fg_color = "black"
                    active_bg = "#BEBEBE"
                elif btn in ["MC", "MR", "M+", "M−", "MS", "%", "CE", "C", "⌫", "1/x", "x²", "√x"]:
                    bg_color = "#A5A5A5"     # Light gray top buttons
                    fg_color = "black"
                    active_bg = "#BEBEBE"
                else:
                    bg_color = "#333333"     # Dark gray for numbers
                    fg_color = "white"
                    active_bg = "#505050"

                # --- Create Button ---
                button = tk.Button(
                    frame,
                    text=btn,
                    font=("Segoe UI", 16, "bold"),
                    bg=bg_color,
                    fg=fg_color,
                    activebackground=active_bg,
                    activeforeground=fg_color,
                    relief="ridge",
                    bd=0,
                    command=action,
                    height=2,
                    width=6,
                )#.pack(side="left", expand=True, fill="both", padx=2, pady=2)
                        # --- Hover effect bindings ---
                button.bind("<Enter>", lambda e, b=button: b.config(bg="white", fg="black"))
                button.bind("<Leave>", lambda e, b=button, bg=bg_color, fg=fg_color: b.config(bg=bg, fg=fg))

                # --- Place button ---
                button.pack(side="left", expand=True, fill="both", padx=2, pady=2)

    def click(self, key):
        # --- Clear and control keys ---
        if key in ["C", "CE"]:
            self.expression = ""
            self.result_shown = False
        elif key == "⌫":
            self.expression = self.expression[:-1]
        elif key == "=":
            self.equal()
            print(self.result_shown )
            return
        elif key == "+/-":
            self.toggle_sign()
        elif key == "√x":
            self.square_root()
        elif key == "x²":
            self.square()
        elif key == "1/x":
            self.reciprocal()
        elif key == "%":
            self.percentage()
        elif key == "M+":
            self.memory_add()
        elif key == "M−":
            self.memory_subtract()
        elif key == "MR":
            self.memory_recall()
        elif key == "MC":
            self.memory_clear()
        elif key == "MS":
            self.memory_store()
        else:
            # --- main input logic ---
            symbol = self.convert_symbol(key)

            if self.result_shown:
                # if result was just shown and user presses a number or dot → start new expression
                if symbol.isdigit() or symbol == ".":
                    self.expression = symbol
                else:
                    # if user presses an operator → continue with last result
                    self.expression += symbol
                self.result_shown = False
            else:
                self.expression += symbol

        # --- update display ---
        self.input_text.set(self.expression)


    # --- Helper Functions ---
    def convert_symbol(self, key):
        mapping = {"×": "*", "÷": "/"}
        return mapping.get(key, key)
    
    def equal(self):
        try:
            global expression
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
            self.result_shown = True  # ✅😁 Mark result displayed
        except:
            self.input_text.set("Error")
            self.expression = ""
            self.result_shown = False

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
        except:
            self.expression = "Error hoice!"

    def toggle_sign(self):
        if self.expression:
            if self.expression.startswith("-"):
                self.expression = self.expression[1:]
            else:
                self.expression = "-" + self.expression

    def square_root(self):
        try:
            value = eval(self.expression)
            self.expression = str(sqrt(value))
        except:
            self.expression = "Error"

    def square(self):
        try:
            value = eval(self.expression)
            self.expression = str(value ** 2)
        except:
            self.expression = "Error"

    def reciprocal(self):
        try:
            value = eval(self.expression)
            self.expression = str(1 / value)
        except:
            self.expression = "Error"

    def percentage(self):
        try:
            value = eval(self.expression)
            self.expression = str(value / 100)
        except:
            self.expression = "Error"

    # --- Memory Functions ---
    def memory_add(self):
        try:
            self.memory += float(eval(self.expression))
        except:
            pass

    def memory_subtract(self):
        try:
            self.memory -= float(eval(self.expression))
        except:
            pass

    def memory_recall(self):
        self.expression = str(self.memory)

    def memory_clear(self):
        self.memory = 0

    def memory_store(self):
        try:
            self.memory = float(eval(self.expression))
        except:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap(r"_icons\cal_icon.ico")
    app = Calculator(root)
    root.mainloop()
