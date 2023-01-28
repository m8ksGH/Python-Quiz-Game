from pyfiglet import figlet_format
from termcolor import colored

ascii_art = figlet_format('Welcome to a Python related quiz test!!!')
colored_ascii = colored(ascii_art, 'yellow')
print(colored_ascii)

import termcolor

termcolor.cprint("*** WELCOME PLAYER YOU ARE HERE FOR A SUIT TEST FOR AN INTRODUCTION OF THE BASICS OF PYTHON, \n    HERE ARE SOME QUESTIONS FOR YOU TO ANSWER COMPLTETELY THANK YOU! *** ", "yellow")
name_player = input("Please enter your name: ")
print("Hi! " + name_player + " " +  "Please choose the correct answer thank you enjoy!\nMultiple choices.")

import random

# A list of questions
questions = [
    "1.) He is a Dutch programmer best known as the creator of the Python programming language where he developed on 1991.\n a. Albert Einstien \n b. Guido Van Rossum\n c. Bill Gates",
    "2.) This is a named location used to store data in the memory. It is helpful to think of these as a container\n that holds data that can be changed later in the program.\n a. Variables\n b. String\n c. List",
    "3.) This is a type of variable whose value cannot be changed.\n a. Integer\n b. String\n c. Constants",
    "4.) These are the reserved words in Python. We cannot use these as a variable name, function name or any other identifier.\n They are used to define the syntax and structure of the Python language.\n a. Contstants\n b. Function\n c. Keywords\n d. Arguments",
    "5.) This is an ordered sequence of items used in python, this are also used to store multiple items in a single variable. \n this are one of 4 built-in  data types in Python used to store collections of data, all with different qualities and usage.\n a. Set\n b. List \n c. Dictionary",
]

# A list of answers to the questions
answers = [
    "b",
    "a",
    "c",
    "c",
    "b",
]

# Initialize the score to 0
score = 0

# Ask the user each question
for i in range(len(questions)):
    print(questions[i])
    user_answer = str(input())
    
    # If the user's answer is correct, increase their score by 1
    if user_answer == answers[i]:
        score += 1

# Check if the user passed or failed
if score >= 3:
    print("You passed! Your score is", score)

    import time
    import tkinter as tk
    root = tk.Tk()
    root.title("Python Quiz Game")
    root.geometry("600x400")

    label = tk.Label(root, text=" You passed! answers are: \n 1. b, 2. a, 3. c, 4. c, 5. b  \nYour score is " + str(score) + " \nPlease click the X button on the \nupperright \ncorner to show your \nsupprised greetings!", width= 600, height= 400,
        bg= "black", fg= "yellow", font=('Arial',30,'bold'))

    label.pack()

    root.mainloop()

    
    import time
    from tkinter import *
    WIDTH = 500
    HEIGHT = 500
    xVelocity = 0.5
    yVelocity = 0.5

    window = Tk()

    canvas = Canvas(window,width=WIDTH,height=HEIGHT)
    canvas.pack()
    bg = PhotoImage(file='bg.png')
    bga = canvas.create_image(0,0,image=bg,anchor=NW)

    photo_image = PhotoImage(file='t.png')
    my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

    image_width = photo_image.width()
    image_height = photo_image.height()

    while True:
      coordinates = canvas.coords(my_image)
      print(coordinates)
      if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
          xVelocity = -xVelocity
      if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
          yVelocity = -yVelocity
      canvas.move(my_image,xVelocity,yVelocity)
      window.update()
      time.sleep(0.01)
    window.mainloop()
else:
    print("You failed. Your score is", score)
    
    import time
    import tkinter as tk
    root = tk.Tk()
    root.title("Python Quiz Game")
    root.geometry("600x400")

    label = tk.Label(root, text=" You failed! answers are: \n 1. b, 2. a, 3. c, 4. c, 5. b   \nYour score is " + str(score) + " \nPlease click the X button on the \nupperright \ncorner to show your \nsupprised warning!", width= 600, height= 400,
        bg= "black", fg= "yellow", font=('Arial',30,'bold'))

    label.pack()

    root.mainloop()
    
    from tkinter import *
    import time

    WIDTH2 = 500
    HEIGHT2 = 500
    xVelocity2 = 0.5
    yVelocity2 = 0.5

    window2 = Tk()

    canvas2 = Canvas(window2,width=WIDTH2,height=HEIGHT2)
    canvas2.pack()
    bg2 = PhotoImage(file='bg2.png')
    bga2 = canvas2.create_image(0,0,image=bg2,anchor=NW)

    photo_image2 = PhotoImage(file='t2.png')
    my_image2 = canvas2.create_image(0,0,image=photo_image2,anchor=NW)

    image_width2 = photo_image2.width()
    image_height2 = photo_image2.height()

    while True:
      coordinates2 = canvas2.coords(my_image2)
      print(coordinates2)
      if(coordinates2[0]>=(WIDTH2-image_width2) or coordinates2[0]<0):
          xVelocity2 = -xVelocity2
      if(coordinates2[1]>=(HEIGHT2-image_height2) or coordinates2[1]<0):
          yVelocity2 = -yVelocity2
      canvas2.move(my_image2,xVelocity2,yVelocity2)
      window2.update()
      time.sleep(0.01)
    window2.mainloop()














