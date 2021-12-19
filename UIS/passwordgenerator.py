import string
from random import randint, choice
from tkinter import *

passwordmax = 20
def changepasswordmaxlenght(n): 
    global passwordmax 
    passwordmax = n
    print(n)

def generatepassword():
    all_chars = string.ascii_letters + string.digits
    password = "".join(choice(all_chars) for x in range(0,int(passwordmax)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    print(passwordmax)


colorbg = "#2D5C95"

root = Tk()
root.title("Générateur de mot de passe")
root.geometry("1080x720")
root.config(bg=colorbg)

frame = Frame(
    root,
    bg=colorbg
)

#création d'images
width = 300
height = 300
image = PhotoImage(file="UIS/lock.png").zoom(15).subsample(32)
canvas = Canvas(
    frame, 
    width= width,
    height= height,
    bg=colorbg,
    bd=0,
    highlightthickness=0
)

canvas.create_image(width / 2 , height / 2, image=image)
canvas.grid(row=0,column=0,sticky=W)
#création d'une sous boite
right_frame = Frame(
    frame,
    bg=colorbg
)
right_frame.grid(row=0,column=1,sticky=W)

#création de titre
labeltile = Label(
    right_frame,
    text="Mot de passe",
    font=("Helvetica",20),
    bg=colorbg,
    fg="white"
)
labeltile.pack()
#création d'un champ/entrée/input
password_entry = Entry(
    right_frame,
    font=("Helvetica",20),
    bg=colorbg,
    fg="white"
)
password_entry.pack()
#création d'un bouton
generatepasswordbutton = Button(
    right_frame,
    text="Génerer",
    font=("Helvetica",20),
    bg=colorbg,
    fg="white",
    command=generatepassword
)
generatepasswordbutton.pack(fill=X)
scale_password_length = Scale(
    right_frame,
    orient='horizontal', 
    from_=4, 
    to=20,
    resolution=2, 
    tickinterval=16,
    length=100, 
    label="Password length", 
    bg=colorbg,
    fg="white",
    highlightthickness=0, 
    command=changepasswordmaxlenght
)

scale_password_length.pack(expand=True)

#place la right_frame à droite de la frame principale


 
#affiche la frame
frame.pack(expand=YES)

#création d'un menu
menu_bar = Menu(root)
file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Nouveau",command=generatepassword)
file_menu.add_command(label="Quitter",command=root.quit)
menu_bar.add_cascade(label="Fichier",menu=file_menu)
root.config(menu=menu_bar)



root.mainloop()