""" This an EVM mini project """

from tkinter import *
from tkinter import messagebox
import time
import sqlite3
from winsound import *
from PIL import ImageTk



root=Tk()
root.geometry('900x700')
root.resizable()
root.title('EVM PROJECT')
bg1=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\election-2009-3h.jpg")
bg2=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\img1.png")
bg3=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\voterloginimg.jpg")
bg4=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\devcontact.jpg")
bg5=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\finalresimg.jpg")
devbg=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\m_teamlogo1-removebg-preview (1).png")
response=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\thankyou2.jpg")
bg6=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\m_lock2.jpg")
bg7=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\m_wp2691496-cyber-security-wallpapers.jpg")
bg8=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\m_s1.jpg")
bg9=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\build.jpg")
bg10=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\m_pexels-pixabay-459301.jpg")
bg11=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\tedy.jpg")
bg12=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\m_pexels-johannes-plenio-1102909.jpg")
bg13=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\m_graph.jpg")
bg14=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\m_pexels-pixabay-326055.jpg")
bg15=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\m_pexels-simon-berger-1266810.jpg")
bg16=ImageTk.PhotoImage(file="C:\\Users\\EC1051AX\\PycharmProjects\\Evmpackage\\m_error.jpg")

x=StringVar() #These are all variables holdes entries in Entry field
y=StringVar()
a=IntVar()
b=StringVar()
c=StringVar()
d=StringVar()
e=IntVar()
f=StringVar()
g=StringVar()
h=StringVar()
i=StringVar()
k=StringVar()
l=StringVar()
m=IntVar()
n=StringVar()
o=StringVar()
p=StringVar()
t=StringVar()




def home():

    """
        This is the home page of our machine
        """
    
    x.set("")
    y.set("")
     
    f1=Frame()
    f1.place(x=0,y=0,width=900,height=700)
    f1.configure(background="#E0B0FF")

    bg_image=Label(f1,image=bg1).place(x=0,y=0,relwidth=1,relheight=1)

    #l1=Label(text='HOME PAGE',font=("Algerian",35),fg='#800000')
    #l1.place(x=300,y=30)

    b1=Button(f1,image=bg2,text='Authority Login',cursor="hand2",font=('Rockwell Extra Bold',16),bg="black",fg='white',activebackground="purple",activeforeground="red",command=authologin)
    b1.place(x=50,y=50,height=150,width=250)

    b1=Button(f1,image=bg3,text='Voters Login',cursor="hand2",font=('Rockwell Extra Bold',16),bg="black",fg='white',activebackground="purple",activeforeground="red",command=voterlogin)
    b1.place(x=50,y=200,height=150,width=250)

    b1=Button(f1,image=bg4,text='Devlopers Contact',cursor="hand2",font=('Rockwell Extra Bold',16),bg="black",activebackground="black",activeforeground="red",fg='white',command=devcontact)
    b1.place(x=50,y=500,height=150,width=250)

    b1=Button(f1,image=bg5,text='Final Results',cursor="hand2",font=('Rockwell Extra Bold',16),bg="black",fg='white',activebackground="purple",activeforeground="red",command=authologinresult)
    b1.place(x=50,y=350,height=150,width=250)

   
def authologin():
    '''
        Authority Login Page '''
    

    #bg_img=Label(f3,image=bg6).place(x=0,y=0,relwidth=1,relheight=1)
    
    f2=Frame()
    bg_img=Label(f2,image=bg6).place(x=0,y=0,relwidth=1,relheight=1)
    f2.place(x=0,y=0,width=900,height=700)
    f3=Frame(f2)
    f3.place(x=480,y=150,width=400,height=400)
    f2.configure(background="#E0B0FF")

    
   
    #authoaudio()

    l1=Label(f3,text='Authority Login',font=("Copperplate Gothic Bold",20,'bold'),fg='#010413')
    l1.place(x=70,y=15)

    l2=Label(f3,text='Username',font=("Copperplate Gothic Bold",15,'bold'),fg='#010413')
    l2.place(x=20,y=100)

    e1=Entry(f3,font=("Copperplate Gothic Bold",14),textvariable=x)
    e1.place(x=180,y=100,width=180)

    l2=Label(f3,text='Password',font=("Copperplate Gothic Bold",15,'bold'),fg='#010413')
    l2.place(x=20,y=170)

    e2=Entry(f3,font=("Copperplate Gothic Bold",14,'bold'),show="*",textvariable=y)
    e2.place(x=180,y=170,width=180)
    
    
    b1=Button(f3,text='Login',font=('Eras Bold ITC',12),bg='#506876',fg='white',activebackground="purple",activeforeground="red",command=msgbox)
    b1.place(x=150,y=220,height=50,width=100)

    b1=Button(f3,text='<-HOME',font=('Eras Bold ITC',12),bg='#506876',fg='white',activebackground="purple",activeforeground="red",command=home)
    b1.place(x=20,y=300,height=50,width=100)
  #done

