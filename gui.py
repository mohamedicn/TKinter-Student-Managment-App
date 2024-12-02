from tkinter import *
from tkinter import StringVar , Label , ttk , scrolledtext  , messagebox
from main_module import *
from tkinter import Toplevel
import sys

def verifier():
    a=b=c=d=e=f=g=h=i=j=0
    txt.delete(1.0,END)
    if not aa.get() or aa.get() == "SELECT":
        txt.insert(INSERT," \n\n------------------------------>>\n\nSelect Section Properly \n")
        a=1
    if not bb.get():
        txt.insert(INSERT,"Type First Name \n")
        b=1
    if not cc.get():
        txt.insert(INSERT,"Type Last Name\n")
        c=1
    if not dd.get() or dd.get() == "SELECT":
        txt.insert(INSERT,"Select Class Properly \n")
        d=1
    if not ee.get() or ee.get() == "SELECT":
        txt.insert(INSERT,"Select Section Properly \n")
        e=1
    if not ff.get() or ff.get() == "SELECT":
        txt.insert(INSERT,"Select Gender Properly \n")
        f=1
    if not ii.get() or ii.get() == "SELECT":
        txt.insert(INSERT,"Type Mobile Number\n")
        i=1
    if not jj.get():
        txt.insert(INSERT,"Type Address\n")
        j=1
        
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or g==1 or h==1 or i==1 or j==1 :
        return 1
    else:
        return 0

# TO verify Update Student entries
def verifier1():
    a=b=c=d=e=f=g=h=i=j=k=0
    txt.delete(1.0,END)
    if not roll_roll1.get():
        txt.insert(INSERT,"Type Roll Number \n")
        k=1
    if not aa1.get() or aa1.get() == "SELECT":
        txt.insert(INSERT," \n\n------------------------------>>\n\nSelect Section Properly \n")
        a=1
    if not bb1.get():
        txt.insert(INSERT,"Type First Name \n")
        b=1
    if not cc1.get():
        txt.insert(INSERT,"Type Last Name\n")
        c=1
    if not dd1.get() or dd1.get() == "SELECT":
        txt.insert(INSERT,"Select Class Properly \n")
        d=1
    if not ee1.get() or ee1.get() == "SELECT":
        txt.insert(INSERT,"Select Section Properly \n")
        e=1
    if not ff1.get() or ff1.get() == "SELECT":
        txt.insert(INSERT,"Select Gender Properly \n")
        f=1
   
    if not ii1.get() or ii1.get() == "SELECT":
        txt.insert(INSERT,"Type Mobile Number\n")
        i=1
    if not jj1.get():
        txt.insert(INSERT,"Type Address\n")
        j=1
        
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or g==1 or h==1 or i==1 or j==1 :
        return 1
    else:
        return 0

def add_student() :
    if verifier() == 0 :
        student = {"session" : aa.get() , "first_name" : bb.get() , "last_name" : cc.get() , "class" : dd.get() ,  "section" : ee.get() , "gender" : ff.get() ,"mobile" : ii.get(),"address" : jj.get()}

        return_data = student_create(student)
        txt.delete(1.0,END)
        for key, value in return_data.items() :
            roll=str(key)
            txt.insert(INSERT,"\n------------------------------>>\n")
            txt.insert(INSERT,"Your Details -->>"+"\n\nRoll No. : "+roll+"\nName : "+return_data[key]["first_name"]+" "+return_data[key]["last_name"]+"\nClass : "+return_data[key]["class"]+"\nMobile : "+return_data[key]["mobile"]+"\nAddress :"+return_data[key]["address"],"\n")

        aa.delete(0,END)
        bb.delete(0,END)
        cc.delete(0,END)
        dd.delete(0,END)
        ee.delete(0,END)
        ff.delete(0,END)
        ii.delete(0,END)
        jj.delete(0,END)


def view_student() :
    return_data = student_list()
    txt.delete(1.0,END)
    txt.insert(INSERT,"\n Roll No.,\tStudent Name,\t\t\t Class ,\t\t Section,\t\t Mobile ,\t\t\t\t Address \n")
    for key, value in return_data.items() :
        if return_data[key] == "This Record is Deleted from System" :
            continue
        else :
            roll=str(key)
        txt.insert(INSERT,"\n"+roll+",\t"+return_data[key]["first_name"]+" "+return_data[key]["last_name"]+",\t\t\t"+return_data[key]["class"]+",\t\t"+return_data[key]["section"]+",\t"+",\t"+return_data[key]["mobile"]+",\t\t\t\t"+return_data[key]["address"],"\n")
