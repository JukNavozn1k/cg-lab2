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

def BresenhamV4(x1,y1,x2,y2): # четырёхсвязная развёртка 
    x,y,dx,dy,s1,s2 = x1,y1,abs(x2-x1),abs(y2-y1),sign(x2-x1),sign(y2-y1)
    l = None
    if dy<dx: l = False
    else:
        l = True
        dx,dy = dy,dx
    e = 2*dy-dx
    for i in range(1,dx+dy):
        draw_dot(x,y)
        if e < 0:
            if l: y = y + s2
            else: x = x + s1
            e = e+2*dy
        else:
            if l : x = x + s1
            else: y = y + s2
            e = e - 2*dx
    draw_dot(x,y)


def Beizer(P):
    m = 4 # количество точек исходного многоугольника
    R = [] # массив с координатами точек нового многоугольника 
    xn,yn,t,step = P[0][0],P[0][1],0,0.01
    for i in P:
        tmp = []
        for j in i:
            tmp.append(j)
        R.append(tmp)
    print(R)
    BresenhamV4(P[0][0],P[0][1],P[1][0],P[1][1])
    pass        
     

#  Алгоритмы отрисовки ~



# ~UI Функционал
def callback(event): # метод отслеживания нажатий
    global counter,coords,var
    coords.append([int(event.x),int(event.y)])
    if counter >= 3: 
        print('Current click: ',counter + 1)
        print(coords)
        Beizer(coords)
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