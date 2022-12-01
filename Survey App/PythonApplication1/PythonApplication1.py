from tkinter import *
from tkinter.ttk import Labelframe
class Survey:
    def __init__(self,root):
        self.root = root
        self.root.title("Survey App")
        self.root.geometry("700x400")
        self.root.config(bg="black")
        #Variables
        name=StringVar()
        age=IntVar()
        gender=StringVar()
        city=StringVar()
        occupation=StringVar()
        experience=StringVar()
        certificates=StringVar()
        hobbies=StringVar()
        feedback=StringVar()
        record = StringVar()
        def yes():
            txtarea.delete('1.0',END)
            txtarea.insert(END,"            Welcome To The Survey")
            txtarea.insert(END,f"\n ===========================================")
            txtarea.insert(END,f"\n Name: {name.get()}")
            txtarea.insert(END,f"\n Age: {age.get()} years")
            txtarea.insert(END,f"\n Gender: {gender.get()}")
            txtarea.insert(END,f"\n City: {city.get()}")
            txtarea.insert(END,f"\n Occupation: {occupation.get()}")
            txtarea.insert(END,f"\n Experience: {experience.get()}")
            txtarea.insert(END,f"\n Certificates: {certificates.get()}")
            txtarea.insert(END,f"\n Hobbies: {hobbies.get()}")
            txtarea.insert(END,f"\n Feedback: {feedback.get()}")
            txtarea.insert(END,f"\n Record: {record.get()}")
            txtarea.insert(END,f"\n===========================================")
            txtarea.insert(END,f"\n Thank you for your response!!")
        def no():
            quit()
        def reset():
            txtarea.insert(END,f"Please fill your data again")
        #Creating user name 
        f1_lbl=Label(root,text="Name: ",font=("arial" ,12," bold"),bg="black",fg="lightblue").grid(row=0,column=0)
        f1_text=Entry(root,font=("arial",12,"bold"),textvariable=name,width=10).grid(row=0,column=2,padx=5,pady=5)

        f2_lbl=Label(root,text="Age: ",font=("arial" ,12," bold"),bg="black",fg="lightblue").grid(row=1,column=0)
        f2_text=Entry(root,font=("arial",12,"bold"),textvariable=age,width=10).grid(row=1,column=2,padx=5,pady=5)

        f3_lbl=Label(root,text="Gender: ",font=("arial" ,12," bold"),bg="black",fg="lightblue").grid(row=2,column=0)
        f3_text=Entry(root,font=("arial",12,"bold"),textvariable=gender,width=10).grid(row=2,column=2,padx=5,pady=5)

        f4_lbl=Label(root,text="City: ",font=("arial" ,12," bold"),bg="black",fg="lightblue").grid(row=3,column=0)
        f4_text=Entry(root,font=("arial",12,"bold"),textvariable=city,width=10).grid(row=3,column=2,padx=5,pady=5)

        f5_lbl=Label(root,text="Occupation: ",font=("arial" ,12," bold"),bg="black",fg="lightblue").grid(row=4,column=0)
        f5_text=Entry(root,font=("arial",12,"bold"),textvariable=occupation,width=10).grid(row=4,column=2,padx=5,pady=5)

        f6_lbl=Label(root,text="Experience: ",font=("arial" ,12," bold"),bg="black",fg="lightblue").grid(row=5,column=0)
        f6_text=Entry(root,font=("arial",12,"bold"),textvariable=experience,width=10).grid(row=5,column=2,padx=5,pady=5)

        f7_lbl=Label(root,text="Certificates: ",font=("arial" ,12," bold"),bg="black",fg="lightblue").grid(row=6,column=0)
        f7_text=Entry(root,font=("arial",12,"bold"),textvariable=certificates,width=10).grid(row=6,column=2,padx=5,pady=5)

        f8_lbl=Label(root,text="Hobbies: ",font=("arial" ,12," bold"),bg="black",fg="lightblue").grid(row=7,column=0)
        f8_text=Entry(root,font=("arial",12,"bold"),textvariable=hobbies,width=10).grid(row=7,column=2,padx=5,pady=5)

        f9_lbl=Label(root,text="Feedback: ",font=("arial" ,12," bold"),bg="black",fg="lightblue").grid(row=8,column=0)
        f9_text=Entry(root,font=("arial",12,"bold"),textvariable=feedback,width=10).grid(row=8,column=2,padx=5,pady=5)

        f10_lbl=Label(root,text="Record data: ",font=("arial" ,12," bold"),bg="black",fg="lightblue").grid(row=9,column=0)
        f10_text=Entry(root,font=("arial",12,"bold"),textvariable=record,width=10).grid(row=9,column=2,padx=5,pady=5)
        #Buttons 
        yes_button=Button(root,text="Yes",font=("arail",10,"bold"),command=yes).grid(row=10,column=0)
        no_button=Button(root,text="No",font=("arial",10,"bold"),command=no).grid(row=10,column=1)
        reset_button=Button(root,text="Reset",font=("arail",10,"bold"),command=reset).grid(row=10,column=2)
        #Submission Form
        F5=Frame(root,bd=10,relief=GROOVE,bg="black")
        F5.place(x=270,y=20,width=395,height=320)
        submit_title = Label(F5,text="Submitted Form",font="arial 15 bold",bd=7,relief=GROOVE,fg="lightblue",bg="black").pack(fill=X)
        scroll_y = Scrollbar(F5,orient=VERTICAL)
        txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill = Y)
        scroll_y.config(command=txtarea.yview)
        txtarea.pack(fill=BOTH,expand=1)
    #Functionality
root=Tk()
obj=Survey(root)
root.mainloop()