def fetch_student_data():
    try:
        roll_no = roll_roll1.get()
        # Add debug log
        print("Roll number entered:", roll_no)
        student_data = student_list().get(roll_no)  # fetch student_list() is a function returning a dict
        
        if student_data:

            aa1.set(student_data["session"])
            fn1.set(student_data["first_name"])
            ln1.set(student_data["last_name"])
            dd1.set(student_data["class"])
            ee1.set(student_data["section"])
            ff1.set(student_data["gender"])
            mob1.set(student_data["mobile"])
            ad1.set(student_data["address"])
        else:
            messagebox.showwarning("Not Found", f"No data found for Roll Number {roll_no}.")
    except Exception as e:
        print("Error:", e)
def update_student() :
    if verifier1() == 0 :
        rollNo = roll_roll1.get()
        student = {"session" : aa1.get() , "first_name" : bb1.get() , "last_name" : cc1.get() , "class" : dd1.get() ,  "section" : ee1.get() , "gender" : ff1.get(),"mobile" : ii1.get(),"address" : jj1.get()}
        return_data = student_update(rollNo,student)
        txt.delete(1.0,END)
        for key, value in return_data.items() :
            if key == rollNo :
                rollNo=str(key)
                txt.insert(INSERT,"\n------------------------------>>\n")
                txt.insert(INSERT,"Updated Details -->>"+"\n\nRoll No. : "+rollNo+"\nName : "+return_data[key]["first_name"]+" "+return_data[key]["last_name"]+"\nClass : "+return_data[key]["class"]+"\nMobile : "+return_data[key]["mobile"]+"\nAddress :"+return_data[key]["address"],"\n")

        aa1.delete(0,END)
        bb1.delete(0,END)
        cc1.delete(0,END)
        dd1.delete(0,END)
        ee1.delete(0,END)
        ff1.delete(0,END)
        ii1.delete(0,END)
        jj1.delete(0,END)
        
def delete_student() :
    messagebox.showwarning("Warning","Are you sure ?")
    data = student_delete(entry_delete.get())
    txt.delete(1.0,END)
    txt.insert(INSERT,data)





def classwise():
    return_data = student_list()
    txt.delete(1.0, END)
    txt.insert(INSERT, "\n Roll No.,\tStudent Name,\t\t\t Class ,\t\t Section,\t\t Mobile ,\t\t\t\t Address \n")
    
    # Ensure class is selected correctly, section is optional
    if combo_class.get() in ('1', '2', '3'):  # Class is selected
        for key, value in return_data.items():
            if return_data[key] == "This Record is Deleted from System":
                continue
            else:
                roll = str(key)
                student_class = return_data[key]["class"]
                student_section = return_data[key]["section"]
                
                if combo_class.get() == student_class:
                    # If section is selected, check if section matches
                    if combo_class_section.get() in ('A', 'B', 'C') and combo_class_section.get() == student_section:
                        txt.insert(INSERT, "\n" + roll + ",\t" + return_data[key]["first_name"] + " " + return_data[key]["last_name"] + ",\t\t\t" + student_class + ",\t\t" + student_section + ",\t" + return_data[key]["mobile"] + ",\t\t\t\t" + return_data[key]["address"], "\n")
                    # If section is not selected, show all sections of the selected class
                    elif combo_class_section.get() == "" or combo_class_section.get() not in ('A', 'B', 'C'):
                        txt.insert(INSERT, "\n" + roll + ",\t" + return_data[key]["first_name"] + " " + return_data[key]["last_name"] + ",\t\t\t" + student_class + ",\t\t" + student_section + ",\t" + return_data[key]["mobile"] + ",\t\t\t\t" + return_data[key]["address"], "\n")


    
