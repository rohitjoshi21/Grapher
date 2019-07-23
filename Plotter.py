#!/usr/bin/python3

import tkinter as tk
from math import *
import grapher

root = tk.Tk()
root.resizable(0,0)
root.title('Curve Sketching')
root.withdraw()
root.update_idletasks()
x = (root.winfo_screenwidth() - 850) / 2
y = (root.winfo_screenheight() - 700) / 2
root.geometry("+%d+%d" % (x, y))
root.deiconify()

#Initial Variables
h = 100
k = -155
scrsize = 500


def draw(*args):
    initial = graph.get_vars()
    graph.reset_var()
    graph.speed(graph.spd)
    final = graph.get_vars()
    if initial != final:
        graph.resetgraph()
        
    orgfunc = func.get()
    newfunc,msg = grapher.editFunc(orgfunc)
    
    if newfunc != None:
        graph.screen.tracer(1)
        graph.plot_func(orgfunc,newfunc)
    else:
        func.set(msg)
    
def reset():
    graph.tracer(0)
    graph.reset_var()
    graph.resetgraph()
    
        
        
#Upper Part
ent = tk.Frame(root,bg = '#234',width = 850,height = 100)
ent.grid(row = 0, column = 0)
ent.propagate(False)

func = tk.StringVar()
entryfrm = tk.Frame(ent, width = 500,height = 50,bg = '#090')
entryfrm.grid(row = 0, column = 0, pady = 5)
entryfrm.propagate(False)

enter = tk.Entry(entryfrm,font=('Times',25),textvariable = func)
enter.pack(expand=True,fill=tk.BOTH)
enter.focus()
enter.bind('<Return>',draw)

#Buttons
btnsfrm = tk.Frame(ent, width = 350,height = 50,bg = '#234')
btnsfrm.grid(row = 0, column = 1)
btnsfrm.propagate(False)

#DrawButton
btnfrm1 = tk.Frame(btnsfrm, width = 175, height = 50)
btnfrm1.grid(row =0, column = 1)
btnfrm1.propagate(False)
drawbtn = tk.Button(btnfrm1, command = draw, text = 'Draw',font = ('Arial',15))
drawbtn.pack(expand= True, fill = tk.BOTH)

#ResetButton
btnfrm2 = tk.Frame(btnsfrm, width = 175, height = 50)
btnfrm2.grid(row = 0, column = 2)
btnfrm2.propagate(False)
resetbtn = tk.Button(btnfrm2, command = reset, text = 'Reset',font = ('Arial',15))
resetbtn.pack(expand= True, fill = tk.BOTH)

#Text Label
def writeText(framename, text):
    txtfrm = tk.Frame(framename, width = 250, height = 50, bg = '#645')
    txtfrm.grid(row = 0, column = 0)
    txtfrm.propagate(False)
    lbl = tk.Label(txtfrm,text = text, bg = '#564',font = ('Times',20))
    lbl.pack(expand = True, fill = tk.BOTH)

#Entry Box
def getEntry(framename):
    enfrm = tk.Frame(framename,bg = '#435', width = 250, height = 50)
    enfrm.grid(row = 1, column = 0)
    enfrm.propagate(False)
    new = tk.StringVar()
    entt = tk.Entry(enfrm,font=('Times',20), textvariable = new)
    entt.pack(expand = True, fill = tk.BOTH)
    return new

#Body Part
bdfrm = tk.Frame(root,width = 850, height = 600,bg = '#321')
bdfrm.grid(row = 1, column = 0)
bdfrm.propagate(False)

#Vertical Menu
vmenfrm = tk.Frame(bdfrm, width = 250, height = 600, bg = '#234')
vmenfrm.grid(row = 0, column = 0, sticky = tk.N)
vmenfrm.propagate(False)

xfrm = tk.Frame(vmenfrm, height = 100, width = 250, bg = '#454')
xfrm.grid(row = 0, column = 0)
writeText(xfrm, 'X-Range:-')
x_range = getEntry(xfrm)
x_range.set('10')

yfrm = tk.Frame(vmenfrm, height = 100, width = 250, bg = '#356')
yfrm.grid(row = 1, column = 0)
writeText(yfrm, 'Y-Range:-')
y_range = getEntry(yfrm)
y_range.set('10')

spdfrm = tk.Frame(vmenfrm, height = 100, width = 250, bg = '#893')
spdfrm.grid(row = 3, column = 0)
writeText(spdfrm,'Speed')
sclfrm = tk.Frame(spdfrm,width = 250, height = 50, bg = '#653')
sclfrm.grid(row = 1, column = 0)
sclfrm.propagate(False)

speed = tk.IntVar()
speed.set(10)
scl = tk.Scale(sclfrm, variable = speed, from_=1.0, to=10.0,orient=tk.HORIZONTAL)
scl.pack(expand = True, fill = tk.BOTH)


zmfrm = tk.Frame(vmenfrm, height = 100, width = 250, bg = '#963')
zmfrm.grid(row = 4, column = 0)
writeText(zmfrm,'Size')
sclfrm = tk.Frame(zmfrm,width = 250, height = 50, bg = '#645')
sclfrm.grid(row = 1, column = 0)
sclfrm.propagate(False)

size = tk.IntVar()
size.set(10)
scl = tk.Scale(sclfrm, variable = size, from_=1.0, to=10.0,orient=tk.HORIZONTAL)
scl.pack(expand = True, fill = tk.BOTH)


#Main Canvas
canfrm = tk.Frame(bdfrm, width = 600, height = 600,bg='#543')
canfrm.grid(row =0, column = 1)
canfrm.propagate(False)

canvas = tk.Canvas(canfrm,bg = '#F65',relief = tk.SUNKEN,bd = 3)
canvas.pack(expand = True, fill = tk.BOTH,padx = 5, pady = 5)


#Calling graph object
graph = grapher.Graph(canvas,h,k,x_range,y_range,size,speed,scrsize)

#Initializing graph
graph.reset_var()
graph.drawAxes()
graph.drawNum()

root.update()
tk.mainloop()

