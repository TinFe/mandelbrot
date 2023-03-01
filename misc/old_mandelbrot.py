from tk import *
root = Tk()
root.geometry('600x400')
root.title('Mandelbrot Set')
c = Canvas(root, width=600, height = 400)
c.pack()



i = 2
r = 1


#Function that checks if any complex number is in the Mandelbrot set.
import cmath
def isnan(n):
    return n!=n

def is_mandel(c):

    z = 0
    i = 0
    while i < 50:
        z=z*z+c
        i+=1
    if isnan(z) == True:
        return False
    else:
        return True


    
def circle_maker(x,y):
    #creates a circle about the given (x,y) coordinate
    c.create_oval(x-r,y+r,x+r,y-r, fill = 'blue')


def drawer():
    x=0
    y=0

    
    while y<400:
        while x<600:
            x1 = ((x*.005)-2)
            y1 = (((y*-.005)+1)*1j)
            c = complex(x1+y1)
            
            #the above 3 lines converts the x and y coordinates that the computer uses for drawing into a complex number that coresponds to a position in the complex plane
            #to allow for easy shifting and zooming, I will add an a, b, c, and d c
            if is_mandel(c) == True:
                circle_maker(x,y)
                x+=i
            else:
                x+=i
        x=0
        y+=1


drawer()
print('press Enter to close')
input()
