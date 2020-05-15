from tkinter import *
from math import *
from scipy import interpolate

#Исходные данные
X=[4,5,6.5,8,4,6,7,8]
Y=[2,1,4.5,2,6,8,8,7]

T=[0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0]
points=8


def f(t, tp):

    if tp=="spline":
       #tck = interpolate.splrep(T, X, s=0)
       #return interpolate.splev(t, tck, der=0)
       ff = interpolate.UnivariateSpline(T, X)
       return ff(t)
    else:
       ff=interpolate.interp1d(T, X, kind = 'cubic')
       return ff(t)

def g(t, tp):
    if tp=="spline":
      #tck = interpolate.splrep(T, Y, s=0)
      #return interpolate.splev(t, tck, der=0)
      gg = interpolate.UnivariateSpline(T, Y)
      return gg(t)
    else:
       gg=interpolate.interp1d(T, Y, kind = 'cubic')
       return gg(t)


root=Tk()#Создаем окно

canvas = Canvas(root, width = 500, height = 500, bg = "lightblue", cursor = "pencil")#Создаем холст

canvas.pack()

scale=50
maxval_y=500
minval=10

#Рисуем оси координат
canvas.create_line(minval,maxval_y,minval,0,width=2,arrow=LAST)
canvas.create_line(0,maxval_y-minval,maxval_y,maxval_y-minval,width=2,arrow=LAST)



for i in range(points):
 canvas.create_oval(X[i]*scale, maxval_y-Y[i]*scale, X[i]*scale+ 4, maxval_y-Y[i]*scale + 4, fill = 'black')

#Сплайн-интеполированные координаты
Xs=[]
Ys=[]

#Координаты, интерполированные кубич. интерп.
Xc=[]
Yc=[]

step=T[points-1]/(maxval_y-1)#шаг интерполяции

for i in range(maxval_y):
   t=i*step

   Xs.append(f(t, "spline"))
   Ys.append(g(t, "spline"))

   Xc.append(f(t, "cubic"))
   Yc.append(g(t, "cubic"))

   canvas.create_oval(Xs[i]*scale, maxval_y-Ys[i]*scale, Xs[i]*scale+ 2, maxval_y-Ys[i]*scale + 2, fill = 'red')
   canvas.create_oval(Xc[i]*scale, maxval_y-Yc[i]*scale, Xc[i]*scale+ 2, maxval_y-Yc[i]*scale + 2, fill = 'yellow')

   
   

   
 


root.mainloop()


