import random
from app_bot.config import ARRAY_LEN
from app_bot.config import len_check


class KeyGen:
    def __init__(self, length):
        self.array_gen = ARRAY_LEN
        self.length = int(length)
        self.password = self.generate_password()

    def generate_password(self):
        if self.length < len_check:
            return f'Ошибка: длина пароля должна быть не меньше {len_check} символов'
        elif len(self.array_gen) > self.length:
            password = ''.join(random.sample(self.array_gen, self.length))
            password_with_dashes = ''
            for i, char in enumerate(password):
                password_with_dashes += char
                if (i + 1) % 4 == 0 and i != self.length - 1:
                    password_with_dashes += '-'
            return password_with_dashes
        else:
            return f'Ошибка: длина пароля должна быть меньше {len(self.array_gen)} символов'

    def __str__(self):
        return self.password
