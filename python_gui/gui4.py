#!/usr/bin/python	
from tkinter import *  # imports the Tkinter lib
import RPi.GPIO as GPIO  # imports the GPIO lib

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

root = Tk()  # create the root object
root.wm_title("LED GUI")  # sets title of the window
root.configure(bg="#CCFFFF")  # change the background color
root.attributes("-fullscreen", True)  # set to fullscreen

def gpiogui(p,labelset,ledButtset,r1,c1,r2,c2):
    GPIO.setup(p, GPIO.OUT)

    labelset = Label(root, text="start", font="Vernada 26 bold",
                    fg="#000",
                    bg="#FFFF33")

    def btnClicker():
        ledButtset["text"] = "switch" + str(p)
        # label_2["text"]="LED "+ str(a) + status
        if GPIO.input(p):
            GPIO.output(p, GPIO.LOW)
            status = " OFF"
            labelset["text"] = "LED " + str(p) + " OFF"
            labelset["fg"] = "#606060"
            labelset["bg"] = "#E0E0E0"
        else:
            GPIO.output(p, GPIO.HIGH)
            status = " ON"
            labelset["text"] = "LED " + str(p) + " ON"
            labelset["fg"] = "#000"
            labelset["bg"] = "#FFFF33"

    ledButtset = Button(root, text="switch" + str(p), background="#FF8000",
                        command=btnClicker, height=3, width=15, font="Arial 16 bold")

    ledButtset.grid(row=r1, column=c1)
    labelset.grid(row=r2, column=c2)




def btnExit():
    root.destroy()

def end_fullscreen(event):
    root.attributes("-fullscreen", False)


label_1 = Label(root, text="Raspberry Pi GUI", font="Verdana 18 bold",
                fg="#000",
                bg="#99B898",
                pady=20,
                padx=40)
exitButton = Button(root, text="Exit", background="#FF0000",
                    command=btnExit, height=5, width=15, font="Arial 16 bold") # C06C84



label_1.grid(row=0, column=0)

label_2 = Label(root)
button1 = Button(root)
gpiogui(16,label_2,button1,1,0,1,1)

label_3 = Label(root)
button2 = Button(root)
gpiogui(20,label_3,button2,2,0,2,1)

label_4 = Label(root)
button3 = Button(root)
gpiogui(21,label_4,button3,3,0,3,1)

exitButton.grid(row=4, column=0)



root.bind("<Escape>", end_fullscreen)
root.mainloop()  # starts the GUI loop
