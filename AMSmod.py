from tkinter import *
from tkinter import ttk
import sqlite3

den1, den2 = '', ''
nm, fl_nm, fl_no, frst, eco = '', '', '', '', ''
Top, stp = 0, 0
passwrd = ''
imgtp=0


def config(root):
    root.title("WELCOME TO NETAJI INTERNATIONAL AIRPORT")
    root.geometry("1350x700+0+0")
    #root.configure(bg='#00ffff')
    root.state("zoom")


def create3():
    con = sqlite3.connect('airways.db')
    cur1 = con.cursor()
    str = "create table MAIN (NAME VARCHAR(100),DATE_OF_BIRTH VARCHAR(30),RELIGION VARCHAR(30),NATIONALITY VARCHAR(30),ADDRESS VARCHAR(100),STATE VARCHAR(30),MOBILE_NO INTEGER,EMAIL_ID VARCHAR(100),DESTINATION VARCHAR(100),FLIGHT_N0 VARCHAR(30),CLASS VARCHAR(30));"
    cur1.execute(str)
    con.commit()
    con.close()


def create():
    con = sqlite3.connect('airways.db')
    cur1 = con.cursor()
    str = "create table DESTINATION (NAME VARCHAR(100), FLIGHT_AVAILABLE VARCHAR(30), FLIGHT_NO VARCHAR(10) PRIMARY KEY,NO_OF_FIRST_CLASS INTEGER,NO_OF_ECONOMY_CLASS INTEGER);"
    cur1.execute(str)
    con.commit()
    con.close()


def drop_dest():
    con = sqlite3.connect('airways.db')
    cur1 = con.cursor()
    str = "drop table DESTINATION;"
    cur1.execute(str)
    con.commit()
    con.close()


def show_dest():
    global Top
    tv = ttk.Treeview(Top, columns=(1, 2, 3, 4, 5), show='headings', height=38)
    tv.place(x=10, y=40, width=1000)
    tv.heading(1, text="NAME")
    tv.heading(2, text="FLIGHT_AVAILABLE")
    tv.heading(3, text="FLIGHT_NO")
    tv.heading(4, text='FIRST_CLASS')
    tv.heading(5, text='ECONOMY_CLASS')
    con = sqlite3.connect('airways.db')
    cur1 = con.cursor()
    str = "select *from DESTINATION;"
    cur1.execute(str)
    rows = cur1.fetchall()
    for i in rows:
        tv.insert('', 'end', values=i)

    con.close()


def insert4():
    con = sqlite3.connect('airways.db')
    cur1 = con.cursor()
    str = "insert into DESTINATION values('{}','{}','{}',{},{})".format(nm.get().upper(), fl_nm.get().upper(),
                                                                        fl_no.get(), frst.get(), eco.get())
    cur1.execute(str)
    lb = Label(Top, text='DATA SAVED', font=('arial', 13, 'bold'))
    lb.place(x=400, y=600)
    con.commit()
    con.close()


def insert3():
    global nm, fl_nm, fl_no, frst, eco
    fr1 = Frame(Top, bg='#9999cc')
    fr1.place(x=10, y=150, width=700, height=300)
    lb1 = Label(fr1, text='NAME:', font=('arial', 13, 'bold'))
    lb1.place(x=10, y=10)
    nm = Entry(fr1, font=('arial', 15, 'bold'))
    nm.place(x=10, y=40)
    lb2 = Label(fr1, text='FLIGHT TO TRAVEL:', font=('arial', 13, 'bold'))
    lb2.place(x=10, y=90)
    fl_nm = Entry(fr1, font=('arial', 15, 'bold'))
    fl_nm.place(x=10, y=120)
    lb3 = Label(fr1, text='FLIGHT NO:', font=('arial', 13, 'bold'))
    lb3.place(x=300, y=90)
    fl_no = Entry(fr1, font=('arial', 15, 'bold'))
    fl_no.place(x=300, y=120)
    lb4 = Label(fr1, text='NO. OF FIRST CLASS:', font=('arial', 13, 'bold'))
    lb4.place(x=10, y=170)
    frst = Entry(fr1, font=('arial', 15, 'bold'))
    frst.place(x=10, y=200)
    lb5 = Label(fr1, text='NO. OF ECONOMY CLASS:', font=('arial', 13, 'bold'))
    lb5.place(x=300, y=170)
    eco = Entry(fr1, font=('arial', 15, 'bold'))
    eco.place(x=300, y=200)
    sub = Button(fr1, text='SUBMIT', command=insert4)
    sub.place(x=10, y=250)


