import fcntl, termios, struct
#import random
import time
import os
#from tabulate import tabulate
def slep1():
  time.sleep(1)
def slep2():
  time.sleep(2)
def slep3():
  time.sleep(3)
def clr():
  os.system('clear')
def terminal_size():
      th, tw, hp, wp = struct.unpack('HHHH',
          fcntl.ioctl(0, termios.TIOCGWINSZ,
          struct.pack('HHHH', 0, 0, 0, 0)))
      global width
      width = tw
      return tw, th
terminal_size()

def title():
  print(" * *"*int(width/4))
  print("~ THE MATH QUIZ ~".center(width))
  print(" * *"*int(width/4))
  print("\n")
title()
print("What is your name?".center(width))
inputname = True
while inputname == True:
  name = input()
  if not name.isalpha():
    print("Please enter a real name")
  elif name.isalpha():
    print("\n")
    print(f"Welcome {name} to ~ THE MATH QUIZ ~".center(width))
    inputname = False
    slep2()
    clr()  
  else:
    print("Please enter a real name")
    
