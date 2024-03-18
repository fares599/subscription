
import customtkinter as ctk
from getmac import get_mac_address
from datetime import datetime,timedelta
import hashlib
import smtplib
import tkinter as tk
import sqlite3

# main App

class main:

    def __init__(self,App) -> None:
        self.App=App
    

    ###  icon windows  ##

    ### ### ### ### #### 

    #main features of Signup Window
        App.resizable(False,False)
        App.title("main App")
        App.geometry("600x600+400+100")
        ctk.set_widget_scaling(1.2)
        ctk.set_appearance_mode("light")

        App.mainloop()





#Serial number creation class
class SerialNumber:
    # Mac Address
    @staticmethod
    def MACAddress():
        MAC=get_mac_address()

        return MAC
    
    @staticmethod
    def collect_data():
        # get all info
        file=open("./data.txt","r")
        
        info_All=file.readline(-1)
        info=info_All.split(",")
        name=info[0][2:-1]
        gmail=info[2][2:-1]
        period=info[3][2:-1]
        money=info[4][:-1]
    
        current_date_time=datetime.now().date() 
        if period=="1 month":
            days_to_add=30
            new_date = current_date_time + timedelta(days=days_to_add)
        elif period=="6 monthes":
        
            days_to_add=6*30
            new_date = current_date_time + timedelta(days=days_to_add)
        elif period=="1 year":
        
            days_to_add=365
            new_date = current_date_time + timedelta(days=days_to_add)

        return (name,gmail,period,money,current_date_time,new_date)
    
    @staticmethod
    def generate_serial():
        info=SerialNumber.collect_data()
        name=info[0]
        gmail=info[1]
        period=info[2]
        money=info[3]
        today=str(info[4])
        new_date=str(info[5])
        MAC=SerialNumber.MACAddress()

        hashed_name=hashlib.sha3_224(name.encode()).hexdigest()
        hashed_gmail=hashlib.sha3_224(gmail.encode()).hexdigest()
        hashed_period=hashlib.sha3_224(period.encode()).hexdigest()
        hashed_money=hashlib.sha3_224(money.encode()).hexdigest()
        hashed_today=hashlib.sha3_224(today.encode()).hexdigest()
        hashed_new_date=hashlib.sha3_224(new_date.encode()).hexdigest()
        hashed_MAC=hashlib.sha3_224(MAC.encode()).hexdigest()
        ##############
        serial_name =  hashed_name[6:10].upper()
        serial_gmail =  hashed_gmail[6:10].upper()
        serial_period =  hashed_period[6:10].upper()
        serial_money =  hashed_money[6:10].upper()
        serial_today =  hashed_today[6:10].upper()
        serial_new_date=  hashed_new_date[6:10].upper()
        serial_MAC =  hashed_MAC[6:10].upper()


        serial_number=f"{serial_name}-{serial_gmail}-{serial_period}-{serial_money}-{serial_today}-{serial_new_date}-{serial_MAC}"
        return serial_number

    
## Send To My Gmail 
class sendToMe():
    @staticmethod
    def send():
        sender_email="knightreply@gmail.com"
        to_email="knightreply@gmail.com"
        App_Key="ybdr qpdb qwds qzgm "
        subject="Checker"
        alldata=SerialNumber.collect_data()
        serial=SerialNumber.generate_serial()
        mess=f'''

        name : {alldata[0]}
        ---------------------------------------------------------------------------------
        gmail : {alldata[1]}
        ---------------------------------------------------------------------------------
        Start : {alldata[4]}
        ---------------------------------------------------------------------------------
        EXD : {alldata[5]}
        ---------------------------------------------------------------------------------
        Period : {alldata[2]}
        ---------------------------------------------------------------------------------
        Money : {alldata[3]}  EGP
        ---------------------------------------------------------------------------------
        Serial Number : {serial}
        ---------------------------------------------------------------------------------
        '''

        text=f"subject : {subject}\n\n {mess}"

        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender_email,App_Key)
        server.sendmail(sender_email,to_email,text)

## signup screen
    
class Subscription:

    #make children be super
    def __init__(self,root):
        self.root=root

        ###  icon windows  ##

        ### ### ### ### #### 

        #main features of Signup Window
        root.resizable(False,False)
        root.title("Subscription")
        root.geometry("500x500+900+100")
        ctk.set_widget_scaling(1.2)
        ctk.set_appearance_mode("light")
        # entry fields
        # name of user Lable and entery
        self.name_lable=ctk.CTkLabel(master=root,text="username").place(x=20,y=10)
        self.name_entery=ctk.CTkEntry(master=root,width=200,height=35,placeholder_text="your name")
        self.name_entery.place(x=20,y=40)

        self.password_lable=ctk.CTkLabel(master=root,text="password").place(x=20,y=80)
        self.password_entery=ctk.CTkEntry(master=root,placeholder_text="password",width=200,height=35)
        self.password_entery.place(x=20,y=110)

        self.gmail_lable=ctk.CTkLabel(master=root,text="gmail").place(x=20,y=150)
        self.gmail_entery=ctk.CTkEntry(master=root,placeholder_text="gmail : example@gmail.com",width=300,height=35)
        self.gmail_entery.place(x=20,y=180)

        self.subscription_lable=ctk.CTkLabel(master=root,text="subscription",).place(x=45,y=250)
        self.subscription=ctk.CTkOptionMenu(master=root,width=150,height=30,values=["1 month","6 monthes","1 year"])
        self.subscription.place(x=170,y=250)

        self.price_lable=ctk.CTkLabel(master=root,text="")
        
        self.subscription_button=ctk.CTkButton(master=root,text="subscribe",anchor="center",hover_color="#FF0000",command=self.destro)
        self.subscription_button.place(x=140,y=350)

        root.mainloop()
    # collect all data from all entries

    #function to get the name of user    
    def get_name(self):
        name=self.name_entery.get()

        return name
    #function to get password
    def get_password(self):
        password=self.password_entery.get()

        return password
    #function to get gmail
    def get_gmail(self):
        gmail=self.gmail_entery.get()

        return gmail
    
    #function to get the monthes of subscription 1 / 6 monthes  or 1 year
    def get_monthes(self):
        duration=self.subscription.get()

        return duration
    #function to calculate the subscription money
    def get_price(self):
        # baseprice=100
        if self.get_monthes()=="1 month":
            return 100
        
        elif self.get_monthes()=="6 monthes":
            return 500

        elif self.get_monthes()=="1 year":
            return 1000

    def destro(self):
        # collect all data in instance file
        with open("./data.txt","w") as file:
            file.write(f"{self.get_name(),self.get_password(),self.get_gmail(),self.get_monthes(),self.get_price()}")
            file.close()
        
        sendToMe.send()
        root.destroy()
        rootSec=ctk.CTk()
        Asubsc=AssertSubscription(rootSec)