def show_main():
    global Top
    tv = ttk.Treeview(Top, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), show='headings', height=38)
    tv.place(x=10, y=40, width=2000)
    tv.heading(1, text="NAME")
    tv.heading(2, text='DEST')
    tv.heading(3, text='FL NO.')
    tv.heading(4, text='CLASS')
    tv.heading(5, text="DOB")
    tv.heading(6, text="REL")
    tv.heading(7, text='NAT')
    tv.heading(8, text='ADD')
    tv.heading(9, text='STATE')
    tv.heading(10, text='MOB NO.')
    tv.heading(11, text='EMAIL')
    con = sqlite3.connect('airways.db')
    cur1 = con.cursor()
    str = "select NAME, DESTINATION, FLIGHT_N0, CLASS, DATE_OF_BIRTH, RELIGION, NATIONALITY, ADDRESS, STATE, MOBILE_NO, EMAIL_ID from MAIN;"
    cur1.execute(str)
    rows = cur1.fetchall()
    for i in rows:
        tv.insert('', 'end', values=i)

    con.close()


def drop_main():
    con = sqlite3.connect('airways.db')
    cur1 = con.cursor()
    str = "drop table MAIN;"
    cur1.execute(str)
    con.commit()
    con.close()


def win1():
    global Top,imgtp
    Top = Toplevel()
    Top.geometry('1350x700')
    Top.title('ADMIN PAGE')
    Top.configure(bg='#333333')
    lbtp=Label(Top,image=imgtp)
    lbtp.pack()
    shw = Button(Top, text='SHOW MAIN TABLE', command=show_main)
    shw.place(x=10, y=10)
    ct = Button(Top, text='CREATE MAIN TABLE', command=create3)
    ct.place(x=150, y=10)
    drpmn = Button(Top, text='DELETE MAIN TABLE', command=drop_main)
    drpmn.place(x=150, y=50)
    dest = Button(Top, text='CREATE DESTINATIONS', command=create)
    dest.place(x=295, y=10)
    dest2 = Button(Top, text='SHOW DESTINATIONS', command=show_dest)
    dest2.place(x=450, y=10)
    dest3 = Button(Top, text='DROP DESTINATIONS', command=drop_dest)
    dest3.place(x=295, y=50)
    dest4 = Button(Top, text='INSERT DESTINATION', command=insert3)
    dest4.place(x=450, y=50)


def step2():
    ps = passwrd.get()
    ps = ps.upper()
    if ps == 'WEAREONE':
        lb1 = Label(stp, text='HELLO SIR, CLICK CONTINUE TO PROCEED', font=('times new roman', 10, 'bold'))
        lb1.place(x=10, y=90)
        cont = Button(stp, text='CONTINUE', command=win1)
        cont.place(x=10, y=120)
    else:
        lb2 = Label(stp, text='ACCESS DENIED', font=('times new roman', 10, 'bold'))
        lb2.place(x=10, y=100)


def step1():
    global stp
    stp = Toplevel()
    stp.geometry('350x150')
    stp.title('PASS')
    stp.configure(bg='#000000')
    ps = Label(stp, text='ENTER PASSWORD:', font=('times new roman', 13, 'bold'))
    ps.place(x=10, y=10)
    global passwrd
    passwrd = Entry(stp, show='*', font=('times new roman', 15, 'bold'))
    passwrd.place(x=10, y=50)
    accept = Button(stp, text='->', command=step2)
    accept.place(x=250, y=50)


def insert2():
    con = sqlite3.connect('airways.db')
    cur1 = con.cursor()
    str = "insert into MAIN values('{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}');".format(en.get().upper(),
                                                                                                  en2.get(),
                                                                                                  en3.get().upper(),
                                                                                                  en4.get().upper(),
                                                                                                  en5.get().upper(),
                                                                                                  en6.get().upper(),
                                                                                                  en7.get(), en8.get(),
                                                                                                  en9.get().upper(),
                                                                                                  den1.get(),
                                                                                                  den2.get().upper())
    cur1.execute(str)
    done = Label(root, text="IT'S OUR PLEASURE TO HELP YOU TRAVEL. YOUR DATA HAS BEEN SAVED",
                 font=('times new roman', 15, 'bold'))
    done.place(x=600, y=700)
    con.commit()
    con.close()


