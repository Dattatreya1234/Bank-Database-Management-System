#! /usr/bin/python3
import pprint
import tkinter as tk
from tkinter import messagebox

from tkinter import *
from prettytable import PrettyTable
from tkinter import ttk
import os
import subprocess
import mysql.connector
from datetime import datetime
import time
from PIL import Image,ImageTk


db=mysql.connector.connect(host='localhost',user='root',passwd='1db19cs041',database='bank')
cur=db.cursor()


root=Tk()
root.title("WELCOME TO My Bank")

#stored procedure
"""
    DELIMITER $$
    
    CREATE PROCEDURE getMonth(
        IN   month VARCHAR(2))
    BEGIN
        SELECT * FROM payment
        WHERE p_date LIKE CONCAT('____-',month,'%');
    END$$

    DELIMITER ;

"""

T1,T2,T3=0,0,0
def First_page(root):
    global T1,T2,T3
    frame=Frame(root,height=500,width=800,bg='ivory')
    frame.pack()

    label=Label(root,text='WELCOME TO My Bank',font=('Times new roman',25))
    label.place(x=200,y=50)

    button=Button(root,text='LogIn',font=('times new roman',20),command=check_pass,bg='green')
    button.place(x=350,y=350)

    L1 = tk.Label(root, text="Username", font=("Arial Bold", 15), bg='ivory')
    L1.place(x=150, y=200)
    T1 = tk.Entry(root, width = 30, bd = 5)
    T1.place(x=280, y=200)

    L2 = tk.Label(root, text="Password", font=("Arial Bold", 15), bg='ivory')
    L2.place(x=150, y=250)
    T2 = tk.Entry(root, width = 30, show='*', bd = 5)
    T2.place(x=280, y=250)

    reg_button=Button(root,text='Register',font=("Arial Bold",15),bg='blue',command=create_pass)
    reg_button.place(x=340,y=400)
    

def check_pass():
    global root,T1,T2,T3
    try:
        with open('password.txt','r')as f:
            lines=f.read()
            if T1.get()+'='+T2.get() in lines and T1.get()!='' and T2.get()!='':
                entity_page()
            else:
                label=Label(root,text='Invalid username or password.Try again',font=('times new roman',15))
                label.place(x=200,y=100)
    except:
        label=Label(root,text='Invalid username or password.Try again',font=('times new roman',15))
        label.place(x=200,y=100)

def create_pass():
    global root,T1,T2,T3


    #to clean up  previous window
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='ivory')
    label.place(x=0,y=0)


    #this window
    L1 = tk.Label(root, text="Username", font=("Arial Bold", 15), bg='ivory')
    L1.place(x=150, y=200)
    T1 = tk.Entry(root, width = 30, bd = 5)
    T1.place(x=380, y=200)

    L2 = tk.Label(root, text="Password", font=("Arial Bold", 15), bg='ivory')
    L2.place(x=150, y=250)
    T2 = tk.Entry(root, width = 30, show='*', bd = 5)
    T2.place(x=380, y=250)

    L2 = tk.Label(root, text="Confirm Password", font=("Arial Bold", 15), bg='ivory')
    L2.place(x=150, y=300)
    T3 = tk.Entry(root, width = 30, show='*', bd = 5)
    T3.place(x=380, y=300)

    reg_button=Button(root,text='Done',font=("Arial Bold",15),bg='blue',command=add_pass)
    reg_button.place(x=440,y=400)


def add_pass():
    global root,T1,T2,T3

    if T2.get()!=T3.get():
        label=Label(root,text='Incorrect Password. Enter again',font=('times new roman',20))
        label.place(x=100,y=100)
    else:
        try:
            with open('password.txt','r')as f:
                data=f.read()
            with open('password.txt','w')as f:
                f.write(data+'\n')
                f.write(T1.get()+'='+T2.get())

            entity_page()
        except:
            with open('password.txt','w')as f:
                f.write(T1.get()+'='+T2.get())

            entity_page()

def entity_page():
    global root
    #cleaning previous window
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='ivory')
    label.place(x=0,y=0)

    #this window
    label=Label(root,text='WELCOME TO My Bank ',font=('Times new roman',20),bg='blue')
    label.place(x=200,y=20)

    label=Label(root,text='Choose the Entity ',font=('Times new roman',20),bg='white')
    label.place(x=250,y=100)


    Button = tk.Button(root, text="Branch", font=("Arial", 15),command=branch)
    Button.place(x=50, y=150+25)

    Button = tk.Button(root, text="Customer", font=("Arial", 15),command=customer)
    Button.place(x=200+25, y=150+25)

    Button = tk.Button(root, text="Account", font=("Arial", 15),command=account)
    Button.place(x=350+50, y=150+25)

    Button = tk.Button(root, text="Deposit", font=("Arial", 15),command=deposit)
    Button.place(x=450+75, y=150+25)

    Button = tk.Button(root, text="Withdraw", font=("Arial", 15),command=withdraw)
    Button.place(x=50, y=300+25)

    Button = tk.Button(root, text="Loan", font=("Arial", 15),command=loan)
    Button.place(x=200, y=300+25)
    
    Button = tk.Button(root, text="Borrower", font=("Arial", 15),command=borrower)
    Button.place(x=300, y=300+25)
    
    

def branch():
    global root
    #clean previous window
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Branch Table',font=('Times new roman',15),bg='white')
    label.place(x=350,y=10)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=entity_page)
    Button.place(x=10, y=50)
    
    Button = tk.Button(root, text="Insert", font=("Arial", 15),command=insert_branch)
    Button.place(x=110, y=50)

    Button = tk.Button(root, text="Delete", font=("Arial", 15),command=delete_branch)
    Button.place(x=210, y=50)

    Button = tk.Button(root, text="Update", font=("Arial", 15),command=update_branch)
    Button.place(x=310, y=50)

    Button = tk.Button(root, text="Search", font=("Arial", 15),command=search_branch)
    Button.place(x=410, y=50)
    
    view_branch()


