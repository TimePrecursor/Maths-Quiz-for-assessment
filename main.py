#The folowing code is completely original and of my own design. 

import fcntl, termios, struct
import random
import time
import os
lastscore = 0

#creating the sleep timers (for aesthetic purposes only)
def slep1():
  time.sleep(1)
def slep2():
  time.sleep(2)
def slep3():
  time.sleep(3)

#find terminal size
def terminal_size():
  th, tw, hp, wp = struct.unpack(
    'HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0,
                                                           0)))
  global width
  width = tw
  return tw, th
terminal_size()

#main title layout
def title():
  print(" * *" * int(width / 4))
  print("~ THE MATH QUIZ ~".center(width))
  print(" * *" * int(width / 4))
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
  e = random.randint(1, 3)
  pt1 = random.randint(0, 11)
  pt2 = random.randint(0, 11)
  if e == 1:
    pt3 = "+"
    answer_is = (pt1 + pt2)
  elif e == 2:
    pt3 = "-"
    answer_is = (pt1 - pt2)
  elif e == 3:
    pt3 = "x"
    pt1 = random.randint(0, 6)
    pt2 = random.randint(0, 6)
    answer_is = ((pt1) * (pt2))
  #the answer for the question (to be checked with later)
  question1 = ((f"what is: {pt1} {pt3} {pt2}"))


#asks for name
print("What is your name?".center(width))
inputname = True
while inputname == True:
  name = input()
  #name checker (it wont allow non letters)
  if not name.isalpha() or len(name)<2:
    print("Please enter a real name")
  elif name.isalpha():
    print("\n")
    slep1()
    #welcoming the player
    print(f"Welcome {name} to ~ THE MATH QUIZ ~".center(width))
    inputname = False
    slep2()
    clr()
  else:
    #if the input contains non letters
    print("Please enter a real name")
print("\n")
question()
print(question1.center(width))


#answer checker fuction set up (self explanitory)
def answer_checker():
  global checkanswer
  global questiontries
  checkanswer = True
  questiontries = 1
  while checkanswer == True:
    #counting to 2, if over, the next question begins
    questiontries += 1
    answer = str(input())
    #Had a problem earlier with input not being a int:
    if answer == str(answer_is):
      print("correct")
      checkanswer = False
    elif answer != str(answer_is) and questiontries < 3:
      print("\n")
      print("Wrong!  Last try!".center(width))
    else:
      print("\nWrong agian!  Next qeustion...".center(width))
      checkanswer = False
#activates the answer checker function
answer_checker()

print("\n\nDONE")
