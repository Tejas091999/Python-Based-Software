from email.policy import default
from tkinter import *
from tkinter import font
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, askopenfilenames,asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None 
    Textarea.delete(1.0,END)
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None 
    else:
        root.title(os.path.basename(file)+"-Notepad")
        Textarea.delete(1.0,END)
        f = open(file,"r")
        Textarea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None 
        else:
            f = open(file,"w")
            f.write(Textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
            print("File Saved")
    else:
        f= open(file,"w")
        f.write(Textarea.get(1.0,END))
        f.close()
def exitApp():
    root.destroy()
def cut():
    Textarea.event_generate(("<<Cut>>"))
def copy():
    Textarea.event_generate(("<<Copy>>"))
def paste():
    Textarea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","Notepad By Tejas!!")
if __name__=="__main__":
    root = Tk()
    root.title("Untitled Notepad")
    root.geometry("644x788")
    Textarea=Text(root,font="lucida 13")
    file = None
    Textarea.pack(fill=BOTH,expand=True)
#FILE MENU STARTS
#Creating menu bar
    MenuBar=Menu(root)
    FileMenu=Menu(MenuBar,tearoff=0)
    FileMenu.add_command(label="New",command="newFile")
#To open the existing file
    FileMenu.add_command(label="Open",command="openFile")
#To save the current file
    FileMenu.add_command(label="Save",command="saveFile")
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command="exitApp")
    MenuBar.add_cascade(label="File",menu=FileMenu)
#EDIT MENU STARTS
    EditMenu=Menu(MenuBar,tearoff=0)
#To Cut,Copy,Paste
    EditMenu.add_command(label="Cut",command="cut")
    EditMenu.add_command(label="Copy",command="copy")
    EditMenu.add_command(label="Paste",command="paste")
    MenuBar.add_cascade(label="Edit",menu=EditMenu)
#HELP MENU STARTS
    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command="about")
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    root.config(menu=MenuBar)
#ADDING SCROLL BAR
    Scroll = Scrollbar(Textarea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=Textarea.yview)
    Textarea.config(yscrollcommand=Scroll.set)

    root.mainloop() 