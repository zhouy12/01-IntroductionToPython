"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Michelle Zhou.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

star = rg.SimpleTurtle()
star.pen = rg.Pen('pink', 5)
star.speed = 10
circle = rg.SimpleTurtle()
circle.pen = rg.Pen('red', 5)
circle.speed = star.speed

size = 120

for k in range(10):
    circle.draw_circle(size)

    circle.pen_up()
    circle.left(90)
    circle.forward(12)
    circle.right(90)
    circle.pen_down()

    size = size-12

for k in range(6):
    star.left(60)
    star.forward(60)
    star.right(120)
    star.forward(60)







