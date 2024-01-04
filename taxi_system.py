from tkinter import *
from tkinter import ttk
import random
import time
from PIL import ImageTk, Image
from tkinter import messagebox
# import PIL.Image
from PIL import ImageTk,Image
import mysql.connector 
import pymysql  


class client:
    def __init__(self,root):
        self.root = root
        self.root.title("Taxi Booking System")
        self.root.geometry('1050x600+320+200') 
        self.root.configure(background='black')

        global tot 

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref=StringVar()

        var2=IntVar()  #kilo meter travelling

        varl1=StringVar()    # pickup location
        varl2=StringVar()    # drop location
        varl3=StringVar()    # no of passangers
        self.reset_counter=0

        Firstname=StringVar()
        Surname=StringVar()
        Mobile=StringVar()
        Email=StringVar()

        Km=StringVar()
        total=StringVar()
        Receipt=StringVar()

        Km.set("0")
        total.set('0')


    #==========================================Define Functiom==================================================


        
        def Kilo():
            if var2.get() == 0:
                self.txtKm.configure(state=DISABLED)
                Km.set("0")
            elif var2.get() == 1 and varl1.get() != "" and varl2.get() != "":
                self.txtKm.configure(state=NORMAL)
                if varl1.get() == "Kathmandu":
                    switch ={"Bhaktapur": 15,"Pokhara": 158,"Lalitpur":8,"Kathmandu": 0}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Bhaktapur":
                    switch ={"Bhaktapur": 0,"Pokhara": 250,"Lalitpur":150,"Kathmandu": 15}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Pokhara":
                    switch ={"Bhaktapur": 250,"Pokhara": 0,"Lalitpur":150,"Kathmandu": 158}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Lalitpur":
                    switch ={"Bhaktapur": 13,"Pokhara": 150,"Lalitpur":0,"Kathmandu": 8}
                    Km.set(switch[varl2.get()])        

        def reset():
            Km.set("0")
            
            Firstname.set("")
            Surname.set("")
            Mobile.set("")
            Email.set("")

            self.txtReceipt1.delete("1.0",END)
            self.txtReceipt2.delete("1.0",END)
            self.txtReceipt3.delete("1.0",END)
            self.txtReceipt4.delete("1.0",END)

            self.ride_status.delete("1.0",END)
            
            var2.set(0)
            
            varl1.set("0")
            varl2.set("0")
            varl3.set("0")

            total.set("0")


            self.cboPickup.current(0)
            self.cboDrop.current(0)
            
            self.txtKm.configure(state=DISABLED)
            self.reset_counter=1


        def total_paid():
            c= IntVar()
            c=Km.get()
            self.tot = IntVar()
            self.tot = 50 + int(c)*14
            total.set(self.tot)
        

        def conform_booking():
            d_recept = Receipt_Ref.get()
            d_order_date = DateofOrder.get()
            d_f_name = Firstname.get()
            d_l_name = Surname.get()
            d_mobile = Mobile.get()
            d_email =  Email.get()
            d_pickup = varl1.get()
            d_drop = varl2.get()
            d_no_of_passanger = varl3.get()
            d_cost = self.tot

            self.ride_status.insert(END,"Searching Taxi")            
            
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@@@SpideX2152",
            database="spide_login"
            )

            mycursor = mydb.cursor()
            sql = "INSERT INTO client_booking (recept_id, first_name, last_name, date, mobile, email, pickup, drop_location, passanger_count, cost) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            # val = ("John", "Highway 21")
            mycursor.execute(sql,( d_recept, d_f_name, d_l_name, d_order_date, d_mobile, d_email, d_pickup, d_drop, d_no_of_passanger, d_cost))
            
            mydb.commit()
            messagebox.showinfo('Success', 'Booking Confirmed')
            mydb.close()


        def receipt():
            if self.reset_counter == 0 and Firstname.get()!="" and Surname.get()!="" and Mobile.get()!=""  and Email.get()!="":
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                self.txtReceipt3.delete("1.0",END)
                self.txtReceipt4.delete("1.0",END)
                x=random.randint(10853,500831)
                randomRef = str(x)
                Receipt_Ref.set(randomRef)

                self.txtReceipt1.insert(END,"Receipt Ref:\n")
                self.txtReceipt2.insert(END, Receipt_Ref.get() + "     \n")
                self.txtReceipt1.insert(END,'Date:\n')
                self.txtReceipt2.insert(END, DateofOrder.get() + "     \n")
                self.txtReceipt1.insert(END,'Firstname:\n')
                self.txtReceipt2.insert(END, Firstname.get() + "     \n")
                self.txtReceipt1.insert(END,'Surname:\n')
                self.txtReceipt2.insert(END, Surname.get() + "     \n")     
                self.txtReceipt3.insert(END,'Mobile:\n')
                self.txtReceipt4.insert(END, Mobile.get() + "\n")
                self.txtReceipt1.insert(END,'Email:\n')
                self.txtReceipt2.insert(END, Email.get() + "     \n")
                self.txtReceipt3.insert(END,'From:\n')
                self.txtReceipt4.insert(END, varl1.get() + "\n")
                self.txtReceipt3.insert(END,'To:\n')
                self.txtReceipt4.insert(END, varl2.get() + "      \n")
                self.txtReceipt3.insert(END,'Passanger Count:\n')
                self.txtReceipt4.insert(END, varl3.get() + "     \n")
                self.txtReceipt3.insert(END,'Total Cost:\n')
                self.txtReceipt4.insert(END, self.tot )
                
            else:
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                self.txtReceipt1.insert(END,"\nNo Input")
                
    ##### main frame

        self.MainFrame=Frame(self.root)
        self.MainFrame.pack(fill=BOTH,expand=True)
        

        Tops = Frame(self.MainFrame, bd=10,bg='black', width=1350,relief=RIDGE)
        Tops.pack(side=TOP,fill=BOTH)

        self.lblTitle=Label(Tops,font=('arial',50,'bold'),bg='black',fg='blue',text="          Book Your Taxi Today ")
        self.lblTitle.grid()

    #================================================customerframedetail=============================================================
        CustomerDetailsFrame=LabelFrame(self.MainFrame, width=1350,bg='black',height=1000,bd=20, padx=10, pady=10, relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM,fill=BOTH,expand=True)

        FrameDetails=Frame(CustomerDetailsFrame, width=1330,bg='black',height=230,bd=10,padx=10, pady=10, relief=RIDGE)
        FrameDetails.pack(side=TOP,fill=BOTH,expand=True)

        CustomerName=LabelFrame(FrameDetails, width=550,height=220,bg='black',fg='blue',bd=10, font=('arial',12,'bold'),text="Customer Info", relief=RIDGE)
        CustomerName.place(x=50,y=5)

        TravelFrame = LabelFrame(FrameDetails,bd=10, width=550,height=220, bg='black',fg='blue',font=('arial',12,'bold'),text="Booking Detail", relief=RIDGE)
        TravelFrame.place(x=460 , y=5)



    #===============================================recipt======================================================================
        Receipt_BottonFrame=LabelFrame(CustomerDetailsFrame,bd=10,bg='black', width=450,height=250,pady=5, relief=RIDGE)
        Receipt_BottonFrame.pack(side=BOTTOM,fill=BOTH,expand=True)

        ReceiptFrame=LabelFrame(Receipt_BottonFrame, width=750,height=100,bd=8, font=('arial',12,'bold'),text="Receipt", relief=RIDGE, bg='white')
        ReceiptFrame.place(x=50, y=0)

        ButtonFrame=LabelFrame(Receipt_BottonFrame, width=250,height=160,bd=4,bg='black', relief=RIDGE)
        ButtonFrame.place(x=730, y=0)
        
        TotalFrame=LabelFrame(Receipt_BottonFrame, width=150,height=160,bd=4, font=('arial',12,'bold'),text="Total Cost",bg='black',fg='blue', relief=RIDGE)
        TotalFrame.place(x=550, y=0)
        Label(TotalFrame,text='Booking cost', font=('arial',10,'bold'),bg='black',fg='white').grid(row=0, column=0)
        Label(TotalFrame,text=': Rs.50', font=('arial',10,'bold'),bg='black',fg='white').grid(row=0, column=1)
        Label(TotalFrame,text='Per Km ', font=('arial',10,'bold'),bg='black',fg='white').grid(row=1, column=0)
        Label(TotalFrame,text=': Rs.14', font=('arial',10,'bold'),bg='black',fg='white').grid(row=1, column=1)
        # Frame(TotalFrame,height=2,width=130,bg='black').grid(row=3,column=0 , columnspan=2,rowspan=2)
        Label(TotalFrame,text='Total Cost ', font=('arial',10,'bold'),bg='black',fg='white').grid(row=4, column=0)
        self.total_box = Label(TotalFrame,textvariable=total, font=('arial',10,'bold'),bg='black',fg='white').grid(row=4, column=1)

        
        statusframe=LabelFrame(Receipt_BottonFrame, width=150,height=50,bd=4, font=('arial',12,'bold'),text="Ride Status",bg='black',fg='blue', relief=RIDGE)
        statusframe.place(x=550, y=100)
        
        self.ride_status = Label(statusframe, font=('arial',10,'bold'),bg='black',fg='white')
        self.ride_status.grid(row=0, column=0)
        
    #=========================================================CustomerName====================================================

        self.lblFirstname=Label(CustomerName,font=('arial',14,'bold'),bg='black',fg='white',text="Firstname",bd=7)
        self.lblFirstname.grid(row=0,column=0,sticky=W)
        self.txtFirstname=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Firstname,bd=7,insertwidth=2,justify=RIGHT)
        self.txtFirstname.grid(row=0,column=1)

        self.lblSurname=Label(CustomerName,font=('arial',14,'bold'),bg='black',fg='white',text="Surname",bd=7)
        self.lblSurname.grid(row=1,column=0,sticky=W)
        self.txtSurname=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Surname,bd=7,insertwidth=2,justify=RIGHT)
        self.txtSurname.grid(row=1,column=1,sticky=W)

        self.lblMobile=Label(CustomerName,font=('arial',14,'bold'),bg='black',fg='white',text="Mobile",bd=7)
        self.lblMobile.grid(row=2,column=0,sticky=W)
        self.txtMobile=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Mobile,bd=7,insertwidth=2,justify=RIGHT)
        self.txtMobile.grid(row=2,column=1)

        self.lblEmail=Label(CustomerName,font=('arial',14,'bold'),text="Email",bd=7,bg='black',fg='white')
        self.lblEmail.grid(row=3,column=0,sticky=W)
        self.txtEmail=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Email,bd=7,insertwidth=2,justify=RIGHT)
        self.txtEmail.grid(row=3,column=1)

 
    #===============================================Cab Information==============================================================
        self.lblPickup=Label(TravelFrame,font=('arial',14,'bold'),text="Pickup",bd=7,bg='black',fg='white')
        self.lblPickup.grid(row=0,column=0,sticky=W)

        self.cboPickup =ttk.Combobox(TravelFrame, textvariable = varl1 , state='readonly', font=('arial',20,'bold'), width=14)
        self.cboPickup['value']=('','Kathmandu','Lalitpur','Pokhara','Bhaktapur')
        self.cboPickup.current(0)
        self.cboPickup.grid(row=0,column=1)

        self.lblDrop=Label(TravelFrame,font=('arial',14,'bold'),text="Drop",bd=7,bg='black',fg='white')
        self.lblDrop.grid(row=1,column=0,sticky=W)

        self.cboDrop =ttk.Combobox(TravelFrame, textvariable = varl2 , state='readonly', font=('arial',20,'bold'), width=14)
        self.cboDrop['value']=('','Bhaktapur','Pokhara','Kathmandu','Lalitpur')
        self.cboDrop.current(0)
        self.cboDrop.grid(row=1,column=1)

        self.no_passanger=Label(TravelFrame,font=('arial',14,'bold'),text="Passangers Count",bd=7,bg='black',fg='white')
        self.no_passanger.grid(row=2,column=0,sticky=W)

        self.passanger_count =ttk.Combobox(TravelFrame, textvariable = varl3 , state='readonly', font=('arial',20,'bold'), width=14)
        self.passanger_count['value']=('','1','2','3','4')
        self.passanger_count.current(1)
        self.passanger_count.grid(row=2,column=1)

        self.chkKm=Checkbutton(TravelFrame,text="Distance(KM)",variable = var2, onvalue=1, offvalue=0,font=('arial',16,'bold'),bg='black',fg='white',command=Kilo).grid(row=4, column=0, sticky=W)
        self.txtKm=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Km,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN,highlightthickness=0)
        self.txtKm.grid(row=4,column=1)


    #=======================================Receipt====================================================================================

        self.txtReceipt1 = Text(ReceiptFrame,width = 16, height = 9,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt1.grid(row=0,column=0,columnspan=1)
        self.txtReceipt2 = Text(ReceiptFrame,width = 16, height = 9,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt2.grid(row=0,column=2,columnspan=1)
        self.txtReceipt3 = Text(ReceiptFrame,width = 16, height = 9,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt3.grid(row=0,column=3,columnspan=1)
        self.txtReceipt4 = Text(ReceiptFrame,width = 16, height = 9,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt4.grid(row=0,column=4,columnspan=1)


    #======================================Button========================================================================================
        
        self.btnTotal = Button(ButtonFrame,padx=18,bd=7,font=('arial',11,'bold'),width = 15,text='Total',bg='black',fg='blue',command=total_paid).grid(row=0,column=0)
        self.btnReceipt = Button(ButtonFrame,padx=18,bd=7,font=('arial',11,'bold'),width = 15,text='Receipt',bg='black',fg='blue',command=receipt).grid(row=1,column=0)
        self.btnReset = Button(ButtonFrame,padx=18,bd=7,font=('arial',11,'bold'),width = 15,text='Reset',bg='black',fg='blue',command=reset).grid(row=2,column=0)
        self.btnExit = Button(ButtonFrame,padx=18,bd=7,font=('arial',11,'bold'),width = 15,text='Conform Book',bg='black',fg='blue',command=conform_booking).grid(row=3,column=0)
        
class admin:
    
    def __init__(self,root):
        self.root = root
        self.root.title("Admins System")
        self.root.geometry("1250x600+320+200") 
        self.root.configure(background='black')


   #================================================self.mainframe========================================================================

        self.MainFrame=Frame(self.root,bg='black')
        self.MainFrame.pack(fill=BOTH,expand=True)
        
        Tops = Frame(self.MainFrame,bg='black', bd=10, width=1350,relief=RIDGE)
        Tops.pack(side=TOP,fill=BOTH)

        self.lblTitle=Label(Tops,font=('arial',50,'bold'),bg='black',fg='blue',text="\t   Admin's Control System ")
        self.lblTitle.grid()

        ###############
        Button(self.MainFrame,text="REFRESH",command=self.refresh,bg='black',relief=RIDGE,bd=5,fg='blue',font=('arial',15,'bold')).pack()

    #================================================customerframedetail=============================================================
        self.AdminDetailsFrame=LabelFrame(self.MainFrame, width=1350,height=500,bd=20,bg='black', pady=5, relief=RIDGE)
        self.AdminDetailsFrame.pack(side=BOTTOM,fill=BOTH,expand=True)

        self.CustomerDetailsFrame=LabelFrame(self.AdminDetailsFrame,text="Customer's Request",fg="white", width=1350,height=100,bd=10,bg='black', pady=3, relief=RIDGE)
        self.CustomerDetailsFrame.pack(side=TOP,fill=BOTH,expand=True)

        self.DriverDetailsFrame=LabelFrame(self.AdminDetailsFrame,text="Driver's Detail", width=1350,fg="white",height=300,bd=10,bg='black', pady=3, relief=RIDGE)
        self.DriverDetailsFrame.pack(side=BOTTOM,fill=BOTH,expand=True)

        
    
    
    def refresh(self):
        ######
    
        e=Label(self.CustomerDetailsFrame,width=8,text='Recept Id',bd=2,font=("",12,'bold'), relief='ridge',anchor='w',bg='black',fg='blue')
        e.grid(row=0,column=0)
        e=Label(self.CustomerDetailsFrame,width=10,text='User Name',bd=2,font=("",12,'bold'),padx=5, relief='ridge',anchor='w',bg='black',fg='blue')
        e.grid(row=0,column=1)
        e=Label(self.CustomerDetailsFrame,width=8,text='Date',bd=2,font=("",12,'bold'),padx=5, relief='ridge',anchor='w',bg='black',fg='blue')
        e.grid(row=0,column=2)
        e=Label(self.CustomerDetailsFrame,width=11,text='Mobile No',bd=2,font=("",12,'bold'),padx=5, relief='ridge',anchor='w',bg='black',fg='blue')
        e.grid(row=0,column=3)
        e=Label(self.CustomerDetailsFrame,width=16,text='Email',bd=2,font=("",12,'bold'),padx=15, relief='ridge',anchor='w',bg='black',fg='blue')
        e.grid(row=0,column=4)
        e=Label(self.CustomerDetailsFrame,width=13,text='PickUP Location',bd=2,font=("",12,'bold'),padx=5, relief='ridge',anchor='w',bg='black',fg='blue')
        e.grid(row=0,column=5)
        e=Label(self.CustomerDetailsFrame,width=12,text='Drop Location',bd=2,font=("",12,'bold'),padx=5, relief='ridge',anchor='w',bg='black',fg='blue')
        e.grid(row=0,column=6)
        e=Label(self.CustomerDetailsFrame,width=4,text='Cost',bd=2,font=("",12,'bold'),padx=5, relief='ridge',anchor='w',bg='black',fg='blue')
        e.grid(row=0,column=7)
        e=Label(self.CustomerDetailsFrame,width=12,text='Drivers Activity',bd=2,font=("",12,'bold'),padx=5, relief='ridge',anchor='w',bg='black',fg='blue')
        e.grid(row=0,column=8)
        
        ##########
        def send_message(client_id, driver_id):
            
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@@@SpideX2152",
            database="spide_login"
            )

            mycursor = mydb.cursor()

            # sql_part_1 = f"CREATE TABLE IF NOT EXISTS driver_{driver_id} (id INT ,user_name VARCHAR(50),date VARCHAR(50),"
            # sql = f"CREATE TABLE IF NOT EXISTS driver_{driver_id} (id INT, user_name VARCHAR(50), date VARCHAR(50), phne_num VARCHAR(50), pickup VARCHAR(50), drop_location VARCHAR(50), total_cash VARCHAR(50))"
            # mycursor.execute(sql)
            # myresult = mycursor.fetchall()
            
            sql = f"SELECT recept_id, first_name, date, mobile, pickup, drop_location, cost FROM client_booking WHERE id={client_id}"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()

            i = 1
            # j=0
            for x in myresult: 
                # print (x)
                # sql = f"INSERT INTO driver_{driver_id} (id ,user_name, date, phne_num ,pickup, drop_location, total_cash) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                sql = f"INSERT INTO driver_{driver_id} (id, user_name, date, phne_num, pickup, drop_location, total_cash) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                # sql = f"INSERT INTO driver_{driver_id} (id, user_name, date, phne_num, pickup, drop_location, total_cash) VALUES (%d, %s, %s, %d, %s, %s, %d)"

                mycursor.execute(sql, x)
                mydb.commit()
                i+=1
            
            messagebox.showinfo("Success", "Request Sent Successfully")

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='@@@SpideX2152',
            database='spide_login'
        )
        cursor = conn.cursor()

        # Fetch client information from the database
        cursor.execute("SELECT * FROM client_booking")
        rows = cursor.fetchall()

        cursor.execute("SELECT id FROM driver_database")
        all_drivers_id = cursor.fetchall()
        ids_driver = [item[0] for item in all_drivers_id]
        # print (all_drivers_id)
        # print(ids_driver)
        # print ( all_drivers_id )
        # Display clients in a table format with OptionMenu and Send button for each row
        for i, row in enumerate(rows):
            client_id = row[0]
            client_recept = row[1]
            client_name = row[2]
            client_date = row[4]
            client_phone_num = row[5]
            client_email = row[6]
            client_pickup = row[7]
            client_drop = row[8]
            client_passnger_count = row[9]
            client_cost = row[10]
            driver_ids = all_drivers_id  # Replace this with actual driver IDs fetched from the database

            # Display client information
            Label(self.CustomerDetailsFrame, text=client_recept,bg='black',fg='white').grid(row=i+1, column=0)
            Label(self.CustomerDetailsFrame,bg='black',fg='white', text=client_name).grid(row=i+1, column=1)
            Label(self.CustomerDetailsFrame,bg='black',fg='white', text=client_date).grid(row=i+1, column=2)
            Label(self.CustomerDetailsFrame,bg='black',fg='white', text=client_phone_num).grid(row=i+1, column=3)
            Label(self.CustomerDetailsFrame,bg='black',fg='white', text=client_email).grid(row=i+1, column=4)
            Label(self.CustomerDetailsFrame,bg='black',fg='white', text=client_pickup).grid(row=i+1, column=5)
            Label(self.CustomerDetailsFrame,bg='black',fg='white', text=client_drop).grid(row=i+1, column=6)
            Label(self.CustomerDetailsFrame,bg='black',fg='white', text=client_cost).grid(row=i+1, column=7)

            # Create OptionMenu for driver IDs
            driver_var = StringVar(self.root)
            driver_var.set("Select Drivers ID")  # Set default driver ID
            # id_test = [1,2,3,4]
            driver_menu = OptionMenu(self.CustomerDetailsFrame, driver_var, *ids_driver)
            driver_menu.grid(row=i+1, column=8)

            # Create Send button
            send_button = Button(self.CustomerDetailsFrame, text="Send",font=("",13,"bold"),bg="black",fg="blue", relief='ridge',bd=4, command=lambda client_id=client_id, driver_id=driver_var: send_message(client_id, driver_id.get()))
            send_button.grid(row=i+1, column=9)

        # Close database connection
        conn.close()


        e=Label(self.DriverDetailsFrame,width=8,text='Drivers Id',bd=2,font=("",12,'bold'), relief='ridge',anchor='w',bg='black',fg='blue')
        e.grid(row=0,column=0)
        e=Label(self.DriverDetailsFrame,width=8,text='User Name',bd=2,font=("",12,'bold'), relief='ridge',anchor='w',bg='black',fg='blue')
        e.grid(row=0,column=1)
        e=Label(self.DriverDetailsFrame,width=8,text='Taxi No.',bd=2,font=("",12,'bold'), relief='ridge',anchor='w',bg='black',fg='blue')
        e.grid(row=0,column=2)
        e=Label(self.DriverDetailsFrame,width=8,text='Phone No.',bd=2,font=("",12,'bold'), relief='ridge',anchor='w',bg='black',fg='blue')
        e.grid(row=0,column=3)
        e=Label(self.DriverDetailsFrame,width=8,text='Status',bd=2,font=("",12,'bold'), relief='ridge',anchor='w',bg='black',fg='blue')
        e.grid(row=0,column=4)
        
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@@@SpideX2152",
        database="spide_login"
        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT id, name,taxi_number, mobile, status FROM driver_database")
        myresult = mycursor.fetchall()
        
        i = 1
        j=0
        for x in myresult: 
            for j in range(len(x)):

                aac=StringVar()
                aac = x[j]
                e = Label(self.DriverDetailsFrame,width=9,text=aac, bd=8, fg='white',bg='black') 
                e.grid(row=i,column=j) 
            i+=1

class driver():
    def __init__(self,root):
        self.root = root
        self.root.title("Drivers System")
        self.root.geometry("1250x600+320+200") 
        self.root.configure(background='black')


   #================================================self.mainframe========================================================================

        self.MainFrame=Frame(self.root,bg='black')
        self.MainFrame.pack(fill=BOTH,expand=True)
        
        self.Tops = Frame(self.MainFrame, bd=10, bg='black',width=1350,relief=RIDGE)
        self.Tops.pack(side=TOP,fill=BOTH)

        self.lblTitle=Label(self.Tops,font=('arial',50,'bold'), bg='black',fg='blue',text="Driver's Control System")
        self.lblTitle.pack()


    #================================================customerframedetail=============================================================
        self.CustomerDetailsFrame=LabelFrame(self.MainFrame, width=1350,height=500,bd=20,bg='black', pady=5, relief=RIDGE)
        self.CustomerDetailsFrame.pack(side=BOTTOM,fill=BOTH,expand=True)


        self.driver_signup_page()


    def driver_signup_page(self):

        self.frame=Frame (self.CustomerDetailsFrame, width=350,height=332, bg="white",bd=10,relief=RIDGE)
        self.frame.place(x=450, y=52)

        Label(self.frame, text='Registration', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23,"bold")).place(x=70, y=5)

        #######  User Name 
        def on_enter(e):
            self.user_name.delete(0, 'end')

        def on_leave(e):
            self.name=self.user_name.get()
            if self.name=='':
                self.user_name.insert(0, 'User Name')

        self.user_name = Entry (self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11,'bold'))
        self.user_name.place(x=40, y=75)
        self.user_name.insert(0, 'User Name')
        self.user_name.bind('<FocusIn>', on_enter)
        self.user_name.bind('<FocusOut>', on_leave)

        Frame (self.frame, width=260, height=1, bg='black').place(x=35, y=95)

        ####### taxi number
        def on_enter(e):
            self.taxi_number.delete (0, 'end')

        def on_leave(e):
            self.name=self.taxi_number.get()
            if self.name=='':
                self.taxi_number.insert(0, 'taxi_number')

        self.taxi_number = Entry (self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11,'bold'))
        self.taxi_number.place(x=40, y=155)
        self.taxi_number.insert(0, 'taxi_number')
        self.taxi_number.bind('<FocusIn>', on_enter)
        self.taxi_number.bind('<FocusOut>', on_leave)

        Frame (self.frame, width=260, height=1, bg='black').place(x=35,y=175)


        ###### phone number
        def on_enter(e):
            self.phone_num.delete (0, 'end')

        def on_leave(e):
            self.name=self.phone_num.get()
            if self.name=='':
                self.phone_num.insert(0,'Phone Number')

        self.phone_num = Entry (self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11,'bold'))
        self.phone_num.place(x=40, y=115)
        self.phone_num.insert(0,'Phone Number')
        self.phone_num.bind('<FocusIn>', on_enter)
        self.phone_num.bind('<FocusOut>', on_leave)

        Frame (self.frame, width=260, height=1, bg='black').place(x=35,y=135)
        Button (self.frame, width=39, pady=7, text='Submit Details', bg='#57a1f8',fg='white', border=0, command=self.driver_db_connect).place(x=35, y=205)
        Button (self.frame, width=39, pady=7, text='Login', bg='black',fg='white', border=0, command=self.driver_login_page).place(x=35, y=255)
       
        
    def driver_db_connect(self):
        taxi_no = int(self.taxi_number.get())
        print(taxi_no)
        
        # mycursor.execute("CREATE TABLE driver_database (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), mobile BIGINT, taxi_number VARCHAR(255), status VARCHAR(255))")
       
        if self.user_name.get()== "" or self.taxi_number.get()== "" or self.phone_num.get()== "" : 
            messagebox.showerror('Error', 'All fields are requiblack') 
        else: 
            # print(self.acc_type.get())
            conn= mysql.connector.connect(host = 'localhost',user='root',password='@@@SpideX2152',database='spide_login') 
            c= conn.cursor() 
            s="INSERT INTO driver_database( name, taxi_number, mobile, status) VALUES(%s, %s, %s, %s)" 
            c.execute(s,(self.user_name.get(),self.taxi_number.get(),self.phone_num.get(),"Vacant")) 
            messagebox.showinfo('success','Successfully Registered ') 

            sql = "SELECT id FROM driver_database WHERE taxi_number = %s"
            # sql = "SELECT * FROM customers WHERE address = %s"
            c.execute(sql,(taxi_no,))
            myresult = c.fetchall()
            extracted_number = myresult[0][0]
            print(extracted_number)
            
            sql = f"CREATE TABLE IF NOT EXISTS driver_{extracted_number} (id INT, user_name VARCHAR(50), date VARCHAR(50), phne_num VARCHAR(50), pickup VARCHAR(50), drop_location VARCHAR(50), total_cash VARCHAR(50))"
            c.execute(sql)

            conn.commit() 
            conn.close() 
            

            Button(self.MainFrame,text="refresh",bg='black',relief=RIDGE,bd=5,fg='blue',font=('arial',15,'bold'),command=self.driver_main).pack()

            # self.driver_main()

    def driver_login_page(self):
        
        self.driver_frame=Frame (self.CustomerDetailsFrame, width=350,height=332, bg="white",bd=10,relief=RIDGE)
        self.driver_frame.place(x=450, y=52)

        heading = Label (self.driver_frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23,"bold"))
        heading.place(x=100, y=5)
        #########--

        def on_enter(e):
            self.user.delete(0, 'end')

        def on_leave(e):
            self.name=self.user.get()
            if self.name=='':
                self.user.insert(0, 'Username')

        self.user = Entry (self.driver_frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind('<FocusIn>', on_enter)
        self.user.bind('<FocusOut>', on_leave)

        Frame (self.driver_frame, width=295, height=2, bg='black').place(x=25, y=107)

        ###########-
        def on_enter(e):
            self.taxi_number.delete (0, 'end')

        def on_leave(e):
            self.name=self.taxi_number.get()
            if self.name=='':
                self.taxi_number.insert(0, 'password')

        self.taxi_number = Entry (self.driver_frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
        self.taxi_number.place(x=30, y=160)
        self.taxi_number.insert(0, 'Taxi Number')
        self.taxi_number.bind('<FocusIn>', on_enter)
        self.taxi_number.bind('<FocusOut>', on_leave)

        Frame(self.driver_frame, width=295, height=2, bg='black').place(x=25,y=187)

        ###############################################################

        Button (self.driver_frame, width=39, pady=7, text='Sign in', bg='#57a1f8',fg='white', border=0, command=self.driver_login_connection).place(x=35, y=224)
        print()

    def driver_login_connection(self):
        
        if self.user.get() == '' or self.taxi_number.get()== '' : 
            messagebox.showerror('error', 'All fields are requiblack') 
        else: 
            con=pymysql.connect(host='localhost',user='root',password='@@@SpideX2152',database='spide_login') 
            my_cursor=con.cursor() 
            s="SELECT * FROM driver_database where name =%s and taxi_number =%s" 
            my_cursor.execute(s,(self.user.get(),self.taxi_number.get()))
            row =my_cursor.fetchone() 
            if row== None: 
                messagebox.showerror('error', 'Invalid username or password') 
        
            else:
                conn= mysql.connector.connect(host = 'localhost',user='root',password='@@@SpideX2152',database='spide_login') 
                c= conn.cursor() 
                t= conn.cursor() 
                
                q="SELECT id FROM driver_database where name =%s and taxi_number =%s"
                
                
                t.execute(q,(self.user.get(),self.taxi_number.get()))
                self.driver_id = t.fetchall()
                self.extracted_value = self.driver_id[0][0]
                # print(extracted_value)

                if self.driver_id != []:
                        n_name = self.user.get()
                        Button(self.MainFrame,text="refresh", bg='black',fg='blue',command=lambda: self.driver_main(n_name)).pack()
                        self.driver_frame.destroy()
                        self.driver_main(n_name)                
                else:
                    messagebox.showerror('error', 'Invalid username or password')
                
        print()

    def driver_main(self,n_name):
        mess = f"Welcome {n_name}"
        self.secframe=LabelFrame(self.CustomerDetailsFrame, text="Ride Details", width=1350,height=500,bd=5,bg='black', pady=3,padx=3,fg="white", relief=RIDGE)
        self.secframe.grid(row=1,column=0)

        
        self.frame.destroy()
        
        Label(self.CustomerDetailsFrame,text = mess, font=("",20,"bold"),bg="black",fg="blue").grid(row=0,column=0)
        
        e=Label(self.secframe,width=8,text='Recept Id',borderwidth=5,font=("",10,'bold'),padx=5, relief='ridge',anchor='w', bg='black',fg='blue')
        e.grid(row=2,column=0)
        e=Label(self.secframe,width=10,text='First Name',borderwidth=5,font=("",10,'bold'),padx=5, relief='ridge',anchor='w', bg='black',fg='blue')
        e.grid(row=2,column=1)
        e=Label(self.secframe,width=10,text='Date',borderwidth=5,font=("",10,'bold'),padx=5, relief='ridge',anchor='w', bg='black',fg='blue')
        e.grid(row=2,column=2)
        e=Label(self.secframe,width=12,text='Mobile No',borderwidth=5,font=("",10,'bold'),padx=5, relief='ridge',anchor='w', bg='black',fg='blue')
        e.grid(row=2,column=3)
        e=Label(self.secframe,width=15,text='PickUP Location',borderwidth=5,font=("",10,'bold'),padx=5, relief='ridge',anchor='w', bg='black',fg='blue')
        e.grid(row=2,column=4)
        e=Label(self.secframe,width=15,text='Drop Location',borderwidth=5,font=("",10,'bold'),padx=5, relief='ridge',anchor='w', bg='black',fg='blue')
        e.grid(row=2,column=5)
        e=Label(self.secframe,width=5,text='Cost',borderwidth=5,font=("",10,'bold'),padx=5, relief='ridge',anchor='w', bg='black',fg='blue')
        e.grid(row=2,column=6)
        e=Label(self.secframe,width=13,text='Drivers Activity',borderwidth=5,font=("",10,'bold'),padx=5, relief='ridge',anchor='w', bg='black',fg='blue')
        e.grid(row=2,column=7)


        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@@@SpideX2152",
        database="spide_login"
        )

        mycursor = mydb.cursor()
        d_ic_check = f"SELECT * FROM driver_{self.extracted_value}"
        mycursor.execute(d_ic_check)
        
        myresult = mycursor.fetchall()
        # print(myresult)
        ##########
        i = 3
        j=0
        print(myresult)
        for x in myresult: 
            print(x)
            for j in range(len(x)):
                aac=StringVar()
                aac = x[j]
                print( aac )
                e = Label(self.secframe,text=aac, bd=8,width=7, fg='white',bg='black') 
                e.grid(row=i,column=j)
                
            e = Button(self.secframe,text="Accept",font=("",9,'bold'),bg="black",fg='blue',relief="ridge",command=self.driver_accept)
            e.grid(row=i,column=7)

            e = Button(self.secframe,text="Completed",font=("",9,'bold'),bg="black",fg='blue',relief="ridge",command=self.drive_completed)
            e.grid(row=i,column=8)

            i+=1


    def driver_accept(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@@@SpideX2152",
        database="spide_login"
        )

        mycursor = mydb.cursor()
        
        sql = f"UPDATE driver_database SET status = 'In Ride' WHERE id = {self.extracted_value} "

        mycursor.execute(sql)

        mydb.commit()

        sql = f"SELECT id FROM driver_{self.extracted_value}"        
        mycursor.execute(sql)

        myresult = mycursor.fetchall()
        print(myresult)

    def drive_completed(self):
        
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@@@SpideX2152",
        database="spide_login"
        )

        mycursor = mydb.cursor()
        
        sql = f"UPDATE driver_database SET status = 'Vacant' WHERE id = {self.extracted_value} "

        mycursor.execute(sql)

        mydb.commit()

        sql = f"SELECT id FROM driver_{self.extracted_value}"        
        mycursor.execute(sql)

        myresult = mycursor.fetchall()
        print(myresult)

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.geometry("870x450+300+200")
        self.root.title('Registration form')
        self.root.configure(bg="black")
        self.create_widgets()

    def create_widgets(self):
        
        self.img = ImageTk.PhotoImage (Image.open('lopic.png'))
        Label (self.root, image=self.img, bg='black').place(x=50, y=50)

        frame=Frame (self.root, width=350,height=332, bg="white")
        frame.place(x=450, y=52)

        heading = Label (frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23,"bold"))
        heading.place(x=100, y=5)
        #########--

        def on_enter(e):
            self.user.delete(0, 'end')

        def on_leave(e):
            self.name=self.user.get()
            if self.name=='':
                self.user.insert(0, 'Username')

        self.user = Entry (frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind('<FocusIn>', on_enter)
        self.user.bind('<FocusOut>', on_leave)

        Frame (frame, width=295, height=2, bg='black').place(x=25, y=107)

        ###########-
        def on_enter(e):
            self.code.delete (0, 'end')

        def on_leave(e):
            self.name=self.code.get()
            if self.name=='':
                self.code.insert(0, 'password')

        self.code = Entry (frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
        self.code.place(x=30, y=160)
        self.code.insert(0, 'Password')
        self.code.bind('<FocusIn>', on_enter)
        self.code.bind('<FocusOut>', on_leave)

        Frame (frame, width=295, height=2, bg='black').place(x=25,y=187)

        ###############################################################

        Button (frame, width=39, pady=7, text='Sign in', bg='#57a1f8',fg='white', border=0, command=self.logged_in).place(x=35, y=224)
        label=Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light',9))
        label.place(x=75, y=290)

        sign_up= Button (frame,width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=self.signup_page)
        sign_up.place(x=215,y=290)


    def logged_in(self): 

        if self.user.get() == '' or self.code.get()== '' : 
            messagebox.showerror('error', 'All fields are requiblack') 
        else: 
            con=pymysql.connect(host='localhost',user='root',password='@@@SpideX2152',database='spide_login') 
            my_cursor=con.cursor() 
            s="SELECT * FROM book where username =%s and password =%s" 
            my_cursor.execute(s,(self.user.get(),self.code.get()))
            row =my_cursor.fetchone() 
            if row== None: 
                messagebox.showerror('error', 'Invalid username or password') 
        
            else:
                conn= mysql.connector.connect(host = 'localhost',user='root',password='@@@SpideX2152',database='spide_login') 
                c= conn.cursor() 
                t= conn.cursor() 
                
                q="SELECT * FROM book where username =%s and password =%s and acc_type = %s"
                
                c.execute(q,(self.user.get(),self.code.get(),"Admin"))
                admin_che = c.fetchall()
                
                t.execute(q,(self.user.get(),self.code.get(),"Customer"))
                client_check = t.fetchall()
                
                if admin_che != [] :
                    application = admin(root)
                
                elif client_check != []:
                    application = client(root)
                
                else:
                    driver_application = driver(root)
                
    
    def connect_database(self): 

            if self.email.get()== "" or self.user_name.get()== "" or self.password.get()== "" : 
                messagebox.showerror('Error', 'All fields are requiblack') 
            else: 
                print(self.acc_type.get())
                conn= mysql.connector.connect(host = 'localhost',user='root',password='@@@SpideX2152',database='spide_login') 
                c= conn.cursor() 
                s="INSERT INTO book(email, username, password, acc_type, phone_num) VALUES(%s, %s, %s, %s, %s)" 
                c.execute(s,(self.email.get(),self.user_name.get(),self.password.get(),self.acc_type.get(),self.phone_num.get())) 
                conn.commit() 
                conn.close() 
                messagebox.showinfo('success','Successfully Registeblack ') 
                self.create_widgets()

    def signup_page(self):
        
        frame=Frame (self.root, width=350,height=332, bg="white")
        frame.place(x=450, y=52)

        Label(frame, text='Registration', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23,"bold")).place(x=70, y=5)

        #######  User Name 
        def on_enter(e):
            self.user_name.delete(0, 'end')

        def on_leave(e):
            self.name=self.user_name.get()
            if self.name=='':
                self.user_name.insert(0, 'User Name')

        self.user_name = Entry (frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11,'bold'))
        self.user_name.place(x=40, y=75)
        self.user_name.insert(0, 'User Name')
        self.user_name.bind('<FocusIn>', on_enter)
        self.user_name.bind('<FocusOut>', on_leave)

        Frame (frame, width=260, height=1, bg='black').place(x=35, y=95)

        ####### Password
        def on_enter(e):
            self.password.delete (0, 'end')

        def on_leave(e):
            self.name=self.password.get()
            if self.name=='':
                self.password.insert(0, 'Password')

        self.password = Entry (frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11,'bold'))
        self.password.place(x=40, y=195)
        self.password.insert(0, 'Password')
        self.password.bind('<FocusIn>', on_enter)
        self.password.bind('<FocusOut>', on_leave)

        Frame (frame, width=260, height=1, bg='black').place(x=35,y=215)


        ####### email
        def on_enter(e):
            self.email.delete (0, 'end')

        def on_leave(e):
            self.name=self.email.get()
            if self.name=='':
                self.email.insert(0, 'Email')

        self.email = Entry (frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11,'bold'))
        self.email.place(x=40,y=115)
        self.email.insert(0, 'Email')
        self.email.bind('<FocusIn>', on_enter)
        self.email.bind('<FocusOut>', on_leave)

        Frame (frame, width=260, height=1, bg='black').place(x=35,y=135)


        ###### phone number
        def on_enter(e):
            self.phone_num.delete (0, 'end')

        def on_leave(e):
            self.name=self.phone_num.get()
            if self.name=='':
                self.phone_num.insert(0,'Phone Number')

        self.phone_num = Entry (frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11,'bold'))
        self.phone_num.place(x=40, y=155)
        self.phone_num.insert(0,'Phone Number')
        self.phone_num.bind('<FocusIn>', on_enter)
        self.phone_num.bind('<FocusOut>', on_leave)

        Frame (frame, width=260, height=1, bg='black').place(x=35,y=175)

        ######## account type
        self.acc_type=StringVar()
        
        self.option=['Customer','Driver']
        # self.acc_holder = Label(frame,text='Account Type', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',11)).place(x=25,y=240)
        self.counter_e=OptionMenu(frame,self.acc_type,*self.option).place(x=50,y=225)
        self.acc_type.set('Choose Your Role')

        Button (frame, width=25, pady=7, text='Sign Up', bg='#57a1f8',fg='white', border=0, command=self.connect_database).place(x=80, y=270)
        



if __name__ == "__main__":
    root = Tk()
    application = RegistrationForm(root)
    root.mainloop()