def view_branch():
    frame=Frame(root,bd=5,relief=RIDGE,bg='tomato')
    frame.place(x=10,y=100,width=750,height=400)

    x_scroll=Scrollbar(frame,orient=HORIZONTAL)
    y_scroll=Scrollbar(frame,orient=VERTICAL)

    table=ttk.Treeview(frame,columns=("assets",'branch_name','branch_city'),xscrollcommand=x_scroll.set,
    yscrollcommand=y_scroll.set)

    x_scroll.pack(side=BOTTOM,fill=X)
    y_scroll.pack(side=RIGHT,fill=Y)
    x_scroll.config(command=table.xview)
    y_scroll.config(command=table.yview)
    table.heading('assets',text="Assets in Rs.")
    table.heading('branch_name',text="Branch Name")
    table.heading('branch_city',text="Branch City")
    table['show']='headings'

    table.column("assets",width=100)


    table.pack()



    cur.execute("SELECT * FROM branch;")

    data =cur.fetchall()
    db.commit()
    if len(data)!=0:
        for row in data:
            table.insert('',END,values=row)

e1,e2,e3,e4,e5,e6=0,0,0,0,0,0
def insert_branch():
    global e1,e2,e3,e4,e5,e6
    #clean the window
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)


    #create the window
    label=Label(root,text='assets',font=('Times new roman',20),bg='white')
    label.place(x=50,y=10)

    label=Label(root,text='Branch_name',font=('Times new roman',20),bg='white')
    label.place(x=50,y=60)

    label=Label(root,text='Branch city',font=('Times new roman',20),bg='white')
    label.place(x=50,y=110)

    
    e1=Entry(root,width=50)
    e2=Entry(root,width=50)
    e3=Entry(root,width=50)
    
    e1.place(x=350,y=10)
    e2.place(x=350,y=60)
    e3.place(x=350,y=110)
    
    Button = tk.Button(root, text="Back", font=("Arial", 15),command=branch)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Commit", font=("Arial", 15),command=insert_branch_command)
    Button.place(x=400, y=400)

def insert_branch_command():
    global root
    try:
        sql="INSERT INTO branch values(%s,%s,%s);"
        if len(e1.get())>3:
            invalid('branch')
        else:

            vals=e1.get(),e2.get(),e3.get()
            cur.executemany(sql,[vals])
            db.commit()
            branch()
    except:
        insert_branch()
def invalid(page):
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    if page=='branch':
        label=Label(root,text='Enter valid branch name',font=('Times new roman',30),bg='white')
        label.place(x=170,y=200)

        button=Button(root,text='Re-enter',font=('Times new roman',20),command=insert_branch)
        button.place(x=300,y=400)
    elif page=='customer':
        label=Label(root,text='Enter valid customer id',font=('Times new roman',30),bg='white')
        label.place(x=170,y=200)

        button=Button(root,text='Re-enter',font=('Times new roman',20),command=insert_customer)
        button.place(x=300,y=400)
def delete_branch():
    global e1
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Branch Name:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e1=Entry(root,width=50)
    e1.place(x=300,y=200)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=branch)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Commit", font=("Arial", 15),command=delete_branch_command)
    Button.place(x=400, y=400)


def delete_branch_command():
    try:
        sql="DELETE FROM branch WHERE branch_name=%s;"
        cur.execute(sql,[e1.get()])
        db.commit()
        branch()
    except:
        l=Label(root,text='Invalid Entry',font=('times new roman',15))
        l.place(x=100,y=300)

def update_branch():
    global e1
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Branch Name:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e1=Entry(root,width=50)
    e1.place(x=300,y=200)

    Button = tk.Button(root, text="OK", font=("Arial", 15),command=update)

    Button.place(x=300, y=400)

def update():
    try:
        global e1,e2,e3,e4,e5,e6
        #clean
        label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
        label.place(x=0,y=0)

        sql='SELECT * FROM branch WHERE branch_name=%s;'
        vals=[e1.get()]
        cur.execute(sql,vals)

        label=Label(root,text='Assets',font=('Times new roman',20),bg='white')
        label.place(x=50,y=10)

        label=Label(root,text='Branch Name',font=('Times new roman',20),bg='white')
        label.place(x=50,y=60)

        label=Label(root,text='Branch City',font=('Times new roman',20),bg='white')
        label.place(x=50,y=110)

        
        e1=Entry(root)
        e2=Entry(root)
        e3=Entry(root)
        
        data=cur.fetchall()
        arr=[e1,e2,e3]
        count=0
        for val in data[0]:
            arr[count].insert(0,val)
            count+=1

        e1.place(x=350,y=10)
        e2.place(x=350,y=60)
        e3.place(x=350,y=110)
        
        label=Button(root,text='Modify',font=('Times new roman',20),bg='blue',command=update_command)
        label.place(x=300,y=400)


    except:
        l=Label(root,text='Invalid Branch name',font=('times new roman',15))
        l.place(x=100,y=300)
        update_branch()

def update_command():
    try:
        sql="UPDATE branch SET assets=%s,branch_city=%s where branch_name=%s;"
        vals=e1.get(),e3.get(),e2.get()
        cur.executemany(sql,[vals])
        db.commit()
        branch()
    except:
        update_branch()
def search_branch():
    global e1
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Branch Name:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e1=Entry(root,width=50)
    e1.place(x=300,y=200)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=branch)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Search", font=("Arial", 15),command=search)
    Button.place(x=400, y=400)
def search():
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)
    try:
        sql='SELECT * FROM branch WHERE branch_name=%s;'
        val=[e1.get()]
        cur.execute(sql,val)

        Button = tk.Button(root, text="OK", font=("Arial", 15),command=branch)
        Button.place(x=300, y=400)

        for val in cur:
            count=0
            Y=50
            names=['Assets : ','Branch Name : ','Branch City : ']
            for i in val:
                label=Label(root,text=names[count]+str(i),font=('Times new roman',20),bg='tomato')
                label.place(x=10,y=Y)
                Y+=50
                count+=1
        db.commit()
    except:
        l=Label(root,text='Invalid Farmer Id',font=('times new roman',15))
        l.place(x=100,y=300)
        search_branch()


#customerpage
def customer():
    global root
    #clean previous window
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Customer Table',font=('Times new roman',15),bg='white')
    label.place(x=350,y=10)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=entity_page)
    Button.place(x=10, y=50)

    Button = tk.Button(root, text="Insert", font=("Arial", 15),command=insert_customer)
    Button.place(x=110, y=50)

    Button = tk.Button(root, text="Delete", font=("Arial", 15),command=delete_customer)
    Button.place(x=210, y=50)

    Button = tk.Button(root, text="Update", font=("Arial", 15),command=update_customer)
    Button.place(x=310, y=50)

    Button = tk.Button(root, text="Search", font=("Arial", 15),command=search_customer)
    Button.place(x=410, y=50)

    view_customer()


