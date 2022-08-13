import random
from tkinter import *
from PIL import ImageTk

def roll_dice():
    result = random.randint(1, 6)
    result_cube = Label(text=f'{result}', font='Arial 80')
    result_cube.grid(row=3, column=0, columnspan=4)



window = Tk()
window.title('Игра КОСТИ')
window.geometry('500x400+500+200')
text_1 = Label(text='Игра кости. Брось и узнай свой результат.\n\n', font='Arial 18')
text_1.grid(row=1, column=0, columnspan=4)

image_cube = ImageTk.PhotoImage(file='cube.jpg')
image_btn = Button(window, height=100, image=image_cube, command=roll_dice)
image_btn.grid(row=2, column=0, columnspan=4)
window.mainloop()