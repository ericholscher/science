from Tkinter import *
from chaos.simify import *

generator = PolygonToSimlist([0+0j, 1.0/3.0+0j, .5+(sqrt(3)/6)*1j, 2.0/3.0+0j, 1+0j])

triangle = PolygonToSimlist([-.5+0j, 0+1j, .5+0j, -.5+0j])

def drawkoch(i, last, canvas):
    kochsims = [Similarity(1,0),]
    for j in range(i):
        kochsims = ChainSims(kochsims, generator)
    kochsims = ChainSims(triangle, kochsims)
    curve = canvas.create_polygon(*SimlistToPixels(kochsims, 600, 600)+
                                  [{'fill':'yellow', 'outline':'black'}])
    if i < last:
        window.after(1000, canvas.delete, curve)
    if i <= last:
        window.after(1000, drawkoch, i+1, last, canvas)

window = Tk()
window.title('Koch snowflake')
canvas = Canvas(window, width=600, height=600)
canvas.pack()
drawkoch(0, 5, canvas)
window.mainloop()
