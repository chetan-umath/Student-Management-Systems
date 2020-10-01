from Tkinter import *
from tkMessageBox import *
import sqlite3

#------------------------------------------------------------------------------//---------------------//-------------------------/////---------------------------------------
def page3():
    root = Tk()
    v_course=IntVar()
    v_dept=IntVar()
    v_certifi=IntVar()
    con=sqlite3.Connection('mydbms')
    cur=con.cursor()
    cur.execute('create table if not exists stu_data(roll_no number(5) primary key,fname varchar(10),lname varchar(10),dob varchar(11),father varchar(10),course varchar(5),dept varchar(5),sem varchar(11),address varchar(20),mobile number,email varchar(10),cgpa number(4,2),dist varchar(30),state varchar(5))')


def page3():
    root = Tk()
    v_course=IntVar()
    v_dept=IntVar()
    v_certifi=IntVar()
    con=sqlite3.Connection('mydbms')
    cur=con.cursor()
    cur.execute('create table if not exists stu_data(roll_no number(5) primary key,fname varchar(10),lname varchar(10),dob varchar(11),father varchar(10),course varchar(5),dept varchar(5),sem varchar(11),address varchar(20),mobile number,email varchar(10),cgpa number(4,2),dist varchar(30),state varchar(5))')


    root.attributes('-fullscreen',True)
    shortcutbar = Frame(root, height=100, bg='light blue')
    Label(shortcutbar,text='\nStudent Personal Information',font='Algerian 22',fg='red',bg='light blue').pack(side=TOP,anchor=CENTER)
    shortcutbar.pack(expand=NO, fill=X)




    def initialize():
        e_roll.delete(0,END)
        e_fname.delete(0,END)
        e_lname.delete(0,END)
        e_dob_day.delete(0,END)
        e_father_name.delete(0,END)
        v_course=0
        v_dept=0
        e_sem.delete(0,END)
        e_address.delete(0,END)
        e_phone.delete(0,END)
        e_email.delete(0,END)
        e_cgpa.delete(0,END)
        e_dist.delete(0,END)
        e_state.delete(0,END)



    def save():
        a1=str()
        a2=str()
        if e_roll.get()!='':
            if e_fname.get().isdigit() or e_lname.get().isdigit():
                    showerror('Invalid Name!!',' Please Enter valid name')
            if v_course.get()==0:
                a1='B.Tech'
            elif v_course.get()==1:
                a1='M.Tech'
            elif v_course.get()==2:
                a1='PHD'
                    
            if v_dept.get()==0:
                 a2='CSE'
            elif v_dept.get()==1:
                 a2='ECE'
            elif v_dept.get()==2:
                 a2='MEC'
            elif v_dept.get()==3:
                 a2='CE'
            elif v_dept.get()==4:
                 a2='CHE'
             
            cur.execute('insert into stu_data values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(e_roll.get(),e_fname.get(),e_lname.get(),e_dob_day.get(),e_father_name.get(),a1,a2,e_sem.get(),e_address.get(),e_phone.get(),e_email.get(),e_cgpa.get(),e_dist.get(),e_state.get()))
            
            showinfo('success','save data completed!!')
            root.destroy()
            page4()
        else:
            showerror('ERROR','Enrollment number field cannot be empty')


    def search(x):
        def go1(y):
            cur.execute("select * from stu_data where fname='"+y+"'")
            #showinfo('result',cur.fetchone())
            r=Tk()
            r.attributes('-fullscreen',True)
            shortcutbar = Frame(r, height=100, bg='light blue')
            Label(shortcutbar,text='\nStudent Full Detial\n\n',font='Time 22',fg='red',bg='light blue').pack(side=TOP,anchor=CENTER)
            shortcutbar.pack(expand=NO, fill=X)
            Label(shortcutbar,text= cur.fetchone(),font='Time 15',fg='blue').pack(side=TOP,anchor=CENTER)

            Label(r, text='\n\n\nthis is the Enrollment no ,first name,last name ,date of birth,course,branch,semester,CGPA,contact no.,\nEmail,Addres,Distict and state where they belong are respectively',fg='red',font='Times 20').pack(side=TOP,anchor=CENTER)    
            Label(r, text=cur.fetchone(),fg='red',font='cambaria 12',bg='light blue').pack(side=TOP,anchor=CENTER)
            def Quit(event=None):
                if askokcancel("Quit", "Do you really want to Quit?"):
                    r.destroy()
                    
            shortcutbar = Frame(r, height=768, bg='light blue')
           
            Button(shortcutbar, text='EXIT',width=16,height=1,bg='grey',fg='black',font='Times 12 bold',command=Quit).pack(side=LEFT, anchor=SW)
            shortcutbar.pack(side=BOTTOM,expand=NO, fill=BOTH)
            
            
         
            
        def go3(y):
            cur.execute("select * from stu_data where roll_no="+y)
            #showinfo('result',cur.fetchone())
            r=Tk()
            r.attributes('-fullscreen',True)
            shortcutbar = Frame(r, height=100, bg='light blue')
            Label(shortcutbar,text='\nStudent Full Detial\n\n',font='Time 22',fg='red',bg='light blue').pack(side=TOP,anchor=CENTER)
            shortcutbar.pack(expand=NO, fill=X)
            Label(shortcutbar,text= cur.fetchone(),font='Time 15',fg='blue').pack(side=TOP,anchor=CENTER)

            Label(r, text='\n\n\nthis is the Enrollment no ,first name,last name ,date of birth,course,branch,semester,CGPA,contact no.,\nEmail,Addres,Distictand state where they belong are respectively',fg='red',font='Times 20').pack(side=TOP,anchor=CENTER)    
            Label(r, text=cur.fetchone(),fg='red',font='cambaria 12',bg='light blue').pack(side=TOP,anchor=CENTER)
            def Quit(event=None):
                if askokcancel("Quit", "Do you really want to Quit?"):
                    r.destroy()
                    
            shortcutbar = Frame(r, height=768, bg='light blue')
           
            Button(shortcutbar, text='EXIT',width=16,height=1,bg='grey',fg='black',font='Times 12 bold',command=Quit).pack(side=LEFT, anchor=SW)
            shortcutbar.pack(side=BOTTOM,expand=NO, fill=BOTH)
            
                   
            
                    
            
        if x==1:
            cur.execute('select * from stu_data group by cgpa having max(cgpa)')
            #showinfo('result',cur.fetchone())
            r=Tk()
            r.attributes('-fullscreen',True)
            shortcutbar = Frame(r, height=100, bg='light blue')
            Label(shortcutbar,text='\nStudent Full Detial\n\n',font='Time 22',fg='red',bg='light blue').pack(side=TOP,anchor=CENTER)
            shortcutbar.pack(expand=NO, fill=X)
            Label(shortcutbar,text= cur.fetchone(),font='Time 15',fg='blue').pack(side=TOP,anchor=CENTER)

            Label(r, text='\n\n\nthis is the Enrollment no ,first name,last name ,date of birth,course,branch,semester,CGPA,contact no.,\nEmail,Addres,Distict and state where they belong are show respectively',fg='red',font='Times 20').pack(side=TOP,anchor=CENTER)    
            Label(r, text=cur.fetchone(),fg='red',font='cambaria 12',bg='light blue').pack(side=TOP,anchor=CENTER)
            def Quit(event=None):
                if askokcancel("Quit", "Do you really want to Quit?"):
                    r.destroy()
                    
            shortcutbar = Frame(r, height=768, bg='light blue')
           
            Button(shortcutbar, text='EXIT',width=16,height=1,bg='grey',fg='black',font='Times 12 bold',command=Quit).pack(side=LEFT, anchor=SW)
            shortcutbar.pack(side=BOTTOM,expand=NO, fill=BOTH)
            
                   
            
            


            
        elif x==2:


            r=Tk()
            r.attributes('-fullscreen',True)
            shortcutbar = Frame(r, height=100, bg='light blue')
            Label(shortcutbar,text='\nStudent Full Detial Using First Name\n',font='Time 22',fg='red',bg='light blue').pack(side=TOP,anchor=CENTER)
            shortcutbar.pack(expand=NO, fill=X)
            

            Label(r, text='\n\n\nEnter First Name\n',fg='red',font='Cambaria 15').pack(side=TOP,anchor=CENTER)
            name=Entry(r)
            name.pack(side=TOP,anchor=CENTER)
            Button(r,text='Search',bg='light blue',command=lambda:go1(name.get())).pack(side=TOP,anchor=CENTER)
            def Quit(event=None):
                if askokcancel("Quit", "Do you really want to Quit?"):
                    r.destroy()
                    page1()
            shortcutbar = Frame(r, height=768, bg='light blue')
           
            Button(shortcutbar, text='EXIT',width=16,height=1,bg='grey',fg='black',font='Times 12 bold',command=Quit).pack(side=LEFT, anchor=SW)
            shortcutbar.pack(side=BOTTOM,expand=NO, fill=BOTH)
            
            
    
       
        else:

            r=Tk()
            r.attributes('-fullscreen',True)
            shortcutbar = Frame(r, height=100, bg='light blue')
            Label(shortcutbar,text='\nStudent Full Detial Using Enrollment number\n',font='Time 22',fg='red',bg='light blue').pack(side=TOP,anchor=CENTER)
            shortcutbar.pack(expand=NO, fill=X)
            

            Label(r, text='\n\n\nEnter Enrollment number\n',fg='red',font='Cambaria 15').pack(side=TOP,anchor=CENTER)
            numb=Entry(r)
            numb.pack(side=TOP,anchor=CENTER)
            
            Button(r,text='Search',bg='light blue',command=lambda:go3(numb.get())).pack(side=TOP,anchor=CENTER)
            def Quit(event=None):
                if askokcancel("Quit", "Do you really want to Quit?"):
                    r.destroy()
                    page1()
            shortcutbar = Frame(r, height=768, bg='light blue')
           
            Button(shortcutbar, text='EXIT',width=16,height=1,bg='grey',fg='black',font='Times 12 bold',command=Quit).pack(side=LEFT, anchor=SW)
            shortcutbar.pack(side=BOTTOM,expand=NO, fill=BOTH)
            
            
            


    shortcutbar2 = Frame(root)
    e_roll = Entry(shortcutbar2)
    toolbar2 = Label(shortcutbar2, text="\tEnrollment No.                                 ",font='Times 12 bold',fg='blue')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e_roll.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar2.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)

    shortcutbar3 = Frame(root)
    e_fname = Entry(shortcutbar3)
    toolbar2 = Label(shortcutbar3, text="\tFirst Name                                        ",font='Times 12 bold',fg='blue')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)  
    e_fname.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar3.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)


    shortcutbar4 = Frame(root)
    e_lname = Entry(shortcutbar4)
    toolbar2 = Label(shortcutbar4, text="\tLast Name                                        ",font='Times 12 bold',fg='blue')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)  
    e_lname.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar4.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)


    shortcutbar4 = Frame(root)
    e_dob_day = Entry(shortcutbar4)
    toolbar2 = Label(shortcutbar4, text="\tDate of birth(DD/MM/YYYY)          ",font='Times 12 bold',fg='blue')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e_dob_day.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar4.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
        
    shortcutbar4 = Frame(root)
    e_father_name = Entry(shortcutbar4)
    toolbar2 = Label(shortcutbar4, text="\tFather\'s Name:                                 ",font='Times 12 bold',fg='blue')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e_father_name.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar4.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)


    Label(root, text = '\tCourse:',fg='black',font='Times 12 bold').pack(side=TOP,expand=NO,anchor=NW)
    Radiobutton(root,text='\t     B.Tech',padx=20,variable=v_course,value=0,font='Times 12 bold').pack(anchor=W)
    Radiobutton(root,text='\t     M.Tech',padx=20,variable=v_course,value=1,font='Times 12 bold').pack(anchor=W)
    Radiobutton(root,text='\t     Ph.d',padx=20,variable=v_course,value=2,font='Times 12 bold').pack(anchor=W)
    Label(root, text = '\tBranch',fg='black',font='Times 12 bold').pack(side=TOP,expand=NO,anchor=NW)
    Radiobutton(root,text='\t     CSE',padx=20,variable=v_dept,value=0,font='Times 12 bold').pack(anchor=W)
    Radiobutton(root,text='\t     ECE',padx=20,variable=v_dept,value=1,font='Times 12 bold').pack(anchor=W)
    Radiobutton(root,text='\t     MEC',padx=20,variable=v_dept,value=2,font='Times 12 bold').pack(anchor=W)
    Radiobutton(root,text='\t     CE',padx=20,variable=v_dept,value=3,font='Times 12 bold').pack(anchor=W)
    Radiobutton(root,text='\t     CHE',padx=20,variable=v_dept,value=4,font='Times 12 bold').pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)

    shortcutbar4 = Frame(root)
    e_sem = Entry(shortcutbar4)
    toolbar2 = Label(shortcutbar4, text="\tSemester    ",font='Times 12 bold',fg='blue')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e_sem.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar4.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)

    shortcutbar5 = Frame(root)
    e_cgpa = Entry(shortcutbar4)
    toolbar2 = Label(shortcutbar4, text="\t\t\tCGPA    ",font='Times 12 bold',fg='blue')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e_cgpa.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar5.pack(expand=NO, fill=X)

    shortcutbar6 = Frame(root)
    e_phone = Entry(shortcutbar4)
    toolbar2 = Label(shortcutbar4, text="\t\t\tPhone no.     \t",font='Times 12 bold',fg='blue')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e_phone.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar6.pack(expand=NO, fill=X)




    shortcutbar4 = Frame(root)
    e_email = Entry(shortcutbar4)
    toolbar2 = Label(shortcutbar4, text="\tEmail    ",font='Times 12 bold',fg='blue')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e_email.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar4.pack(expand=NO, fill=X)



    shortcutbar7 = Frame(root)
    e_address = Entry(shortcutbar4)
    toolbar2 = Label(shortcutbar4, text="\t\tAddress    ",font='Times 12 bold',fg='blue')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e_address.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar4.pack(expand=NO, fill=X)



    shortcutbar8 = Frame(root)
    e_dist = Entry(shortcutbar4)
    toolbar2 = Label(shortcutbar4, text="\t\tDistrict    ",font='Times 12 bold',fg='blue')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e_dist.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar4.pack(expand=NO, fill=X)

    shortcutbar9 = Frame(root)
    e_state = Entry(shortcutbar4)
    toolbar2 = Label(shortcutbar4, text="\t\tState    ",font='Times 12 bold',fg='blue')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e_state.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar4.pack(expand=NO, fill=X)


    
    def page4():
      
        r=Tk()
        r.attributes('-fullscreen',True)

        shortcutbar = Frame(r, height=100, bg='black')
        Label(shortcutbar,text='\n--------What is in Your Mind --------',font='Cambaria 22',fg='Pink',bg='black').pack(side=TOP,anchor=CENTER)


        shortcutbar.pack(expand=NO, fill=X)
        shortcutbar1 = Frame(r, height=100)
        Label(shortcutbar1,text='\n\n\n').pack(side=TOP,anchor=CENTER)
        Label(shortcutbar1,text='\n').pack(side=TOP,anchor=CENTER)
        Label(shortcutbar1,text='\n').pack(side=TOP,anchor=CENTER)
        Label(shortcutbar1,text='\n').pack(side=TOP,anchor=CENTER)

        shortcutbar1.pack(expand=NO, fill=X)


        shortcutbar2 = Frame(r, height=100)
        Label(shortcutbar2,text='Please Chose Your Option\n What You Want to Do',font='Cambaria 15',fg='orange').pack(side=TOP,anchor=CENTER)


        shortcutbar2.pack(expand=NO, fill=X)
        


        def new():
            r.destroy()
            page3()
        def Quit(event=None):
            if askokcancel("Quit", "Do you really want to Quit?"):
               r.destroy()
               page1()

        def Back(event=None):
            r.destroy()
            page2()
        def view():
            r.destroy()
            p=Tk()
            p.attributes('-fullscreen',True)

            shortcutbar2 = Frame(p, height=100, bg='light blue')
            Label(shortcutbar2,text='\nThrough what Reference You Want To View Data',font='Time 24',fg='red',bg='light blue').pack(side=TOP,anchor=CENTER)
            shortcutbar2.pack(expand=NO, fill=X)
            Label(p,text='\n').pack()
           # Label(j,text='Enter Yours choise').grid(row=0,columnspan=10)
            Label(p,text='\n').pack()
            Label(p,text='\n').pack()
          
            Label(p,text='After Press the Button in new page\n \nFill the Entry',fg='blue',font='Comic 12 bold').pack()
            Label(p,text='\n').pack()
            Label(p,text='\n').pack()
            def fun2():
                p.destroy()
                search(4)
            def fun3():
                p.destroy()
                search(1)

            def fun4():
                p.destroy()
                search(2)
                
            Button(p,text=' Enrollment _no  ',font='Comic 15 bold',bg='light green',command=lambda:fun2()).pack()
            Label(p,text='\n').pack()
            Button(p,text=' Highest cgpa    ',font='Comic 15 bold',bg='light green',command=lambda:fun3()).pack()
            Label(p,text='\n').pack()
            Button(p,text='  First name       ',font='Comic 15 bold',bg='light green',command=lambda:fun4()).pack()
            def Quit(event=None):
                if askokcancel("Quit", "Do you really want to Quit?"):
                    p.destroy()
                    page1()
            shortcutbar = Frame(p, height=768, bg='light blue')
           
            Button(shortcutbar, text='EXIT',width=16,height=1,bg='grey',fg='black',font='Times 12 bold',command=Quit).pack(side=LEFT, anchor=SW)
            shortcutbar.pack(side=BOTTOM,expand=NO, fill=BOTH)
            
                
            

        Label(r,text='\n').pack()
        Label(r,text='\n').pack()
        Button(r,text='  New   ',font='Comic 15 bold',bg='light green',command=lambda:new()).pack()
        Label(r,text='\n').pack()

        Button(r,text='  View  ',font='Comic 15 bold',bg='light green',command=lambda:view()).pack()
        Label(r,text='\n').pack()

        Button(r,text='  Back  ',font='Comic 15 bold',bg='light green',command=lambda:Back()).pack()

        Label(r,text='\n').pack()

        Button(r,text='  Exit   ',font='Comic 15 bold',bg='light green',command=lambda:Quit()).pack()
        shortcutbar = Frame(r, height=50, bg='light blue')
           
            
        shortcutbar.pack(side=BOTTOM,expand=NO, fill=BOTH)


   # Button(root,text='Retrive',font='Comic 12 bold',bg='light gray',command=lambda:fun1()).pack()
        

    Button(root,text='SUBMIT',font='Comic 10 bold',bg='light blue',command=lambda:save()).pack()

    def Quit(event=None):
            if askokcancel("Quit", "Do you really want to Quit?"):
                root.destroy()
                page1()
    shortcutbar2 = Frame(root, height=768, bg='light green')
    Button(shortcutbar2, text='EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 12 bold',command=Quit).pack(side=RIGHT, anchor=SW)
    shortcutbar2.pack(side=BOTTOM,expand=NO, fill=BOTH)
        










