#Import additional packages for this repl to work properly.
import qrcode
import tkinter as tk
import random
from PIL import Image
import pyperclip

#Generating a window
window = tk.Tk()
window.title("QR Code Generator")
window.geometry("500x250")
window.resizable(False, False)
window.configure(bg="white")

#Some Variable set-ups
data = tk.StringVar()
copydata = tk.StringVar()

def QRGen(e):
  #This function is the same as GenerateQR():. This one is used for QR Generation via Enter key (when focusing on Entry box). As a difference, this function has (e) and the other one has () at the end.
  list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
  repeatValue = 8
  name = "QR_"
  while repeatValue > 0:
    name = (name + list[random.randrange(0, len(list))])
    repeatValue = (repeatValue - 1)
  
  data = entry1.get()
  img = qrcode.make(data)
  img.save(name + ".png")
  texttitle = tk.Label(text = "Sucess!", fg = "green", bg = "white", font = ("Helvetica", 10, "bold"))
  texttitle.pack()
  texttitle.place(x=83, y=130)
  text = tk.Label(text = "View the project files and download your QR Code", bg = "white", fg = "darkgray")
  text.pack()
  text.place(x=83, y=145)

  text2 = tk.Label(text = "Right click the image and click [Save As]", bg = "white", fg = "darkgray")
  text2.pack()
  text2.place(x=83, y=160)

def GenerateQR():
  #QR Code generator
  #List of available symbols to create a filename
  list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
  #Some Starter variable set-ups. RepeatValue for "Repeat" loop and Name to start generating a filename
  repeatValue = 8
  name = "QR_"
  while repeatValue > 0:
    #Filename generation
    name = (name + list[random.randrange(0, len(list))])
    repeatValue = (repeatValue - 1)
  
  #QR Code generation
  data = entry1.get()
  img = qrcode.make(data)
  img.save(name + ".png")
  texttitle = tk.Label(text = "Sucess!", fg = "green", bg = "white", font = ("Helvetica", 10, "bold"))
  texttitle.pack()
  texttitle.place(x=83, y=130)
  text = tk.Label(text = "View the project files and download your QR Code", bg = "white", fg = "darkgray")
  text.pack()
  text.place(x=83, y=145)

  text2 = tk.Label(text = "Right click the image and click [Save As]", bg = "white", fg = "darkgray")
  text2.pack()
  text2.place(x=83, y=160)


def temp_text(e):
  #Placeholder remover
  entry1.delete(0, "end")

def CopyText(e):
  #Text copying function
  copydata = entry1.get()
  pyperclip.copy(copydata)


def PasteText(e):
  #Text pasting function
  copiedData = pyperclip.paste()
  entry1.insert(copiedData)

#Text box to enter data to be encoded
entry1 = tk.Entry(bg="lightgray", width=40, textvariable = data)
#Temporary text (Placeholder)
entry1.insert(0, "Enter a value to encode here:")
entry1.pack()
entry1.place(x=85, y=50)
#Some binds like Enter key, Ctrl + C, Ctrl + V and Mouse-click to delete Placeholder
entry1.bind("<FocusIn>", temp_text)
entry1.bind("<Return>", QRGen)
entry1.bind("<Control-C>", CopyText)
entry1.bind("<Control-V>", PasteText)

#Generate the QR Code button
button = tk.Button(text="Generate QR Code", bg="#ff0000", width=37, fg="white", font=("helvetica", 9, 'bold'), command = GenerateQR, relief = "raised")
button.pack()
button.place(x=85, y=73)

#Mainloop for your window
window.mainloop()