if __name__=="__main__":
    root=Tk()
    w=1300
    h=600
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.resizable(False, False)
    root.geometry(f'{w}x{h}+{int(x)}+{int(y)}')  
    root.title("Student Management")
    
    # ----------------------
    
    sess = StringVar()
    fn = StringVar()
    ln = StringVar()
    cl = StringVar()
    sect = StringVar()
    gen = StringVar()
    fa_name= StringVar()
    mo_name = StringVar()
    mob = StringVar()
    ad = StringVar()
    
    heading=Label(root,text="New Student",font=("Arial",12),foreground ="#ee9a4d")
    label_a=Label(root,text="Session :",font=("Arial",10),width=10)
    label_b=Label(root,text="First Name :",font=("Arial",10),width=10)
    label_c=Label(root,text="Last Name :",font=("Arial",10),width=10)
    label_d=Label(root,text="Class :",font=("Arial",10),width=10)
    label_e=Label(root,text="Section :",font=("Arial",10),width=10)
    label_f=Label(root,text="Gender :",font=("Arial",10),width=10)
    # label_g=Label(root,text="Father Name :",font=("Arial",10),width=10)
    # label_h=Label(root,text="Mother Name :",font=("Arial",10),width=10)
    label_i=Label(root,text="Mobile :",font=("Arial",10),width=10)
    label_j=Label(root,text="Address :",font=("Arial",10),width=10)
    
    aa = ttk.Combobox(root,width=20)    # Session entry
    aa['values']= ("SELECT","2024-1","2024-3","2024-6","2024-9","2024-12","2025-3","2025-6","2025-9","2025-12")
    aa.current(0) #set the selected item
    
    bb=Entry(root,textvariable=fn,width=20)    # first name
    
    cc=Entry(root,textvariable=ln,width=20)    # last name
    
    dd = ttk.Combobox(root,width=20)    # class name
    dd['values']= ("SELECT",1, 2, 3)
    dd.current(0) #set the selected item
    
    ee = ttk.Combobox(root,width=20)    # section name
    ee['values']= ("A","B","C")
    ee.current(0) #set the selected item
    
    ff = ttk.Combobox(root,width=20)    # gender
    ff['values']= ("SELECT","Male","Female")
    ff.current(0) #set the selected item
    
    
    ii=Entry(root,textvariable=mob,width=20)    # mobile
    
    jj=Entry(root,textvariable=ad,width=20)    # address

   
    heading1=Label(root,text="Update Student",font=("Arial",12),foreground ="#ee9a4d")
    label_roll=Label(root,text="Roll Number :",font=("Arial",10),width=10)
    label_a1=Label(root,text="Session :",font=("Arial",10),width=10)
    label_b1=Label(root,text="First Name :",font=("Arial",10),width=10)
    label_c1=Label(root,text="Last Name :",font=("Arial",10),width=10)
    label_d1=Label(root,text="Class :",font=("Arial",10),width=10)
    label_e1=Label(root,text="Section :",font=("Arial",10),width=10)
    label_f1=Label(root,text="Gender :",font=("Arial",10),width=10)
    # label_g1=Label(root,text="Father Name :",font=("Arial",10),width=10)
    # label_h1=Label(root,text="Mother Name :",font=("Arial",10),width=10)
    label_i1=Label(root,text="Mobile :",font=("Arial",10),width=10)
    label_j1=Label(root,text="Address :",font=("Arial",10),width=10)

    roll1 = StringVar()
    sess1 = StringVar()
    fn1 = StringVar()
    bb1 = StringVar()
    ln1 = StringVar()
    cl1 = StringVar()
    sect1 = StringVar()
    gen1 = StringVar()
    # fa_name1= StringVar()
    # mo_name1 = StringVar()
    mob1 = StringVar()
    ad1 = StringVar()

    roll_roll1=Entry(root,textvariable=roll1,width=20)    # Roll Number

    aa1 = ttk.Combobox(root,width=20)    # Session entry
    aa1['values']= ("SELECT","2024-1","2024-3","2024-6","2024-9","2024-12","2025-3","2025-6","2025-9","2025-12")
    aa1.current(0) #set the selected item
    
    bb1=Entry(root,textvariable=fn1,width=20)    # first name
    
    cc1=Entry(root,textvariable=ln1,width=20)    # last name
    
    dd1 = ttk.Combobox(root,width=20)    # class name
    dd1['values']= ("SELECT",1, 2, 3)
    dd1.current(0) #set the selected item
    
    ee1 = ttk.Combobox(root,width=20)    # section name
    ee1['values']= ("A","B","C")
    ee1.current(0) #set the selected item
    
    ff1 = ttk.Combobox(root,width=20)    # gender
    ff1['values']= ("SELECT","Male","Female")
    ff1.current(0) #set the selected item
    

    
    ii1=Entry(root,textvariable=mob1,width=20)    # mobile
    
    jj1=Entry(root,textvariable=ad1,width=20)    # address

    # ----------------------
    roll_delete = StringVar()
    heading2=Label(root,text="Delete Student",font=("Arial",12),foreground ="#ee9a4d")
    label_del=Label(root,text="Record",font=("Arial",12),width=10)
    label_delete=Label(root,text="Roll Number :",font=("Arial",12),width=10)
    entry_delete=Entry(root,textvariable=roll_delete,font=("Arial",12),width=10)
    
    def addnew():
        
        heading.grid(row=8 , column=1,columnspan=2)
        
        label_a.grid(row=9 , column=1)
        label_b.grid(row=10 , column=1)
        label_c.grid(row=11 , column=1)
        label_d.grid(row=12 , column=1)
        label_e.grid(row=13 , column=1)
        label_f.grid(row=14 , column=1)
        label_i.grid(row=17 , column=1)
        label_j.grid(row=18 , column=1)
  
        aa.grid(row=9 , column=2)   
        bb.grid(row=10 , column=2)
        cc.grid(row=11 , column=2)
        dd.grid(row=12 , column=2)
        ee.grid(row=13 , column=2)
        ff.grid(row=14 , column=2)
        ii.grid(row=17 , column=2)
        jj.grid(row=18 , column=2)

        b1=Button(root,text="ADD",command=lambda: add_student(),width=40,background = '#4E8975', foreground ="white",font=("Arial",11))
        b1.grid(row=21 , column=1, columnspan=2)    
   
    def update() :
        
        heading1.grid(row=8 , column=3,columnspan=2)
        
        label_roll.grid(row=9 , column=3)
        label_a1.grid(row=10 , column=3)
        label_b1.grid(row=11 , column=3)
        label_c1.grid(row=12 , column=3)
        label_d1.grid(row=13 , column=3)
        label_e1.grid(row=14 , column=3)
        label_f1.grid(row=15 , column=3)
        label_i1.grid(row=18 , column=3)
        label_j1.grid(row=19 , column=3)
