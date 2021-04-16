import tkinter as tk
import tkinter.font as tkFont
from model.os import addToClipBoard

def integer_checkbox_toggle(integer, password):
    password.set_has_integer(integer.get())


def upper_lower_checkbox_toggle(upper_lower, password):
    password.set_has_upper_lower_case(upper_lower.get())


def spec_char_checkbox_toggle(spec_char, password):
    password.set_has_spec_char(spec_char.get())


def transform_password_by_star(self_password):
    transformed_password = ""
    i = 0
    while i < len(self_password):
        print(i)
        transformed_password += "*"
        i += 1

    return transformed_password


def get_password_formated(self_password, hide_password):
    if hide_password == 1:
        return transform_password_by_star(self_password)
    else:
        return self_password


def on_click_generate_password(self_password, hide_password, formated_password, password):
    password.generate_password()
    self_password.set(password.get_password())
    formated_password.set(get_password_formated(password.get_password(), hide_password.get()))


def on_click_toggle_hide_password(self_password, formated_password):
    if self_password.get() == formated_password.get():
        formated_password.set(get_password_formated(self_password.get(), 1))
    else:
        formated_password.set(get_password_formated(self_password.get(), 0))


def on_click_copy_password(password, message):
    addToClipBoard(str(password.get()))
    message.set("Copied !")


def save_password():
    print("save_password")


class Window:
    def __init__(self, root, password):
        self.password = tk.StringVar()
        self.formated_password = tk.StringVar()
        self.formated_password.set(password.get_password())

        self.check_integer = tk.IntVar(value=password.get_has_integer())
        self.check_upper_lower = tk.IntVar(value=password.get_has_upper_lower_case())
        self.check_spec_char = tk.IntVar(value=password.get_has_spec_char())
        self.check_hide_password = tk.IntVar(value=password.get_hide_password())
        self.copied_message = tk.StringVar()

        def toggle_check_hide_password():
            password.toggle_hide_password()

        print(self.check_hide_password.get())
        # setting title
        root.title("Password generator")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(align_str)
        root.resizable(width=False, height=False)

        # style
        fg_white = "#333333"
        bg_grey = "#efefef"
        times_28 = tkFont.Font(family='Times', size=28)
        times_13 = tkFont.Font(family='Times', size=13)
        times_10 = tkFont.Font(family='Times', size=10)

        # app title
        title_label = tk.Label(root, font=times_28, fg=fg_white, justify="center", text="Password Generator")
        title_label.place(x=0, y=0, width=600, height=80)

        # checkbox for include integer
        integer_checkbox = tk.Checkbutton(root, font=times_13, fg=fg_white, justify="left", text="Add integer")
        integer_checkbox["variable"] = self.check_integer
        integer_checkbox["command"] = lambda: integer_checkbox_toggle(self.check_integer, password)
        integer_checkbox.place(x=80, y=80, width=222, height=30)

        # checkbox for shuffle lowercase and uppercase
        upper_lower_checkbox = tk.Checkbutton(root, font=times_13, fg=fg_white, justify="left",
                                              text="Add lower/uppercase")
        upper_lower_checkbox["variable"] = self.check_upper_lower
        upper_lower_checkbox["command"] = lambda: upper_lower_checkbox_toggle(self.check_upper_lower, password)
        upper_lower_checkbox.place(x=80, y=120, width=222, height=30)

        # checkbox for include special characters
        spec_char_checkbox = tk.Checkbutton(root, font=times_13, fg=fg_white, justify="left", text="Add special characteres")
        spec_char_checkbox["variable"] = self.check_spec_char
        spec_char_checkbox["command"] = lambda: spec_char_checkbox_toggle(self.check_spec_char, password)
        spec_char_checkbox.place(x=80, y=160, width=222, height=30)

        # minimum characters
        # default 6
        min_char_entry = tk.Entry(root, font=times_13, fg=fg_white, justify="center")
        min_char_entry.insert(0, "Min. character: (6 def)")
        min_char_entry.place(x=340, y=80, width=180, height=40)

        # maximum characters
        # default 13
        max_char_entry = tk.Entry(root, font=times_13, fg=fg_white, justify="center")
        max_char_entry.insert(0, "Max. character: (13 def)")
        max_char_entry.place(x=340, y=150, width=180, height=40)

        # button for generate the password
        btn_ft = tkFont.Font(family='Times', size=16)
        generate_button = tk.Button(root, bg="#efefef", font=btn_ft, fg="#000000", justify="center", text="Generate")
        generate_button["command"] = lambda: on_click_generate_password(self.password, self.check_hide_password, self.formated_password, password)
        generate_button.place(x=180, y=220, width=231, height=44)

        # title for the generated password
        generated_password_title_label = tk.Label(root, font=times_13, fg=fg_white, justify="center", text="Result generation")
        generated_password_title_label.place(x=0, y=320, width=600, height=32)

        # the generated password
        generated_password = tk.Label(root, font=times_13, fg=fg_white, justify="center")
        generated_password["textvariable"] = self.formated_password
        generated_password.place(x=0, y=400, width=600, height=30)

        # param for toggle hide password after generation
        hide_password_after_generation = tk.Checkbutton(root, font=times_10, fg=fg_white, justify="center", text="Hide after generation ?")
        hide_password_after_generation["variable"] = self.check_hide_password
        hide_password_after_generation["command"] = toggle_check_hide_password
        hide_password_after_generation.place(x=0, y=270, width=600, height=30)

        toggle_hide_password = tk.Button(root, font=times_10, bg=bg_grey, fg=fg_white, justify="center", text="Show")
        toggle_hide_password["command"] = lambda: on_click_toggle_hide_password(self.password, self.formated_password)
        toggle_hide_password.place(x=180, y=360, width=100, height=30)

        copy_password_button = tk.Button(root, font=times_10, bg=bg_grey, fg=fg_white, justify="center", text="Copy")
        copy_password_button["command"] = lambda: on_click_copy_password(self.password, self.copied_message)
        copy_password_button.place(x=310, y=360, width=100, height=30)

        copied_label = tk.Label(root, font=times_10, fg=fg_white, justify="center")
        copied_label["textvariable"] = self.copied_message
        copied_label.place(x=410, y=360, width=100, height=30)

        save_password_button = tk.Button(root)
        save_password_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        save_password_button["font"] = ft
        save_password_button["fg"] = "#000000"
        save_password_button["justify"] = "center"
        save_password_button["text"] = "Save"
        save_password_button.place(x=310, y=440, width=100, height=30)
        save_password_button["command"] = save_password

        key_password_entry = tk.Entry(root)
        key_password_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        key_password_entry["font"] = ft
        key_password_entry["fg"] = "#333333"
        key_password_entry["justify"] = "center"
        key_password_entry["text"] = "Key"
        key_password_entry.place(x=180, y=440, width=100, height=30)
