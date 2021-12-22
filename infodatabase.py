from tkinter import *
import sqlite3

root=Tk()
root.title("INFORMATION")
root.geometry("304x500")
root.configure(bg='#66d9ff')

con=sqlite3.connect('Infodata.db')
c=con.cursor()

"""
c.execute('''CREATE TABLE details(
    first_name text,
    last_name text,
    age integer,
    gender text,
    address text,
    city text,
    state text,
    zipcode integer
)
''')
"""

def submit():
    con=sqlite3.connect('Infodata.db')
    c=con.cursor()

    c.execute('INSERT INTO details VALUES(:first_name,:last_name,:age,:gender,:address,:city,:state,:zipcode)',
    {
        'first_name':firstname_box.get(),
        'last_name':lastname_box.get(),
        'age':age_box.get(),
        'gender':gender_box.get(),
        'address':address_box.get(),
        'city':city_box.get(),
        'state':state_box.get(),
        'zipcode':zipcode_box.get()
    })

    firstname_box.delete(0,END)
    lastname_box.delete(0,END)
    age_box.delete(0,END)
    gender_box.delete(0,END)
    address_box.delete(0,END)
    city_box.delete(0,END)
    state_box.delete(0,END)
    zipcode_box.delete(0,END)

    con.commit()
    con.close()

def show():
    con=sqlite3.connect('Infodata.db')
    c=con.cursor()

    c.execute('SELECT *,oid FROM details')
    record=c.fetchall()
    
    printrec=""
    for r in record:
        printrec+=str(r[8])+"   "+str(r[0])+" "+str(r[1])+"\n"
        details=Label(root,text=printrec)
        details.grid(row=14,column=0,columnspan=2)
        


    con.commit()
    con.close()

def save():
    con=sqlite3.connect('Infodata.db')
    c=con.cursor()

    c.execute('''UPDATE details SET
        first_name= :first_name,
        last_name=:last_name,
        age=:age,
        gender=:gender,
        address=:address,
        city=:city,
        state=:state,
        zipcode=:zipcode
        WHERE oid=:oid
         ''',
        {
        'first_name':firstnameedit_box.get(),
        'last_name':lastnameedit_box.get(),
        'age':ageedit_box.get(),
        'gender':genderedit_box.get(),
        'address':addressedit_box.get(),
        'city':cityedit_box.get(),
        'state':stateedit_box.get(),
        'zipcode':zipcodeedit_box.get(),
        'oid':selectid_box.get()
        }
    
    )
    

    con.commit()
    con.close()
    editor.destroy()

def edit():
    global editor
    editor=Tk()
    editor.title("Edit Details")
    editor.geometry("250x250")
    editor.configure(bg='#ffa366')

    con=sqlite3.connect('Infodata.db')
    c=con.cursor()

    firstnameedit=Label(editor,text="First Name")
    firstnameedit.grid(row=0,column=0,padx=8,pady=(5,0))
    lastnameedit=Label(editor,text="Last Name")
    lastnameedit.grid(row=1,column=0)
    ageedit=Label(editor,text="Age")
    ageedit.grid(row=2,column=0)
    genderedit=Label(editor,text="Gender")
    genderedit.grid(row=3,column=0)
    addressedit=Label(editor,text="Address")
    addressedit.grid(row=4,column=0)
    cityedit=Label(editor,text="City")
    cityedit.grid(row=5,column=0)
    stateedit=Label(editor,text="State")
    stateedit.grid(row=6,column=0)
    zipcodeedit=Label(editor,text="Zipcode")
    zipcodeedit.grid(row=7,column=0)

    global firstnameedit_box
    global lastnameedit_box
    global ageedit_box
    global genderedit_box
    global addressedit_box
    global cityedit_box
    global stateedit_box
    global zipcodeedit_box

    firstnameedit_box=Entry(editor,width=25,borderwidth=2)
    firstnameedit_box.grid(row=0,column=1,pady=(5,0))
    lastnameedit_box=Entry(editor,width=25,borderwidth=2)
    lastnameedit_box.grid(row=1,column=1)
    ageedit_box=Entry(editor,width=25,borderwidth=2)
    ageedit_box.grid(row=2,column=1)
    genderedit_box=Entry(editor,width=25,borderwidth=2)
    genderedit_box.grid(row=3,column=1)
    addressedit_box=Entry(editor,width=25,borderwidth=2)
    addressedit_box.grid(row=4,column=1)
    cityedit_box=Entry(editor,width=25,borderwidth=2)
    cityedit_box.grid(row=5,column=1)
    stateedit_box=Entry(editor,width=25,borderwidth=2)
    stateedit_box.grid(row=6,column=1)
    zipcodeedit_box=Entry(editor,width=25,borderwidth=2)
    zipcodeedit_box.grid(row=7,column=1)

    savebtn=Button(editor,text="Save Record",command=save)
    savebtn.grid(row=8,column=0,columnspan=2,padx=10,pady=5,ipadx=50)

    c.execute('SELECT * FROM details WHERE oid='+selectid_box.get())
    saverec=c.fetchall()

    for s in saverec:
        firstnameedit_box.insert(0,s[0])
        lastnameedit_box.insert(0,s[1])
        ageedit_box.insert(0,s[2])
        genderedit_box.insert(0,s[3])
        addressedit_box.insert(0,s[4])
        cityedit_box.insert(0,s[5])
        stateedit_box.insert(0,s[6])
        zipcodeedit_box.insert(0,s[7])


    con.commit()
    con.close()

    editor.mainloop()

