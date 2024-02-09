import random


class KeyGen:
    def __init__(self, length):
        self.array_gen = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*+?'
        self.length = length
        self.password = self.generate_password()

    def generate_password(self):
        if self.length < 8:
            return f'Ошибка: длина пароля должна быть не меньше 8 символов'
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


key_gen = KeyGen(int(input('Введите длину символов: ')))

print(key_gen)
