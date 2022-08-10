import tkinter as tk
import random
# Рандомно выбираем число, создаем список для сохранения истории попыток.
number = random.randint(1, 100)
history = []
def search_number():
    value = numb.get()
    try:
        if number > int(value):
            return f'Нет не угадал. Мое число больше {value}.'
        elif number < int(value):
            return f'Опять не угадал. Мое число меньше {value}.'
        else:
            return True
    except Exception:
        return 'Введи пожалуйста число.'



def ountput_result():
    result = search_number()
    scor = 1
    history.append(f'{result}')
    if result != True:
        answer_number = tk.Label(text=f'Попытка {scor}: {result}')
        answer_number.grid(row=4 + int(f'{scor}'), column=1)
        scor += 1
        search_number()
    else:
        answer_number = tk.Label(text=f'Поздравляю мое число {numb.get()}.Ты угадал.')
        answer_number.grid(row=4, column=1)
        history_answer = tk.Label(text=[f for f in history])
        history_answer.grid(row=5, column=1)
        print(history)

# Создаем окно программы, указываем размеры,
# запускаем
proga = tk.Tk()
proga.title('Угадай число')
proga.geometry('500x700+500+200')
task = tk.Label(text='Игра "Угадай число.\n"'
                  'Компьютер загадает число от 1 до 100\n'
                  'Попробуй его отгадать\n\n')
task.grid(row=0, column=1)
number_input = tk.Label(text='Введите число: ', width=12, height=0)
number_input.grid(row=1, column=0)

numb = tk.Entry()
numb.grid(row=1, column=1)

# Кнопка для подтверждения операции
btn_1 = tk.Button(text='Да', command=ountput_result)
btn_1.grid(row=1, column=2)

proga.mainloop()
