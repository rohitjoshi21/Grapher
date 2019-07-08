from turtle import RawTurtle, TurtleScreen
from math import *

class Graph(RawTurtle,TurtleScreen):
    
    def __init__(self,canvas,h,k,xr,yr,size,speed,screensize = 500):
        screen = TurtleScreen(canvas)
        RawTurtle.__init__(self,screen)
        self.screen = screen
        self.screen.tracer(0)
        self.h = h
        self.k = k
        self.xr = xr
        self.yr = yr
        self.size = size
        self.speedturt = speed
        self.d = 0.05
        self.nofunc = 0
        self.screensize = screensize
        self.hideturtle()                                    
        self.pensize(1)
        self.reset_var()

    def drawAxes(self):
        #self.screen.tracer(0)
        xlen = self.width/2
        ylen = self.height/2
        self.up()
        self.goto(self.h,self.k)
        self.down()
        for axis in [(0,"X",xlen),(90,"Y",ylen)]:
            self.seth(axis[0])
            self.forward(axis[2])
            self.up()
            self.fd(10)
            self.write(axis[1],font=('Times',13,'bold'))
            self.back(10)
            self.down()
            self.goto(self.h,self.k)
            self.backward(axis[2])
            self.up()
            self.bk(15)
            self.write(axis[1]+"'",font=('Times',13,'bold'))
            self.fd(15)
            self.down()
            self.goto(self.h,self.k)

    def drawNum(self):
        x = self.xrange
        y = self.yrange
        intX = int(x/3)
        intY = int(y/3)
        nX = intX
        nY = intY
        dx = (intX/x) * self.width/2
        dy = (intY/y) * self.height/2
        self.up()
        text_style = ('Cambria',10,'bold')
        self.goto(self.h+5,self.k)
        self.write('O',font = text_style)
        self.goto(self.h,self.k)
        changedX = False
        changedY = False
        for i in range(3):
            if x >=3:
                changedX = True
                self.goto(dx+self.h,0+self.k)
                self.write(nX,font= text_style)
                self.goto(-dx+self.h,0+self.k)
                self.write(-nX,font= text_style)
            if y >=3:
                changedY = True
                self.goto(-15+self.h,dy+self.k)
                self.write(nY,font= text_style)
                self.goto(-19+self.h,-dy+self.k)
                self.write(-nY,font= text_style)
            nX += intX
            nY += intY
            dx = (nX/x) * self.width/2
            dy = (nY/y) * self.height/2

        if not changedX:
            self.goto(self.h,self.k)
            dx = (1/x) * self.width/2
            for i in range(1,int(x)):
                self.goto(dx+self.h,0+self.k)
                self.write(i,font= text_style)
                self.goto(-dx+self.h,0+self.k)
                self.write(-i,font= text_style)
        if not changedY:
            self.goto(self.h,self.k)
            dy = (1/x) * height/2
            for i in range(1,int(x)):
                self.goto(-15+self.h,dy+self.k)
                self.write(i,font= text_style)
                self.goto(-19+self.h,-dy+self.k)
                self.write(-i,font= text_style)
        self.ht()

    def f(self,function,x):
        try:
            return x, eval(function)
        except:
            self.up()
            if x > -self.xrange:
                return self.f(function,(x-self.d))
            else:
                return x,None


    def plot_func(self,ofunc,nfunc):
        self.screen.tracer(1)
        self.st()
        self.pensize(2)
        xt = self.xrange
        yt = self.yrange
        x = xt
        self.penup()
        while x >= -xt:
            ft = self.f(nfunc,x)
            if ft[1] != None:
                x1 = ft[0]/xt*self.width/2
                y1 = ft[1]/yt*self.height/2
                if y1<=self.height/2 and y1>=-self.height/2:
                    self.goto(x1+self.h,y1+self.k)
                    self.down()
                else:
                    self.up()
            else:
                break
            x -= self.d
        
        self.nofunc += 1
        self.up()
        self.goto(-self.width/2+self.h,self.width/2+self.k+self.nofunc*(-20))
        self.write("f(x) = "+ofunc,font=('Mv Voli',15,'bold'))
        self.ht()
        self.screen.tracer(0)

    def resetgraph(self):
        self.nofunc = 0
        self.speed(self.spd)
        self.reset()
        self.drawAxes()
        self.drawNum()
        
    def reset_var(self):
        self.xrange = int(self.xr.get())
        self.yrange = int(self.yr.get())
        self.sizenum = self.size.get()
        self.width = self.sizenum/10 * self.screensize
        self.height = self.sizenum/10 * self.screensize
        self.spd = self.speedturt.get() if self.speedturt.get() < 10 else 0
        
    def get_vars(self):
        return (self.xrange,self.yrange,self.sizenum)

def editFunc(old_func):
    new_func = ""
    replaceable = [('^','**'),('cot','1/tan'),('cosec','1/sin'),('sec','1/cos')]
    
    #Modifying algebraic forms in programmable form
    for i in range(len(old_func)-1):
        if old_func[i].isdigit() and old_func[i+1].isalpha():
            new_func += old_func[i]+"*"
        else:
            new_func += old_func[i]
    new_func += old_func[-1]

##    #Replacing all the variables with 'x'
##    for i,c in enumerate(new_func):
##        if c.isalpha() and c != 'x':
##            new_func = new_func.replace(c,'x')
##            
    

    #Replacing some terms
    for term in replaceable:
        new_func = new_func.replace(term[0],term[1])

    
    #Checking whether it is solvable or not
    x = 2
    try:
        y = eval(new_func)
    except:
        x = 5
        try:
            y = eval(new_func)
        except:
            msg = 'Function not recognized'
            return None, msg
    return new_func, None