def authologinresult():
    f2=Frame()
    bg_img=Label(f2,image=bg7).place(x=0,y=0,relwidth=1,relheight=1)
    f2.place(x=0,y=0,width=900,height=700)
    f3=Frame(f2)
    f3.place(x=100,y=150,height=400,width=400)
    f2.configure(background="#E0B0FF")

    l1=Label(f3,text='Authority Login For Result',font=("Copperplate Gothic Bold",14,'bold'),fg='#0C090A')
    l1.place(x=30,y=15)
    #l1=Label(f2,text='***AUTHORTY LOGIN FOR RESULT***',font=("Algerian",30),bg="#E0B0FF",fg='#800000')
    #l1.place(x=150,y=35)

    l1=Label(f3,text='Username',font=("Copperplate Gothic Bold",15,'bold'),fg='#0C090A')
    l1.place(x=20,y=100)

    e1=Entry(f3,font=("Copperplate Gothic Bold",14),textvariable=x)
    e1.place(x=180,y=100,width=180)

    
    l2=Label(f3,text='Password',font=("Copperplate Gothic Bold",15,'bold'),fg='#0C090A')
    l2.place(x=20,y=170)

    e2=Entry(f3,font=("Copperplate Gothic Bold",14,'bold'),show="*",textvariable=y)
    e2.place(x=180,y=170,width=180)

    b1=Button(f3,text='Login',font=('Eras Bold ITC',12),bg='#04303c',fg='white',activebackground="purple",activeforeground="red",command=msgbox1)
    b1.place(x=150,y=220,height=50,width=100)

    b1=Button(f3,text='<-HOME',font=('Eras Bold ITC',12),bg='#0b3d56',fg='white',activebackground="purple",activeforeground="red",command=home)
    b1.place(x=20,y=300,height=50,width=100)


    


def voterlogin():
    f2=Frame()
    bg_img=Label(f2,image=bg8).place(x=0,y=0,relwidth=1,relheight=1)
    f2.place(x=0,y=0,width=900,height=700)
    f3=Frame(f2)
    f3.place(x=50,y=150,height=400,width=400)
    #f3.configure(background="#E0B0FF")

    l1=Label(f3,text='Voter Login',font=("Copperplate Gothic Bold",20,'bold'),fg='#010413')
    l1.place(x=70,y=15)

    l1=Label(f3,text='Username',font=("Copperplate Gothic Bold",15,'bold'),fg='#0C090A')
    l1.place(x=20,y=100)

    e1=Entry(f3,font=("Copperplate Gothic Bold",14),textvariable=h)
    e1.place(x=180,y=100,width=180)

    l2=Label(f3,text='Password',font=("Copperplate Gothic Bold",15,'bold'),fg='#0C090A')
    l2.place(x=20,y=170)

    e2=Entry(f3,font=("Copperplate Gothic Bold",14,'bold'),show="*",textvariable=i)
    e2.place(x=180,y=170,width=180)
    
    b3=Button(f3,text='Login',font=('Eras Bold ITC',12),bg='#072758',fg='white',activebackground="purple",activeforeground="red",command=voterlogincheck)
    b3.place(x=150,y=220,height=50,width=100)

    b4=Button(f3,text='<-HOME',font=('Eras Bold ITC',12),bg='#072758',fg='white',activebackground="purple",activeforeground="red",command=home)
    b4.place(x=20,y=300,height=50,width=100)

    b5=Button(f3,text='Register',font=('Eras Bold ITC',12),bg='#072758',fg='white',activebackground="purple",activeforeground="red",command=register)
    b5.place(x=280,y=300,height=50,width=100)


def register():
    f4=Frame()
    bg_image=Label(f4,image=bg9).place(x=0,y=0,relwidth=1,relheight=1)
    f4.place(x=0,y=0,width=900,height=700)
    f5=Frame(f4)
    f5.place(x=200,y=150,width=500,height=400)
    f4.configure(background="#E0B0FF")

    l2=Label(f5,text='NEW VOTER REGISTRATION',font=("Impact",18),fg='#800000')
    l2.place(x=110,y=15)


    l3=Label(f5,text='Enter Name',font=("Eras Bold ITC",16))
    l3.place(x=50,y=70)

    e3=Entry(f5,font=("Eras Bold ITC",14),textvariable=n)
    e3.place(x=200,y=70,width=200)

    l4=Label(f5,text='Enter Username',font=("Eras Bold ITC",12,'bold'))
    l4.place(x=50,y=130)

    e4=Entry(f5,font=("Eras Bold ITC",14),textvariable=k)
    e4.place(x=200,y=130,width=200)

    l5=Label(f5,text='Enter Password',font=("Eras Bold ITC",12,'bold'))
    l5.place(x=50,y=200)

    e5=Entry(f5,font=("Eras Bold ITC",14),textvariable=l)
    e5.place(x=200,y=200,width=200)

    l6=Label(f5,text='Enter Date \nOf Birth',font=("Eras Bold ITC",12,'bold'))
    l6.place(x=80,y=240)

    l7=Label(f5,text='DD',font=("Eras Bold ITC",13,'bold'),fg='#3e3673')
    l7.place(x=200,y=240)

    l8=Label(f5,text='MM',font=("Eras Bold ITC",13,'bold'),fg='#3e3673')
    l8.place(x=280,y=240)

    l9=Label(f5,text='YYYY',font=("Eras Bold ITC",13,'bold'),fg='#3e3673')
    l9.place(x=360,y=240)

    e6=Entry(f5,font=("Eras Bold ITC",14),textvariable=o)
    e6.place(x=190,y=290,width=100)

    e7=Entry(f5,font=("Eras Bold ITC",14),textvariable=p)
    e7.place(x=270,y=290,width=100)

    e8=Entry(f5,font=("Eras Bold ITC",14),textvariable=m)#remember
    e8.place(x=350,y=290,width=100)

    b1=Button(f5,text='<-HOME',font=('Eras Bold ITC',12),bg='#f18a0c',fg='white',activebackground="purple",activeforeground="red",command=home)
    b1.place(x=20,y=340,height=50,width=100)

    b2=Button(f5,text='SUBMIT',font=('Eras Bold ITC',12),bg='#f18a0c',fg='white',activebackground="purple",activeforeground="red",command=checkage)
    b2.place(x=210,y=340,height=50,width=100)

    b3=Button(f5,text='BACK',font=('Eras Bold ITC',12),bg='#f18a0c',fg='white',activebackground="purple",activeforeground="red",command=voterlogin)
    b3.place(x=380,y=340,height=50,width=100)

