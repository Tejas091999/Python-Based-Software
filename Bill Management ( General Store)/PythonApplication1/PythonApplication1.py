
from tkinter import*
from tkinter.ttk import Labelframe
from turtle import title
import math,random,os
from tkinter import messagebox
class Bill_app():
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title= Label(self.root,text="Billing software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
#VARIABLES
#Cosmetics Varaiables
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.lotion=IntVar()
#Grocery Variables
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
#Cold Drink Variables
        self.maza=IntVar()
        self.coke=IntVar()
        self.frooti=IntVar()
        self.thumps_up=IntVar()
        self.limca=IntVar()
        self.spirit=IntVar()
#Total Product Price
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
#Customer
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

#CUSTOMER DETAIL FRAME
        F1=LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),fg = "gold",bg = bg_color,bd=10,relief=GROOVE)
        F1.place(x=0,y=80,relwidth=1)
        cname_label=Label(F1,text="Customer Name:",bg=bg_color,font=("times new roman",18,"bold"),fg="white").grid(row=0,column=0,padx=20,pady=5)
        cname_txt = Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphn_label=Label(F1,text="Contact No:",bg=bg_color,font=("times new roman",18,"bold"),fg="white").grid(row=0,column=2,padx=20,pady=5)
        cphn_txt = Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        cbill_label=Label(F1,text="Bill Number:",bg=bg_color,font=("times new roman",18,"bold"),fg="white").grid(row=0,column=4,padx=20,pady=5)
        cbill_txt = Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

        bill_btn=Button(F1,text="Search",width=10,command=self.find_bill,bd=7,font="arial 12 bold",fg="black").grid(row=0,column=6,pady=10,padx=10)
