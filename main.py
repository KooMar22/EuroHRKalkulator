# Import required modules
from tkinter import Frame, Label, Entry, Button, Tk, END


# Define fonts
MESSAGE_FONT = ("Arial", 12, "bold")
CURRENCY_FONT = ("Arial", 16, "bold")
NUMERIC_FONT = ("Arial", 16)
CLEAR_BTN_FONT = ("Arial", 15, "bold")


class CurrencyConverterApp():
    def __init__(self, window):
        """
        Initialization of CurrencyConverterApp object.
        This is the main Tkinter window.
        """
        self.window = window
        self.window.title("Markanov EuroHR Kalkulator")

        self.tecaj_euro_u_kune = 7.53450
        self.tecaj_kune_u_euro = 1 / self.tecaj_euro_u_kune

        self.current_input_currency = "EUR"
        self.current_output_currency = "HRK"

        # Frame and label for fixed currency exchange rate
        self.fixed_rate_frame = Frame(master=window, bg="red")
        self.fixed_rate_frame.grid(column=0, row=0, columnspan=3, sticky="ew")
        self.fixed_rate_label = Label(master=self.fixed_rate_frame,
                                         text=f"Markanov EuroHR Kalkulator\nFiksni tečaj konverzije:\n1 EUR = {self.tecaj_euro_u_kune}.",
                                         font=MESSAGE_FONT,
                                         bg="red", fg="white")
        self.fixed_rate_label.grid(column=0, row=0, padx=10, pady=10)

        # Bind the Key event to handle key presses
        self.window.bind("<Key>", self.on_key_press)

        # Frame and labels for displayed amounts
        self.currency_frame = Frame(master=window, bg="blue")
        self.currency_frame.grid(column=0, row=1, columnspan=3, sticky="ew", pady=10)

        self.input_currency_label = Label(
            master=self.currency_frame, text="From:", font=CURRENCY_FONT,
                                            bg="blue", fg="white")
        self.input_currency_label.grid(column=0, row=0, sticky="ew", padx=5)

        self.from_currency_label = Label(master=self.currency_frame,
                                        text=self.current_input_currency,
                                    font=CURRENCY_FONT, bg="blue", fg="white")
        self.from_currency_label.grid(column=2, row=0, sticky="ew", padx=5)

        self.output_currency_label = Label(
                                    master=self.currency_frame, text="To:",
                                    font=CURRENCY_FONT, bg="blue", fg="white")
        self.output_currency_label.grid(column=0, row=1, sticky="ew", padx=5)
        
        self.to_currency_label = Label(
                                    master=self.currency_frame,
                                    text=self.current_output_currency,
                                    font=CURRENCY_FONT, bg="blue", fg="white")
        self.to_currency_label.grid(column=2, row=1, sticky="ew", padx=5)

        self.entry_currency_text = Entry(master=self.currency_frame,
                                font=CURRENCY_FONT,
                                bg="blue", fg="white", justify="center", width=7)
        self.entry_currency_text.grid(column=1, row=0, padx=5, pady=5, sticky="nsew")
        self.entry_currency_text.bind("<KeyRelease>", self.update_converted_value)

        self.converted_value_label = Label(
                                master=self.currency_frame, text="",
                                font=CURRENCY_FONT,
                                bg="blue", fg="white")
        self.converted_value_label.grid(column=1, row=1, sticky="ew")

        # Frame and buttons for numerical values
        self.buttons_frame = Frame(master=window)
        self.buttons_frame.grid(column=0, row=2, columnspan=3)

        self.number_buttons = []
        for num in range(1, 10):
            button = Button(self.buttons_frame, text=str(num),
                               command=lambda n=num: self.update_input(str(n)),
                               font=NUMERIC_FONT, height=2, width=5)
            self.number_buttons.append(button)
            row, col = divmod(num - 1, 3)
            button.grid(column=col, row=row)

        self.zero_button = Button(master=self.buttons_frame, text="0",
                                     command=lambda: self.update_input("0"),
                                     font=NUMERIC_FONT, height=2, width=5)
        self.zero_button.grid(column=1, row=3)

        self.decimal_button = Button(master=self.buttons_frame, text=".",
                                        command=lambda: self.update_input("."),
                                        font=NUMERIC_FONT, height=2, width=5)
        self.decimal_button.grid(column=0, row=3)

        self.clear_button = Button(master=self.buttons_frame, text="C",
                                      command=self.clear_input,
                                      font=CLEAR_BTN_FONT, height=2, width=5)
        self.clear_button.grid(column=2, row=3)

        # Frame and buttons for currency buttons
        self.currency_buttons_frame = Frame(master=window)
        self.currency_buttons_frame.grid(column=0, row=3, columnspan=3)

        self.currency_buttons = []
        for currency in ["EUR > HRK", "HRK > EUR"]:
            button = Button(master=self.currency_buttons_frame, text=currency,
                               command=lambda c=currency: self.change_currency(c))
            self.currency_buttons.append(button)
            button.grid(column=len(self.currency_buttons) - 1, row=0)

        self.change_currency("EUR > HRK")

    def on_key_press(self, event):
        """
        Function for handling key presses
        """
        key = event.char
        if key.isdigit() or key == ".":
            self.update_input(key)

    def set_currency_style(self, bg_color, fg_color):
        """
        Configuring the style for chosen currency.
        """
        self.currency_frame.config(bg=bg_color)
        self.input_currency_label.config(bg=bg_color, fg=fg_color)
        self.from_currency_label.config(bg=bg_color, fg=fg_color)
        self.output_currency_label.config(bg=bg_color, fg=fg_color)
        self.to_currency_label.config(bg=bg_color, fg=fg_color)
        self.entry_currency_text.config(bg=bg_color, fg=fg_color)
        self.converted_value_label.config(bg=bg_color, fg=fg_color)

    def change_currency(self, new_currency):
        """
        Implementing the changing currency function and style change.
        """
        if new_currency == "EUR > HRK":
            self.set_currency_style("blue", "white")
            self.currency_buttons[0].config(bg="blue", fg="white")
            self.currency_buttons[1].config(bg="white", fg="black")
            self.current_input_currency = "EUR"
            self.current_output_currency = "HRK"

        elif new_currency == "HRK > EUR":
            self.set_currency_style("red", "white")
            self.currency_buttons[1].config(bg="red", fg="white")
            self.currency_buttons[0].config(bg="white", fg="black")
            self.current_input_currency = "HRK"
            self.current_output_currency = "EUR"

        self.update_currency_labels()
        self.from_currency_label.config(text=self.current_input_currency)
        self.to_currency_label.config(text=self.current_output_currency)
        self.converted_value_label.config(text="")

    def update_input(self, value):
        """
        Implementing the updating of input values while also handling decimal and
        limiting it to 2 digits.
        """
        current_input = self.entry_currency_text.get()
        
        # Don't add another decimal if already added
        if value == "." and "." in current_input:
            return
        
        if "." in current_input:
            _, decimal_part = current_input.split(".")
            if len(decimal_part) >= 2:
                return
            
        new_input = current_input + value
        self.entry_currency_text.delete(0, END)  # Clear the input field
        self.entry_currency_text.insert(0, new_input)  # Insert the new value
        self.update_converted_value()

    def clear_input(self):
        """
        Implementing the clear of input function.
        """
        self.entry_currency_text.delete(0, END)
        self.converted_value_label.config(text="")

    def update_converted_value(self):
        """
        Implementing the update of converted values.
        """
        input_value = self.entry_currency_text.get()
        try:
            value = float(input_value)
            if self.current_input_currency == "EUR":
                converted_value = value * self.tecaj_euro_u_kune
            else:
                converted_value = value * self.tecaj_kune_u_euro
            
            converted_value_rounded = round(converted_value, 2)
            self.converted_value_label.config(text=converted_value_rounded)
        except ValueError:
            self.entry_currency_text.config(text="")

    def update_currency_labels(self):
        """
        Implementing the update of currency labels when changing currency.
        """
        self.entry_currency_text.config(text="")
        self.converted_value_label.config(text="")


if __name__ == "__main__":
    window = Tk()
    app = CurrencyConverterApp(window)
    window.mainloop()