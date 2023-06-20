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
def clr():
  os.system('clear')
  title()
print("What is your name?".center(width))
inputname = True
while inputname == True:
  name = input()
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

def choosediff():
  print("Choose your difficulty".center(width))
  print("1 = Easy       ".center(width))
  print("2 = Normal     ".center(width))
  print("3 = Hard       ".center(width))
  print("4 = Extreme    ".center(width))
  print("5 = IMPOSSIBLE ".center(width))
choosediff()
def chooseword():
  global word
  global levelchoosing
  global lvlchoice
  while levelchoosing == True:
    lvlchoice = input()
    if lvlchoice == "1":
      word = random.choice(lvl1_words)
      levelchoosing = False
    elif lvlchoice == "2":
      word = random.choice(lvl2_words)
      levelchoosing = False
    elif lvlchoice == "3":
      word = random.choice(lvl3_words)
      levelchoosing = False
    elif lvlchoice == "4":
      word = random.choice(lvl4_words)
      levelchoosing = False
    elif lvlchoice == "5":
      word = random.choice(lvl5_words)
      levelchoosing = False
    else:
      print("Please enter a number from 1 to 5")