from tkinter import *
import os
import sys
import random
import tkinter.messagebox

colors =['Black','Red','Blue','Green','Pink','Purple','Brown','Yellow','Orange','White']
score=0
timeleft=30
class label:
    def __init__(self, master):
        self.master = master
        master.title("Think you know your colors?")

        self.label = Label(master, text="Type in the color of the words, "+ "\n" +" not the word displayed!")
        self.start = Label(master, text="Press enter or click start to begin")
        self.timeLabel = Label(master, text="Time left: " + str(timeleft), font=('Times New Roman', 12))
        self.colorlabel = Label(master, font=('Times New Roman', 60))
        self.status= Label(master,text="This program about to start...", bd=1, relief=SUNKEN, anchor=W)

        self.label.pack()
        self.start.pack()
        self.timeLabel.pack()
        self.colorlabel.pack()
        self.status.pack(side=BOTTOM,fill=X)
class button:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()

        self.startButton = Button(master, text="Start")
        self.startButton.pack(side=RIGHT)

        self.quitButton=Button(master, text ="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def restart(self,master):
        self.restart_button = Button(master, text="Click to Restart Game", command=self.restart)
        self.restart_button.pack()


def startGame(Event):
    if timeleft == 30:
        countdown()
    nextColor()

root = Tk()
root.geometry("375x250")
b=button(root)
l=label(root)
entry = Entry(root)
entry.pack()
entry.focus_set()

def nextColor():
    global score
    global timeleft
    if timeleft > 0:
        entry.focus_set()
    if entry.get().lower() == colors[1].lower():
        score += 1
    entry.delete(0, END)
    random.shuffle(colors)
    l.label.config(fg=str(colors[1]), text=str(colors[0]),font="times 18")
    l.start.config(text="Score: " + str(score))

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        l.timeLabel.config(text="Time left: " + str(timeleft))
        l.label.after(1000, countdown)
        if timeleft<20 and timeleft>11:
            print("Your down to 20 seconds")
        if timeleft<10 and timeleft>0:
            print("Hurry!! you only have 10 seconds left")
        if timeleft==0:
            tkinter.messagebox.showinfo("GameOver!!" ,"Your Score is: " + str(score))
            #tkinter.messagebox.showinfo("surprise!!" ,"Guess what i got to work")
            answer= tkinter.messagebox.askquestion("Restart?", "Would like to restart?")
            if answer == 'yes':
              restart()

def restart():
    python=sys.executable
    os.execl(python, python, * sys.argv)


root.bind('<Return>', startGame)
root.bind('<Button-1>',startGame)

root.mainloop()