def view_customer():
    frame=Frame(root,bd=5,relief=RIDGE,bg='tomato')
    frame.place(x=10,y=100,width=750,height=400)

    x_scroll=Scrollbar(frame,orient=HORIZONTAL)
    y_scroll=Scrollbar(frame,orient=VERTICAL)

    table=ttk.Treeview(frame,columns=('cust_name',"cust_id",'cust_phno','cust_city'),xscrollcommand=x_scroll.set,
    yscrollcommand=y_scroll.set)

    x_scroll.pack(side=BOTTOM,fill=X)
    y_scroll.pack(side=RIGHT,fill=Y)
    x_scroll.config(command=table.xview)
    y_scroll.config(command=table.yview)
    table.heading('cust_name',text="Customer name")
    table.heading('cust_id',text="Customer id")
    table.heading('cust_phno',text="Customer phno")
    table.heading('cust_city',text="Customer city")
    table['show']='headings'

    table.column("cust_id",width=100)


    table.pack()



    cur.execute("SELECT * FROM customer;")

    data =cur.fetchall()
    db.commit()
    if len(data)!=0:
        for row in data:
            table.insert('',END,values=row)

def insert_customer():
    global e1,e2,e3,e4,e5,e6
    #clean the window
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)


    #create the window
    label=Label(root,text='Customer name',font=('Times new roman',20),bg='white')
    label.place(x=50,y=10)

    label=Label(root,text='Customer id',font=('Times new roman',20),bg='white')
    label.place(x=50,y=110)

    label=Label(root,text='Customer phno',font=('Times new roman',20),bg='white')
    label.place(x=50,y=210)

    label=Label(root,text='Customer city',font=('Times new roman',20),bg='white')
    label.place(x=50,y=310)


    e1=Entry(root,width=50)
    e2=Entry(root,width=50)
    e3=Entry(root,width=50)
    e4=Entry(root,width=50)

    e1.place(x=350,y=10)
    e2.place(x=350,y=110)
    e3.place(x=350,y=210)
    e4.place(x=350,y=310)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=customer)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Commit", font=("Arial", 15),command=insert_customer_command)
    Button.place(x=400, y=400)

def insert_customer_command():
    try:
        
        sql="INSERT INTO customer values(%s,%s,%s,%s);"
        vals=e1.get(),e2.get(),e3.get(),e4.get()
        cur.executemany(sql,[vals])
        db.commit()
        customer()
    except:
        insert_customer()
def delete_customer():
    global e2
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Customer Id:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e2=Entry(root,width=50)
    e2.place(x=300,y=200)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=customer)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Commit", font=("Arial", 15),command=delete_customer_command)
    Button.place(x=400, y=400)


def delete_customer_command():
    try:
        sql="DELETE FROM customer WHERE cust_id=%s;"
        print(e2.get())
        cur.execute(sql,[e2.get()])
        db.commit()
        customer()
    except:
        l=Label(root,text='Invalid Entry',font=('times new roman',15))
        l.place(x=100,y=300)

def update_customer():
    global e2
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Customer id:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e2=Entry(root,width=50)
    e2.place(x=300,y=200)

    Button = tk.Button(root, text="OK", font=("Arial", 15),command=update_customer_1)

    Button.place(x=300, y=400)

def update_customer_1():
    try:
        global e1,e2,e3,e4,e5,e6
        #clean
        label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
        label.place(x=0,y=0)

        sql='SELECT * FROM customer WHERE cust_id=%s;'
        vals=[e2.get()]
        cur.execute(sql,vals)

        label=Label(root,text='Customer name',font=('Times new roman',20),bg='white')
        label.place(x=50,y=10)

        label=Label(root,text='Customer id',font=('Times new roman',20),bg='white')
        label.place(x=50,y=110)

        label=Label(root,text='Customer phno',font=('Times new roman',20),bg='white')
        label.place(x=50,y=210)

        label=Label(root,text='Customer city',font=('Times new roman',20),bg='white')
        label.place(x=50,y=310)

        e1=Entry(root)
        e2=Entry(root)
        e3=Entry(root)
        e4=Entry(root)

        data=cur.fetchall()
        arr=[e1,e2,e3,e4]
        count=0
        for val in data[0]:
            arr[count].insert(0,val)
            count+=1

        e1.place(x=350,y=10)
        e2.place(x=350,y=110)
        e3.place(x=350,y=210)
        e4.place(x=350,y=310)

        label=Button(root,text='Modify',font=('Times new roman',20),bg='blue',command=update_command_customer)
        label.place(x=300,y=400)


    except:
        l=Label(root,text='Invalid account number',font=('times new roman',15))
        l.place(x=100,y=300)
        update_customer()

def update_command_customer():
    try:
        sql="UPDATE customer SET cust_name=%s,cust_phno=%s,cust_city=%s WHERE cust_id=%s;"
        vals=e1.get(),e3.get(),e4.get(),e2.get()
        cur.executemany(sql,[vals])
        db.commit()
        customer()
    except:
        update_customer()
def search_customer():
    global e2
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Customer id:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e2=Entry(root,width=50)
    e2.place(x=300,y=200)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=customer)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Search", font=("Arial", 15),command=search_customer_1)
    Button.place(x=400, y=400)
def search_customer_1():
    global e2
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)
    try:
        sql='SELECT * FROM customer WHERE cust_id=%s;'
        val=[e2.get()]
        cur.execute(sql,val)

        Button = tk.Button(root, text="OK", font=("Arial", 15),command=customer)
        Button.place(x=300, y=400)

        for val in cur:
            count=0
            Y=50
            names=['Customer name: ','Customer id: ','Customer phno: ','Customer city: ']
            for i in val:
                label=Label(root,text=names[count]+str(i),font=('Times new roman',20),bg='tomato')
                label.place(x=10,y=Y)
                Y+=50
                count+=1
        db.commit()
    except:
        l=Label(root,text='Invalid Customer Id',font=('times new roman',15))
        l.place(x=100,y=300)
        search_customer()

def account():
    global root
    #clean previous window
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='account Table',font=('Times new roman',15),bg='white')
    label.place(x=350,y=10)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=entity_page)
    Button.place(x=10, y=50)

    Button = tk.Button(root, text="Insert", font=("Arial", 15),command=insert_account)
    Button.place(x=110, y=50)

    Button = tk.Button(root, text="Delete", font=("Arial", 15),command=delete_account)
    Button.place(x=210, y=50)

    Button = tk.Button(root, text="Update", font=("Arial", 15),command=update_account)
    Button.place(x=310, y=50)

    Button = tk.Button(root, text="Search", font=("Arial", 15),command=search_account)
    Button.place(x=410, y=50)

    view_account()