def delete():
    con=sqlite3.connect('Infodata.db')
    c=con.cursor()

    c.execute('DELETE from details WHERE oid='+selectid_box.get())

    con.commit()
    con.close()

firstname=Label(root,text="First Name")
firstname.grid(row=0,column=0,padx=8,pady=(5,0))
lastname=Label(root,text="Last Name")
lastname.grid(row=1,column=0)
age=Label(root,text="Age")
age.grid(row=2,column=0)
gender=Label(root,text="Gender")
gender.grid(row=3,column=0)
address=Label(root,text="Address")
address.grid(row=4,column=0)
city=Label(root,text="City")
city.grid(row=5,column=0)
state=Label(root,text="State")
state.grid(row=6,column=0)
zipcode=Label(root,text="Zipcode")
zipcode.grid(row=7,column=0)

firstname_box=Entry(root,width=35,borderwidth=2)
firstname_box.grid(row=0,column=1,pady=(5,0))
lastname_box=Entry(root,width=35,borderwidth=2)
lastname_box.grid(row=1,column=1)
age_box=Entry(root,width=35,borderwidth=2)
age_box.grid(row=2,column=1)
gender_box=Entry(root,width=35,borderwidth=2)
gender_box.grid(row=3,column=1)
address_box=Entry(root,width=35,borderwidth=2)
address_box.grid(row=4,column=1)
city_box=Entry(root,width=35,borderwidth=2)
city_box.grid(row=5,column=1)
state_box=Entry(root,width=35,borderwidth=2)
state_box.grid(row=6,column=1)
zipcode_box=Entry(root,width=35,borderwidth=2)
zipcode_box.grid(row=7,column=1)

submitbtn=Button(root,text="Add Record",command=submit)
submitbtn.grid(row=8,column=0,columnspan=2,padx=10,pady=5,ipadx=50)

showbtn=Button(root,text="Show Records",command=show)
showbtn.grid(row=9,column=0,columnspan=2,padx=10,pady=5,ipadx=44)

selectid=Label(root,text="Select ID")
selectid.grid(row=11,column=0)

selectid_box=Entry(root,width=35,borderwidth=2)
selectid_box.grid(row=11,column=1)

editbtn=Button(root,text="Edit Record",command=edit)
editbtn.grid(row=12,column=0,columnspan=2,pady=5,padx=10,ipadx=50)

deletebtn=Button(root,text="Delete Record",command=delete)
deletebtn.grid(row=13,column=0,columnspan=2,pady=5,padx=10,ipadx=44)

con.commit()
con.close()

root.mainloop()