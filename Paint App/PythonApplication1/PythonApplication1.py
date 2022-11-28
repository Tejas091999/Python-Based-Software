from tkinter import *
from tkinter.ttk import Labelframe
from tkinter import Scale
from tkinter import colorchooser,filedialog,messagebox 
root=Tk()
root.title("Paint App")
root.state("zoomed")
#CANVAS
canvas=Canvas(root,bg="white",bd=5,relief=GROOVE,height=600,width=1300)
canvas.place(x=100,y=100)
#VARIABLES
eraser_color="white"
pen_color="black"
#FUNCTIONS
def canvas_color():
    global eraser_color
    color=colorchooser.askcolor()
    canvas.configure(bg=color[1])
    eraser_color=color[1]
def save():
    file_name=filedialog.asksaveasfilename(defaultextension=".jpg")
    x=root.winfo_rootx()+canvas.winfo_x()
    y=root.winfo_rooty()+canvas.winfo_y()
    x1=x+canvas.winfo_width()
    y1=y+canvas.winfo_height()
    #ImageGrab.grab().crop((x,y,x1,y1).save(file_name))
    messagebox.showinfo("Paint Notificaton","Image is saved")
def eraser():
    global pen_color
    pen_color=eraser_color
def clear():
    canvas.delete("all")
def paint():
   x1,y1=(event.x-2),(event.y-2)
   x2,y2=(event.x+2),(event.y+2)
   canvas.create_oval(x1,y1,x2,y2,fill=pen_color,width=pen_size.get())
canvs.bind("<B1-Motion",paint)
def select_color():
    global pen_color 
    pen_color= col
#CREATING FRAMES
color_frame=Labelframe(root,text="Colors",relief=RIDGE)
color_frame.place(x=0,y=0,width=400,height=50)

tool_frame=Labelframe(root,text="Tools",relief=RIDGE)
tool_frame.place(x=410,y=0,width=200,height=50)

pen_size=Labelframe(root,text="Pen size",relief=RIDGE)
pen_size.place(x=615,y=0,width=210,height=70)
colors= ["#E8DAEF","#F1C40F","#7D3C98","#1B2631","#7B241C","#F4D03F","#34495E","#D35400","#626567","#58D68D","#154360"]
i=j=0
for color in colors:
    Button(color_frame,bd=3,relief=RIDGE,width=3,bg=color,command=lambda col=color:select_color(col).grid(row=j,column=i,padx=1)
    i=i+1
#CREATING TOOL BUTTON
canvas_color_b1=Button(tool_frame,text="Canvas",bd=4,relief=RIDGE,command=canvas_color)
canvas_color_b1.grid(row=0,column=0,padx=2)
save_b2=Button(tool_frame,text="Save",bd=4,relief=RIDGE,command=save)
save_b2.grid(row=0,column=1,padx=2)
eraser_b3=Button(tool_frame,text="Eraser",bd=4,relief=RIDGE,command=eraser)
eraser_b3.grid(row=0,column=2,padx=2)
clear_b4=Button(tool_frame,text="Clear",bd=4,relief=RIDGE,command=clear) 
clear_b4.grid(row=0,column=3,padx=2)
#PEN AND ERASER SIZE
pen_size=Scale(pen_size,orient=HORIZONTAL,from_=0,to=50,length=170)
pen_size.grid(row=0,column=0)
root.mainloop()
