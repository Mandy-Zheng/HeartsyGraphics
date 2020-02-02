#Amanda Zheng
import math
f=open("pic.ppm","w")
s="P3 \n 500 500 \n 255 \n "

def heart(x,y,size,startx,starty):
    y=-1*y
    correct=False;
    if x>=startx-20 and x<=startx:
        if pow(size-pow((-x+startx)-pow(size,0.5),2),0.5)-starty>=y:
            correct= True
        if pow(size,0.5) * math.acos( 1 + ( 1 / (pow( size, 0.5 ) ) ) * ( x - startx ) ) - pow(size,0.5 )*math.pi-starty<=y:
            if(correct):
                return True
        else:
            correct=False
    if x>=startx and x<=startx+20:
        if pow(size-pow((x-startx)-pow(size,0.5),2),0.5)-starty>=y:
            correct=True
        if pow(size,0.5)*math.acos(1-(1/(pow(size,0.5)))*(x-startx))-pow(size,0.5)*math.pi-starty<=y:
            if(correct):
                return True
        else:
            correct=False
    return correct

print("pic.png")
for x in range(500):
    for y in range(500):
        if heart(y,x,100,250,250):
            s+="244 225 230 "
        elif heart(y,x,100,300,200):
            s+="226 163 179 "
        elif heart(y,x,100,350,150):
            s+="153 27 40 "
        elif heart(y,x,100,400,100):
            s+="20 0 5 "
        elif heart(y,x,100,450,50):
            s+="211 76 110 "
        elif heart(y,x,100,200,200):
            s+="219 84 97 "
        elif heart(y,x,100,150,150):
            s+="255 206 211 "
        elif heart(y,x,100,100,100):
            s+="142 59 68 "
        elif heart(y,x,100,50,50):
            s+="106 69 72 "
        else:
            s+="255 "+str(135+(x//5))+" "+str(135+(x//5))+" "
f.write(s)
f.close()
