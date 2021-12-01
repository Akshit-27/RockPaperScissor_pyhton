from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import time
window=Tk()
window.resizable(False, False)
window.geometry("400x400")
window.title("Rock Paper Scissors Game")
window.configure(bg="#d3d3d3")

user_lb = Label(window,text="User's Move",bg="#D3D3D3", fg="#000000",font=("monospace",15,"bold")).place(x=30,y=20)
comp_lb = Label(window,text="Computer's Move",bg="#D3D3D3", fg="#000000",font=("monospace",15,"bold")).place(x=200,y=20)

res_lb =  Label(window,text="",bg="#D3D3D3", fg="#000000",font=("monospace",15,"bold"))
res_lb.place(x=100,y=280)

comp_possible_moves = ['rockp1.png', 'paper-p1.png', 'scissors-p1.png']
user_possible_moves = ['rockp2.png', 'paper-p2.png', 'scissors-p2.png']

user = random.choice(user_possible_moves)
computer = random.choice(comp_possible_moves)

img1 = ImageTk.PhotoImage(Image.open(user))
img2 = ImageTk.PhotoImage(Image.open(computer))

move_lb1 = Label(window, image=img1,width=150,height=150,bg="#d3d3d3")
move_lb2 = Label(window, image=img2,width=150,height=150,bg="#d3d3d3")

def play():
    img1=ImageTk.PhotoImage(Image.open(random.choice(user_possible_moves)))
    move_lb1.configure(image=img1)
    move_lb1.image=img1
    move_lb1.place(x=20,y=80)
    print(img1)
    if(img1=="dice_1.png"):
        print("1")

    img2 = ImageTk.PhotoImage(Image.open(random.choice(comp_possible_moves)))
    move_lb2.configure(image=img2)
    move_lb2.image = img2
    move_lb2.place(x=230,y=80)
    print("entering logic\n")
    logic()
    if(img1==img2):
        print("equal")
    # res_lb.config(text ="!!YOU WIN!!")

    # res = messagebox.askyesno("Confirm", "Do You Want to Play Again ?")
    # if (res == False):
    #     window.destroy()
    # else:
    #     pass

def exit():
    msg = messagebox.askyesno("Confirm", "Are you sure you want to exit ?")
    if (msg == True):
        window.destroy()
    else:
        pass
def logic():
    if(user==computer):
        print("Tie")
    elif((user-computer)%3==1):
        print("You win")
    else:
        print("Comp wins")
    print("returning logic\n")
    return

def another_play():
    user=random.choice(['rockp1.png', 'paper-p1.png', 'scissors-p1.png'])
    time.sleep(1)
    comp=random.choice(['rockp2.png', 'paper-p2.png', 'scissors-p2.png'])
    print(user)
    print(comp)
    if user == computer:
        print("Game Tied")

    # elif user == "rockp2.png" and computer == "paper-p1.png":
    #     print("rock win")
    #
    # elif user == "rockp2.png" and computer == "scissors-p1.png":
    #     print("scissor win")
    #
    # elif user == "paper-p2.png" and computer == "rockp1.png":
    #     print("rock win")
    #
    # elif user == "paper-p2.png" and computer == "scissors-p1.png":
    #     print("rock win")
    #
    # elif user == "scissors-p2.png" and computer == "paper-p1.png":
    #     print("scissors  win")
    #
    # elif user == "scissors-p2.png" and computer == "rockp1.png":
    #     print("rock  win")
    #
    # elif user == "scissors-p2.png" and computer == "scissors-p1.png":
    #     print("Game Tied")

    # elif user == "paper-p2.png" and computer == "paper-p1.png":
    #     print("Game Tied")


roll_btn = Button(window,text="Play Game",command=another_play,width=15,bg="black",fg="white")
roll_btn.place(x=50,y=330)
exit_btn = Button(window,text="Exit",command=exit,width=15,bg="black",fg="white").place(x=250,y=330)
my_lb = Label(window,text="Developed By Akshit Agarwal",bg="#D3D3D3", fg="black",font=("cambria",11,"italic")).place(x=110,y=375)
window.mainloop()