def checkage():
    cyear=time.strftime("%Y")
    votyear=m.get()
    cyear=int(cyear)

    calyear=cyear-votyear

    if calyear>=18 and votyear!=0 :
        messagebox.showinfo("message","YOU ARE ELIGIBLE FOR VOTEING")
        dbregis()

        

    else:
        messagebox.showwarning("Warning","YOU ARE NOT ELIGIBLE FOR VOTEING")
        


    k.set("")
    l.set("")
    m.set("")
    n.set("")
    o.set("")
    p.set("")

def dbregis():

    #ADDING ENTRIES IN DATABASE
    if k.get()=="" and l.get()=="" and m.get()=="" and n.get()=="" and o.get()=="" and p.get=="":
        messagebox.showerror("Error","Data Should Not Empty")
    elif k.get()=="" or l.get()=="" or m.get()=="" or n.get()=="" or o.get()=="" or p.get=="":
        messagebox.showerror("Error","Some Field is Empty")
    else:
        
        f14=Frame()
        f14.place(x=0,y=0,width=900,height=700)
        f14.configure(background="#E0B0FF")
        bg_image=Label(f14,image=bg15).place(x=0,y=0,relwidth=1,relheight=1)

        f15=Frame(f14,bg='#697fa1')
        f15.place(x=200,y=300,width=500,height=300)

        db=sqlite3.connect('voterlogin.db')
        cr=db.cursor()

        user=cr.execute("select name from voterinfo where name='"+k.get()+"'")
        for i in user:
            messagebox.showwarning("Warning","Username Already Exists..\nChoose Another Username")
            register()
            break
        else:     
            cr.execute("insert into voterinfo(name,password,status) values('"+k.get()+"','"+l.get()+"','NV')")

            db.commit()
            db.close()

            l1=Label(f15,text="Your Registration Is Successful!!!\n Thank You..!!",font=("Copperplate Gothic Bold",16,'bold'),bg='#697fa1')
            l1.place(x=25,y=70)

            b3=Button(f15,text='Login',font=('Copperplate Gothic Bold',15),bg='#404b29',fg='white',activebackground="purple",activeforeground="red",command=voterlogin)
            b3.place(x=180,y=170,height=70,width=120)
    

                          
def msgbox():

    #CHECK WEATHER THE PASSWORD OF AUTORITY IS CORRECT OR NOT.
    
    if("123"==x.get() and "123"==y.get()):
        messagebox.showinfo("message","LOGIN SUCESSFUL")
        datetimeinfo()
    else:
        messagebox.showerror("error","INVALID PASSWORD")
        print(x.get)
    x.set("")
    y.set("")
  #done

def msgbox1():
     #CHECK WEATHER THE PASSWORD OF AUTORITY IS CORRECT OR NOT IN RESULT SECTION.
    
    if("123"==x.get() and "123"==y.get()):
        messagebox.showinfo("message","LOGIN SUCESSFUL")
        result()
    else:
        messagebox.showerror("error","INVALID PASSWORD")
        #print(x.get())
    x.set("")
    y.set("")
    
        
        
