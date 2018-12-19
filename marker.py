from Tkinter import *
import random
from tkinter import messagebox

color = 'black'
selectedWord = 'hey now'

#word = canvas.create_text(100,180,text=':(', font=('Calibri',60), fill='white')
#error = canvas.create_text(500,300, text="Your PC ran into a problem and needs to restart. We're just ", font=('Calibri',25), fill='white')
#error2 = canvas.create_text(465,345, text="collecting some error info, and then we'll restart for you.", font=('Calibri',25), fill='white')    

#Resets textbox
def message():
    wordChoice.config(text='')

#Selects a random word out of the list, and labels it on wordChoice for 2 seconds
def selectRandomWord():
    canvas.delete('all')
    global selectedWord
    wordList = [
    'apple','banana','dog','cat','orange', 'umbrella','scissors','lemonade','phone','burger','pizza','Obama','penny','cookie','tiger','tree',
    'train','car','bus','airplane','house','book','pencil'
    ]
    selectedWord = random.choice(wordList)
    wordChoice.config(text=selectedWord)
    wordChoice.after(2000,message)

#Paint algorithm
def paint(event):
    t = thickness_intvar.get()
    x1, y1 = (event.x - int(t)), (event.y - int(t))
    x2, y2 = (event.x + int(t)), (event.y + int(t))
    canvas.create_oval(x1,y1,x2,y2,outline='',fill=color)
    
#All methods change the color of the paintbrush
def white():
    global color
    color = 'white'    
    
def red():
    global color
    color = 'red'
    
def orange():
    global color
    color = 'orange'
    
def yellow():
    global color
    color = 'yellow'
    
def green():
    global color
    color = 'green'
    
def blue():
    global color
    color = 'blue'
    
def purple():
    global color
    color = 'purple'
    
def black():
    global color
    color = 'black'

#Function checks if the word user inputed into text box matches the chosen word
def checkGuess():
    global guess
    guess = guessWord.get()
    guessWord.delete('0',END)
    if guess == selectedWord:
        wordChoice.config(text='Yay')
    else:
        wordChoice.config(text='No')

#Initialize
root = Tk()

#Defines thickness_intvar and sets to 10
thickness_intvar = IntVar()
thickness_intvar.set(10)

#Create drawing canvas
canvas = Canvas(root, height = 300, width = 300, bg='white')
canvas.grid(row=0,column=0,columnspan=8,rowspan=3)
#canvas.pack(expand=YES, fill=BOTH)
canvas.bind('<B1-Motion>', paint)

#Start game button
startGame = Button(root, height = 2, width = 20, text='Start Game', bd=0, bg='#f29b9b', fg = 'white', command=selectRandomWord)
startGame.grid(row=0,column=8,columnspan = 2)

#Text box for user input for guessed word
guessWord = Entry(root,bd=0)
guessWord.grid(row=1,column=8, pady=10)

#Button next to the Entry that inputs answer through command checkGuess
guessWordButton = Button(root, height = 1, width = 10, text = 'Guess', bd= 0, bg='#f29b9b', fg='white', command=checkGuess)
guessWordButton.grid(row=1,column=9,pady=10)

#Label initialized that either prints the selected word or writes if the user is right or wrong in their guess
wordChoice = Label(root, height = 1, width = 10, text = '')
wordChoice.grid(row=2,column=8,columnspan=2)

#Width of all color buttons
buttonWidth = 4

#All the color buttons initialized
eraser = Button(root, height=1,width=buttonWidth,bg='white',command=white)
eraser.grid(row=4,column=0)

redButton = Button(root, height=1,width=buttonWidth,bg='red', command=red)
redButton.grid(row=4,column=1)

orangeButton = Button(root, height=1,width=buttonWidth,bg='orange', command=orange)
orangeButton.grid(row=4,column=2)

yellowButton = Button(root, height=1,width=buttonWidth,bg='yellow', command=yellow)
yellowButton.grid(row=4,column=3)

greenButton = Button(root, height=1,width=buttonWidth,bg='green', command=green)
greenButton.grid(row=4,column=4)

blueButton = Button(root, height=1,width=buttonWidth,bg='blue', command=blue)
blueButton.grid(row=4,column=5)

purpleButton = Button(root, height=1,width=buttonWidth,bg='purple', command=purple)
purpleButton.grid(row=4,column=6)

blackButton = Button(root, height=1,width=buttonWidth,bg='black', command=black)
blackButton.grid(row=4,column=7)

#Thickness slider to change thickness of paintbrush
thicknessSlider = Scale(root, from_=1, to=20, variable=thickness_intvar, label='Thickness')
thicknessSlider.grid(row=4,column=8,columnspan=2)

root.mainloop()