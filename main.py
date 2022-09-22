from hashlib import shake_128

from tkinter import *
import tkinter


def sign(x):
    if x >= 0: return 1
    return -1

# ~ Алгоритмы отрисовки
def draw_dot(x,y,col='black'): # в tkinter нет возможности отрисовать точку, а потому рисуем очень маленький круг
    x1,y1 = x-1,y-1
    x2,y2 = x+1,y+1
    canvas.create_oval(x1, y1, x2, y2,fill=col,width=1,outline=col)


def Beizer(step,m,R,P):
    pass        
     

#  Алгоритмы отрисовки ~



# ~UI Функционал
def callback(event): # метод отслеживания нажатий
    global counter,coords,var
    coords.append([int(event.x),int(event.y)])
    if counter >= 3: 
        print('Current click: ',counter + 1)
        print(coords)
        # Simple(coords[0][0],coords[0][1],coords[1][0],coords[1][1]) # P.S сделать так чтобы пользователь мог выбирать режим посредством тыкания кнопок
        coords = []
        counter = 0
        
    else: 
        print('Current click: ',counter + 1)
        counter += 1

def clear(): # очистить холст
    canvas.delete("all") 
# UI Функционал~

if __name__ == "__main__":
    # Инициализация и базовая настройки окна
    root = Tk()
    root.title('Лабораторная работа № 2 Реализация вывода сплайнов Безье')
    root.resizable(0, 0)

    # Инициализация важных переменных
    counter = 0 # переменная, в которой хранится номер клика мыши
    coords = [] # координаты точек
    mode = {'Beizer':Beizer} # массив функциий (алгоритмов по которым будет делаться отрисовка)

    # Инициализация и настройка холста
    canvas= Canvas(root, width=800, height=600,bg='white')
    canvas.bind("<Button-1>", callback)
    canvas.pack()
   

    # Кнопка очистки очистка холста
    clsBtn = tkinter.Button(root,text='Очистить холст',command=clear)
    clsBtn.pack()
    root.mainloop()