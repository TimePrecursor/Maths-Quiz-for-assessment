import fcntl, termios, struct
import random
import time
import os
#from tabulate import tabulate
def slep1():
  time.sleep(1)
def slep2():
  time.sleep(2)
def slep3():
  time.sleep(3)

#Find terminal size
def terminal_size():
      th, tw, hp, wp = struct.unpack('HHHH',
          fcntl.ioctl(0, termios.TIOCGWINSZ,
          struct.pack('HHHH', 0, 0, 0, 0)))
      global width
      width = tw
      return tw, th
terminal_size()

#title layout
def title():
  print(" * *"*int(width/4))
  print("~ THE MATH QUIZ ~".center(width))
  print(" * *"*int(width/4))
  print("\n")
title()

#clearing screen and printing title
def clr():
  os.system('clear')
  title()

#math questions setup
def question():
  global question1
  global pt1
  global pt2
  global pt3
  global answer_is
  e = random.randint(1,3)
  pt1 = random.randint(0,11)
  pt2 = random.randint(0,11)
  if e == 1:
    pt3 = "+"
    answer_is = (pt1+pt2)
  elif e == 2:
    pt3 = "-"
    answer_is = (pt1-pt2)
  elif e == 3:
    pt3 = "x"
    answer_is = ((pt1)*(pt2))
  question1 = ((f"what is: {pt1} {pt3} {pt2}"))

  

#asks for name
print("What is your name?".center(width))
inputname = True
while inputname == True:
  name = input()
  #name checker
  if not name.isalpha():
    print("Please enter a real name")
  elif name.isalpha():
    print("\n")
    slep1()
    print(f"Welcome {name} to ~ THE MATH QUIZ ~".center(width))
    inputname = False
    slep2()
    clr()  
  else:
    print("Please enter a real name")

print("\n")
question()
print(question1.center(width))
checkanswer = True
while checkanswer == True:
  answer = str(input())
  print(answer_is)  
  if answer == str(answer_is):
    print("correct")
    checkanswer = False
  else:
    print("wrong")
print("\nDONE")