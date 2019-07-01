# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:54:32 2019

@author: XZ
"""
import tkinter as tk
from tkinter import messagebox
import pymysql

db = pymysql.connect(host="localhost", user="root",
                     password="Bo13602371572@", database="Lab_2", port=3306)

class basedesk():
    def __init__(self,master):
        self.root = master
        self.root.config()
        self.root.title('Welcome to MIS')
        self.root.geometry('600x400')
        
        login_face(self.root)        
                
class login_face():
    def __init__(self,master):
        
        self.master = master

        #基准界面login_face
        self.login_face = tk.Frame(self.master,)
        self.login_face.pack()
        
        # welcome image
        self.canvas = tk.Canvas(self.login_face, height=400, width=600)
#        image_file = tk.PhotoImage(file='bg.png')
#        self.image = self.canvas.create_image(0, 0, anchor='nw', image=image_file)
        self.canvas.pack(side='top')

        
        # user information
        tk.Label(self.login_face, text='User name: ', background="#%02x%02x%02x" % (153, 204, 204)).place(x=160, y= 150)
        tk.Label(self.login_face, text='Password: ', background="#%02x%02x%02x" % (153, 204, 204)).place(x=160, y= 190)

        self.var_usr_name = tk.StringVar()
        self.var_usr_name.set('administrator')
        entry_usr_name = tk.Entry(self.login_face, textvariable=self.var_usr_name, background="#%02x%02x%02x" % (207, 229, 228))
        entry_usr_name.place(x=290, y=150)
        self.var_usr_pwd = tk.StringVar()
        entry_usr_pwd = tk.Entry(self.login_face, textvariable=self.var_usr_pwd, show='*', background="#%02x%02x%02x" % (207, 229, 228))
        entry_usr_pwd.place(x=290, y=190)
        
        # login and sign up button
        btn_login = tk.Button(self.login_face, text='Login', command=self.usr_login)
        btn_login.place(x=260, y=230)
        
        #btn.pack()
        
    def usr_login(self,):
        usr_name = self.var_usr_name.get()
        usr_pwd = self.var_usr_pwd.get()
        
        if usr_name == "administrator":
            if usr_pwd != "0000":
                tk.messagebox.showerror(message='Error, your password is wrong, try again.')
            else:
                self.login_face.destroy()
                option_face(self.master, 0)
                
        elif usr_name == "teacher":
            if usr_pwd != "0000":
                tk.messagebox.showerror(message='Error, your password is wrong, try again.')
            else:
                self.login_face.destroy()
                option_face(self.master, 1)
            
        elif usr_name == "student":
            if usr_pwd !="0000":
                tk.messagebox.showerror(message='Error, your password is wrong, try again.')
            else:
                self.login_face.destroy()
                query_face(self.master, 2)
        else:
            tk.messagebox.showerror(message='Invalid user name, try again.') 

class option_face():
    def __init__(self,master, authority):
        self.authority = authority
        self.master = master
        self.option_face = tk.Frame(self.master,)
        self.option_face.pack()
        
        self.canvas = tk.Canvas(self.option_face, height=400, width=600,)
        self.canvas.pack(side='top')
        
        tk.Label(self.option_face, text="MODIFY").place(x=160, y=30)
        tk.Label(self.option_face, text="QUERY").place(x=350, y=30)
        
        btn_student = tk.Button(self.option_face,text='Student',command=self.modify_student)
        btn_student.place(x=160,y=80)
        btn_course = tk.Button(self.option_face,text='Course',command=self.modify_course)
        btn_course.place(x=160,y=130)
        btn_chosen = tk.Button(self.option_face,text='Course Choosing',command=self.modify_coursechoosing)
        btn_chosen.place(x=160,y=180)
        btn_query = tk.Button(self.option_face,text='ALL',command=self.show_query)
        btn_query.place(x=350,y=130)
        btn_back = tk.Button(self.option_face,text='Back',command=self.back)
        btn_back.place(x=10, y=300)
        
        #case teacher
        if self.authority == 1:
            btn_student.config(state=tk.DISABLED)
            btn_course.config(state=tk.DISABLED)
            btn_chosen.config(text = 'Score')

    def back(self):
        self.option_face.destroy()
        login_face(self.master)

    def modify_student(self):
        self.option_face.destroy()
        m_student_face(self.master, self.authority)
        
    def modify_course(self):
        self.option_face.destroy()
        m_course_face(self.master, self.authority)
        
    def modify_coursechoosing(self):
        self.option_face.destroy()
        m_courseChoosing_face(self.master, self.authority)
    
    def show_query(self):
        self.option_face.destroy()
        query_face(self.master, self.authority)
        
class m_student_face():
    def __init__(self, master, authority):
        self.authority=authority
        self.master = master
        self.face = tk.Frame(self.master)
        self.face.pack()
        
        self.canvas = tk.Canvas(self.face, height=1000, width=1000)
        self.canvas.pack(side='top')
        
        tk.Label(self.face, text='Name: ').place(x=150, y= 80)
        tk.Label(self.face, text='ID: ').place(x=150, y= 40)
        tk.Label(self.face, text='Gender: ').place(x=150, y= 120)
        tk.Label(self.face, text='Entrance Age: ').place(x=150, y= 160)       
        tk.Label(self.face, text='Entrance Year: ').place(x=150, y= 200)
        tk.Label(self.face, text='Class: ').place(x=150, y= 240)

        self.var_list=[]
        entry_list=[]
        for i in range(6):
            self.var_list.append(tk.StringVar())
            entry_list.append(tk.Entry(self.face, textvariable=self.var_list[i]))
            entry_list[i].place(x=270, y=40*(i+1))

        btn_search = tk.Button(self.face, text='Search',command=self.search)
        btn_search.place(x=420, y=40)
        btn_insert = tk.Button(self.face, text='Insert',command=self.insert)
        btn_insert.place(x=150, y=300)
        btn_update = tk.Button(self.face, text='Update',command=self.update)
        btn_update.place(x=250, y=300)        
        btn_delete = tk.Button(self.face, text='Delete',command=self.delete)
        btn_delete.place(x=350, y=300)
        btn_back = tk.Button(self.face, text='Back',command=self.back)
        btn_back.place(x=10, y=300)
        btn_clear = tk.Button(self.face, text='Clear', command=self.clear)
        btn_clear.place(x=450, y=300)
    
    def back(self):
        self.face.destroy()
        option_face(self.master, self.authority)

    def clear(self):
        for i in range(len(self.var_list)):
            self.var_list[i].set("")

    def search(self):
        cur = db.cursor()
        sql = ""
        print(self.var_list[0].get())
        print(self.var_list[1].get())
        if self.var_list[0].get() is "":
            sql = """select *  from Student where Student.S_Name='%s'"""%(self.var_list[1].get())
        elif self.var_list[1].get() is "":
            sql = """select *  from Student where Student.ID='%s'""" % (self.var_list[0].get())
        cur.execute(sql)
        self.data = cur.fetchall()
        if len(self.data) == 0:
            tk.messagebox.showwarning("WARNING", message="Student: " + self.var_list[0].get() + " is not found!")
            return
        for i in range(6):
            self.var_list[i].set(self.data[0][i])


    def insert(self):
        cur = db.cursor()
        print(self.var_list[0].get())
        print(self.var_list[1].get())
        if int(self.var_list[3].get())<10 or int(self.var_list[3].get())>50:
            tk.messagebox.showwarning("WARNING",message="Student's Entance Age should be in range 10-50!")
            return

        sql = """insert into Student(ID ,S_Name,Gender,age,school_year,class ) 
        values('%s', '%s', '%s', %s, %s, %s)"""%(self.var_list[0].get(), self.var_list[1].get(),
                                                self.var_list[2].get(), self.var_list[3].get(),
                                                 self.var_list[4].get(), self.var_list[5].get())
        cur.execute(sql)
        db.commit()
        tk.messagebox.showinfo(message="Insert Student: " + self.var_list[0].get() + " successfully!")
        self.clear()

    def update(self):
        cur = db.cursor()
        for i in range(6):
            if  self.var_list[i].get() == "":
                tk.messagebox.showerror(message="Fill in all the blanks.")
                return
            if int(self.var_list[3].get()) < 10 or int(self.var_list[3].get()) > 50:
                tk.messagebox.showwarning("WARNING", message="Student's Entance Age should be in range 10-50!")
                return

        sql = """
                update Student set S_Name= '%s',Gender='%s', 
                age=%s, school_year=%s,class=%s where ID = %s;
            """ % (self.var_list[1].get(),
                    self.var_list[2].get(), self.var_list[3].get(),
                    self.var_list[4].get(), self.var_list[5].get(), self.var_list[0].get())
        cur.execute(sql)
        db.commit()
        tk.messagebox.showinfo(message="Update Student: " + self.var_list[0].get()+" successfully!")
        self.clear()

    def delete(self):
        cur = db.cursor()
        sql = "delete from Choose where Student_ID=%s" % (self.var_list[0].get())
        cur.execute(sql)
        sql = "delete from Student where ID=%s" % (self.var_list[0].get())
        cur.execute(sql)
        db.commit()
        tk.messagebox.showinfo(message="Delete Student: " + self.var_list[0].get() + " successfully!")
        self.clear()

class m_course_face():
    def __init__(self, master, authority):
        self.authority=authority
        self.master = master
        self.face = tk.Frame(self.master)
        self.face.pack()
        
        self.canvas = tk.Canvas(self.face, height=1000, width=1000)
        self.canvas.pack(side='top')
        
        tk.Label(self.face, text='Course ID: ').place(x=150, y= 40)
        tk.Label(self.face, text='Name: ').place(x=150, y= 80)
        tk.Label(self.face, text='Teacher ID: ').place(x=150, y= 120)
        tk.Label(self.face, text='Credit: ').place(x=150, y= 160)       
        tk.Label(self.face, text='Grade: ').place(x=150, y= 200)
        tk.Label(self.face, text='Canceled Year: ').place(x=150, y= 240)

        self.var_list = []
        entry_list = []
        for i in range(6):
            self.var_list.append(tk.StringVar())
            entry_list.append(tk.Entry(self.face, textvariable=self.var_list[i]))
            entry_list[i].place(x=270, y=40 * (i + 1))

        btn_search = tk.Button(self.face, text='Search', command=self.search)
        btn_search.place(x=420, y=40)
        btn_insert = tk.Button(self.face, text='Insert', command=self.insert)
        btn_insert.place(x=150, y=300)
        btn_update = tk.Button(self.face, text='Update', command=self.update)
        btn_update.place(x=250, y=300)
        btn_delete = tk.Button(self.face, text='Delete', command=self.delete)
        btn_delete.place(x=350, y=300)
        btn_back = tk.Button(self.face, text='Back', command=self.back)
        btn_back.place(x=10, y=300)
        btn_clear = tk.Button(self.face, text='Clear', command=self.clear)
        btn_clear.place(x=450, y=300)

    def back(self):
        self.face.destroy()
        option_face(self.master, self.authority)

    def clear(self):
        for i in range(len(self.var_list)):
            self.var_list[i].set("")

    def search(self):
        cur = db.cursor()
        sql = ""
        print(self.var_list[0].get())
        print(self.var_list[1].get())
        if self.var_list[0].get() is "":
            sql = """select *  from Class where Class.C_Name='%s'""" % (self.var_list[1].get())
        elif self.var_list[1].get() is "":
            sql = """select *  from Class where Class.ID='%s'""" % (self.var_list[0].get())
        cur.execute(sql)
        self.data = cur.fetchall()
        if len(self.data) == 0:
            tk.messagebox.showwarning("WARNING", message="Course: " + self.var_list[0].get() + " is not found!")
            return
        for i in range(6):
            self.var_list[i].set(self.data[0][i])

    def insert(self):
        cur = db.cursor()
        print(self.var_list[0].get())
        print(self.var_list[1].get())
        sql = """insert into Class(ID ,C_Name,Teacher_ID, Credit, Suitable_Grade, Cancel_Year) 
               values('%s', '%s', '%s', %s, %s, %s)""" % (self.var_list[0].get(), self.var_list[1].get(),
                                                          self.var_list[2].get(), self.var_list[3].get(),
                                                          self.var_list[4].get(), self.var_list[5].get())
        cur.execute(sql)
        db.commit()
        tk.messagebox.showinfo(message="Insert Course: " + self.var_list[0].get() + " successfully!")
        self.clear()

    def update(self):
        cur = db.cursor()
        for i in range(6):
            if self.var_list[i].get() == "":
                tk.messagebox.showerror(message="Fill in all the blanks.")
                return
        sql = """
                       update Class set C_Name= '%s',Teacher_ID='%s', 
                       Credit=%s, Suitable_Grade=%s,Cancel_Year=%s where ID = %s;
                   """ % (self.var_list[1].get(),
                          self.var_list[2].get(), self.var_list[3].get(),
                          self.var_list[4].get(), self.var_list[5].get(), self.var_list[0].get())
        cur.execute(sql)
        db.commit()
        tk.messagebox.showinfo(message="Update Course: " + self.var_list[0].get() + " successfully!")
        self.clear()

    def delete(self):
        cur = db.cursor()
        sql = "delete from Choose where Course_ID=%s" % (self.var_list[0].get())
        cur.execute(sql)
        sql = "delete from Class where ID=%s" % (self.var_list[0].get())
        cur.execute(sql)
        db.commit()
        tk.messagebox.showinfo(message="Delete Course: " + self.var_list[0].get() + " successfully!")
        self.clear()


class m_courseChoosing_face():
    def __init__(self, master, authority):
        self.authority = authority
        self.master = master
        self.face = tk.Frame(self.master)
        self.face.pack()
        
        self.canvas = tk.Canvas(self.face, height=1000, width=1000)
        self.canvas.pack(side='top')
        
        tk.Label(self.face, text='Student ID: ').place(x=150, y= 40)
        tk.Label(self.face, text='Course ID ').place(x=150, y= 80)
        tk.Label(self.face, text='Teacher ID: ').place(x=150, y= 120)
        tk.Label(self.face, text='Chosen year: ').place(x=150, y= 160)       
        tk.Label(self.face, text='Score: ').place(x=150, y= 200)

        self.var_list = []
        self.entry_list = []
        for i in range(5):
            self.var_list.append(tk.StringVar())
            self.entry_list.append(tk.Entry(self.face, textvariable=self.var_list[i]))
            self.entry_list[i].place(x=270, y=40 * (i + 1))

        btn_search = tk.Button(self.face, text='Search', command=self.search)
        btn_search.place(x=420, y=40)
        btn_insert = tk.Button(self.face, text='Insert', command=self.insert)
        btn_insert.place(x=150, y=300)
        btn_update = tk.Button(self.face, text='Update', command=self.update)
        btn_update.place(x=250, y=300)
        btn_delete = tk.Button(self.face, text='Delete', command=self.delete)
        btn_delete.place(x=350, y=300)
        btn_back = tk.Button(self.face, text='Back', command=self.back)
        btn_back.place(x=10, y=300)
        btn_clear = tk.Button(self.face, text='Clear', command=self.clear)
        btn_clear.place(x=450, y=300)

        # case adminitrator
        if self.authority == 0:
            self.entry_list[4].config(state=tk.DISABLED)
        else:
            btn_insert.place_forget()
            btn_delete.place_forget()
            for i in (2, 3):
                self.entry_list[i].config(state=tk.DISABLED)

    def back(self):
        self.face.destroy()
        option_face(self.master, self.authority)

    def clear(self):
        for i in range(len(self.var_list)):
            self.var_list[i].set("")
        if self.authority == 1:
            self.entry_list[0].config(state=tk.NORMAL)
            self.entry_list[1].config(state=tk.NORMAL)

    def search(self):
        cur = db.cursor()
        sql = ""
        print(self.var_list[0].get())
        print(self.var_list[1].get())
        sql = """select *  from Choose 
            where Choose.Student_ID ='%s' and Choose.Course_ID ='%s'""" % (self.var_list[0].get(),self.var_list[1].get())
        cur.execute(sql)
        self.data = cur.fetchall()
        print(self.data)
        if len(self.data) == 0:
            tk.messagebox.showwarning("WARNING", message="Not found!")
            return
        for i in range(5):
            self.var_list[i].set(self.data[0][i])
        if self.authority == 1:
            self.entry_list[0].config(state=tk.DISABLED)
            self.entry_list[1].config(state=tk.DISABLED)

    def insert(self):
        cur = db.cursor()
        print(self.var_list[0].get())
        print(self.var_list[1].get())
        sql="""select Class.ID, Teacher_ID from Class where  Class.ID='%s'and Teacher_ID='%s'"""%(self.var_list[1].get(),self.var_list[2].get())
        cur.execute(sql)
        self.data = cur.fetchall()
        if len(self.data) == 0:
            tk.messagebox.showwarning("WARNING", message="Teacher: "
                                                         + self.var_list[2].get()
                                                         + " is not teaching course " + self.var_list[1].get())
            return

        sql="""select Student.school_year,Class.Suitable_Grade 
        from Student,Class 
        where Student.ID='%s' and Class.ID='%s' and Student.school_year<=Class.Suitable_Grade"""%(self.var_list[0].get(),self.var_list[1].get())
        cur.execute(sql)
        self.data = cur.fetchall()
        if len(self.data) == 0:
            tk.messagebox.showwarning("WARNING", message="Student: "
                                                         + self.var_list[0].get()
                                                         + " can not choose course " + self.var_list[1].get())
            return

        sql = """insert into Choose(Student_ID,Course_ID,Teacher_ID,Choose_Year,Grade) 
               values('%s', '%s', '%s', %s, %s)""" % (self.var_list[0].get(), self.var_list[1].get(),
                                                          self.var_list[2].get(), self.var_list[3].get(),
                                                          "null")
        cur.execute(sql)
        db.commit()
        tk.messagebox.showinfo(message="Insert Course: " + self.var_list[0].get() + " successfully!")
        self.clear()

    def update(self):
        cur = db.cursor()
        for i in range(5):
            if self.var_list[i].get() == "":
                tk.messagebox.showerror(message="Fill in all the blanks.")
                return

        sql = """select Class.ID, Teacher_ID from Class where Class.ID='%s'and Teacher_ID='%s'""" %(self.var_list[1].get(),self.var_list[2].get())
        cur.execute(sql)
        self.data = cur.fetchall()
        if len(self.data) == 0:
            tk.messagebox.showwarning("WARNING", message="Teacher: "
                                                         + self.var_list[2].get()
                                                         + " is not teaching course " + self.var_list[1].get())
            return

        if self.authority == 0:
            sql = """
                                   update Choose set Course_ID='%s', 
                            Teacher_ID='%s', Choose_Year=%s,Grade=%s where Student_ID= '%s';
                               """ % (self.var_list[1].get(), self.var_list[2].get(),
                                      self.var_list[3].get(), "null", self.var_list[0].get())
        else:
            sql = """
                                   update Choose set Course_ID='%s', 
                            Teacher_ID='%s', Choose_Year=%s,Grade=%s where Student_ID= '%s';
                               """ % (self.var_list[1].get(), self.var_list[2].get(),
                                      self.var_list[3].get(), self.var_list[4].get(), self.var_list[0].get())
        cur.execute(sql)
        db.commit()
        tk.messagebox.showinfo(message="Update successfully!")
        self.clear()
        if self.authority == 1:
            self.entry_list[0].config(state=tk.NORMAL)
            self.entry_list[1].config(state=tk.NORMAL)

    def delete(self):
        cur = db.cursor()
        sql = "delete from Choose where Student_ID=%s" % (self.var_list[0].get())
        cur.execute(sql)
        db.commit()
        tk.messagebox.showinfo(message="Delete successfully!")
        self.clear()

        
        
class query_face():
    def __init__(self, master, authority):
        self.authority = authority
        self.master = master
        self.face = tk.Frame(self.master,)
        self.face.pack()
        
        self.canvas = tk.Canvas(self.face, height=1000, width=1000)
        self.canvas.pack(side='top')
        
        items = [('Student',0),('Score',1),('Course Choosing',2),('Teacher',3),('Average',4)]
        self.selection = tk.IntVar(0)
        for item, n in items:
            #case student
            if(self.authority == 2 and (n == 3 or n == 4)):
                continue
            tk.Radiobutton(self.face, text=item,
                            variable=self.selection, value=n,
                    command=self.select).place(x=(n+1)*100-50, y=20)

        self.label1 = tk.Label(self.face, text='Name')
        self.label1.place(x=30, y=50)
        self.label2 = tk.Label(self.face, text='ID')
        self.label2.place(x=280, y=50)
        self.label3 = tk.Label(self.face, text='Course')

        self.var1 = tk.StringVar()
        entry1 = tk.Entry(self.face, textvariable=self.var1)
        entry1.place(x=120, y=50)
        self.var2 = tk.StringVar()
        entry2 = tk.Entry(self.face, textvariable=self.var2)
        entry2.place(x=380, y=50)
        self.var3 = tk.StringVar()
        self.entry3 = tk.Entry(self.face, textvariable=self.var3)
            
        btn_search = tk.Button(self.face, text='Search',command=self.search)
        btn_search.place(x=530, y=50)
        btn_back = tk.Button(self.face, text='Back',command=self.back)
        btn_back.place(x=10, y=10)
        
        self.table = tk.Frame(self.face)
        self.table.place(x=0,y=100)
        
#        attributes = [("Student’s ID", "Name", "Gender", "Entrance Age", "Entrance Year","Class", ),
#                      ("Course’s ID", "Name", "Teacher’s ID", "Credit", "Grade"),
#                      ()]
        
        self.header = (("Student ID","Name","Gender","Entrance Age", "Entrance Year" , "Class", "Course ID", "Course Name","Score"),
                       ("Student ID", "Student Name", "Course ID","Course Name","Score"),
                       ("Student ID", "Student Name", "Course ID","Course Name","Choose.Grade"),
                       ("Teacher Name","Teacher ID","Course ID","Course Name"),
                       ("Average Score",))
        self.data = ()
        self.build_table()

    def select(self, ):
        keys = [('Name', 'ID'), ('Student(N/ID)', 'Course(N/ID)'),
                ('Name', 'ID'), ('Name', 'ID'), ('Student', 'Class')]
        self.label1.config(text=keys[self.selection.get()][0])
        self.label2.config(text=keys[self.selection.get()][1])
        if self.selection.get() == 4:
            self.entry3.place(x=380, y=70)
            self.label3.place(x=280, y=70)
        else:
            self.entry3.place_forget()
            self.label3.place_forget()
        print(self.selection.get())
        
    def back(self):
        self.face.destroy()
        if self.authority == 2:
            login_face(self.master)
        else:
            option_face(self.master, self.authority)

    def build_table(self):
        self.table.destroy()
        self.table = tk.Frame(self.face)
        self.table.place(x=0, y=100)
        self.widgets = list()
        row = 0
        self.widgets.append([])
        for i in range(len(self.header[self.selection.get()])):
            self.widgets[row].append(tk.Label(self.table, text=self.header[self.selection.get()][i], bg="white"))
            self.widgets[row][i].grid(row=row, column=i, sticky="nsew")
        for row in range(len(self.data)):
            self.widgets.append([])
            for i in range(len(self.data[0])):
                self.widgets[row+1].append(tk.Label(self.table, text=self.data[row][i], bg="white"))
                self.widgets[row+1][i].grid(row=row+1, column=i, sticky="nsew")

        self.table.grid_columnconfigure(1, weight=1)
        self.table.grid_columnconfigure(2, weight=1)
        # invisible row after last row gets all extra space
        self.table.grid_rowconfigure(row+1, weight=1)
        
    def search(self):
        #global db
        #db = pymysql.connect(host="localhost", user="root",
        #                     password="Bo13602371572@", database="Lab_2", port=3306)

        cur = db.cursor()
        sql=""
        if self.selection.get() == 0:

            if self.var1.get() is "" and self.var2.get() is "":

                sql = """select S.ID, S.S_Name, S.Gender, S.age, S.school_year, S.class,Ch.Course_ID,Cl.C_Name,Ch.Grade
                    from Student as S, Choose as Ch, Class as Cl where S.ID = Ch.Student_ID and Ch.Course_ID=Cl.ID """
            elif self.var1.get() is "":
                sql = """select S.ID, S.S_Name, S.Gender, S.age, S.school_year, S.class,  Ch.Course_ID,Cl.C_Name,Ch.Grade
                from Student as S, Choose as Ch, Class as Cl
                where S.ID = Ch.Student_ID and Ch.Course_ID=Cl.ID and
                     S.ID = %s"""%(self.var2.get())
            elif self.var2.get() is "":
                sql = """select S.ID, S.S_Name, S.Gender, S.age, S.school_year, S.class, Ch.Course_ID,Cl.C_Name,Ch.Grade
                               from Student as S, Choose as Ch, Class as Cl
                               where S.ID = Ch.Student_ID and Ch.Course_ID=Cl.ID and
                                    S.S_Name = '%s'""" % (self.var1.get())
            else:
                sql = """select S.ID, S.S_Name, S.Gender, S.age, S.school_year, S.class, Ch.Course_ID,Cl.C_Name,Ch.Grade
                                               from Student as S, Choose as Ch, Class as Cl
                                               where S.ID = Ch.Student_ID and Ch.Course_ID=Cl.ID and
                                                    S.S_Name = '%s' and S.ID = %s""" % (self.var1.get(),self.var2.get())

        elif self.selection.get() == 1:


            if self.var1.get() is "" and self.var2.get() is "":
                sql = """select S.ID, S.S_Name, Ch.Course_ID,Cl.C_Name,Ch.Grade
                    from Student as S, Choose as Ch, Class as Cl where S.ID = Ch.Student_ID and Ch.Course_ID=Cl.ID """
            elif self.var2.get() is "":
                sql = """select S.ID, S.S_Name, Ch.Course_ID,Cl.C_Name,Ch.Grade
                from Student as S, Choose as Ch, Class as Cl
                where S.ID = Ch.Student_ID and Ch.Course_ID=Cl.ID and
                     S.ID = %s"""%(self.var1.get())
            elif self.var1.get() is "":
                sql = """select S.ID, S.S_Name, Ch.Course_ID,Cl.C_Name,Ch.Grade
                               from Student as S, Choose as Ch, Class as Cl
                               where S.ID = Ch.Student_ID and Ch.Course_ID=Cl.ID and
                                    Ch.Course_ID = '%s'""" % (self.var2.get())
            else:
                sql = """select S.ID, S.S_Name,  Ch.Course_ID,Cl.C_Name,Ch.Grade
                                               from Student as S, Choose as Ch, Class as Cl
                                               where S.ID = Ch.Student_ID and Ch.Course_ID=Cl.ID and
                                                    S.ID = %s and Ch.Course_ID = '%s'""" % (self.var1.get(),self.var2.get())
        elif self.selection.get() == 2:

            if self.var1.get() is "" and self.var2.get() is "":
                sql = """select S.ID, S.S_Name, Ch.Course_ID,Cl.C_Name,Ch.Grade
                from Student as S, Choose as Ch, Class as Cl
                where S.ID = Ch.Student_ID and Ch.Course_ID=Cl.ID"""
            elif self.var2.get() is "":
                sql = """select S.ID, S.S_Name, Ch.Course_ID,Cl.C_Name,Ch.Grade
                from Student as S, Choose as Ch, Class as Cl
                where S.ID = Ch.Student_ID and Ch.Course_ID=Cl.ID and
                     S.S_Name = '%s'"""%(self.var1.get())
            elif self.var1.get() is "":
                sql = """select S.ID, S.S_Name, Ch.Course_ID,Cl.C_Name,Ch.Grade
                               from Student as S, Choose as Ch, Class as Cl
                               where S.ID = Ch.Student_ID and Ch.Course_ID=Cl.ID and
                                    S.ID = '%s'""" % (self.var2.get())
            else:
                sql = """select S.ID, S.S_Name,  Ch.Course_ID,Cl.C_Name,Ch.Grade
                                               from Student as S, Choose as Ch, Class as Cl
                                               where S.ID = Ch.Student_ID and Ch.Course_ID=Cl.ID and
                                                     S.S_Name = '%s' and S.ID = '%s'""" % (self.var1.get(),self.var2.get())
        elif self.selection.get() == 3:
            if self.var1.get() is "" and self.var2.get() is "":
                sql = """select Te.T_Name,Te.ID,Cl.ID,Cl.C_Name
                          from  Class as Cl ,Teacher as Te where Te.ID=Cl.Teacher_ID """
            elif self.var2.get() is "":
                sql = """select Te.T_Name,Te.ID,Cl.ID,Cl.C_Name
                      from  Class as Cl ,Teacher as Te where Te.ID=Cl.Teacher_ID
                      and Te.T_Name = '%s'""" % (self.var1.get())
            elif self.var1.get() is "":
                sql = """select Te.T_Name,Te.ID,Cl.ID,Cl.C_Name
                                     from  Class as Cl ,Teacher as Te where Te.ID=Cl.Teacher_ID
                                     and Te.ID = '%s'""" % (self.var2.get())
            else:
                sql = """select Te.T_Name,Te.ID,Cl.ID,Cl.C_Name
                                     from  Class as Cl ,Teacher as Te where Te.ID=Cl.Teacher_ID
                                     and Te.T_Name = '%s'and Te.ID = '%s'""" % (self.var1.get(),self.var2.get())

        elif self.selection.get() == 4:
            if self.var1.get() is "" and self.var2.get() is ""and self.var3.get() is "":
                sql = """select avg(Ch.Grade)
                                 from Student as S, Choose as Ch, Class as Cl where S.ID = Ch.Student_ID and Ch.Course_ID=Cl.ID """
            elif self.var2.get() is "" and self.var3.get() is "":
                sql = """select avg(Ch.Grade)
                                 from Student as S, Choose as Ch, Class as Cl where S.ID = Ch.Student_ID and Ch.Course_ID=Cl.ID  
                             and S.ID = '%s'""" % (self.var1.get())
            elif self.var1.get() is "" and self.var3.get() is "":
                sql = """select avg(Ch.Grade)
                                 from Student as S, Choose as Ch, Class as Cl where S.ID = Ch.Student_ID and Ch.Course_ID=Cl.ID  
                             and S.class = '%s'""" % (self.var2.get())
            elif self.var1.get() is "" and self.var2.get() is "":
                sql = """select avg(Ch.Grade)
                                from Student as S, Choose as Ch, Class as Cl where S.ID = Ch.Student_ID and Ch.Course_ID=Cl.ID  
                                 and Ch.Course_ID = '%s'""" % (self.var3.get())

        cur.execute(sql)
        self.data = cur.fetchall()
        # print(self.data)
        # print(type(self.data))
        self.build_table()
        db.commit()

if __name__ == '__main__':    
    root = tk.Tk()
    basedesk(root)
    root.mainloop()

