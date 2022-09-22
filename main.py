from tkinter import *
from methods import *
import tkinter
from time import sleep


# ~ Алгоритмы отрисовки
def draw_dot(x,y,col='black'):
    global root,sbsm
    x1,y1 = x-1,y-1
    x2,y2 = x+1,y+1
    if sbsm.get() == 0:canvas.create_oval(x1, y1, x2, y2,fill=col,width=1,outline=col) 
    else:
        sleep(0.001)
        canvas.create_oval(x1, y1, x2, y2,fill='red',width=1,outline='red') 
        root.update()
    #canvas.create_line(x,y,x-1,y-1)

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
    m = len(P) # количество точек исходного многоугольника
    xn,yn,t,step = P[0][0],P[0][1], 0 , 0.01

    while True:
        R = [] + P # массив с координатами точек нового многоугольника 
       
        # вычисление точек
        for j in range(m,1,-1):
            for i in range(0,j-1):
                R[i][0] = R[i][0] + round(t*(R[i+1][0]-R[i][0]))
                R[i][1] = R[i][1] + round(t*(R[i+1][1]-R[i][1]))
        BresenhamV4(R[0][0],R[0][1],xn,yn)
        t,xn,yn = t + step, R[0][0] , R[0][1]
        if t > 1: break
    pass        
     

#  Алгоритмы отрисовки ~



# ~UI Функционал
def callback(event): # метод отслеживания нажатий
    global counter,coords,var
    coords.append([int(event.x),int(event.y)])
    if len(coords) > 1:
        tmp = len(coords)
        BresenhamV4(coords[tmp-2][0],coords[tmp-2][1],coords[tmp-1][0],coords[tmp-1][1])
         
    print('Current click: ',counter + 1)
    counter += 1
def drawBeizer(event): # правая кнопка мыши, отрисовка бейзера
    global counter,coords,var
    if counter <= 2:
         print('Ошибка: накликайте ещё точек')
    else:
        print('m  = ',counter)
        print('coords = ', coords)
        Beizer(coords)
        coords = []
        counter = 0

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
    

    # Инициализация и настройка холста
    canvas= Canvas(root, width=800, height=600,bg='white')
    canvas.bind("<Button-1>", callback)
    canvas.bind("<Button-3>", drawBeizer)
    canvas.pack()
    # Step by step mode (animation)
    sbsm = IntVar()
    sbsmCBtn = Checkbutton(root, text = "Step by step mode",
                      variable = sbsm,
                      onvalue = 1,
                      offvalue = 0)
    sbsmCBtn.pack()


    # Кнопка очистки очистка холста
    clsBtn = tkinter.Button(root,text='Очистить холст',command=clear)
    clsBtn.pack()
    root.mainloop()