#-----------------------------------------------------------///---------------------//---------------------------///-------------------------------------------
def page2():
    root=Tk()
    root.attributes('-fullscreen',True)
    shortcutbar = Frame(root, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='Password Production',bg='gray',fg='red',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
    def Quit(event=None):
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            page1()
    s = Frame(root, height=30, bg='light green')
    Button(s, text='EXIT',width=16,height=1,bg='gray',fg='black',font='Times 12 bold',command=Quit).pack(side=LEFT, anchor=SW)
    s.pack(side=BOTTOM,expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="Welcome \nPlease fill the below Entery to continue.",fg='blue',height=2,font='Calibri 12 bold')
    toolbar1.pack(side=TOP,fill=X,expand=YES)
    shortcutbar1.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO)
    Label(root,text=" ").pack(side=TOP,expand=NO)

    shortcutbar2 = Frame(root)
    e1 = Entry(shortcutbar2)
    toolbar2 = Label(shortcutbar2, text="                                                                               Enrollment No.  \n",font='Arial 10 bold')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e1.pack()
    shortcutbar2.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)

    shortcutbar3 = Frame(root)
    e2 = Entry(shortcutbar3)
    toolbar2 = Label(shortcutbar3, text="                                                                                Password        \n\n",font='Arial 10 bold')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e2.pack()
    shortcutbar3.pack(expand=NO, fill=X)
  

    

    
       
    def info():
            if(str(e1.get())=='' or str(e2.get())==''):
                s=showerror(title="Error",message='Fill the entries.')

           
            else:
                 if (int(str(e1.get()))==151453 and int(str(e2.get()))==151453):
                    root.destroy()
                    page3()

                 else:
                       Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
                       Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
                       Label(root,text=" The ID or Password is Wrong Please Try Again",fg='red').pack(side=TOP,expand=NO, fill=X)
    def submit(event=None):
        info()
            
    shortcutbar1 = Frame(root, height=1000)


    Button(shortcutbar1, text='SUBMIT',width=16,height=1,bg='light blue',fg='black',font='Times 12 bold',command=submit,relief=RAISED).pack()
    shortcutbar1.pack(expand=NO, fill=X)