def view_account():
    frame=Frame(root,bd=5,relief=RIDGE,bg='tomato')
    frame.place(x=10,y=100,width=750,height=400)

    x_scroll=Scrollbar(frame,orient=HORIZONTAL)
    y_scroll=Scrollbar(frame,orient=VERTICAL)

    table=ttk.Treeview(frame,columns=("acc_no",'cust_id','acc_type','amount'),xscrollcommand=x_scroll.set,
    yscrollcommand=y_scroll.set)

    x_scroll.pack(side=BOTTOM,fill=X)
    y_scroll.pack(side=RIGHT,fill=Y)
    x_scroll.config(command=table.xview)
    y_scroll.config(command=table.yview)
    table.heading('acc_no',text="account number")
    table.heading('cust_id',text="customer id")
    table.heading('acc_type',text="account type")
    table.heading('amount',text="amount")
    table['show']='headings'

    #table.column("acc_no",width=100)


    table.pack()



    cur.execute("SELECT * FROM account;")

    data =cur.fetchall()
    db.commit()
    if len(data)!=0:
        for row in data:
            table.insert('',END,values=row)

e1,e2,e3,e4,e5,e6=0,0,0,0,0,0
def insert_account():
    global e1,e2,e3,e4,e5,e6
    #clean the window
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)


    #create the window
    label=Label(root,text='account number',font=('Times new roman',20),bg='white')
    label.place(x=50,y=10)

    label=Label(root,text='customer id',font=('Times new roman',20),bg='white')
    label.place(x=50,y=60)

    label=Label(root,text='account type',font=('Times new roman',20),bg='white')
    label.place(x=50,y=110)

    label=Label(root,text='amount',font=('Times new roman',20),bg='white')
    label.place(x=50,y=160)

    e1=Entry(root,width=50)
    e2=Entry(root,width=50)
    e3=Entry(root,width=50)
    e4=Entry(root,width=50)
    

    e1.place(x=350,y=10)
    e2.place(x=350,y=60)
    e3.place(x=350,y=110)
    e4.place(x=350,y=160)
   
    Button = tk.Button(root, text="Back", font=("Arial", 15),command=account)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Commit", font=("Arial", 15),command=insert_account_command)
    Button.place(x=400, y=400)

def insert_account_command():
    try:
        sql="INSERT INTO account values(%s,%s,%s,%s);"
        vals=e1.get(),e2.get(),e3.get(),e4.get()
        cur.executemany(sql,[vals])
        db.commit()
        account()
    except:
        insert_account()
def delete_account():
    global e1
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='account number:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e1=Entry(root,width=50)
    e1.place(x=300,y=200)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=account)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Commit", font=("Arial", 15),command=delete_account_command)
    Button.place(x=400, y=400)


def delete_account_command():
    try:
        sql="DELETE FROM account WHERE acc_no=%s;"
        cur.execute(sql,[e1.get()])
        db.commit()
        account()
    except:
        l=Label(root,text='Invalid Entry',font=('times new roman',15))
        l.place(x=100,y=300)

def update_account():
    global e1
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='account number:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e1=Entry(root,width=50)
    e1.place(x=300,y=200)

    Button = tk.Button(root, text="OK", font=("Arial", 15),command=update_account_1)

    Button.place(x=300, y=400)

def update_account_1():
    try:
        global e1,e2,e3,e4,e5,e6
        #clean
        label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
        label.place(x=0,y=0)

        sql='SELECT * FROM account WHERE acc_no=%s;'
        vals=[e1.get()]
        cur.execute(sql,vals)

        label=Label(root,text='account number',font=('Times new roman',20),bg='white')
        label.place(x=50,y=10)

        label=Label(root,text='customer id',font=('Times new roman',20),bg='white')
        label.place(x=50,y=60)

        label=Label(root,text='account type',font=('Times new roman',20),bg='white')
        label.place(x=50,y=110)

        label=Label(root,text='amount',font=('Times new roman',20),bg='white')
        label.place(x=50,y=160)

      


        e1=Entry(root)
        e2=Entry(root)
        e3=Entry(root)
        e4=Entry(root)
      

        data=cur.fetchall()
        arr=[e1,e2,e3,e4]
        count=0
        for val in data[0]:
            arr[count].insert(0,val)
            count+=1

        e1.place(x=350,y=10)
        e2.place(x=350,y=60)
        e3.place(x=350,y=110)
        e4.place(x=350,y=160)
       

        label=Button(root,text='Modify',font=('Times new roman',20),bg='blue',command=update_command_account)
        label.place(x=300,y=400)


    except:
        l=Label(root,text='Invalid account number',font=('times new roman',15))
        l.place(x=100,y=300)
        update_account()

def update_command_account():

    sql="UPDATE account SET cust_id=%s,acc_type=%s,amount=%s WHERE acc_no=%s;"
    vals=e2.get(),e3.get(),e4.get(),e1.get()
    cur.executemany(sql,[vals])
    db.commit()
    account()

def search_account():
    global e1
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='account number:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e1=Entry(root,width=50)
    e1.place(x=300,y=200)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=account)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Search", font=("Arial", 15),command=search_account_1)
    Button.place(x=400, y=400)
def search_account_1():
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)
    try:
        sql='SELECT * FROM account WHERE acc_no=%s;'
        val=[e1.get()]
        cur.execute(sql,val)

        Button = tk.Button(root, text="OK", font=("Arial", 15),command=account)
        Button.place(x=300, y=400)

        for val in cur:
            count=0
            Y=50
            names=['account number: ','customer_id: ','account type: ','amount: ']
            for i in val:
                label=Label(root,text=names[count]+str(i),font=('Times new roman',20),bg='tomato')
                label.place(x=10,y=Y)
                Y+=50
                count+=1
        db.commit()
    except:
        l=Label(root,text='Invalid account number',font=('times new roman',15))
        l.place(x=100,y=300)
        search_account()


