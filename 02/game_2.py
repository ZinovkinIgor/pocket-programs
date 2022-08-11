import random
from tkinter import *
from PIL import ImageTk

element = {
    1: 'Камень',
    2: 'Ножницы',
    3: 'Бумага'
}
# Функция обрабатывает данные если пользователь выбрал камень
def exemple_stone():
    res = random.randint(1, 3)
    user_res = 1
    if res == user_res:
        result = Label(text = f'{element[user_res]} & {element[res]} = ничья')
        result.pack()
    elif user_res == 1 and res == 2:
        result = Label(text = f'{element[user_res]} & {element[res]} = победа')
        result.pack()
    else:
        result = Label(text = f'{element[user_res]} & {element[res]} = проигрыш')
        result.pack()

# Функция обрабатывает данные если пользователь выбрал ножницы
def exemple_Scissors():
    res = random.randint(1, 3)
    user_res = 2
    if res == user_res:
        result = Label(text = f'{element[user_res]} & {element[res]} = ничья')
        result.pack()
    elif user_res == 2 and res == 3:
        result = Label(text = f'{element[user_res]} & {element[res]} = победа')
        result.pack()
    else:
        result = Label(text = f'{element[user_res]} & {element[res]} = проигрыш')
        result.pack()

# Функция обрабатывает данные если пользователь выбрал бумагу
def exemple_Paper():
    res = random.randint(1, 3)
    user_res = 2
    if res == user_res:
        result = Label(text=f'{element[user_res]} & {element[res]} = ничья')
        result.pack()
    elif user_res == 3 and res == 1:
        result = Label(text=f'{element[user_res]} & {element[res]} = победа')
        result.pack()
    else:
        result = Label(text=f'{element[user_res]} & {element[res]} = проигрыш')
        result.pack()

window = Tk()
window.title('Игра камень, ножницы, бумага')
window.geometry('500x450+500+200')
window.resizable(0, 0)
imgStone = ImageTk.PhotoImage(file='picture/1.jpg')
btnStone = Button(window, height=70, image=imgStone, font='Arial 15 bold', compound=LEFT, text='Камень', command=exemple_stone)
btnStone.pack()
imgScissors = ImageTk.PhotoImage(file='picture/2.jpg')
btnScissors = Button(window, height=70, image=imgScissors, font='Arial 15 bold', compound=LEFT, text='Камень', command=exemple_Scissors)
btnScissors.pack()
imgPaper = ImageTk.PhotoImage(file='picture/3.jpg')
btnPaper = Button(window, height=70, image=imgPaper, font='Arial 15 bold', compound=LEFT, text='Камень', command=exemple_Paper)
btnPaper.pack()

window.mainloop()
