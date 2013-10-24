#Joshua Winchester 902947827
# Joshua.winchester@gatech.edu
# I worked on this assignment alone and used only the course materials and the python documentation.

from Myro import *
from Graphics import *

win = Window("Super Face", 750 , 750)

#creates the head and draws it
head = Circle((375,375),300)
head.fill = Color(255,242,242)
head.draw(win)

## #creates the right eye
## rEye = Oval((510,300), 50,25)
## rEye.fill = Color(255,255,255)
## rEye.draw(win)

## #creates the left eye
## lEye = Oval((240,300), 50,25)
## lEye.fill = Color(255,255,255)
## lEye.draw(win)
## 
## #creates the irises
## rIris = Circle((510,300), 10)
## rIris.fill = Color(157,165,252)
## rIris.draw(win)

## lIris = Circle((240,300), 10)
## lIris.fill = Color(157,165,252)
## lIris.draw(win)

#creates the pupils for the eyes
rPup = Circle((510,300), 13)
rPup.fill = Color(0,0,0)
rPup.draw(win)

lPup = Circle((240,300), 13)
lPup.fill = Color(0,0,0)
lPup.draw(win)

#draws a nose
## upper = Line((375,350),(400,425))
## upper.draw(win)
## 
## lower = Line((400,425),(375,425))
## lower.draw(win)

#draws the tattoo
##
## uno = Line((360,100),(370,150))
## uno.outline = Color(105,0,0)
## uno.border = 3
## uno.draw(win)
## 
## dos = Line((370,150),(350,140))
## dos.outline = Color(105,0,0)
## dos.border = 3
## dos.draw(win)
## 
## tres = Line((350,140),(360,180))
## tres.outline = Color(105,0,0)
## tres.border = 3
## tres.draw(win)

# draws and animates the mouth
#dy1 = 500
#dy2 = 500
#curve = Curve((250,550),(350,dy1),(400,dy2),(500,550))
#while dy1 < 600:
 #   curve.undraw()
 #   dy1 = dy1 + 5
 #   dy2 = dy2 + 5
curve = Curve((250,550),(350,500),(400,500),(500,550))
curve.draw(win)
  #  wait(.25)

## #writes a message
## msg = Text((375, 40),"I'm Harry Potter!")
## msg.fill = Color(0,0,0)
## msg.fontSize = 36
## msg.draw(win)