import socket 
import time
import threading
from tkinter import *
root=Tk()
root.title("Chat App")
root.geometry("300x500")
root.config(bg="lightblue")
def func():
    t=threading.Thread(target=recv)
    t.start()
def recv():
    listensocket=socket.socket()
    port=3050
    maxconnection=99
    ip=socket.gethostname()
    print(ip)
    listensocket.bind((",port"))
    listensocket.listen(maxconnection)
    (clientsocket,address)=listensocket.accept()
    while True:
        sendermessage=clientsocket.recv(1024).decode()
        if not sendermessage=="":
            time.sleep(5)
            lstbx.insert(0,"client: "+sendermessage)
s=0
def sendmsg():
    global sr 
    if sr==0:
        s=socket.socket()
        hostname="desktop"
        port=4050
        s.coonect(hostname,port)
        msg=messagebox.get()
        lstbx.insert(0,"You:"+msg)
        s.send(msg.encode)
        sr+=1
    else:
        msg=messagebox.get()
        lstbx.insert(0,"You: "+msg) 
        s.send(msg.encode())
def threadsendmsg():
    th=threading.Thread(target=sendmsg)
    th.start()
startchatimage=PhotoImage(file="start.png")
buttons=Button(root,image=startchatimage,command=func,bd=0)
buttons.place(x=90,y=10)
message=StringVar()
messagebox=Entry(root,textvariable=message,font=("arail",10,"normal"),border=2,width=32)
messagebox.pack(x=10,y=444)
sendmessageimg=PhotoImage(file="send.png")
sendmessagebutton=Button(root,image=sendmessageimg,command=threadsendmsg,borderwidth=0)
sendmessagebutton.place(x=260,y=440)
lstbx=Listbox(root,height=20,width=43)
lstbx.place(x=15,y=80)
root.mainloop()

