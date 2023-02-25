from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
question_count_passwords = int(input('Сколько паролей тебе нужно сгенерировать?'))
question_length = int(input("Какой длины?"))
question_numbers = input('Должен ли пароль включать в себя цифры?').strip()
question_upper = input('Включать ли в пароль, буквы верхнего регистра?').strip()
question_lower = input('Включать ли в пароль, буквы нижнего регистра?').strip()
question_symbols = input('Должны ли быть там спец.символы?').strip()
question_delete = input('Исключать ли неоднозначные символы?').strip()
if question_numbers.lower() == 'д':
    chars += digits
if question_lower.lower() == 'д':
    chars += lowercase_letters
if question_upper.lower() == 'д':
    chars += uppercase_letters
if question_symbols.lower() == 'д':
    chars += punctuation
if question_delete.lower() == 'д':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')
def generate_password(question_length, chars):
    password = ''
    for j in range(question_length):
        password += choice(chars)
    return password
for _ in range(question_count_passwords):
    generate_password(question_length, chars)
print(_)