def datetimeinfo():

    #GETTING EXACT DATE AND INFO FROM AUTHORITY

    f4=Frame()
    f4.place(x=0,y=0,height=700,width=900)
    f4.configure(background="#E0B0FF")

    #bg_image=Label(f4,image=bg14).place(x=0,y=0,relwidth=1,relheight=1)

    l1=Label(f4,text="Enter Start Time Of Election In (H)",font=("Franklin Gothic Heavy",16),bg='#E0B0FF')
    l1.place(x=50,y=100)

    e1=Entry(f4,font=('Eras Bold ITC',16),textvariable=a)
    e1.place(x=70,y=150)

    
    l7=Label(f4,text="Time Is In AM OR PM",font=("Franklin Gothic Heavy",16),bg='#E0B0FF')
    l7.place(x=500,y=100)

    e6=Entry(f4,font=('Eras Bold ITC',16),textvariable=t)
    e6.place(x=520,y=150)


    l2=Label(f4,text="Enter Day OF Election In (DD)",font=("Franklin Gothic Heavy",16),bg='#E0B0FF')
    l2.place(x=50,y=200)

    e2=Entry(f4,font=("Franklin Gothic Heavy",16),textvariable=b)
    e2.place(x=70,y=250)

    l3=Label(f4,text="Enter Month In Which Elections will Conduct (MM)",font=("Franklin Gothic Heavy",16),bg='#E0B0FF')
    l3.place(x=50,y=320)

    e3=Entry(f4,font=("Franklin Gothic Heavy",16),textvariable=c)
    e3.place(x=70,y=370)

    l4=Label(f4,text="Enter Year In Which Elections will Conduct (YYYY)",font=("Franklin Gothic Heavy",16),bg='#E0B0FF')
    l4.place(x=50,y=450)

    e4=Entry(f4,font=("Franklin Gothic Heavy",16),textvariable=d)
    e4.place(x=70,y=500)

    l5=Label(f4,text="How Many Hours Required For Election Process",font=("Franklin Gothic Heavy",16),bg='#E0B0FF')
    l5.place(x=50,y=580)

    l6=Label(f4,text="NOTE: All Entries Must Be Decimal Numbers Only!!!",font=("Stencil",16),fg='#DC143C',bg='#E0B0FF')
    l6.place(x=100,y=20)

    e5=Entry(f4,font=("Franklin Gothic Heavy",16),textvariable=e)
    e5.place(x=70,y=630)

    c1=Checkbutton(text="I agree All the \nterms and condisions",font=("Franklin Gothic Heavy",16),bg='#E0B0FF')
    c1.place(x=600,y=400)

    b1=Button(f4,text="SUBMIT",font=("Franklin Gothic Heavy",16),bg='#C71585',fg='white',activebackground="purple",activeforeground="red",command=addnominees)
    b1.place(x=650,y=500)

    b4=Button(f4,text='<-HOME',font=('Franklin Gothic Heavy',16),bg='#C71585',fg='white',activebackground="purple",activeforeground="red",command=home)
    b4.place(x=650,y=550)
  #done


def checktime():

    #CHECK WEATHER THE TIME OF ELECTION IS OVER OR NOT

    dt=time.strftime("%d")
    m=time.strftime("%m")
    y=time.strftime("%Y")
    d1=b.get()
    m1=c.get()
    y1=d.get()
    

    if dt+"/"+m+"/"+y==d1+"/"+m1+"/"+y1:
        l1=[]
        l2=[]
        x=a.get() #starting hrs
        y=e.get() #how many hrs
        tunit=t.get() #AM/PM

        if tunit=='PM' or tunit=='pm' or tunit=='Pm':
            if x==12:
                x=12
                total=x+y+1
            else:
                x=x+12
                total=x+y+1
        elif tunit=='AM' or tunit=='am':
            if x==12:
                x=0
                total=x+y+1
            else:    
                total=x+y+1
        else:
            messagebox.showwarning("Warning","Wrong Input AM OR PM ONLY")
            
            
        while(x!=total):
            if(x>=12):
                l2.append(str(x)+'PM')
            else:
                if(str(x)=='0'or str(x)=='1'or str(x)=='2' or str(x)=='3'or str(x)=='4'or str(x)=='5'or str(x)=='6'or str(x)=='7'or str(x)=='8'or str(x)=='9'):
                    l1.append('0'+str(x)+'AM')
                else:
                    
                    l1.append(str(x)+'AM')

            x=x+1

        l3=l1+l2
        print(l3,"currenttime", time.strftime("%H%p"))

        if (time.strftime("%H%p")) in l3:
             evm()
        else:
            messagebox.showerror("ERROR","SORRY VOTEING TIME IS OVER")
            h.set("")
            i.set("")
            

    else:
        messagebox.showinfo("Message","Voteing Is Not Started Yet..!!")
        h.set("")
        i.set("")
        
    
def addnominees():

    #ADD NOMINIEES WHICH ARE TAKING PART IN ELECTION 
    
    global f5
    if  b.get()=="" and c.get()=="" and d.get()=="" and e.get()=="" and t.get=="":
        messagebox.showerror("Error","Data Should Not Empty")
    elif b.get()=="" or c.get()=="" or d.get()=="" or e.get()=="" or t.get=="":
        messagebox.showerror("Error","Some Field is Empty")
    else:
        
        f6=Frame()
        f6.place(x=0,y=0,height=700,width=900)
        f6.configure(background="#E0B0FF")

        bg_image=Label(f6,image=bg10).place(x=0,y=0,relwidth=1,relheight=1)

        f5=Frame(f6)
        f5.place(x=200,y=120,height=550,width=550)

        l0=Label(f5,text="CANDIDATES INFORMATION",font=("Copperplate Gothic Bold",20,'bold'),fg="#800000")
        l0.place(x=40,y=25)

        l1=Label(f5,text="Enter Full Name Of Nominee",font=("Franklin Gothic Heavy",18,'bold'),fg='#551434')
        l1.place(x=90,y=100)

        e1=Entry(f5,font=("Franklin Gothic Heavy",18),textvariable=f)
        e1.place(x=110,y=160)

    
        l3=Label(f5,text="Enter Voting Symbol For Above Nominee",font=("Franklin Gothic Heavy",18,'bold'),fg='#551434')
        l3.place(x=30,y=220)

        e3=Entry(f5,font=("Franklin Gothic Heavy",18),textvariable=g)
        e3.place(x=110,y=280)

        l4=Label(f5,text="If U Want To Add More Candidates Just Press Submit.\n After Adding All The candidates Just Press Done.\n Thank U.",font=("Franklin Gothic Heavy",12,'bold'))
        l4.place(x=50,y=370)

        b1=Button(f5,text="SUBMIT",font=("Franklin Gothic Heavy",12),bg='#594c6d',fg='white',activebackground="purple",activeforeground="red",command=candiddb)
        b1.place(x=200,y=480,width=100,height=50)

        b2=Button(f5,text="DONE",font=("Franklin Gothic Heavy",12),bg='#683d69',fg='white',activebackground="purple",activeforeground="red",command=authodone)
        b2.place(x=350,y=480,width=100,height=50)

        b4=Button(f5,text='<-HOME',font=('Franklin Gothic Heavy',12),bg='#C71585',fg='white',activebackground="purple",activeforeground="red",command=home)
        b4.place(x=50,y=480,width=100,height=50)
  #done

