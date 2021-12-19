from tkinter import *
import webbrowser


def robloxgame_link():
    webbrowser.open_new("https://www.roblox.com/games/2889847733/ANCIENT-OBBY-NEW-UPDATES")


root = Tk()
root.title("Application")
root.geometry("1080x720")
root.minsize(480,360)
root.iconbitmap("UIS/logo.ico")
root.config(background="#5A4DC6")
#fenêtre
frame = Frame(
    root, 
    bg="#5A4DC6" 
)
#créations de label
label_title = Label(
    frame,
    text="Ancient Obby", 
    font=("Gill Sans MT Condensed",40), 
    bg="#5A4DC6",
    fg="#FFFFFF"
)

label_subtitle = Label(
    frame,
    text="Ancient Obby is a fun roblox game !", 
    font=("Gill Sans MT Condensed",25), 
    bg="#5A4DC6", 
    fg="#FFFFFF"
)
roblox_button = Button(
    frame,
    text="Play ! ",
    font=("Gill Sans MT Condensed",25), 
    bg="#FFFFFF", 
    fg="#5A4DC6",
    command= robloxgame_link
)

#affichage
label_title.pack()
label_subtitle.pack()
roblox_button.pack(pady=25,fill=X)
frame.pack(expand=YES)
#caca

root.mainloop()