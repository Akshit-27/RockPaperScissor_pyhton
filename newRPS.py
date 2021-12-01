from tkinter import *
import random
from tkinter import messagebox
from PIL import Image,ImageTk
gamewin = Tk()
gamewin.resizable(False, False)
gamewin.geometry("400x400+550+200")
gamewin.title("Rock Paper Scissors Game")
gamewin.configure(bg="#d3d3d3")

user_lb = Label(gamewin,text="User's Move",bg="#D3D3D3", fg="#000000",font=("monospace",15,"bold")).place(x=30,y=20)
comp_lb = Label(gamewin,text="Computer's Move",bg="#D3D3D3", fg="#000000",font=("monospace",15,"bold")).place(x=200,y=20)

comp_possible_moves = ['rock-round-comp.jpg', 'paper-round-comp.jpg', 'scissor-round-comp.jpg']
# computer = random.choice(comp_possible_moves)

def playrock():
    print("YOU PLAYED Rock")
    computer = random.choice(comp_possible_moves)
    image1 = Image.open("rock-round-user.jpg")
    test = ImageTk.PhotoImage(image1)
    lbl1 = Label(image=test)
    lbl1.image= test
    lbl1.place(x=20,y=70)

    image2 = Image.open(computer)
    imgg = ImageTk.PhotoImage(image2)
    lbl1 = Label(image=imgg)
    lbl1.image = imgg
    lbl1.place(x=220, y=70)

    if computer == "paper-round-comp.jpg":
        mb = messagebox.showinfo("Results", "Paper Wraps Rock !!☹ YOU LOSE ☹ !!")
        print("Paper Wraps Rock !!☹ YOU LOSE ☹ !!")
    if computer == "scissor-round-comp.jpg":
        mb = messagebox.showinfo("Results", "Rock Crushes Scissor!!♕ YOU WIN ♕ !!")
        print("Rock Crushes Scissor!!♕ YOU WIN ♕ !!")
    if computer == "rock-round-comp.jpg":
        mb = messagebox.showinfo("Results", "Game Tied!")
        print("Both Played Rock!!Game Tied")

def playpaper():
    print("YOU PLAYED Paper")
    computer = random.choice(comp_possible_moves)
    image1 = Image.open("paper-round-user.jpg")
    img = ImageTk.PhotoImage(image1)
    lbl1 = Label(image=img)
    lbl1.image = img
    lbl1.place(x=20, y=70)

    image2 = Image.open(computer)
    imgg = ImageTk.PhotoImage(image2)
    lbl1 = Label(image=imgg)
    lbl1.image = imgg
    lbl1.place(x=220, y=70)
    if computer == "paper-round-comp.jpg":
        mb = messagebox.showinfo("Results", "Game Tied!")
        print("Both Played Paper!!Game Tied")
    if computer == "scissor-round-comp.jpg":
        mb = messagebox.showinfo("Results", "Scissor Cuts Paper!!☹ YOU LOSE ☹ !!")
        print("Scissor Cuts Paper!!☹ YOU LOSE ☹ !!")
    if computer == "rock-round-comp.jpg":
        mb = messagebox.showinfo("Results", "Paper Wraps Rock!! ♕ YOU WIN ♕ !!")
        print("Paper Wraps Rock!! ♕ YOU WIN ♕ !!")


def playscissor():
    print("YOU PLAYED Scissor")
    computer = random.choice(comp_possible_moves)
    print(computer)
    image1 = Image.open("scissor-round-user.jpg")
    img = ImageTk.PhotoImage(image1)
    lbl1 = Label(image=img)
    lbl1.image = img
    lbl1.place(x=20, y=70)

    image2 = Image.open(computer)
    imgg = ImageTk.PhotoImage(image2)
    lbl1 = Label(image=imgg)
    lbl1.image = imgg
    lbl1.place(x=220, y=70)
    if computer == "paper-round-comp.jpg":
        mb = messagebox.showinfo("Results", "Scissors Cuts Paper!!♕ YOU WIN ♕ !!")
        print("Scissors Cuts Paper!!♕ YOU WIN ♕ !!")
    if computer == "scissor-round-comp.jpg":
        mb = messagebox.showinfo("Results", "Game Tied!")
        print("Both Played Scissors!!Game Tied")
    if computer == "rock-round-comp.jpg":
        mb = messagebox.showinfo("Results", "Rock Crushes Scissor!!☹ YOU LOSE ☹ !!")
        print("Rock Crushes Scissor!!☹ YOU LOSE ☹ !!")

def quitgame():
    print("YOU QUITED")
    msg = messagebox.askyesno("Confirm", "Are you sure you want to quit ?")
    if (msg == True):
        gamewin.destroy()
    else:
        pass

rock_btn = Button(gamewin, text="Rock", width=10, bg="#7fcfda", font=("courier", 12, "normal"), fg="#000",command=playrock)

paper_btn = Button(gamewin, text="Paper", width=10, bg="#c9dc2f", font=("courier", 12, "normal"), fg="#000",command=playpaper)

scissor_btn = Button(gamewin, text="Scissor", width=10, bg="#ec557f", font=("courier", 12, "normal"), fg="#000",command=playscissor)

quit_btn1 = Button(gamewin, text="Quit Game ", width=36, bg="#F9E79F", font=("courier", 12, "normal"), fg="#000",command=quitgame)

rock_btn.place(x=20,y=300)
paper_btn.place(x=150,y=300)
scissor_btn.place(x=280,y=300)
quit_btn1.place(x=20,y=350)

gamewin.mainloop()