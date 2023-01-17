#BUILDING MAINTIENANCE MANAGENMENT
from tkinter import *
from tkinter.ttk import Labelframe
from tkinter import font
class Maintenance():
    def __init__(self,root):
          self.root = root
          self.root.geometry("1302x700+0+0")
          self.root.title("Building Maintenance")
          bg_color = "#074463"
          title= Label(self.root,text="Building Maintenance",bd=12,relief=GROOVE,bg="black",fg="light blue",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

#VARIABLES 
#WING A   
          self.E_A101=IntVar()
          self.W_A101=IntVar()
          self.G_A101=IntVar()
          self.C_A101=IntVar()

          self.E_A102=IntVar()
          self.W_A102=IntVar()
          self.G_A102=IntVar()
          self.C_A102=IntVar()

          self.E_A103=IntVar()
          self.W_A103=IntVar()
          self.G_A103=IntVar()
          self.C_A103=IntVar()

          self.E_A104=IntVar()
          self.W_A104=IntVar()
          self.G_A104=IntVar()
          self.C_A104=IntVar()
#WING B
          self.E_B101=IntVar()
          self.W_B101=IntVar()
          self.G_B101=IntVar()
          self.C_B101=IntVar()

          self.E_B102=IntVar()
          self.W_B102=IntVar()
          self.G_B102=IntVar()
          self.C_B102=IntVar()

          self.E_B103=IntVar()
          self.W_B103=IntVar()
          self.G_B103=IntVar()
          self.C_B103=IntVar()

          self.E_B104=IntVar()
          self.W_B104=IntVar()
          self.G_B104=IntVar()
          self.C_B104=IntVar()
#TOTAL VARIBLES
          self.total_E=IntVar()
          self.total_W=IntVar()
          self.total_G=IntVar()
          self.total_C=IntVar()

          self.total_E_B=IntVar()
          self.total_W_B=IntVar()
          self.total_G_B=IntVar()
          self.total_C_B=IntVar()
#MEMBER DETAILS 
          F1=LabelFrame(self.root,text="Member Details",font=("times new roman",15,"bold"),fg = "light blue",bg ="black",bd=10,relief=GROOVE)
          F1.place(x=0,y=73,relwidth=1)
          cname_label=Label(F1,text="Member Name:",bg="black",font=("times new roman",18,"bold"),fg="white").grid(row=0,column=0,padx=20,pady=5)
          cname_txt = Entry(F1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

          cphn_label=Label(F1,text="Contact No:",bg="black",font=("times new roman",18,"bold"),fg="white").grid(row=0,column=2,padx=20,pady=5)
          cphn_txt = Entry(F1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

          cflat_label=Label(F1,text="Flat No:",bg="black",font=("times new roman",18,"bold"),fg="white").grid(row=0,column=4,padx=20,pady=5)
          cflat_txt = Entry(F1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

          bill_btn=Button(F1,text="Search",width=10,command=None,bd=7,font="arial 12 bold",fg="black",bg="lightblue").grid(row=0,column=6,pady=10,padx=10)
#BUILDING A 
          F2=LabelFrame(self.root,text="WING A",font=("times new roman", 15 ,"bold"),fg="light blue",bg="black",bd=10,relief=GROOVE)
          F2.place(x=0,y=172,width=650,height=350)
          lightbill_label=Label(F2,text="Elecricity",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=0,column=1,padx=10,pady=10)
          waterbill_label=Label(F2,text="WaterBill",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=0,column=2,padx=10,pady=10)
          gasbill_label=Label(F2,text="GasBill",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=0,column=3,padx=10,pady=10)
          Cleaningbill_label=Label(F2,text="CleaningBill",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=0,column=4,padx=10,pady=10)

          A101_label=Label(F2,text="A 101",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
          A101_E=Entry(F2,width=8,textvariable=self.E_A101,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
          A101_W=Entry(F2,width=8,textvariable=self.W_A101,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=1,column=2,padx=10,pady=10)
          A101_G=Entry(F2,width=8,textvariable=self.G_A101,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=10)
          A101_C=Entry(F2,width=8,textvariable=self.C_A101,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=1,column=4,padx=10,pady=10)

          A102_label=Label(F2,text="A 102",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
          A102_E=Entry(F2,width=8,textvariable=self.E_A102,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
          A102_W=Entry(F2,width=8,textvariable=self.W_A102,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=2,column=2,padx=10,pady=10)
          A102_G=Entry(F2,width=8,textvariable=self.G_A102,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=10)
          A102_C=Entry(F2,width=8,textvariable=self.C_A102,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=2,column=4,padx=10,pady=10)

          A103_label=Label(F2,text="A 103",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
          A103_E=Entry(F2,width=8,textvariable=self.E_A103,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
          A103_W=Entry(F2,width=8,textvariable=self.W_A103,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=3,column=2,padx=10,pady=10)
          A103_G=Entry(F2,width=8,textvariable=self.G_A103,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=3,column=3,padx=10,pady=10)
          A103_C=Entry(F2,width=8,textvariable=self.C_A103,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=3,column=4,padx=10,pady=10)

          A104_label=Label(F2,text="A 104",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
          A104_E=Entry(F2,width=8,textvariable=self.E_A104,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
          A104_W=Entry(F2,width=8,textvariable=self.W_A104,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=4,column=2,padx=10,pady=10)
          A104_G=Entry(F2,width=8,textvariable=self.G_A104,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=4,column=3,padx=10,pady=10)
          A104_C=Entry(F2,width=8,textvariable=self.C_A104,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=4,column=4,padx=10,pady=10)
#BUILDING B 
          F3=LabelFrame(self.root,text="WING B",font=("times new roman", 15 ,"bold"),fg="light blue",bg="black",bd=10,relief=GROOVE)
          F3.place(x=650,y=172,width=650,height=350)
          lightbill_label=Label(F3,text="Elecricity",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=0,column=1,padx=10,pady=10)
          waterbill_label=Label(F3,text="WaterBill",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=0,column=2,padx=10,pady=10)
          gasbill_label=Label(F3,text="GasBill",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=0,column=3,padx=10,pady=10)
          Cleaningbill_label=Label(F3,text="CleaningBill",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=0,column=4,padx=10,pady=10)

          B101_label=Label(F3,text="B 101",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
          B101_E=Entry(F3,width=8,textvariable=self.E_B101,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
          B101_W=Entry(F3,width=8,textvariable=self.W_B101,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=1,column=2,padx=10,pady=10)
          B101_G=Entry(F3,width=8,textvariable=self.G_B101,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=10)
          B101_C=Entry(F3,width=8,textvariable=self.C_B101,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=1,column=4,padx=10,pady=10)

          B102_label=Label(F3,text="B 102",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
          B102_E=Entry(F3,width=8,textvariable=self.E_B102,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
          B102_W=Entry(F3,width=8,textvariable=self.W_B102,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=2,column=2,padx=10,pady=10)
          B102_G=Entry(F3,width=8,textvariable=self.G_B102,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=10)
          B102_C=Entry(F3,width=8,textvariable=self.C_B102,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=2,column=4,padx=10,pady=10)

          B103_label=Label(F3,text="B 103",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
          B103_E=Entry(F3,width=8,textvariable=self.E_B103,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
          B103_W=Entry(F3,width=8,textvariable=self.W_B103,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=3,column=2,padx=10,pady=10)
          B103_G=Entry(F3,width=8,textvariable=self.G_B103,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=3,column=3,padx=10,pady=10)
          B103_C=Entry(F3,width=8,textvariable=self.C_B103,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=3,column=4,padx=10,pady=10)

          B104_label=Label(F3,text="B 104",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
          B104_E=Entry(F3,width=8,textvariable=self.E_B104,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
          B104_W=Entry(F3,width=8,textvariable=self.W_B104,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=4,column=2,padx=10,pady=10)
          B104_G=Entry(F3,width=8,textvariable=self.G_B104,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=4,column=3,padx=10,pady=10)
          B104_C=Entry(F3,width=8,textvariable=self.C_B104,font="arial 15 bold",bd=8,relief=SUNKEN).grid(row=4,column=4,padx=10,pady=10)
#TOTAL FRAME
#TOTAL OF WING A
          F4=LabelFrame(self.root,text="Total Bill A",font=("times new roman", 15 ,"bold"),fg="light blue",bg="black",bd=10,relief=GROOVE)
          F4.place(x=0,y=523,width=650,height=177)
          totalE_label=Label(F4,text="Total Elecircity",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
          totalE_E=Entry(F4,width=5,textvariable=self.total_E,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

          totalW_label=Label(F4,text="Total WaterBill",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
          totalW_W=Entry(F4,width=5,textvariable=self.total_W,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

          totalG_label=Label(F4,text="Total GasBill",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=0,column=2,padx=10,pady=10,sticky="w")
          totalG_G=Entry(F4,width=5,textvariable=self.total_G,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=10)

          totalC_label=Label(F4,text="Total CleaningBill",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=1,column=2,padx=10,pady=10,sticky="w")
          totalC_C=Entry(F4,width=5,textvariable=self.total_C,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=10)

          total_btn_A=Button(F4,text="Total",width=7,command=self.total_A,bd=5,font="arial 15 bold",fg="black",bg="lightblue").grid(row=1,column=4,pady=10,padx=10)
#TOTAL OF WING B
          F5=LabelFrame(self.root,text="Total Bill  B",font=("times new roman", 15 ,"bold"),fg="light blue",bg="black",bd=10,relief=GROOVE)
          F5.place(x=650,y=523,width=650,height=177)
          totalE_label=Label(F5,text="Total Elecircity",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
          totalE_E=Entry(F5,width=5,textvariable=self.total_E_B,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

          totalW_label=Label(F5,text="Total WaterBill",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
          totalW_W=Entry(F5,width=5,textvariable=self.total_W_B,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

          totalG_label=Label(F5,text="Total GasBill",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=0,column=2,padx=10,pady=10,sticky="w")
          totalG_G=Entry(F5,width=5,textvariable=self.total_G_B,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=10)

          totalC_label=Label(F5,text="Total CleaningBill",font=("times new roman",15,"bold"),fg="lightblue",bg="black").grid(row=1,column=2,padx=10,pady=10,sticky="w")
          totalC_C=Entry(F5,width=5,textvariable=self.total_C_B,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=10)

          total_btn_B=Button(F5,text="Total",width=7,command=self.total_B,bd=5,font="arial 15 bold",fg="black",bg="lightblue").grid(row=1,column=4,pady=10,padx=10)
          
#FUNCTIONALITY
    def total_A(self):
        self.E_A01=self.E_A101.get()
        self.E_A02=self.E_A102.get()
        self.E_A03=self.E_A103.get()
        self.E_A04=self.E_A104.get()
        self.total_E_A=(self.E_A01)+(self.E_A02)+(self.E_A03)+(self.E_A04)
        self.total_E.set(str(self.total_E_A))

        self.W_A01=self.W_A101.get()
        self.W_A02=self.W_A102.get()
        self.W_A03=self.W_A103.get()
        self.W_A04=self.W_A104.get()
        self.total_W_A=(self.W_A01)+(self.W_A02)+(self.W_A03)+(self.W_A04)
        self.total_W.set(str(self.total_W_A))

        self.G_A01=self.G_A101.get()
        self.G_A02=self.G_A102.get()
        self.G_A03=self.G_A103.get()
        self.G_A04=self.G_A104.get()
        self.total_G_A=(self.G_A01)+(self.G_A02)+(self.G_A03)+(self.G_A04)
        self.total_G.set(str(self.total_G_A))

        self.C_A01=self.C_A101.get()
        self.C_A02=self.C_A102.get()
        self.C_A03=self.C_A103.get()
        self.C_A04=self.C_A104.get()
        self.total_C_A=(self.C_A01)+(self.C_A02)+(self.C_A03)+(self.C_A04)
        self.total_C.set(str(self.total_C_A))
    def total_B(self):
        self.E_B01=self.E_B101.get()
        self.E_B02=self.E_B102.get()
        self.E_B03=self.E_B103.get()
        self.E_B04=self.E_B104.get()
        self.total_E_b=(self.E_B01)+(self.E_B02)+(self.E_B03)+(self.E_B04)
        self.total_E_B.set(str(self.total_E_b))

        self.W_B01=self.W_B101.get()
        self.W_B02=self.W_B102.get()
        self.W_B03=self.W_B103.get()
        self.W_B04=self.W_B104.get()
        self.total_W_b=(self.W_B01)+(self.W_B02)+(self.W_B03)+(self.W_B04)
        self.total_W_B.set(str(self.total_W_b))

        self.G_B01=self.G_B101.get()
        self.G_B02=self.G_B102.get()
        self.G_B03=self.G_B103.get()
        self.G_B04=self.G_B104.get()
        self.total_G_b=(self.G_B01)+(self.G_B02)+(self.G_B03)+(self.G_B04)
        self.total_G_B.set(str(self.total_G_b))

        self.C_B01=self.C_B101.get()
        self.C_B02=self.C_B102.get()
        self.C_B03=self.C_B103.get()
        self.C_B04=self.C_B104.get()
        self.total_C_b=(self.C_B01)+(self.C_B02)+(self.C_B03)+(self.C_B04)
        self.total_C_B.set(str(self.total_C_b)) 
      
root=Tk()
obj=Maintenance(root)
root.mainloop()