def authodone():
    f9=Frame()
    f9.place(x=0,y=0,height=700,width=900)
    f9.configure(background="#111406")

    bg_image=Label(f9,image=bg11).place(x=0,y=0,relwidth=1,relheight=1)

    f8=Frame(f9)
    f8.place(x=30,y=270,width=380,height=300)
    f8.configure(background="#111406")


    l1=Label(f8,text="**ALL ARE SET FOR VOTING**\n\n Thank You...!!!",font=('Franklin Gothic Heavy',14),bg="#111406",fg="#c74a11")
    l1.place(x=40,y=80)

    b4=Button(f8,text='HOME',font=('Rockwell Extra Bold',12),bg='#768e10',fg='white',activebackground="purple",activeforeground="red",command=home)
    b4.place(x=120,y=200,height=50,width=100)
  #done

def candiddb():

    #ADD ALL INFORMATION OF NOMITNIEES INTO OUR DATABASE
    if f.get()=="" and g.get()=="":
        messagebox.showerror("Error","Data Should Not Empty")
    elif f.get()=="" or g.get()=="":
        messagebox.showerror("Error","Some Field is Empty")
    else:
        
        db=sqlite3.connect('candidatedb.db')

        cr=db.cursor()

        cr.execute("insert into candidinfo(name,symbol,votecnt) values('"+f.get()+"','"+g.get()+"',0)")

        db.commit()
        db.close()

        f.set("")
        g.set("")

        messagebox.showinfo("Message","Candiadte Added \nSuccessfully...")
        #l3=Label(f5,text="Data Recieved Successfully",font=("Rockwell Extra Bold",16),bg='#E0B0FF')
        #l3.place(x=270,y=650)
        #l3['text']=""
  #done

    
def voterlogincheck():
    #CHECK WEATHER THE PASSWORD OR USERNAME ENTERED BY USER IS CORRECT OR NOT.
  
    
    db=sqlite3.connect('voterlogin.db')
    cr=db.cursor()

    x=cr.execute("select name,password from voterinfo where name='"+h.get()+"' and password='"+i.get()+"'")

    for x1 in x:
         messagebox.showinfo("message","LOGIN SUCCESSFUL")
         checktime()
         break
    else:
        messagebox.showerror("Error","INVALID USERNAME OR PASSWORD")
        
           
    db.commit()
    db.close()

    