def deposit():
    global root
    #clean previous window
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Deposit Table',font=('Times new roman',15),bg='white')
    label.place(x=350,y=10)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=entity_page)
    Button.place(x=10, y=50)

    Button = tk.Button(root, text="Insert", font=("Arial", 15),command=insert_deposit)
    Button.place(x=110, y=50)

    Button = tk.Button(root, text="Delete", font=("Arial", 15),command=delete_deposit)
    Button.place(x=210, y=50)

    Button = tk.Button(root, text="Update", font=("Arial", 15),command=update_deposit)
    Button.place(x=310, y=50)

    Button = tk.Button(root, text="Search", font=("Arial", 15),command=search_deposit)
    Button.place(x=410, y=50)

    view_deposit()


def view_deposit():
    frame=Frame(root,bd=5,relief=RIDGE,bg='tomato')
    frame.place(x=10,y=100,width=750,height=400)

    x_scroll=Scrollbar(frame,orient=HORIZONTAL)
    y_scroll=Scrollbar(frame,orient=VERTICAL)

    table=ttk.Treeview(frame,columns=('amount',"acc_no"),xscrollcommand=x_scroll.set,
    yscrollcommand=y_scroll.set)

    x_scroll.pack(side=BOTTOM,fill=X)
    y_scroll.pack(side=RIGHT,fill=Y)
    x_scroll.config(command=table.xview)
    y_scroll.config(command=table.yview)
    table.heading('amount',text="Amount")
    table.heading('acc_no',text="Account no")
    table['show']='headings'

    #table.column("f_id",width=100)


    table.pack()



    cur.execute("SELECT * FROM deposit;")

    data =cur.fetchall()
    db.commit()
    if len(data)!=0:
        for row in data:
            table.insert('',END,values=row)

e1,e2,e3,e4,e5,e6=0,0,0,0,0,0
def insert_deposit():
    global e1,e2,e3,e4,e5,e6
    #clean the window
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)


    #create the window
    label=Label(root,text='Amount',font=('Times new roman',20),bg='white')
    label.place(x=50,y=10)

    label=Label(root,text='Account no',font=('Times new roman',20),bg='white')
    label.place(x=50,y=60)


    e1=Entry(root,width=50)
    e2=Entry(root,width=50)

    e1.place(x=350,y=10)
    e2.place(x=350,y=60)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=deposit)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Commit", font=("Arial", 15),command=insert_deposit_command)
    Button.place(x=400, y=400)

def insert_deposit_command():
    try:
        sql="INSERT INTO deposit values(%s,%s);"
        vals=e1.get(),e2.get()
        cur.executemany(sql,[vals])
        db.commit()
        #need to add to amount in another table
        add_amount=int(vals[0])
        cur.execute("SELECT amount FROM account where acc_no=%s;",[vals[1]])
        
        data=cur.fetchall()
        #print(data)
        prev_amount=int(data[-1][0])
        total=prev_amount+add_amount
        #print(prev_amount)
        #print(total)
        cur.executemany("update account set amount=%s where acc_no=%s;",[(total,vals[1])])

        #print("hi")
        db.commit()
        deposit()
    except:
        print("error")
        insert_deposit()


def delete_deposit():
    global e2
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='acc_no:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e2=Entry(root,width=50)
    e2.place(x=300,y=200)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=deposit)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Commit", font=("Arial", 15),command=delete_deposit_command)
    Button.place(x=400, y=400)


def delete_deposit_command():
    try:
        sql="DELETE FROM deposit WHERE acc_no=%s;"
        cur.execute(sql,[e2.get()])
        db.commit()
        deposit()
    except:
        l=Label(root,text='Invalid Entry',font=('times new roman',15))
        l.place(x=100,y=300)

def update_deposit():
    global e2
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Account no:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e2=Entry(root,width=50)
    e2.place(x=300,y=200)

    Button = tk.Button(root, text="OK", font=("Arial", 15),command=update_deposit_1)

    Button.place(x=300, y=400)

def update_deposit_1():
    try:
        global e1,e2,e3,e4,e5,e6
        #clean
        label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
        label.place(x=0,y=0)

        sql="select * from deposit where acc_no=%s;"
        #print(e2.get())
        vals=(e2.get(),)
        #print(vals)
        cur.execute(sql,vals)

        label=Label(root,text='Amount',font=('Times new roman',20),bg='white')
        label.place(x=50,y=10)

        label=Label(root,text='Account no',font=('Times new roman',20),bg='white')
        label.place(x=50,y=60)


        e1=Entry(root)
        e2=Entry(root)

        data=cur.fetchall()
        arr=[e1,e2]
        count=0
        for val in data[0]:
            arr[count].insert(0,val)
            count+=1

        e1.place(x=350,y=10)
        e2.place(x=350,y=60)

        label=Button(root,text='Modify',font=('Times new roman',20),bg='blue',command=update_command_deposit)
        label.place(x=300,y=400)


    except:
        l=Label(root,text='Invalid Account no',font=('times new roman',15))
        l.place(x=100,y=300)
        update_deposit()

def update_command_deposit():

    sql="UPDATE deposit SET amount=%s WHERE acc_no=%s;"
    vals=[e1.get(),e2.get()]
    cur.execute(sql,vals)
    db.commit()
    deposit()

def search_deposit():
    global e2
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Account no:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e2=Entry(root,width=50)
    e2.place(x=300,y=200)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=deposit)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Search", font=("Arial", 15),command=search_deposit_1)
    Button.place(x=400, y=400)
def search_deposit_1():
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)
    try:
        sql='SELECT * FROM deposit WHERE acc_no=%s;'
        val=[e2.get()]
        cur.execute(sql,val)

        Button = tk.Button(root, text="OK", font=("Arial", 15),command=deposit)
        Button.place(x=300, y=400)

        for val in cur:
            count=0
            Y=50
            names=['Amount: ','Account no: ']
            for i in val:
                label=Label(root,text=names[count]+str(i),font=('Times new roman',20),bg='tomato')
                label.place(x=10,y=Y)
                Y+=50
                count+=1
        db.commit()
    except:
        l=Label(root,text='Invalid Account no',font=('times new roman',15))
        l.place(x=100,y=300)
        search_deposit()

def withdraw():
    global root
    #clean previous window
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Deposit Table',font=('Times new roman',15),bg='white')
    label.place(x=350,y=10)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=entity_page)
    Button.place(x=10, y=50)

    Button = tk.Button(root, text="Insert", font=("Arial", 15),command=insert_withdraw)
    Button.place(x=110, y=50)

    Button = tk.Button(root, text="Delete", font=("Arial", 15),command=delete_withdraw)
    Button.place(x=210, y=50)

    Button = tk.Button(root, text="Update", font=("Arial", 15),command=update_withdraw)
    Button.place(x=310, y=50)

    Button = tk.Button(root, text="Search", font=("Arial", 15),command=search_withdraw)
    Button.place(x=410, y=50)

    view_withdraw()


