import random
import string
from tkinter import *

easy_data = string.ascii_letters
average_data = string.hexdigits
difficult_data = string.ascii_letters + string.hexdigits + string.punctuation

# Легкий пароль
def generator_easy():
    password = ''.join(random.choice(easy_data) for i in range(6))
    result = Label(text=f'Ваш новый пароль:   {password}')
    result.grid(row=7, column=1, columnspan=2, sticky='w')

# Средний пароль
def generator_average():
    password = ''.join(random.choice(average_data) for i in range(10))
    result = Label(text=f'Ваш новый пароль:   {password}')
    result.grid(row=8, column=1, columnspan=2, sticky='w')

# Сложный пароль
def generator_difficult():
    password = ''.join(random.choice(difficult_data) for i in range(16))
    result = Label(text=f'Ваш новый пароль:   {password}')
    result.grid(row=9, column=1, columnspan=2, sticky='w')



def processing():
    window = Tk()
    window.title('Генератор паролей')
    window.geometry('500x400+500+200')
    text = Label(text='Генератор паролей. Выберите сложность пароля')
    text.grid(row=1, column=1)
    btn_1 = Button(text='Легкий', command=generator_easy)
    btn_1.grid(row=2, column=0)
    btn_2 = Button(text='Средний', command=generator_average)
    btn_2.grid(row=2, column=1)
    btn_3 = Button(text='Сложный', command=generator_difficult)
    btn_3.grid(row=2, column=2)

    window.mainloop()

if __name__ == '__main__':
    processing()