##########################################################
        roll_roll1.grid(row=9 , column=4)
        aa1.grid(row=10 , column=4)   
        bb1.grid(row=11 , column=4)
        cc1.grid(row=12 , column=4)
        dd1.grid(row=13 , column=4)
        ee1.grid(row=14 , column=4)
        ff1.grid(row=15 , column=4)
        ii1.grid(row=18 , column=4)
        jj1.grid(row=19 , column=4)

        b2=Button(root,text="UPDATE",command=lambda: update_student(),width=40,background = '#4E8975', foreground ="white",font=("Arial",11))
        b2.grid(row=21 , column=3, columnspan=2)
    # ----------------------
   

    def delete() :

        heading2.grid(row=8 , column=5,columnspan=1)
        label_delete.grid(row=14 , column=5 )
        entry_delete.grid(row=15 , column=5)

        b3=Button(root,text="DELETE",command=lambda: delete_student(),width=25,background = '#4E8975', foreground ="white",font=("Arial",11))
        b3.grid(row=21 , column=5, columnspan=1)
        
    # ----------------------

    dashboard=Label(root,text=" Dashboard ",font=("Arial",16),foreground="#ee9a4d")
    dashboard.grid(row=0,column=0)

    view=Button(root,text="VIEW ALL",background = '#4E8975', foreground ="white",command=lambda: view_student(),width=10,font=("Arial",11))
    view.grid(row=0,column=1)

    add=Button(root,text="NEW",command=addnew,width=10,background = '#4E8975', foreground ="white",font=("Arial",11))
    add.grid(row=0,column=2)

    update=Button(root,text="UPDATE",command=update,width=10,background = '#4E8975', foreground ="white",font=("Arial",11))
    update.grid(row=0,column=3)

    delete=Button(root,text="DELETE",command=delete,width=10,background = '#4E8975', foreground ="white",font=("Arial",11))
    delete.grid(row=0 , column=4)
    
    fetch_button = Button(root, text="Fetch Data", command=fetch_student_data, bg="#4caf50", fg="white")
    fetch_button.grid(row=9 , column=4, columnspan=2)

    txt = scrolledtext.ScrolledText(root,width=120,height=10,background = '#fff8dc', foreground ="#4E8975",font=("Arial",11))
    txt.grid(row=1,column=0,rowspan=5 , columnspan=7)



    combo_class = ttk.Combobox(root,width=15)    # Filter Searches
    combo_class['values']= ("CLASS",1, 2, 3)
    combo_class.current(0) #set the selected item
    combo_class.grid(row=0,column=5)
    
    combo_class_section = ttk.Combobox(root,width=15)    # Filter Searches
    combo_class_section['values']= ("CLASS","A","B","C")
    combo_class_section.current(0) #set the selected item
    combo_class_section.grid(row=0,column=6)

    combo_class_button=Button(root,text="SEARCH",command=classwise,width=10,background = '#4E8975', foreground ="white",font=("Arial",11))
    combo_class_button.grid(row=0,column=7)
    def open_new_window(root):
        # Create a new window
        new_window = Toplevel(root)
        new_window.title("SEARCH By ID")
        ws = new_window.winfo_screenwidth()
        hs = new_window.winfo_screenheight()
        w=600
        h=400
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        new_window.resizable(False, False)
        new_window.geometry(f'{w}x{h}+{int(x)}+{int(y)}')  
        label = Label(new_window, text="SEARCH By ID")
        label.grid(row=0,column=10)
        def fetch_student_datas():
            try:
                roll_no = roll_roll11.get()
                print("Roll number entered:", roll_no)
                student_data = student_list().get(roll_no)  # Assuming student_list() is a function returning a dict

                if student_data:
                    # Update the text in the StringVar objects
                    label_a11_var.set(student_data["session"])
                    label_b11_var.set(student_data["first_name"])
                    label_c11_var.set(student_data["last_name"])
                    label_d11_var.set(student_data["class"])
                    label_e11_var.set(student_data["section"])
                    label_f11_var.set(student_data["gender"])
                    label_i11_var.set(student_data["mobile"])
                    label_j11_var.set(student_data["address"])
                else:
                    messagebox.showwarning("Not Found", f"No data found for Roll Number {roll_no}.")
            except Exception as e:
                print("Error:", e)


        label_a1=Label(new_window,text="Session :",font=("Arial",10),width=10)
        label_b1=Label(new_window,text="First Name :",font=("Arial",10),width=10)
        label_c1=Label(new_window,text="Last Name :",font=("Arial",10),width=10)
        label_d1=Label(new_window,text="Class :",font=("Arial",10),width=10)
        label_e1=Label(new_window,text="Section :",font=("Arial",10),width=10)
        label_f1=Label(new_window,text="Gender :",font=("Arial",10),width=10)
        label_i1=Label(new_window,text="Mobile :",font=("Arial",10),width=10)
        label_j1=Label(new_window,text="Address :",font=("Arial",10),width=10)
        
        label_roll1=Label(new_window,font=("Arial",10),width=10)
        label_a11_var = StringVar()
        label_b11_var = StringVar()
        label_c11_var = StringVar()
        label_d11_var = StringVar()
        label_e11_var = StringVar()
        label_f11_var = StringVar()
        label_i11_var = StringVar()
        label_j11_var = StringVar()

        label_a11 = Label(new_window, font=("Arial", 10), width=10, textvariable=label_a11_var)
        label_b11 = Label(new_window, font=("Arial", 10), width=10, textvariable=label_b11_var)
        label_c11 = Label(new_window, font=("Arial", 10), width=10, textvariable=label_c11_var)
        label_d11 = Label(new_window, font=("Arial", 10), width=10, textvariable=label_d11_var)
        label_e11 = Label(new_window, font=("Arial", 10), width=10, textvariable=label_e11_var)
        label_f11 = Label(new_window, font=("Arial", 10), width=10, textvariable=label_f11_var)
        label_i11 = Label(new_window, font=("Arial", 10), width=20, textvariable=label_i11_var)
        label_j11 = Label(new_window, font=("Arial", 10), width=20, textvariable=label_j11_var)


        label_roll.grid(row=9 , column=3)
        label_a1.grid(row=10 , column=3)
        label_b1.grid(row=11 , column=3)
        label_c1.grid(row=12 , column=3)
        label_d1.grid(row=13 , column=3)
        label_e1.grid(row=14 , column=3)
        label_f1.grid(row=15 , column=3)
        label_i1.grid(row=18 , column=3)
        label_j1.grid(row=19 , column=3)
        label_roll1.grid(row=9 , column=5)
        label_a11.grid(row=10 , column=5)
        label_b11.grid(row=11 , column=5)
        label_c11.grid(row=12 , column=5)
        label_d11.grid(row=13 , column=5)
        label_e11.grid(row=14 , column=5)
        label_f11.grid(row=15 , column=5)
        label_i11.grid(row=18 , column=5)
        label_j11.grid(row=19 , column=5)
        roll_roll11=Entry(new_window,textvariable=roll1,width=20)
        roll_roll11.grid(row=2 , column=2)
        ID_class_button=Button(new_window,text="SEARCH",width=10,command=fetch_student_datas,background = '#4E8975', foreground ="white",font=("Arial",11))
        ID_class_button.grid(row=2,column=5)
    
    ##############################################
        
    combo_class_buttonn=Button(root,text="SEARCH By ID", command=lambda: open_new_window(root),width=14,background = '#4E8975', foreground ="white",font=("Arial",11))
    combo_class_buttonn.grid(row=23 , column=3, columnspan=2)
    

    
    root.mainloop()
    