#-----------------------------------------------------------///---------------------//---------------------------///-------------------------------------------
def aboutus():
    root=Tk()
    root.attributes('-fullscreen',True)

    shortcutbar = Frame(root, height=30, bg='light green')
    toolbar = Label(shortcutbar, text='Student Management System',bg='gray',fg='white',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
   
    Label(root, text='\n\n\n\n\n',fg='black',font='Times 18').pack(side=TOP,anchor=CENTER)
    Label(root, text='Name :  Yuvraj Singh Parmar (151453)',fg='Red',font='Times 18 bold').pack(side=TOP,anchor=CENTER)
    Label(root, text='Branch - CSE(B7)',fg='black',font='Times 16 bold').pack(side=TOP,anchor=CENTER)
    Label(root, text='Email: yuvrajparmar1997@gmail.com',fg='black',font='Times 18 bold').pack(side=TOP,anchor=CENTER)
    Label(root, text='Contact No. : 9589280614',fg='orange',font='Times 18 bold').pack(side=TOP,anchor=CENTER)
    Label(root, text='\nUnder the guiadence of',fg='black',font='Times 18').pack(side=TOP,anchor=CENTER)
    Label(root, text='Dr. Mahesh Kumar sir',fg='black',font='Times 19 bold').pack(side=TOP,anchor=CENTER)
    Label(root, text='\n\n\n\n\n\n\n\n\nClick  NEXT  Button to Continue',fg='black',font='Times 12').pack(side=TOP,anchor=CENTER)
    def sbmt():
        root.destroy()
        page2()
    def Quit(event=None):
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            page1()
    s = Frame(root, height=30, bg='light blue')
    Button(s, text='EXIT',width=16,height=1,bg='light green',fg='black',font='Times 12 bold',command=Quit).pack(side=LEFT, anchor=SW)
    Button(s, text='NEXT',width=16,height=1,bg='light green',fg='black',font='Times 12 bold',command=sbmt).pack(side=RIGHT, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)



#-----------------------------------------------------------///---------------------//---------------------------///----------------------------------------
global page1
def page1():
    root = Tk()
    root.attributes('-fullscreen',True)
    shortcutbar = Frame(root, height=30, bg='light blue')
    shortcutbar.pack(expand=NO, fill=X)
    shortcutbar1 = Frame(root, height=1000)
    Label(shortcutbar1, text='\n\n\n\n\n\n\nStudent Management\n',fg='green',font='Algerian 25').pack(side=TOP,anchor=CENTER)
    Label(shortcutbar1, text='System\n\n\n\n',fg='green',font='Algerian 25').pack(side=TOP,anchor=CENTER)
    Label(shortcutbar1, text='Sign up to Continue\n',fg='orange',font='Times 12').pack(side=TOP,anchor=CENTER)
    
    def abt():
        root.destroy()
        aboutus()
    def sbmt():
        root.destroy()
        page2()
    def Quit(event=None):
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
    Button(shortcutbar1, text='SIGN UP',width=16,height=1,bg='grey',fg='black',font='Times 12 bold',command=sbmt,relief=RAISED).pack()
    shortcutbar1.pack(expand=NO, fill=X)
    
    shortcutbar2 = Frame(root, height=768, bg='light blue')
    Button(shortcutbar2, text='ABOUT ME',width=16,height=1,bg='silver',fg='black',font='Times 12 bold',command=abt).pack(side=LEFT, anchor=SE)
    Button(shortcutbar2, text='EXIT',width=16,height=1,bg='silver',fg='black',font='Times 12 bold',command=Quit).pack(side=RIGHT, anchor=SW)
    shortcutbar2.pack(side=BOTTOM,expand=NO, fill=BOTH)
    root.mainloop()
page1()


#-----------------------------------------------------------///---------------------//---------------------------///----------------------------------------



