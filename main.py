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

def Simple(x1,y1,x2,y2): # первый простой алгоритм
    if x1 != x2:
            m = (y2-y1)/(x2-x1)  
            
            if abs(m) > 1:
                if y1 > y2: 
                    x1,x2 = x2,x1
                    y1,y2 = y2,y1
                x = x1
                for y in range(y1,y2):
                    draw_dot(round(x),y)
                    x = x + (1/m)
            # случай abs(m) > 1, тогда двигаемся по y
            else:
                if x1 > x2: 
                    x1,x2 = x2,x1
                    y1,y2 = y2,y1
                y = y1
                for x in range(x1,x2):
                    draw_dot(x,round(y))
                    y = y + m
    else:
        if y1 == y2:
            draw_dot(x,y)
        else: print('Error! Vertical')
        
     

#  Алгоритмы отрисовки ~

# ~UI Функционал
def callback(event): # метод отслеживания нажатий
    global counter,coords,var
    coords.append([int(event.x),int(event.y)])
    if counter >= 3: 
        print('Current click: ',counter + 1)
        print(coords)
        Simple(coords[0][0],coords[0][1],coords[1][0],coords[1][1]) # P.S сделать так чтобы пользователь мог выбирать режим посредством тыкания кнопок
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
    root.title('Лабораторная работа № 1 Реализация алгоритмов растровой развертки линий')
    root.resizable(0, 0)

    # Инициализация важных переменных
    counter = 0 # переменная, в которой хранится номер клика мыши
    coords = [] # координаты точек
    mode = {'Simple':Simple} # массив функциий (алгоритмов по которым будет делаться отрисовка)

    # Инициализация и настройка холста
    canvas= Canvas(root, width=800, height=600,bg='white')
    canvas.bind("<Button-1>", callback)
    canvas.pack()
    # Инициализация и настройка радиокнопок (для выбора режима)
    var = StringVar()
    var.set('Simple')
    for key in mode:
        rbtn = Radiobutton(text=key,variable=var,value=key)
        rbtn.pack()

    # Кнопка очистки очистка холста
    clsBtn = tkinter.Button(root,text='Очистить холст',command=clear)
    clsBtn.pack()
    root.mainloop()