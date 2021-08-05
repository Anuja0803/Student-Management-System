from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkcalendar import *
import pymysql
from tkinter import messagebox
import re 

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1315x690+0+0")

        title = Label(self.root,text="Student Management System",bd=5,relief=GROOVE,font=("times new roman",25,"bold"),bg="slategray1",fg="navy")
        title.pack(side=TOP,fill=X)

        note=Label(self.root,text="Developed by Anuja , Sakshi & Devyani",bg="white",fg="blue",font=("times new roman",16,"bold"))
        note.pack(side=tk.BOTTOM,padx=150)

        #----------------------Declaring VARIABLES----------------------------------
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.address_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        self.result=StringVar()
        
        #---------------------MANAGE FRAME---------------------------------

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Manage_Frame.place(x=20,y=55,width=450,height=580)

        m_title = Label(Manage_Frame,text="Manage Students",bg="white",fg="navy",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        lbl_roll=Label(Manage_Frame,text="Roll No:",bg="white",fg="navy",font=("times new roman",15,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name:",bg="white",fg="navy",font=("times new roman",15,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(Manage_Frame,text="Email:",bg="white",fg="navy",font=("times new roman",15,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_gender=Label(Manage_Frame,text="Gender:",bg="white",fg="navy",font=("times new roman",15,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=10,pady=10)

        #txt_gender=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        #txt_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_contact=Label(Manage_Frame,text="Contact:",bg="white",fg="navy",font=("times new roman",15,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_dob=Label(Manage_Frame,text="DOB:",bg="white",fg="navy",font=("times new roman",15,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        #cal=Calendar(Manage_Frame,selectmode="day",year=2020,month=11,day=22,date_pattern='yy/mm/dd')
        #cal.grid(row=6,column=1,pady=5,padx=5,sticky="w")

        self.txt_dob=DateEntry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bg="lavender",bd=5,relief=GROOVE,date_pattern='yy/mm/dd')
        self.txt_dob.grid(row=6,column=1,pady=10,padx=25,sticky="w")

        lbl_address=Label(Manage_Frame,text="Address:",bg="white",fg="navy",font=("times new roman",15,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_address=Text(Manage_Frame,width=21,height=3,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        #txt_address=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        #txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        #----------------Button Frame---------------------------------

        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="white")
        btn_Frame.place(x=10,y=520,width=410)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students,bg="lightgray",activebackground="#00B0F0",activeforeground="white",cursor="hand2").grid(row=0,column=0,padx=10,pady=5)
        updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data,bg="lightgray",activebackground="#00B0F0",activeforeground="white",cursor="hand2").grid(row=0,column=1,padx=10,pady=5)
        deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data,bg="lightgray",activebackground="#00B0F0",activeforeground="white",cursor="hand2").grid(row=0,column=2,padx=10,pady=5)
        clearbtn=Button(btn_Frame,text="Cancel",width=10,command=self.clear,bg="lightgray",activebackground="#00B0F0",activeforeground="white",cursor="hand2").grid(row=0,column=3,padx=10,pady=5)
        exitbtn=Button(Manage_Frame,text="Exit",width=10,command=self.iExit,bg="lightgray",activebackground="#00B0F0",activeforeground="white",cursor="hand2").grid(row=10,column=0,padx=10,pady=5)

        #----------------DETAIL FRAME---------------------------------
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Detail_Frame.place(x=500,y=55,width=760,height=580)


        lbl_search=Label(Detail_Frame,text="Search By",bg="white",fg="navy",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20)

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("Roll_No","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",12,"bold"),bg="white",bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",font=("Arial Rounded MT Bold",9),width=10,pady=5,command=self.search_data,bg="lightgray",activebackground="#00B0F0",activeforeground="white",cursor="hand2").grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",font=("Arial Rounded MT Bold",9),width=10,pady=5,command=self.fetch_data,bg="lightgray",activebackground="#00B0F0",activeforeground="white",cursor="hand2").grid(row=0,column=4,padx=10,pady=10)

        
        #-----------------------------Table Frame-----------------------------

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="white")
        Table_Frame.place(x=10,y=70,width=740,height=495)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("Roll","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Roll",text="Roll No.")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Contact",text="Contact")
        self.Student_table.heading("DOB",text="DOB")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("Roll",width=50)
        self.Student_table.column("Name",width=100)
        self.Student_table.column("Email",width=100)
        self.Student_table.column("Gender",width=100)
        self.Student_table.column("Contact",width=100)
        self.Student_table.column("DOB",width=100)
        self.Student_table.column("Address",width=150)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.txt_address.get('1.0',END)=="":
            messagebox.showerror("Error","All fields are required !!")
        else:
            if self.Roll_No_var.get().isnumeric() & self.contact_var.get().isnumeric():
                con=pymysql.connect(host="localhost",user="fred",password="zap",database="stm")
                cur=con.cursor()
                regex_name=re.compile(r'^([a-z]+)([a-z]+ )*([a-z]+)*$',re.IGNORECASE)
                res = regex_name.search(self.name_var.get())
                regex_cn = re.compile(r'[789]\d{9}$')
                cn = regex_cn.search(self.contact_var.get())
                regex_email = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
                email = regex_email.search(self.email_var.get())
                if(cur.execute("select * from students where "+str(self.Roll_No_var.get())+" LIKE roll_no")):
                    messagebox.showerror("Error","Duplicate Roll no entry")
                else:
                    if res:
                        if cn:
                            if email:
                                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.txt_dob.get(),self.txt_address.get('1.0',END)))
                                con.commit()
                                self.fetch_data()
                                self.clear()
                                con.close()
                                messagebox.showinfo("Success","Record has been inserted")
                            else:
                                messagebox.showerror("Error","Invalid Email")
                        else:
                            messagebox.showerror("Error","Invalid Contact Number")
                        
                    else:
                        messagebox.showerror("Error","Invalid Name")
                    
            else:
                messagebox.showerror("Error","Roll Number should be numeric !!")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="fred",password="zap",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    def clear(self):
        #messagebox.showinfo("Confirm","Clear RECORD")
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.txt_dob.selection_clear()
        self.txt_address.delete("1.0",END)
        self.search_txt.set("") 

    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.txt_dob.set_date(row[5])
        self.txt_address.delete("1.0",END) 
        self.txt_address.insert(END,row[6])

    def update_data(self):
        if self.email_var.get()=="" or self.name_var.get()=="" or self.Roll_No_var.get()=="":
            messagebox.showerror("Error","All fields are required !!")
        else:
            regex_name=re.compile(r'^([a-z]+)([a-z]+ )*([a-z]+)*$',re.IGNORECASE)
            res = regex_name.search(self.name_var.get())
            regex_cn = re.compile(r'[789]\d{9}$')
            cn = regex_cn.search(self.contact_var.get())
            regex_email = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
            email = regex_email.search(self.email_var.get())
            if self.Roll_No_var.get().isnumeric():
                if res:
                    if cn:
                        if email:
                            con=pymysql.connect(host="localhost",user="fred",password="zap",database="stm")
                            cur=con.cursor()
                
                            cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                                                        self.name_var.get(),
                                                                                                        self.email_var.get(),
                                                                                                        self.gender_var.get(),
                                                                                                        self.contact_var.get(),
                                                                                                        self.txt_dob.get(),
                                                                                                        self.txt_address.get('1.0',END),
                                                                                                        self.Roll_No_var.get()))
                
                            con.commit()
                            self.fetch_data()
                            self.clear()
                            con.close()
                            messagebox.showinfo("Success","Record has been updated")
                        else:
                             messagebox.showerror("Error","Invalid Email")
                    else:
                        messagebox.showerror("Error","Invalid Contact Number")
                else:
                    messagebox.showerror("Error","Invalid Name")
            else:
                messagebox.showerror("Error","Invalid Roll Number!!")

    def delete_data(self):
        if self.email_var.get()=="" or self.name_var.get()=="" or self.Roll_No_var.get()=="":
            messagebox.showerror("Error","No data selected")
        else :
            con=pymysql.connect(host="localhost",user="fred",password="zap",database="stm")
            cur=con.cursor()
            MsgBox=tk.messagebox.askquestion("Confirm","Delete RECORD",icon='warning')
            if MsgBox=="yes":
                cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
                con.commit()
                con.close()
                self.fetch_data()
                self.clear()
                messagebox.showinfo("Success","Record has been deleted")

    def search_data(self):
    
        if(self.search_by.get()==""):
            messagebox.showerror("Error","No Record found")
        else:
            con=pymysql.connect(host="localhost",user="fred",password="zap",database="stm")
            cur=con.cursor()
            if(cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")):
                cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
                rows=cur.fetchall()        
            
                if len(rows)!=0:
                    self.Student_table.delete(*self.Student_table.get_children())
                    for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
            else:
                messagebox.showerror("Error","No Record found")            
            con.close()
            self.clear()

    def iExit(self):
        iExit= tk.messagebox.askyesno("Student Management System","Do you want to exit")
        if iExit > 0:
            root.destroy()
    

root = Tk()
ob = Student(root)
root.mainloop()