def view_withdraw():
    frame=Frame(root,bd=5,relief=RIDGE,bg='tomato')
    frame.place(x=10,y=100,width=750,height=400)

    x_scroll=Scrollbar(frame,orient=HORIZONTAL)
    y_scroll=Scrollbar(frame,orient=VERTICAL)

    table=ttk.Treeview(frame,columns=('amount',"acc_no"),xscrollcommand=x_scroll.set,
    yscrollcommand=y_scroll.set)

    x_scroll.pack(side=BOTTOM,fill=X)
    y_scroll.pack(side=RIGHT,fill=Y)
    x_scroll.config(command=table.xview)
    y_scroll.config(command=table.yview)
    table.heading('amount',text="Amount")
    table.heading('acc_no',text="Account no")
    table['show']='headings'

    #table.column("f_id",width=100)


    table.pack()



    cur.execute("SELECT * FROM withdraw;")

    data =cur.fetchall()
    db.commit()
    if len(data)!=0:
        for row in data:
            table.insert('',END,values=row)

e1,e2,e3,e4,e5,e6=0,0,0,0,0,0
def insert_withdraw():
    global e1,e2,e3,e4,e5,e6
    #clean the window
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)


    #create the window
    label=Label(root,text='Amount',font=('Times new roman',20),bg='white')
    label.place(x=50,y=10)

    label=Label(root,text='Account no',font=('Times new roman',20),bg='white')
    label.place(x=50,y=60)


    e1=Entry(root,width=50)
    e2=Entry(root,width=50)

    e1.place(x=350,y=10)
    e2.place(x=350,y=60)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=withdraw)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Commit", font=("Arial", 15),command=insert_withdraw_command)
    Button.place(x=400, y=400)

def insert_withdraw_command():
    try:
        sql="INSERT INTO withdraw values(%s,%s);"
        vals=e1.get(),e2.get()
        cur.executemany(sql,[vals])
        db.commit()

        #need to add to amount in another table
        subs_amount=int(vals[0])
        cur.execute("SELECT amount FROM account where acc_no=%s;",[vals[1]])
        
        data=cur.fetchall()
        #print(data)
        prev_amount=int(data[-1][0])
        #print(subs_amount,prev_amount)
        if subs_amount>prev_amount:
            #clean the window
            label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
            label.place(x=0,y=0)
            label=Label(root,text='Insufficient Balance',font=('Times new roman',30),bg='white')
            label.place(x=150,y=150)
            Button = tk.Button(root, text="Back", font=("Arial", 15),command=insert_withdraw)
            Button.place(x=400, y=400)
            
        else:
            total=prev_amount-subs_amount
            cur.executemany("update account set amount=%s where acc_no=%s;",[(total,vals[1])])
            db.commit()
            withdraw()
    except:
        insert_withdraw()


def delete_withdraw():
    global e2
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='acc_no:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e2=Entry(root,width=50)
    e2.place(x=300,y=200)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=withdraw)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Commit", font=("Arial", 15),command=delete_withdraw_command)
    Button.place(x=400, y=400)


def delete_withdraw_command():
    try:
        sql="DELETE FROM withdraw WHERE acc_no=%s;"
        cur.execute(sql,[e2.get()])
        db.commit()
        withdraw()
    except:
        l=Label(root,text='Invalid Entry',font=('times new roman',15))
        l.place(x=100,y=300)

def update_withdraw():
    global e2
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Account no:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e2=Entry(root,width=50)
    e2.place(x=300,y=200)

    Button = tk.Button(root, text="OK", font=("Arial", 15),command=update_withdraw_1)

    Button.place(x=300, y=400)

def update_withdraw_1():
    try:
        global e1,e2,e3,e4,e5,e6
        #clean
        label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
        label.place(x=0,y=0)

        sql='SELECT * FROM withdraw WHERE acc_no=%s;'
        vals=[e2.get()]
        cur.execute(sql,vals)

        label=Label(root,text='Amount',font=('Times new roman',20),bg='white')
        label.place(x=50,y=10)

        label=Label(root,text='Account no',font=('Times new roman',20),bg='white')
        label.place(x=50,y=60)


        e1=Entry(root)
        e2=Entry(root)

        data=cur.fetchall()
        arr=[e1,e2]
        count=0
        for val in data[0]:
            arr[count].insert(0,val)
            count+=1

        e1.place(x=350,y=10)
        e2.place(x=350,y=60)

        label=Button(root,text='Modify',font=('Times new roman',20),bg='blue',command=update_command_withdraw)
        label.place(x=300,y=400)


    except:
        l=Label(root,text='Invalid Account no',font=('times new roman',15))
        l.place(x=100,y=300)
        update_withdraw()

def update_command_withdraw():

    sql="UPDATE withdraw SET amount=%s WHERE acc_no=%s;"
    vals=e1.get(),e2.get()
    cur.executemany(sql,[vals])
    db.commit()
    withdraw()

def search_withdraw():
    global e2
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Account no:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e2=Entry(root,width=50)
    e2.place(x=300,y=200)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=withdraw)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Search", font=("Arial", 15),command=search_withdraw_1)
    Button.place(x=400, y=400)
def search_withdraw_1():
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)
    try:
        sql='SELECT * FROM withdraw WHERE acc_no=%s;'
        val=[e2.get()]
        cur.execute(sql,val)

        Button = tk.Button(root, text="OK", font=("Arial", 15),command=withdraw)
        Button.place(x=300, y=400)

        for val in cur:
            count=0
            Y=50
            names=['Amount: ','Account no: ']
            for i in val:
                label=Label(root,text=names[count]+str(i),font=('Times new roman',20),bg='tomato')
                label.place(x=10,y=Y)
                Y+=50
                count+=1
        db.commit()
    except:
        l=Label(root,text='Invalid Account no',font=('times new roman',15))
        l.place(x=100,y=300)
        search_withdraw()