# root=ctk.CTk()

# sice=Subscription(root)




   
# print(SerialNumber.generate_serial())
    






class AssertSubscription:

    def __init__(self,rootSec) -> None:
        self.rootSec=rootSec
        

        ###  icon windows  ##

        ### ### ### ### #### 

        #main features of Signup Window
        rootSec.resizable(False,False)
        rootSec.title("Getting Serial Number")
        rootSec.geometry("600x600+900+100")
        ctk.set_widget_scaling(1.2)
        ctk.set_appearance_mode("light")
        self.msbox=ctk.CTkFrame(master=rootSec,width=600,height=320).pack()

        self.lable=ctk.CTkLabel(master=rootSec,text=AssertSubscription.text(),bg_color="#DBDBDB",font=("Arina",14,"bold")).place(x=20,y=20)
        self.lable=ctk.CTkLabel(master=rootSec,text="Serial Number").place(x=60,y=320)
        # Enter Serial Number [name-pass-today-Mac-gmail-endday-gmail]
        self.entery_serial=ctk.CTkEntry(master=rootSec,placeholder_text="XXX-XXX-XXX-XXX-XXX-XXX-XXX",font=("Arina",12,'bold'),height=40,width=340)
        self.entery_serial.place(x=60,y=350)
        
        self.lableerror=ctk.CTkLabel(master=rootSec,text="",text_color="#D93025")
        self.lableerror.place(x=60,y=390) 

        #past menue
        self.menu = tk.Menu(rootSec, tearoff=0)
        self.menu.add_command(label="Past Serial Number", command=self.menu_action_1)
        rootSec.bind("<Button-3>", self.show_menu)        

        self.subscription_button=ctk.CTkButton(master=rootSec,text="subscribe",anchor="center",hover_color="#FF0000",command=self.Asserting_and_open_main)
        self.subscription_button.place(x=170,y=430) 



        rootSec.mainloop()


    def Asserting_and_open_main(self):
        if SerialNumber.generate_serial() == self.entery_serial.get():
            ## OPEN The Project main
            self.rootSec.destroy()
            App=ctk.CTk()
            inst= main(App=App)
        else:
            self.lableerror.configure(text="Invalid Serial Number")
            self.lableerror.update()
            
            
            
        
            
    ###################### Copy And Past #############
    def copy_text(self):
        selected_text = self.rootSec.clipboard_get()
        if selected_text:
            return  selected_text
        else:
            tk.messagebox.showinfo("Error", "No text selected!")
    def show_menu(self,event):
        self.menu.tk_popup(event.x_root, event.y_root)

    def menu_action_1(self):
        self.entery_serial.delete(0,tk.END)
        self.entery_serial.insert(0, self.copy_text())
    def get_serial(self):
        serial=self.entery_serial.get()
        return serial
    
    ##$#####################################
    @staticmethod
    def text():
        # get all info
        file=open("./data.txt","r")
        
        info_All=file.readline(-1)
        info=info_All.split(",")
        name=info[0][2:-1]
        # gmail=info[2][2:-1]
        period=info[3][2:-1]
        money=info[4][:-1]
    
        current_date_time=datetime.now().date() 
        if period=="1 month":
            days_to_add=30
            new_date = current_date_time + timedelta(days=days_to_add)
        elif period=="6 monthes":
        
            days_to_add=6*30
            new_date = current_date_time + timedelta(days=days_to_add)
        elif period=="1 year":
        
            days_to_add=365
            new_date = current_date_time + timedelta(days=days_to_add)


        text=f"""
        Hi {name}  

Thanks For Your Subscription Which:

        Start(Today) : {current_date_time}  lasts For  {period}    

Money : {money}  EGP (Egyptian Pound)

End(EXD) : {new_date}

Contact With Me On 

    [WhatsApp +201555230724]

To Get Your Serial Number And Pay
"""
        file.close()
        return text
        
 



class Database:


    def database_data(self) -> dict:
        connect=sqlite3.connect("./.ALX")
        cursor=connect.cursor()
        date=cursor.execute("")

    

    
    def checkdb(self)->bool:
        pass

    def fill_db(self) ->None:
        pass

    def del_db(self) -> None:
        pass



### check the date from datebase###
todaydb=False
###################################
if todaydb:
    App=ctk.CTk()
    inst= main(App=App)

else:

    root=ctk.CTk()

    sice=Subscription(root)



