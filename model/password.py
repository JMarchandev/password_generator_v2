import string
from random import choice, randint


class Password:

    def __init__(
            self,
            has_integer=1,
            has_upper_lower_case=1,
            has_spec_char=0,
            min_char=6,
            max_char=13,
            password="no password now",
            hide_password=1):
        self.has_integer = has_integer
        self.has_upper_lower_case = has_upper_lower_case
        self.has_spec_char = has_spec_char
        self.min_char = min_char
        self.max_char = max_char
        self.password = password
        self.hide_password = hide_password

    def get_has_integer(self):
        return self.has_integer

    def set_has_integer(self, has_integer):
        self.has_integer = has_integer

    def get_has_upper_lower_case(self):
        return self.has_upper_lower_case

    def set_has_upper_lower_case(self, has_upper_lower_case):
        self.has_upper_lower_case = has_upper_lower_case

    def get_has_spec_char(self):
        return self.has_spec_char

    def set_has_spec_char(self, has_spec_char):
        self.has_spec_char = has_spec_char

    def get_min_char(self):
        return self.min_char

    def set_min_char(self, min_char):
        self.min_char = min_char

    def get_max_char(self):
        return self.max_char

    def set_max_char(self, max_char):
        self.max_char = max_char

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_hide_password(self):
        return self.hide_password

    def toggle_hide_password(self):
        if self.hide_password == 0:
            self.hide_password = 1
        else:
            self.hide_password = 0

    def generate_password(self):
        chars = string.ascii_lowercase

        if self.has_integer == 1:
            chars += string.digits

        if self.has_upper_lower_case == 1:
            chars += string.ascii_uppercase

        if self.has_spec_char == 1:
            chars += string.punctuation

        password = "".join(choice(chars) for x in range(randint(self.min_char, self.max_char)))

        self.set_password(password)
