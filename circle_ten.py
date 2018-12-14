from turtle import *

def main ():
  goto(0,0)
  for i in range(10,101,10):
    circle(i)
    penup()
    goto(0,-i)
    pendown()
main()