def evm():
    #VIEW OF EVM MACHINE NAME AND VOTING SYMBOLS.
    #OUR VOTING MACHINE CAPACITY IS 10 NOMINEES AND RESPECTIVE 10 SYMBOLS.
    
    f6=Frame()
    f6.place(x=0,y=0,height=700,width=900)
    f6.configure(background="#E0B0FF")

    my_can=Canvas(f6,width=900,height=700,bg="#E0B0FF")
    my_can.place(x=0,y=0)

    my_can.create_line(430,80,430,670,width=4)
    my_can.create_line(50,160,850,160,width=2)
    my_can.create_line(50,80,850,80,width=2)
    #my_can.create_line(450,170,470,170,width=4,arrowshape=(440,180,24))
    
    db=sqlite3.connect('candidatedb.db')

    cr=db.cursor()


    l1=Label(f6,text="CANDIDATE NAME",font=('Jokerman',18),bg='#E0B0FF')
    l1.place(x=100,y=100)

    l2=Label(f6,text="CANDIDATE SYMBOL",font=('Jokerman',18),bg='#E0B0FF')
    l2.place(x=500,y=100)

    l3=Label(f6,text="Electronic Voting Machine(EVM)",font=('Algerian',22),fg="#800000",bg='#E0B0FF')
    l3.place(x=230,y=20)

    l4=Label(f6,text="WELCOME\n"+h.get(),font=("Franklin Gothic Heavy",12),bg='#E0B0FF',fg='purple')
    l4.place(x=780,y=20)
   
    s1=cr.execute("select name,symbol from candidinfo")

    x=150
    y=160
    a,b,c=50,220,850

    z=1
    t=[Button()]*10
    cnt=0
    

    for n in s1:
        Label(f6,text=n[0],fg='purple',font=("Franklin Gothic Heavy",17),bg='#E0B0FF'). place(x=x,y=y+10)
        x=x+380
        
        t[z]=Button(f6,text=n[1],font=('Rockwell Extra Bold',17),bg='#C71585',fg='white',activebackground="purple",activeforeground="red")
        t[z].place(x=x,y=y,width=120,height=60)
        z=z+1
        x=150
        
        y=y+60

        my_can.create_line(a,b,c,b,width=1)
        b=b+60
        cnt=cnt+1

    l5=Label(f6,text="No One Of The Above",fg='purple',font=("Franklin Gothic Heavy",17),bg='#E0B0FF')
    l5.place(x=150,y=y+10)

    b1=Button(f6,text="NOTA",font=('Rockwell Extra Bold',17),bg='#C71585',fg='white',activebackground="purple",activeforeground="red",command=NOTA)
    b1.place(x=530,y=y,width=120,height=60)

    my_can.create_line(a,b,c,b,width=1)
    db.commit()
    db.close()

    '''for i in range(1,cnt+1):
        t[i].configure(command=lambda: vote1(t[i]))'''
    
    if cnt==2:
        t[1].configure(command=lambda:vote1(t[1]))
        t[2].configure(command=lambda:vote1(t[2]))
    elif cnt==3:
         t[1].configure(command=lambda:vote1(t[1]))
         t[2].configure(command=lambda:vote1(t[2]))
         t[3].configure(command=lambda:vote1(t[3]))
    elif cnt==4:
         t[1].configure(command=lambda:vote1(t[1]))
         t[2].configure(command=lambda:vote1(t[2]))
         t[3].configure(command=lambda:vote1(t[3]))
         t[4].configure(command=lambda:vote1(t[4]))
    elif cnt==5:
         t[1].configure(command=lambda:vote1(t[1]))
         t[2].configure(command=lambda:vote1(t[2]))
         t[3].configure(command=lambda:vote1(t[3]))
         t[4].configure(command=lambda:vote1(t[4]))
         t[5].configure(command=lambda:vote1(t[5]))
    elif cnt==6:
         t[1].configure(command=lambda:vote1(t[1]))
         t[2].configure(command=lambda:vote1(t[2]))
         t[3].configure(command=lambda:vote1(t[3]))
         t[4].configure(command=lambda:vote1(t[4]))
         t[5].configure(command=lambda:vote1(t[5]))
         t[6].configure(command=lambda:vote1(t[6]))
              
    elif cnt==7:
         t[1].configure(command=lambda:vote1(t[1]))
         t[2].configure(command=lambda:vote1(t[2]))
         t[3].configure(command=lambda:vote1(t[3]))
         t[4].configure(command=lambda:vote1(t[4]))
         t[5].configure(command=lambda:vote1(t[5]))
         t[6].configure(command=lambda:vote1(t[6]))
         t[7].configure(command=lambda:vote1(t[7]))
    elif cnt==8:
         t[1].configure(command=lambda:vote1(t[1]))
         t[2].configure(command=lambda:vote1(t[2]))
         t[3].configure(command=lambda:vote1(t[3]))
         t[4].configure(command=lambda:vote1(t[4]))
         t[5].configure(command=lambda:vote1(t[5]))
         t[6].configure(command=lambda:vote1(t[6]))
         t[7].configure(command=lambda:vote1(t[7]))
         t[8].configure(command=lambda:vote1(t[8]))
    elif cnt==9:
         t[1].configure(command=lambda:vote1(t[1]))
         t[2].configure(command=lambda:vote1(t[2]))
         t[3].configure(command=lambda:vote1(t[3]))
         t[4].configure(command=lambda:vote1(t[4]))
         t[5].configure(command=lambda:vote1(t[5]))
         t[6].configure(command=lambda:vote1(t[6]))
         t[7].configure(command=lambda:vote1(t[7]))
         t[8].configure(command=lambda:vote1(t[8]))
         t[9].configure(command=lambda:vote1(t[9]))

    elif cnt==10:
         t[1].configure(command=lambda:vote1(t[1]))
         t[2].configure(command=lambda:vote1(t[2]))
         t[3].configure(command=lambda:vote1(t[3]))
         t[4].configure(command=lambda:vote1(t[4]))
         t[5].configure(command=lambda:vote1(t[5]))
         t[6].configure(command=lambda:vote1(t[6]))
         t[7].configure(command=lambda:vote1(t[7]))
         t[8].configure(command=lambda:vote1(t[8]))
         t[9].configure(command=lambda:vote1(t[9]))
         t[10].configure(command=lambda:vote1(t[10]))
    
              
def NOTA():
    #This Function Is For NOTA Button IN EVM
    
    f7=Frame()
    f7.place(x=0,y=0,height=700,width=900)

    global NOTAcnt
    NOTAcnt=0

    db1=sqlite3.connect('voterlogin.db')
    cr1=db1.cursor()

    xy=cr1.execute("select status from voterinfo where password='"+i.get()+"' ")

    for xyz in xy:
        xyz
    status=list(xyz)

    if status[0] == "NV":

        freq=10000
        tme=2500
        Beep(freq,tme)

        NOTAcnt=NOTAcnt+1

        #l1=Label(f7,text="YOUR VOTE IS SUBMITTED SUCCESSFULLY...!!!\n THANK YOU FOR YOUR VALUABLE RESPONCE",font=("Algerian",25),bg='#E0B0FF',fg='#800000')
        #l1.place(x=90,y=200)

        Label(f7,image=response).place(x=0,y=0,relwidth=1,relheight=1)

        b4=Button(f7,text='<-HOME',font=('Rockwell Extra Bold',20),bg='#535353',fg='white',activebackground="purple",activeforeground="red",command=home)
        b4.place(x=600,y=570,height=100,width=200)
        cr1.execute("update voterinfo set status='Voted' where password='"+i.get()+"' and name='"+h.get()+"' ")
        h.set("")
        i.set("")
    
    else:
        f1=Frame()
        f1.place(x=0,y=0,width=900,height=700)

        bg_image=Label(f1,image=bg16).place(x=0,y=0,relwidth=1,relheight=1)
        messagebox.showerror("WARNING","YOU VOTED ALREADY!!!")
        h.set("")
        i.set("")
        home()

    db1.commit()
    db1.close()                            
    