def borrower():
    global root
    #clean previous window
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Borrower Table',font=('Times new roman',15),bg='white')
    label.place(x=350,y=10)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=entity_page)
    Button.place(x=10, y=50)

    Button = tk.Button(root, text="Insert", font=("Arial", 15),command=insert_borrower)
    Button.place(x=110, y=50)

    Button = tk.Button(root, text="Delete", font=("Arial", 15),command=delete_borrower)
    Button.place(x=210, y=50)

    Button = tk.Button(root, text="Update", font=("Arial", 15),command=update_borrower)
    Button.place(x=310, y=50)

    Button = tk.Button(root, text="Search", font=("Arial", 15),command=search_borrower)
    Button.place(x=410, y=50)

    view_borrower()


def view_borrower():
    frame=Frame(root,bd=5,relief=RIDGE,bg='tomato')
    frame.place(x=10,y=100,width=750,height=400)

    x_scroll=Scrollbar(frame,orient=HORIZONTAL)
    y_scroll=Scrollbar(frame,orient=VERTICAL)

    table=ttk.Treeview(frame,columns=("cust_id",'loan_no'),xscrollcommand=x_scroll.set,
    yscrollcommand=y_scroll.set)

    x_scroll.pack(side=BOTTOM,fill=X)
    y_scroll.pack(side=RIGHT,fill=Y)
    x_scroll.config(command=table.xview)
    y_scroll.config(command=table.yview)
    table.heading('cust_id',text="customer id")
    table.heading('loan_no',text="loan number")
    table['show']='headings'

    #table.column("cust_id",width=100)


    table.pack()



    cur.execute("SELECT * FROM borrower;")

    data =cur.fetchall()
    db.commit()
    if len(data)!=0:
        for row in data:
            table.insert('',END,values=row)

e1,e2,e3,e4,e5,e6=0,0,0,0,0,0
def insert_borrower():
    global e1,e2,e3,e4,e5,e6
    #clean the window
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)


    #create the window
   
    label=Label(root,text='customer id',font=('Times new roman',20),bg='white')
    label.place(x=50,y=60)

    label=Label(root,text='loan number',font=('Times new roman',20),bg='white')
    label.place(x=50,y=110)


    e1=Entry(root,width=50)
    e2=Entry(root,width=50)
  

    e1.place(x=350,y=10)
    e2.place(x=350,y=60)
    
   
    Button = tk.Button(root, text="Back", font=("Arial", 15),command=borrower)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Commit", font=("Arial", 15),command=insert_borrower_command)
    Button.place(x=400, y=400)

def insert_borrower_command():
    try:
        sql="INSERT INTO borrower values(%s,%s);"
        vals=e1.get(),e2.get()
        cur.executemany(sql,[vals])
        db.commit()
        borrower()
    except:
        insert_borrower()
def delete_borrower():
    global e1
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='customer id:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e1=Entry(root,width=50)
    e1.place(x=300,y=200)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=borrower)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Commit", font=("Arial", 15),command=delete_borrower_command)
    Button.place(x=400, y=400)


def delete_borrower_command():
    try:
        sql="DELETE FROM borrower WHERE cust_id=%s;"
        cur.execute(sql,[e1.get()])
        db.commit()
        borrower()
    except:
        l=Label(root,text='Invalid Entry',font=('times new roman',15))
        l.place(x=100,y=300)

def update_borrower():
    global e1
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='cust_id:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e1=Entry(root,width=50)
    e1.place(x=300,y=200)

    Button = tk.Button(root, text="OK", font=("Arial", 15),command=update_borrower_1)

    Button.place(x=300, y=400)

def update_borrower_1():
    try:
        global e1,e2,e3,e4,e5,e6
        #clean
        label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
        label.place(x=0,y=0)

        sql='SELECT * FROM borrower WHERE cust_id=%s;'
        vals=[e1.get()]
        cur.execute(sql,vals)

     
        label=Label(root,text='customer id',font=('Times new roman',20),bg='white')
        label.place(x=50,y=10)

        label=Label(root,text='loan number',font=('Times new roman',20),bg='white')
        label.place(x=50,y=60)

      


        e1=Entry(root)
        e2=Entry(root)
     
      

        data=cur.fetchall()
        arr=[e1,e2]
        count=0
        for val in data[0]:
            arr[count].insert(0,val)
            count+=1

        e1.place(x=350,y=10)
        e2.place(x=350,y=60)

       

        label=Button(root,text='Modify',font=('Times new roman',20),bg='blue',command=update_command_borrower)
        label.place(x=300,y=400)


    except:
        l=Label(root,text='Invalid loan number',font=('times new roman',15))
        l.place(x=100,y=300)
        update_account()

def update_command_borrower():

    sql="UPDATE borrower SET loan_no=%s WHERE cust_id=%s;"
    vals=e2.get(),e1.get()
    cur.executemany(sql,[vals])
    db.commit()
    borrower()

def search_borrower():
    global e1
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='customer:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e1=Entry(root,width=50)
    e1.place(x=300,y=200)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=borrower)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Search", font=("Arial", 15),command=search_borrower_1)
    Button.place(x=400, y=400)
def search_borrower_1():
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)
    try:
        sql='SELECT * FROM borrower WHERE cust_id=%s;'
        val=[e1.get()]
        cur.execute(sql,val)

        Button = tk.Button(root, text="OK", font=("Arial", 15),command=borrower)
        Button.place(x=300, y=400)

        for val in cur:
            count=0
            Y=50
            names=['customer_id: ','loan number: ']
            for i in val:
                label=Label(root,text=names[count]+str(i),font=('Times new roman',20),bg='tomato')
                label.place(x=10,y=Y)
                Y+=50
                count+=1
        db.commit()
    except:
        l=Label(root,text='Invalid loan number',font=('times new roman',15))
        l.place(x=100,y=300)
        search_borrower()


def loan():
    global root
    #clean previous window
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Loan Table',font=('Times new roman',15),bg='white')
    label.place(x=350,y=10)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=entity_page)
    Button.place(x=10, y=50)

    Button = tk.Button(root, text="Insert", font=("Arial", 15),command=insert_loan)
    Button.place(x=110, y=50)

    Button = tk.Button(root, text="Delete", font=("Arial", 15),command=delete_loan)
    Button.place(x=210, y=50)

    Button = tk.Button(root, text="Update", font=("Arial", 15),command=update_loan)
    Button.place(x=310, y=50)

    Button = tk.Button(root, text="Search", font=("Arial", 15),command=search_loan)
    Button.place(x=410, y=50)

    view_loan()