def insert1():
    global den1, den2
    dl1 = Label(root, text="YOUR FLIGHT NO. PLEASE:", font=('times new roman', 15, 'bold'))
    dl1.place(x=800, y=450)
    den1 = Entry(root, font=('times new roman', 15, 'bold'))
    den1.place(x=800, y=490)
    dl2 = Label(root, text="PLEASE MENTION THE CLASS:", font=('times new roman', 15, 'bold'))
    dl2.place(x=800, y=540)
    den2 = Entry(root, font=('times new roman', 15, 'bold'))
    den2.place(x=800, y=580)
    sub = Button(root, text='SUBMIT', command=insert2)
    sub.place(x=800, y=620)


def display():
    dl = Label(root, text='AVAILABLE FLIGHTS ARE DISPLAYED BELOW', font=('times new roman', 15, 'bold'))
    dl.place(x=800, y=100)
    tv = ttk.Treeview(root, columns=(1, 2, 3), show='headings', height=10)
    tv.place(x=730, y=150, width=600)
    tv.heading(1, text="NAME")
    tv.heading(2, text="FL NAME")
    tv.heading(3, text="FL NO.")
    con = sqlite3.connect('airways.db')
    cur1 = con.cursor()
    str = "select NAME, FLIGHT_AVAILABLE, FLIGHT_NO from destination where name='{0}'".format(en9.get().upper())
    cur1.execute(str)
    rows = cur1.fetchall()
    for i in rows:
        tv.insert('', 'end', values=i)

    con.close()
    dbn = Button(root, text='CHOOSE MY FLIGHT', command=insert1)
    dbn.place(x=800, y=400)


root = Tk()
img=PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Programs\Teaching Python\plane1.png")
imgtp=PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Programs\Teaching Python\admin1.png")


backg=Label(root,image=img)
backg.pack()


bn = Button(root, text='ADMIN', command=step1)
bn.place(x=10, y=10)


config(root)
msg = Label(root, text='PLEASE FILL IN CAPITALS', font=('times new roman', 10, 'bold'))
msg.place(x=10, y=100)
lb = Label(root, text='ENTER NAME:', font=('times new roman', 13, 'bold'))
lb.place(x=30, y=150)
en = Entry(root, font=('times new roman', 15, 'bold'))
en.place(x=30, y=180)
lb2 = Label(root, text='ENTER DATE OF BIRTH:', font=('times new roman', 13, 'bold'))
lb2.place(x=30, y=230)
en2 = Entry(root, font=('times new roman', 15, 'bold'))
en2.place(x=30, y=260)
lb3 = Label(root, text='ENTER RELIGION:', font=('times new roman', 13, 'bold'))
lb3.place(x=30, y=310)
en3 = Entry(root, font=('times new roman', 15, 'bold'))
en3.place(x=30, y=340)
lb4 = Label(root, text='ENTER NATIONALITY:', font=('times new roman', 13, 'bold'))
lb4.place(x=320, y=310)
en4 = Entry(root, font=('times new roman', 15, 'bold'))
en4.place(x=320, y=340)
lb5 = Label(root, text='ENTER ADDRESS:', font=('times new roman', 13, 'bold'))
lb5.place(x=30, y=390)
en5 = Entry(root, font=('times new roman', 15, 'bold'))
en5.place(x=30, y=420)
lb6 = Label(root, text='ENTER STATE:', font=('times new roman', 13, 'bold'))
lb6.place(x=320, y=390)
en6 = Entry(root, font=('times new roman', 15, 'bold'))
en6.place(x=320, y=420)
lb7 = Label(root, text='ENTER MOBILE NO. :', font=('times new roman', 13, 'bold'))
lb7.place(x=30, y=470)
en7 = Entry(root, font=('times new roman', 15, 'bold'))
en7.place(x=30, y=500)
lb8 = Label(root, text='ENTER EMAIL ID:', font=('times new roman', 13, 'bold'))
lb8.place(x=320, y=470)
en8 = Entry(root, font=('times new roman', 15, 'bold'))
en8.place(x=320, y=500)
lb9 = Label(root, text='ENTER DESTINATION:', font=('times new roman', 13, 'bold'))
lb9.place(x=30, y=550)
en9 = Entry(root, font=('times new roman', 15, 'bold'))
en9.place(x=30, y=580)
bn1 = Button(root, text='SUBMIT', command=display)
bn1.place(x=320, y=580)

root.mainloop()