def vote1(w):

    #GIVING VOTE TO PERTICULAR NOMINEES 

    f7=Frame()
    f7.place(x=0,y=0,height=700,width=900)
    f7.configure(background="#E0B0FF")

    db1=sqlite3.connect('voterlogin.db')
    cr1=db1.cursor()

    xy=cr1.execute("select status from voterinfo where password='"+i.get()+"' ")

    for xyz in xy:
        xyz
    status=list(xyz)

    
    if status[0] == "NV":

        freq=10000
        tme=2500
        Beep(freq,tme)

        #l1=Label(f7,text="YOUR VOTE IS SUBMITTED SUCCESSFULLY...!!!\n THANK YOU FOR YOUR VALUABLE RESPONCE",font=("Algerian",25),bg='#E0B0FF',fg='#800000')
        #l1.place(x=90,y=200)

        Label(f7,image=response).place(x=0,y=0,relwidth=1,relheight=1)

        b4=Button(f7,text='<-HOME',font=('Rockwell Extra Bold',20),bg='#535353',fg='white',activebackground="purple",activeforeground="red",command=home)
        b4.place(x=600,y=570,height=100,width=200)
    
        cr1.execute("update voterinfo set status='Voted' where password='"+i.get()+"' and name='"+h.get()+"' ")
    

        dby=sqlite3.connect('candidatedb.db')

        cry=dby.cursor()
        text=w['text']

        x2=cry.execute("select votecnt from candidinfo where symbol='"+text+"' ")
        for j in x2:
            y2=j
        z2=list(y2)
        cnt=z2[0]
        vcnt=cnt+1
    

        cry.execute("update candidinfo set votecnt='"+str(vcnt)+"' where symbol='"+text+"' ")
    

        dby.commit()
        dby.close()
        h.set("")
        i.set("")
    else:
        f1=Frame()
        f1.place(x=0,y=0,width=900,height=700)

        bg_image=Label(f1,image=bg16).place(x=0,y=0,relwidth=1,relheight=1)
        messagebox.showerror("WARNING","YOU VOTED ALREADY!!!")
        h.set("")
        i.set("")
        home()

    db1.commit()
    db1.close()
    
def result():
    #DISPLAYING RESULT OF ELECTION.
    #TOTAL VOTERS, VOTING PERCENTAGE ETC..
    
    f10=Frame()
    f10.place(x=0,y=0,height=700,width=900)
    f10.configure(background="#E0B0FF")
    bg_image=Label(f10,image=bg12).place(x=0,y=0,relwidth=1,relheight=1)

    f9=Frame(f10)
    f9.place(x=50,y=150,width=400,height=400)
    
    db=sqlite3.connect('voterlogin.db')
    cr=db.cursor()

    m=cr.execute("select status from voterinfo")

    total=0

    for m1 in m:
        total=total+1

    l0=Label(f9,text="FINAL VOTING ANALYSIS",font=("Times New Roman",18,'bold'),fg='#800000')
    l0.place(x=40,y=20)    

    l1=Label(f9,text="TOTAL VOTERS= "+str(total),font=("Copperplate Gothic Bold",13,'bold'))
    l1.place(x=90,y=80)

    mm=cr.execute("select status from voterinfo where status='NV'")

    notvoted=0


    for mm1 in m:
        notvoted=notvoted+1
        
    voted=total-notvoted

    percentage=(voted/total)*100

    l2=Label(f9,text="NUMBER OF VOTERS ARE\n PARTICIPATED IN ELECTION= "+str(voted),font=("Copperplate Gothic Bold",12,'bold'))
    l2.place(x=50,y=130)

    l3=Label(f9,text="NUMBER OF VOTERS ARE\n NOT PARTICIPATED IN ELECTION= "+str(notvoted),font=("Copperplate Gothic Bold",12,'bold'))
    l3.place(x=15,y=210)

    l4=Label(f9,text="VOTING PERCENTAGE\n= "+str(percentage)+"%",font=("Copperplate Gothic Bold",12,'bold'))
    l4.place(x=50,y=280)

    b1=Button(f9,text='FINAL RESULT',font=('Rockwell Extra Bold',16),bg='#254117',fg='white',activebackground="purple",activeforeground="red",command=finalres)
    b1.place(x=100,y=350)