def view_loan():
    frame=Frame(root,bd=5,relief=RIDGE,bg='tomato')
    frame.place(x=10,y=100,width=750,height=400)

    x_scroll=Scrollbar(frame,orient=HORIZONTAL)
    y_scroll=Scrollbar(frame,orient=VERTICAL)

    table=ttk.Treeview(frame,columns=("loan_no",'amount','branch_name','acc_no'),xscrollcommand=x_scroll.set,
    yscrollcommand=y_scroll.set)

    x_scroll.pack(side=BOTTOM,fill=X)
    y_scroll.pack(side=RIGHT,fill=Y)
    x_scroll.config(command=table.xview)
    y_scroll.config(command=table.yview)
    table.heading('loan_no',text="Loan no")
    table.heading('amount',text="Amount")


    table.heading('branch_name',text="Branch name")
    table.heading('acc_no',text="Account no")
    
    table['show']='headings'

    #table.column("f_id",width=100)


    table.pack()



    cur.execute("SELECT * FROM loan;")

    data =cur.fetchall()
    db.commit()
    if len(data)!=0:
        for row in data:
            table.insert('',END,values=row)

e1,e2,e3,e4,e5,e6=0,0,0,0,0,0
def insert_loan():
    global e1,e2,e3,e4,e5,e6
    #clean the window
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)


    #create the window
    label=Label(root,text='Loan no',font=('Times new roman',20),bg='white')
    label.place(x=50,y=10)

    label=Label(root,text='Amount',font=('Times new roman',20),bg='white')
    label.place(x=50,y=60)

    label=Label(root,text='Branch name',font=('Times new roman',20),bg='white')
    label.place(x=50,y=110)

    label=Label(root,text='Account no',font=('Times new roman',20),bg='white')
    label.place(x=50,y=160)


    e1=Entry(root,width=50)
    e2=Entry(root,width=50)
    e3=Entry(root,width=50)
    e4=Entry(root,width=50)
    

    e1.place(x=350,y=10)
    e2.place(x=350,y=60)
    #e2.insert(0,datetime.now())
    e3.place(x=350,y=110)
    e4.place(x=350,y=160)


    Button = tk.Button(root, text="Back", font=("Arial", 15),command=loan)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Commit", font=("Arial", 15),command=insert_loan_command)
    Button.place(x=400, y=400)

def insert_loan_command():
    try:
        sql="INSERT INTO loan values(%s,%s,%s,%s);"
        vals=e1.get(),e2.get(),e3.get(),e4.get()
        cur.executemany(sql,[vals])
        db.commit()
        loan()
    except:
        insert_loan()
def delete_loan():
    global e1
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Loan no:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e1=Entry(root,width=50)
    e1.place(x=300,y=200)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=loan)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Commit", font=("Arial", 15),command=delete_loan_command)
    Button.place(x=400, y=400)


def delete_loan_command():
    try:
        sql="DELETE FROM loan WHERE loan_no=%s;"
        cur.execute(sql,[e1.get()])
        db.commit()
        loan()
    except:
        l=Label(root,text='Invalid Entry',font=('times new roman',15))
        l.place(x=100,y=300)

def update_loan():
    global e1
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Loan no:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e1=Entry(root,width=50)
    e1.place(x=300,y=200)

    Button = tk.Button(root, text="OK", font=("Arial", 15),command=update_loan_1)

    Button.place(x=300, y=400)

def update_loan_1():
    try:
        global e1,e2,e3,e4,e5,e6
        #clean
        label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
        label.place(x=0,y=0)

        sql='SELECT * FROM loan WHERE loan_no=%s;'
        vals=[e1.get()]
        cur.execute(sql,vals)

        label=Label(root,text='Loan no',font=('Times new roman',20),bg='white')
        label.place(x=50,y=10)

        label=Label(root,text='Amount',font=('Times new roman',20),bg='white')
        label.place(x=50,y=60)

        label=Label(root,text='Branch name',font=('Times new roman',20),bg='white')
        label.place(x=50,y=110)

        label=Label(root,text='Account no',font=('Times new roman',20),bg='white')
        label.place(x=50,y=160)


        e1=Entry(root)
        e2=Entry(root)
        e3=Entry(root)
        e4=Entry(root)

        #e6=Entry(root)

        data=cur.fetchall()
        arr=[e1,e2,e3,e4,e5]
        count=0
        for val in data[0]:
            arr[count].insert(0,val)
            count+=1

        e1.place(x=350,y=10)
        e2.place(x=350,y=60)
        #e2.insert(0,datetime.now())
        e3.place(x=350,y=110)
        e4.place(x=350,y=160)
    
        #e6.place(x=350,y=270)

        label=Button(root,text='Modify',font=('Times new roman',20),bg='blue',command=update_command_loan)
        label.place(x=300,y=400)


    except:
        l=Label(root,text='Invalid laon_no',font=('times new roman',15))
        l.place(x=100,y=300)
        update_loan()

def update_command_loan():

    sql="UPDATE loan SET amount=%s,branch_name=%s,acc_no=%s WHERE loan_no=%s;"
    vals=e2.get(),e3.get(),e4.get(),e1.get()
    cur.executemany(sql,[vals])
    db.commit()
    loan()

def search_loan():
    global e1
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)

    #window
    label=Label(root,text='Loan no:',font=('Times new roman',20),bg='tomato')
    label.place(x=100,y=200)

    e1=Entry(root,width=50)
    e1.place(x=300,y=200)

    Button = tk.Button(root, text="Back", font=("Arial", 15),command=loan)
    Button.place(x=200, y=400)

    Button = tk.Button(root, text="Search", font=("Arial", 15),command=search_loan_1)
    Button.place(x=400, y=400)
def search_loan_1():
    #clean
    label=Label(root,text=' '*800,font=('Times new roman',500),bg='tomato')
    label.place(x=0,y=0)
    try:
        sql='SELECT * FROM loan WHERE loan_no=%s;'
        val=[e1.get()]
        cur.execute(sql,val)

        Button = tk.Button(root, text="OK", font=("Arial", 15),command=loan)
        Button.place(x=300, y=400)

        for val in cur:
            count=0
            Y=50
            names=['Loan no: ','Amount: ','Branch name: ','Account no: ']
            for i in val:
                label=Label(root,text=names[count]+str(i),font=('Times new roman',20),bg='tomato')
                label.place(x=10,y=Y)
                Y+=50
                count+=1
        db.commit()
    except:
        l=Label(root,text='Invalid loan no',font=('times new roman',15))
        l.place(x=100,y=300)
        search_loan()

First_page(root)
root.mainloop()