#COSMETICS FRAME
        F2=LabelFrame(self.root,text="Cosmetics",font=("times new roman", 15 ,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE)
        F2.place(x=5,y=180,width=325,height=390)

        bath_label=Label(F2,text="Bath Soap",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_label=Label(F2,text="Face Cream",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_wash_label=Label(F2,text="Face Wash",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_wash_txt=Entry(F2,width=10,textvariable=self.face_wash,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        hair_s_label=Label(F2,text="Hair Spray",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hair_gel_label=Label(F2,text="Hair Gel",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_gel_txt=Entry(F2,width=10,textvariable=self.gel,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_l_label=Label(F2,text="Body Lotion",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_l_txt=Entry(F2,width=10,textvariable=self.lotion,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
#GROCERIES FRAME
        F3=LabelFrame(self.root,text="Groceries",font=("times new roman", 15 ,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE)
        F3.place(x=340,y=180,width=325,height=390)

        rice_label=Label(F3,text="Rice",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,width=10,textvariable=self.rice,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        food_oil_cream_label=Label(F3,text="Food Oil",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        food_oil_txt=Entry(F3,width=10,textvariable=self.food_oil,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        daal_wash_label=Label(F3,text="Daal",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        daal_wash_txt=Entry(F3,width=10,textvariable=self.daal,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        wheat_label=Label(F3,text="Wheat",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        wheat_txt=Entry(F3,width=10,textvariable=self.wheat,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        sugar_label=Label(F3,text="Sugar",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        sugar_txt=Entry(F3,width=10,textvariable=self.sugar,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        tea_label=Label(F3,text="Tea",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        tea_txt=Entry(F3,width=10,textvariable=self.tea,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
#COLD DRINK FRAME
        F4=LabelFrame(self.root,text="Cold Drinks",font=("times new roman", 15 ,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE)
        F4.place(x=670,y=180,width=325,height=390)

        maza_label=Label(F4,text="Maza",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        maza_txt=Entry(F4,width=10,textvariable=self.maza,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        coke_label=Label(F4,text="Coke",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        coke_txt=Entry(F4,width=10,textvariable=self.coke,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        frooti_label=Label(F4,text="Frooti",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        frooti_txt=Entry(F4,width=10,textvariable=self.frooti,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        thumps_up_label=Label(F4,text="Thumps up",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        thumps_up_txt=Entry(F4,width=10,textvariable=self.thumps_up,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        limca_label=Label(F4,text="Limca",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        limca_txt=Entry(F4,width=10,textvariable=self.limca,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        spirit_label=Label(F4,text="Spirit",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        spirit_txt=Entry(F4,width=10,textvariable=self.spirit,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
#BILL AREA
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1000,y=180,width=350,height=390)
        bill_title = Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill = Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
#BUTTON FRAME
        F6=LabelFrame(self.root,text="Bill Menu",font=("times new roman", 15 ,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE)
        F6.place(x=0,y=560,relwidth=1,height=140)

        tc_label=Label(F6,text="Total Cosmestic Price",font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=20,pady=1,sticky="w")
        tc_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        tg_label=Label(F6,text="Total Groceries Price",font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=20,pady=1,sticky="w")
        tg_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
        
        cd_label=Label(F6,text="Total Cold Drink Price",font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=20,pady=1,sticky="w")
        cd_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        ct_label=Label(F6,text="Cosmestic Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=2,padx=20,pady=1,sticky="w")
        ct_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        gt_label=Label(F6,text="Groceries Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=2,padx=20,pady=1,sticky="w")
        gt_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        dt_label=Label(F6,text="Cold Drink Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=2,padx=20,pady=1,sticky="w")
        dt_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
#BUTTON FRAME 2
        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=740,width=585,height=105)

        total_btn=Button(btn_f,text="Total",command=self.total,bg="cadetblue",fg="white",pady=5,width=8,bd=5,font="arail 15 bold").grid(row=0,column=0,padx=15,pady=15)
        bill_btn=Button(btn_f,text="Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=5,width=8,bd=5,font="arail 15 bold").grid(row=0,column=1,padx=15,pady=15)
        clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",pady=5,width=8,bd=5,font="arail 15 bold").grid(row=0,column=2,padx=15,pady=15)
        exit_btn=Button(btn_f,text="Exit",command=self.exit_app,bg="cadetblue",fg="white",pady=5,width=8,bd=5,font="arail 15 bold").grid(row=0,column=3,padx=15,pady=15)
#FUNCTIONALITY
#========Total========
    def total(self):
        self.so_p=self.soap.get()*40
        self.f_c=self.face_cream.get()*120
        self.f_w=self.face_wash.get()*60
        self.s_p =self.spray.get()*180
        self.g_e=self.gel.get()*140
        self.l_o=self.lotion.get()*180
        self.total_cosmetic_price=(float(self.so_p)+
                                       (self.f_c)+
                                       (self.f_w)+
                                       (self.s_p)+
                                       (self.g_e)+
                                       (self.l_o))
        self.cosmetic_price.set(str(self.total_cosmetic_price))
        self.c_tax=self.total_cosmetic_price*0.05
        self.cosmetic_tax.set(str(self.c_tax))

        self.ri_p=self.rice.get()*60
        self.fo_p=self.food_oil.get()*150
        self.da_p=self.daal.get()*100
        self.wh_p=self.wheat.get()*180
        self.su_p=self.sugar.get()*120
        self.te_p=self.tea.get()*60
        self.total_grocery_price=(float(self.ri_p)+
                                       (self.fo_p)+
                                       (self.da_p)+
                                       (self.wh_p)+
                                       (self.su_p)+
                                       (self.te_p))
        self.grocery_price.set(str(self.total_grocery_price))
        self.g_tax=self.total_grocery_price*0.05
        self.grocery_tax.set(str(self.g_tax))

        self.maz_p=self.maza.get()*40
        self.cok_p=self.coke.get()*35
        self.fro_p=self.frooti.get()*20
        self.thu_p=self.thumps_up.get()*45
        self.lim_p=self.limca.get()*40
        self.spi_p=self.spirit.get()*35
        self.total_cold_drink_price=(float(self.maz_p)+
                                       (self.cok_p)+
                                       (self.fro_p)+
                                       (self.thu_p)+
                                       (self.lim_p)+
                                       (self.spi_p))
        self.cold_drink_price.set(str(self.total_cold_drink_price))
        self.cd_tax =self.total_cold_drink_price*0.05
        self.cold_drink_tax.set(str(self.cd_tax))

        self.total_bill=float(self.total_cosmetic_price + 
                              self.total_grocery_price + 
                              self.total_cold_drink_price +
                              self.c_tax + 
                              self.g_tax +
                              self.cd_tax)
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome To The Shop")
        self.txtarea.insert(END,"\n======================================")
        self.txtarea.insert(END,f"\nBill Number:{self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name:{self.c_name.get()} ")
        self.txtarea.insert(END,f"\nPhone Number:{self.c_phone.get()} ")
        self.txtarea.insert(END,"\n======================================")
        self.txtarea.insert(END,"\n Products\t\tQTY\t\tPrice")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are not given")
        else:
            self.welcome_bill()
    #CONDITIONS (COSMETICS)
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.so_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.f_c}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.f_w}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.s_p}")
            if self.gel.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t{self.gel.get()}\t\t{self.g_e}")
            if self.lotion.get()!=0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t{self.lotion.get()}\t\t{self.l_o}")
    #CONDITIONS (GROCERIES)
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.ri_p}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.fo_p}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.da_p}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.wh_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.su_p}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.te_p}")
    #CONDITIONS (COLD DRINKS)
            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.maz_p}")
            if self.coke.get()!=0:
                self.txtarea.insert(END,f"\n Coke\t\t{self.coke.get()}\t\t{self.cok_p}")
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.fro_p}")
            if self.thumps_up.get()!=0:
                self.txtarea.insert(END,f"\n Thumps_up\t\t{self.thumps_up.get()}\t\t{self.thu_p}")
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.lim_p}")
            if self.spirit.get()!=0:
                self.txtarea.insert(END,f"\n Spirit\t\t{self.spirit.get()}\t\t{self.spi_p}")

            self.txtarea.insert(END,f"\n--------------------------------------")
            if self.cosmetic_tax.get()!="0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="0.0":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="0.0":
                self.txtarea.insert(END,f"\n Cold Drink Tax\t\t\t\t{self.cold_drink_tax.get()}")
            self.txtarea.insert(END,f"\n--------------------------------------")
            self.txtarea.insert(END,f"\n Total Bill\t\t\t\t{self.total_bill}")
            self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
        else:
            return
    def find_bill(self):
        present ="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No")
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to clear?")
        if op>0:
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.lotion.set(0)
    #Grocery Variables
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
    #Cold Drink Variables
            self.maza.set(0)
            self.coke.set(0)
            self.frooti.set(0)
            self.thumps_up.set(0)
            self.limca.set(0)
            self.spirit.set(0)
    #Total Product Price
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
    #Customer
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()

        
root = Tk()
obj = Bill_app(root)
root.mainloop()