def finalres():

    #DISPLAYING NOMINEES NAME, VOTE COUNTS AND WINNER NAME.
    
    f11=Frame()
    f11.place(x=0,y=0,height=700,width=900)
    f11.configure(background="#E0B0FF")
    bg_image=Label(f11,image=bg13).place(x=0,y=0,relwidth=1,relheight=1)

    
    f10=Frame(f11,bg='#331f4c')
    f10.place(x=160,y=150,width=550,height=500)

    l1=Label(f10,text='_._._._._RESULTS_._._._._',font=("Algerian",25),fg='#FDEEF4',bg='#331f4c')
    l1.place(x=80,y=10)


    db=sqlite3.connect('candidatedb.db')

    cr=db.cursor()

    z=cr.execute("select * from candidinfo")

    x=90
    y=70

    for n in z:
        Label(f10,text=n[0],fg='#C71585',font=("Franklin Gothic Heavy",15),bg='#331f4c'). place(x=x,y=y+10)
        x=x+200
        
        Label(f10,text=n[1],font=("Franklin Gothic Heavy",15),bg='#331f4c',fg='#FF2400').place(x=x,y=y+10)

        x=x+150
        Label(f10,text=n[2],font=("Franklin Gothic Heavy",15),bg='#331f4c').place(x=x,y=y+10)
        
        x=90
        
        y=y+60

    l1=Label(f10,text="No One Of The Above",fg='#C71585',font=("Franklin Gothic Heavy",14),bg='#331f4c')
    l1.place(x=90,y=y)

    l2=Label(f10,text="NOTA",font=("Franklin Gothic Heavy",15),bg='#331f4c',fg='#FF2400')
    l2.place(x=x+200,y=y)

    
    ym=cr.execute("select max(votecnt)  from candidinfo ")
    
    
    for sp in ym:
        sp
        
    m=list(sp)
    maxi=m[0]

    res=cr.execute(" select name from candidinfo where votecnt='"+str(maxi)+"' ")

    for fin in res:
        fin
    mn=list(fin)
    mnm=mn[0]

    mulwin=cr.execute("select votecnt  from candidinfo")
    counter=0

    for i in mulwin:
        temp=list(i)
        for j in temp:
            if j==maxi:
                counter=counter+1
                
    if counter==1:
        l0=Label(f10,text="The Winner Is=> "+str(mnm)+"\n Congratulations!!!",font=("Copperplate Gothic Bold",15),bg='#331f4c',fg='white')
        l0.place(x=150,y=420)
    elif counter>=2:
        l0=Label(f10,text="Voting Is Tied Between\n The Candidates..",font=("Copperplate Gothic Bold",15),bg='#331f4c',fg='white')
        l0.place(x=150,y=420)
    elif counter==0:
        l0=Label(f10,text="Sorry Election Is Not Started",font=("Copperplate Gothic Bold",15),bg='#331f4c',fg='white')
        l0.place(x=150,y=420)
        

    

    b1=Button(f10,text='<-Home',font=('Copperplate Gothic Bold',14),bg='#C71585',fg='white',activebackground="purple",activeforeground="red",command=home)
    b1.place(x=20,y=400,height=50,width=100)
       
    db.commit()
    db.close()
    
def devcontact():
    #DEVELOPERS INFORMATION FOR MAINTAINANCE.
    
    f11=Frame()
    f11.place(x=0,y=0,height=700,width=900)
    #f11.configure(bg='cyan')

    bg_image1=Label(f11,image=devbg).place(x=0,y=0,relwidth=1,relheight=1)
    f12=Frame(f11)
    f12.place(x=15,y=80,width=280,height=300)
    f12.configure(background="white")

    f13=Frame(f11)
    f13.place(x=590,y=130,width=300,height=200)
    f13.configure(background="white")
    
    l1=Label(f12,text="_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*",font=('Rockwell Extra Bold',13),fg="red",bg="white")
    l1.place(x=10,y=10)
    
    l1=Label(f12,text="MR. SIDDHESH \n DHAMALE",font=('Rockwell Extra Bold',16),fg="#f47120",bg="white")
    l1.place(x=70,y=40)

    l2=Label(f12,text="MS. GAYATRI\n GUNJAL",font=('Rockwell Extra Bold',16),fg="#721B65",bg="white")
    l2.place(x=70,y=120)

    l1=Label(f12,text="_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*",font=('Rockwell Extra Bold',13),fg="purple",bg="white")
    l1.place(x=10,y=250)

    l4=Label(f13,text=".....SPECIAL THANKS TO.....\n\n MS. REKHA MADAM",font=('Franklin Gothic Heavy',14),fg='#990012',bg="white")
    l4.place(x=30,y=60)

    l1=Label(f13,text="_._._._._._._._._._._._._._._._._._._",font=('Rockwell Extra Bold',16),fg="blue",bg="white")
    l1.place(x=0,y=10)

    l1=Label(f13,text="_._._._._._._._._._._._._._._._._._._",font=('Rockwell Extra Bold',16),fg="red",bg="white")
    l1.place(x=0,y=140)

    b1=Button(f11, text='<-HOME', font=('Eras Bold ITC', 12), bg='#506876', fg='white', activebackground="purple",activeforeground="red", command=home)
    b1.place(x=110,y=350,height=50,width=100)
    
home()

def setvcnt():

    #AFTER END OF PROGRAM SET ALL ENTRIES TO STANDERD FORMAT.
    #ACCORDING TO DEVELOPER.
    
    db=sqlite3.connect('candidatedb.db')

    cr=db.cursor()

    cr.execute("delete from candidinfo")
    db.commit()
    db.close()

    db1=sqlite3.connect('voterlogin.db')
    cr1=db1.cursor()

    cr1.execute("update voterinfo set status='NV' ")
    db1.commit()
    db1.close()


setvcnt()

root.mainloop()
