from tkinter import *
from tkinter.messagebox import *
from math import sin,cos,pi,exp

def draw_function(event):#Рисуем круг (овал)
    global MaxX,MaxY
    Xb=MaxX//2
    Xe=MaxY//2
    R=100
    cv.create_oval(Xb, Xe, Xb+R,Xe+R, outline='purple', width=10)

ID1=0
ID2=0
def showXY(event):#Вывод осей на полотно (прицел)
    global ID1,ID2
    x=event.x
    y=event.y
    cv.delete(ID1)
    cv.delete(ID2)
    ID1 = cv.create_line(0, y, MaxX, y, dash=(3, 5), fill=('black'))
    ID2 = cv.create_line(x, 0, x, MaxY, dash=(3, 5), fill=('black'))

def window_deleted():#"Закрыть окно?"
    if askyesno("ВЫХОД","Вы уверенны, что хотите выйти?"):
      root.destroy()

root = Tk()
root.title("Графика")
root.protocol('WM_DELETE_WINDOW', window_deleted)
root.resizable(False,False)
Kp = 0.7
MaxX=root.winfo_screenwidth()*Kp
MaxY=root.winfo_screenheight()*Kp

cv = Canvas(root, width = MaxX, height = MaxY, bg = "white")
cv.grid(row = 0, columnspan = 9)
cv.bind('<Button-1>', showXY)
cv.bind('<Button-1>',draw_function)

lba0 = Label(root, text = "X:", width = 10, fg = "blue", font = "Ubutu, 12")
lba0.grid(row = 1, column = 0, sticky='e')
lba1 = Label(root, text = "Y:", width = 10,fg = "blue", font = "Ubutu, 12")
lba1.grid(row = 2, column = 0, sticky='e')
lba2 = Label(root, text = "Xmin:", width = 10,fg = "blue", font = "Ubutu, 12")
lba2.grid(row = 1, column = 2, sticky='e')
lba3 = Label(root, text = "Xmax:", width = 10,fg = "blue", font = "Ubutu, 12")
lba3.grid(row = 1, column = 4, sticky='e')
lba4 = Label(root, text = "Ymin:", width = 10,fg = "blue", font = "Ubutu, 12")
lba4.grid(row = 2, column = 2, sticky='e')
lba5 = Label(root, text = "Ymax:", width = 10,fg = "blue", font = "Ubutu, 12")
lba5.grid(row = 2, column = 4, sticky='e')
lba6 = Label(root, text = "Шаг меток:", width = 10,fg = "blue", font = "Ubutu, 12")
lba6.grid(row = 1, column = 6, sticky='e')
lba7 = Label(root, text = "Смещение:", width = 10,fg = "blue", font = "Ubutu, 12")
lba7.grid(row = 2, column = 6, sticky='e')

ent0 = Entry(root, width = 5, font = "Ubuntu, 12")
ent0.grid(row = 1, column = 0)
ent0.insert(0, 0)
ent1 = Entry(root, width = 5, font = "Ubuntu, 12")
ent1.grid(row = 2, column = 0)
ent1.insert(0, 0)
ent2 = Entry(root, width = 5, font = "Ubuntu, 12")
ent2.grid(row = 1, column = 2)
ent2.insert(0, 0)
ent3 = Entry(root, width = 5, font = "Ubuntu, 12")
ent3.grid(row = 2, column = 4)
ent3.insert(0, 0)
ent4 = Entry(root, width = 5, font = "Ubuntu, 12")
ent4.grid(row = 1, column = 2)
ent4.insert(0, 0)
ent5 = Entry(root, width = 5, font = "Ubuntu, 12")
ent5.grid(row = 2, column = 4)
ent5.insert(0, 0)
ent6 = Entry(root, width = 5, font = "Ubuntu, 12")
ent6.grid(row = 1, column = 6)
ent6.insert(0, 0)
ent7 = Entry(root, width = 5, font = "Ubuntu, 12")
ent7.grid(row = 2, column = 6)
ent7.insert(0, 0)

root.mainloop()
