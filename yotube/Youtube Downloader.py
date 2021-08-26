from tkinter import *
import os
import pathlib
def download_click():
    lnk=Entry.get(e1)
    ch=Entry.get(e2)
    os.chdir(pathlib.Path(__file__).parent.resolve())
    comand="youtube-dl "+ch+' '+'"' +lnk+'"'
    os.system("start cmd /K "+comand )

    # # asd="'youtube-dl "https://www.youtube.com/watch?v=zKVIM-lnauo&list=PLftLUHfDSiZ7-RAsH8NskS7AYofykW_WN&index=1"'"
    



def show_choice():

    if (var.get() ==1 ):
           e2.insert('end' ,' --no-playlist ')
    elif(var.get() ==2) :
         e2.insert('end' ,' --playlist-start ')
    elif(var.get() ==3) :
             e2.insert('end' ,' --playlist-end ')
    elif(var.get() ==4) :
             e2.insert('end' ,' --write-description ')   
    elif(var.get() ==5) :
             e2.insert('end' ,' --write-sub --sub-lang en-GB,ar,en ')
    elif(var.get() ==6) :
             e2.insert('end' ,' --extract-audio --audio-format mp3 ')         


root = Tk()
root.title('Youtube Downloader')
root.geometry("500x500+100+20")
lbl = Label(root, text="Youtube Link", font=("Arial Bold", 15))
lbl.grid(column=0, row=0)
e1 = Entry(root,width = 50)
e1.grid(row=0, column=1)
e2 = Entry(root,width = 50)
e2.grid(row=1, column=1)
lbl2 = Label(root, text="any command", font=("Arial Bold", 15))
lbl2.grid(column=0, row=1)

var = IntVar()


R1 = Radiobutton(root, text="no play list", variable=var, value=1,command=show_choice)
R1.grid(row=2, column=0)
R2 = Radiobutton(root, text="start", variable=var, value=2,command=show_choice)
R2.grid(row=2, column=1)
R3 = Radiobutton(root, text="end", variable=var, value=3,command=show_choice)
R3.grid(row=2, column=2)
R4 = Radiobutton(root, text="write description", variable=var, value=4,command=show_choice)
R4.grid(row=3, column=0)
R5 = Radiobutton(root, text="write subtitle", variable=var, value=5,command=show_choice)
R5.grid(row=3, column=1)
R6 = Radiobutton(root, text="mp3", variable=var, value=6,command=show_choice)
R6.grid(row=3, column=2)
btn = Button(root, text="Click Me", command=download_click)
btn.grid(column=1, row=7)


root.mainloop()
