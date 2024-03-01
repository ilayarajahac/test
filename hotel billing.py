from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import random,os,tempfile,smtplib

if not os.path.exists('bills'):
    os.mkdir('bills')

#function part
def clear():
    paroota_entry.delete(0,END)
    chickenrice_entry.delete(0,END)
    Dosai_entry.delete(0,END)
    Idli_entry.delete(0,END)
    eggparoota_label_entry.delete(0,END)

    chicken65_entry.delete(0,END)
    muttonsukka_entry.delete(0,END)
    grillchicken_entry.delete(0,END)
    thanthoorichicken_entry.delete(0,END)
    chickencurry_entry.delete(0,END)

    vannila_entry.delete(0,END)
    straberry_entry.delete(0,END)
    choclate_entry.delete(0,END)
    butterscotch_entry.delete(0,END)
    badhampista_entry.delete(0,END)


    paroota_entry.insert(0,0)
    chickenrice_entry.insert(0,0)
    Dosai_entry.insert(0,0)
    Idli_entry.insert(0,0)
    eggparoota_label_entry.insert(0,0)

    chicken65_entry.insert(0,0)
    muttonsukka_entry.insert(0,0)
    grillchicken_entry.insert(0,0)
    thanthoorichicken_entry.insert(0,0)
    chickencurry_entry.insert(0,0)

    vannila_entry.insert(0,0)
    straberry_entry.insert(0,0)
    choclate_entry.insert(0,0)
    butterscotch_entry.insert(0,0)
    badhampista_entry.insert(0,0)

    foodprice_entry.delete(0,END)
    sidedish_entry.delete(0,END)
    icecreamprice_entry.delete(0,END)

    foodtax_entry.delete(0,END)
    sidedishtax_entry.delete(0,END)
    icecreamtax_entry.delete(0,END)

    name_entry.delete(0,END)
    phone_entry.delete(0,END)
    bill_entry.delete(0,END)

    txtarea.delete(1.0,END)

def sendmail():
    def sendgmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(sendermailidentry.get(),senderpasswordentry.get())
            message=txtare.get(1.0,END)
            receiver_address=receivermailidentry.get()
            ob.sendmail(sendermailidentry.get(),receivermailidentry.get(),message)
            ob.quit()
            messagebox.showinfo("success","Bill send successfully to mail",parent=window1)
            window1.destroy()
        except:
            messagebox.showerror("Error","something went wrong",parent=window1)

    if txtarea.get(1.0,END)=='\n':
        messagebox.showerror("Error","No bill available")
    else:

        window1=Toplevel()
        window1.grab_set()
        window1.resizable(0,0)
        window1.config(bg="grey20")

        sendermailinfoframe=LabelFrame(window1,text="sender mail info",font=("times",20,"bold"),bg="grey",fg="white")
        sendermailinfoframe.grid(row=0,column=0,padx=40,pady=20)

        sendermailidlabel=Label(sendermailinfoframe,text="Sender Email :",font=("times",20,"bold"),bg="grey",fg="white")
        sendermailidlabel.grid(row=0,column=0,padx=10,pady=8)

        sendermailidentry=Entry(sendermailinfoframe,font=("times",20,"bold"))
        sendermailidentry.grid(row=0,column=1,padx=10,pady=8)

        senderpasswordlabel = Label(sendermailinfoframe, text="Sender Email :", font=("times", 20, "bold"), bg="grey",
                                  fg="white")
        senderpasswordlabel.grid(row=1, column=0, padx=10, pady=8)

        senderpasswordentry = Entry(sendermailinfoframe, font=("times", 20, "bold"))
        senderpasswordentry.grid(row=1, column=1, padx=10, pady=8)

        receivermailinfoframe = LabelFrame(window1, text="receiver mail  info", font=("times", 20, "bold"), bg="grey",
                                         fg="white")
        receivermailinfoframe.grid(row=1, column=0, padx=40, pady=20)

        receivermailidlabel = Label(receivermailinfoframe, text="receiver Email :", font=("times", 20, "bold"), bg="grey",
                                  fg="white")
        receivermailidlabel.grid(row=0, column=0, padx=10, pady=8)

        receivermailidentry = Entry(receivermailinfoframe, font=("times", 20, "bold"))
        receivermailidentry.grid(row=0, column=1, padx=10, pady=8)

        messagelabel = Label(receivermailinfoframe, text="message", font=("times", 20, "bold"), bg="grey",
                                    fg="white")
        messagelabel.grid(row=1, column=0, padx=10, pady=8)

        txtare=Text(receivermailinfoframe,font=("times",12,"bold"),bd=2,height=11,width=42)
        txtare.grid(row=2,column=0,columnspan=2)
        txtare.delete(1.0,END)
        txtare.insert(END,txtarea.get(1.0,END).replace('=','').replace("\t\t","\t"))

        txtbutton=Button(window1,text="SEND",font=("times",12,"bold"),width=15)
        txtbutton.grid(row=2,column=0,pady=20)

        window1.mainloop()

def printbill():
    if txtarea.get(1.0,END)=='\n':
        messagebox.showerror("Error","No bill available")
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(txtarea.get(1.0,END))
        os.startfile(file,'print')
def searchbill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==bill_entry.get():
            f=open(f'bills/{i}','r')
            txtarea.delete(1.0,END)
            for data in f:
                txtarea.insert(END,data)
            f.close
            break
    else:
        messagebox.showerror("Error","invalid bill number")


def savebill():
    global billnumber
    result=messagebox.askyesno("confirm","do  you want to save?")
    if result:
        bill_content=txtarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo("Successs",f'{billnumber} is saved successfully')
        billnumber = random.randint(500, 1000)


billnumber=random.randint(500,1000)
def billarea():
    if name_entry.get() == "" or phone_entry.get() == "":
        messagebox.showerror("alert","customer name required")
    elif foodprice_entry.get() == "" or sidedish_entry.get() == "" or icecreamprice_entry.get() == "":
        messagebox.showerror("alert","no product purchased")
    elif foodprice_entry.get() == "0Rs" or sidedish_entry.get() == "0rs" or icecreamprice_entry.get() == "0rs":
        messagebox.showerror("alert","no product selected")
    else:
        txtarea.insert(END,"\t**Welcome customer**\n")
        txtarea.insert(END,f'\nbillnumber:{billnumber}\n')
        txtarea.insert(END, f'\ncustomername:{name_entry.get()}\n')
        txtarea.insert(END, f'\nmobilenumer:{phone_entry.get()}\n')
        txtarea.insert(END,f'========================================\n')
        txtarea.insert(END,f'products\t\tqty\t\tprice\n')
        txtarea.insert(END, f'========================================\n')
        if paroota_entry.get() !='0':
            txtarea.insert(END,f'Parootta\t\t{paroota_entry.get()}\t\t{parrotaprice}Rs\n')
        if chickenrice_entry.get() !='0':
            txtarea.insert(END,f'chickenrice\t\t{chickenrice_entry.get()}\t\t{chickenriceprice}Rs\n')
        if Dosai_entry.get() !='0':
            txtarea.insert(END,f'Dosai\t\t{Dosai_entry.get()}\t\t{dosaiprice}Rs\n')
        if Idli_entry.get() !='0':
            txtarea.insert(END,f'Idli\t\t{Idli_entry.get()}\t\t{idliprice}Rs\n')
        if eggparoota_label_entry.get() !='0':
            txtarea.insert(END,f'Eggparrootta\t\t{eggparoota_label_entry.get()}\t\t{eggparrootaprice}Rs\n')

        if chicken65_entry.get() !='0':
            txtarea.insert(END,f'chicken65\t\t{chicken65_entry.get()}\t\t{chicken65price}Rs\n')
        if muttonsukka_entry.get() !='0':
            txtarea.insert(END,f'Muttonsukka\t\t{muttonsukka_entry.get()}\t\t{muttonsukkaprice}Rs\n')
        if grillchicken_entry.get() !='0':
            txtarea.insert(END,f'Grilledchicken\t\t{grillchicken_entry.get()}\t\t{grillchickenprice}Rs\n')
        if thanthoorichicken_entry.get() !='0':
            txtarea.insert(END,f'tadoorichicken\t\t{thanthoorichicken_entry.get()}\t\t{thanoorichickenprice}Rs\n')
        if chickencurry_entry.get() !='0':
            txtarea.insert(END,f'chickencurry\t\t{chickencurry_entry.get()}\t\t{chickencurryprice}Rs\n')

        if vannila_entry.get() !='0':
            txtarea.insert(END,f'Vannila ice\t\t{vannila_entry.get()}\t\t{vannilaprice}Rs\n')
        if straberry_entry.get() != '0':
            txtarea.insert(END, f'strabwerry ice\t\t{straberry_entry.get()}\t\t{straberryprice}Rs\n')
        if choclate_entry.get() != '0':
            txtarea.insert(END, f'choclate ice\t\t{choclate_entry.get()}\t\t{choclateprice}Rs\n')
        if butterscotch_entry.get() != '0':
            txtarea.insert(END, f'Butterscotch\t\t{butterscotch_entry.get()}\t\t{butterscotchprice}Rs\n')
        if badhampista_entry.get() !='0':
            txtarea.insert(END,f'Badham ice\t\t{badhampista_entry.get()}\t\t{badhampistaprice}Rs\n')
        txtarea.insert(END,f'======================================\n')


        if foodtax_entry.get() !='0.0rS':
            txtarea.insert(END,f'Foddtax\t\t\t\t{foodtax_entry.get()}rs\n')
        if sidedishtax_entry.get() != '0.0rS':
            txtarea.insert(END, f'Sidedishtax\t\t\t\t{sidedishtax_entry.get()}rs\n')
        if icecreamtax_entry.get() != '0.0rS':
            txtarea.insert(END,f'Icetax\t\t\t\t{icecreamtax_entry.get()}rs\n')

        txtarea.insert(END,f'Grand Total\t\t\t{totalbill}rs\n')
        savebill()
def total():

    global parrotaprice,chickenriceprice,dosaiprice,idliprice,eggparrootaprice
    global chicken65price,grillchickenprice,muttonsukkaprice,thanoorichickenprice,chickencurryprice

    global vannilaprice,straberryprice,choclateprice,butterscotchprice,badhampistaprice
    global totalbill


    #foodprice
    parrotaprice=int(paroota_entry.get())*15
    chickenriceprice=int(chickenrice_entry.get())*70
    dosaiprice=int(Dosai_entry.get())*30
    idliprice=int(Idli_entry.get())*7
    eggparrootaprice=int(eggparoota_label_entry.get())*80

    totalfoodprice=parrotaprice+chickenriceprice+dosaiprice+idliprice+eggparrootaprice
    foodprice_entry.delete(0,END)
    foodprice_entry.insert(0,str(totalfoodprice)+'Rs')
    foodpricetax=totalfoodprice*0.08
    foodtax_entry.delete(0,END)
    foodtax_entry.insert(0,str(foodpricetax)+"rs")

    #sidedishprice

    chicken65price=int(chicken65_entry.get())*40
    muttonsukkaprice=int(muttonsukka_entry.get())*70
    grillchickenprice=int(grillchicken_entry.get())*300
    thanoorichickenprice=int(thanthoorichicken_entry.get())*180
    chickencurryprice=int(chickencurry_entry.get())*70

    totalsidedishprice=chicken65price+muttonsukkaprice+grillchickenprice+thanoorichickenprice+chickencurryprice
    sidedish_entry.delete(0,END)
    sidedish_entry.insert(0,str(totalsidedishprice)+'rs')

    sidedishpricetax = totalsidedishprice*0.08
    sidedishtax_entry.delete(0, END)
    sidedishtax_entry.insert(0, str(sidedishpricetax) + "rs")

    #icecream

    vannilaprice=int(vannila_entry.get())*50
    straberryprice=int(straberry_entry.get())*60
    choclateprice=int(choclate_entry.get())*70
    butterscotchprice=int(butterscotch_entry.get())*80
    badhampistaprice=int(badhampista_entry.get())*90

    totaliceprice=vannilaprice+straberryprice+choclateprice+butterscotchprice+badhampistaprice
    icecreamprice_entry.delete(0,END)
    icecreamprice_entry.insert(0,str(totaliceprice)+'rs')

    icepricetax = totaliceprice *0.08
    icecreamtax_entry.delete(0, END)
    icecreamtax_entry.insert(0, str(icepricetax) + "rs")

    totalbill=totalfoodprice+totalsidedishprice+totaliceprice+foodpricetax+sidedishpricetax+icepricetax

#gui part

window = Tk()
window.title("ANBAGAM MESS")
window.config(bg="#2c3e50")
window.iconbitmap("hotel.ico")
window.geometry("1268x680")


myfont = Font(family="times",size=20,weight="bold",slant="italic",underline=1,overstrike=1)
labname1 = Label(window, text="Billing system", bg="#0a3d62", fg="white", padx=20, pady=5, font=myfont, relief=GROOVE)
labname1.pack(fill=X)

customer_detail_frame = LabelFrame(window,text="customer_detail",font=("times",20,"bold"), bg="#0a3d62", fg="white", relief=GROOVE)
customer_detail_frame.pack(fill=X)

name_label = Label(customer_detail_frame,text="Name",font=("times",20,"bold"),bg="#0a3d62",fg="white")
name_label.grid(row=0, column=0,padx=20,pady=2)

name_entry=Entry(customer_detail_frame,font=("arial",20,"bold"), width=15)
name_entry.grid(row=0,column=1,padx=8)

phone_label = Label(customer_detail_frame,text="mobile",font=("times",20,"bold"),bg="#0a3d62",fg="white")
phone_label.grid(row=0, column=2,padx=20, pady=2)

phone_entry=Entry(customer_detail_frame,font=("arial",20,"bold"), width=15)
phone_entry.grid(row=0,column=3,padx=8)

bill_label = Label(customer_detail_frame,text="Billno",font=("times",20,"bold"),bg="#0a3d62",fg="white")
bill_label.grid(row=0, column=4,padx=20, pady=2)

bill_entry=Entry(customer_detail_frame,font=("times",20,"bold"), width=15)
bill_entry.grid(row=0,column=5,padx=8)

search_button=Button(customer_detail_frame,text="Search",font=("times",20,"bold"), bg="#0a3d62",fg="white",command=searchbill)
search_button.grid(row=0, column=6,padx=15)

#foodlist frame

foodname_frame1=Frame(window)
foodname_frame1.pack()

food_labelframe = LabelFrame(foodname_frame1,text="Foodlist", font=("times",20,"bold"), bg="#0a3d62", fg="white", relief=GROOVE)
food_labelframe.grid(row=0, column=0)

parootta_label=Label(food_labelframe,text="Paroota", font=("times",20,"bold"),bg="#0a3d62",fg="white")
parootta_label.grid(row=0,column=0,sticky='w')

paroota_entry=Entry(food_labelframe, font=("arial",20,"bold"), width=5,bd=5)
paroota_entry.grid(row=0,column=1,pady=10,padx=10)
paroota_entry.insert(0,0)

chickenrice_label=Label(food_labelframe,text="Chickenrice", font=("times",20,"bold"),bg="#0a3d62",fg="white")
chickenrice_label.grid(row=1,column=0,sticky='w')

chickenrice_entry=Entry(food_labelframe, font=("arial",20,"bold"), width=5,bd=5)
chickenrice_entry.grid(row=1,column=1,pady=10,padx=10)
chickenrice_entry.insert(0,0)

Dosai_label=Label(food_labelframe,text="Dosai", font=("times",20,"bold"),bg="#0a3d62",fg="white")
Dosai_label.grid(row=2,column=0,sticky='w')

Dosai_entry=Entry(food_labelframe, font=("arial",20,"bold"), width=5,bd=5)
Dosai_entry.grid(row=2,column=1,pady=10,padx=10)
Dosai_entry.insert(0,0)

Idli_label=Label(food_labelframe,text="Idli", font=("times",20,"bold"),bg="#0a3d62",fg="white")
Idli_label.grid(row=3,column=0,sticky='w')

Idli_entry=Entry(food_labelframe, font=("arial",20,"bold"), width=5,bd=5)
Idli_entry.grid(row=3,column=1,pady=10,padx=10)
Idli_entry.insert(0,0)

eggparoota_label=Label(food_labelframe,text="Egg_Parootta", font=("times",20,"bold"),bg="#0a3d62",fg="white")
eggparoota_label.grid(row=4,column=0,sticky='w')

eggparoota_label_entry=Entry(food_labelframe, font=("arial",20,"bold"), width=5,bd=5)
eggparoota_label_entry.grid(row=4,column=1,pady=10,padx=10)
eggparoota_label_entry.insert(0,0)

#sidedish
sidedish_labelframe = LabelFrame(foodname_frame1,text="Sidedish", font=("times",20,"bold"), bg="#0a3d62", fg="white", relief=GROOVE)
sidedish_labelframe.grid(row=0, column=1)

chicken65_label=Label(sidedish_labelframe,text="Chicken65", font=("times",20,"bold"),bg="#0a3d62",fg="white")
chicken65_label.grid(row=0,column=0,sticky='w')

chicken65_entry=Entry(sidedish_labelframe, font=("arial",20,"bold"), width=5,bd=5)
chicken65_entry.grid(row=0,column=1,pady=10,padx=10)
chicken65_entry.insert(0,0)

grillchicken_label=Label(sidedish_labelframe,text="Grill_Chicken", font=("times",20,"bold"),bg="#0a3d62",fg="white")
grillchicken_label.grid(row=1,column=0,sticky='w')

grillchicken_entry=Entry(sidedish_labelframe, font=("arial",20,"bold"), width=5,bd=5)
grillchicken_entry.grid(row=1,column=1,pady=10,padx=10)
grillchicken_entry.insert(0,0)

thanthoorichicken_label=Label(sidedish_labelframe,text="Tandoori_Chicken", font=("times",20,"bold"),bg="#0a3d62",fg="white")
thanthoorichicken_label.grid(row=2,column=0,sticky='w')

thanthoorichicken_entry=Entry(sidedish_labelframe, font=("arial",20,"bold"), width=5,bd=5)
thanthoorichicken_entry.grid(row=2,column=1,pady=10,padx=10)
thanthoorichicken_entry.insert(0,0)

muttonsukka_label=Label(sidedish_labelframe,text="Mutton_sukka", font=("times",20,"bold"),bg="#0a3d62",fg="white")
muttonsukka_label.grid(row=3,column=0,sticky='w')

muttonsukka_entry=Entry(sidedish_labelframe, font=("arial",20,"bold"), width=5,bd=5)
muttonsukka_entry.grid(row=3,column=1,pady=10,padx=10)
muttonsukka_entry.insert(0,0)

chickencurry_label=Label(sidedish_labelframe,text="Chickencurry", font=("times",20,"bold"),bg="#0a3d62",fg="white")
chickencurry_label.grid(row=4,column=0,sticky='w')

chickencurry_entry=Entry(sidedish_labelframe, font=("arial",20,"bold"), width=5,bd=5)
chickencurry_entry.grid(row=4,column=1,pady=10,padx=10)
chickencurry_entry.insert(0,0)

#icecream

Icecream_labelframe = LabelFrame(foodname_frame1,text="Icecream", font=("times",20,"bold"), bg="#0a3d62", fg="white", relief=GROOVE)
Icecream_labelframe.grid(row=0, column=2)

vannila_label=Label(Icecream_labelframe,text="Vannila", font=("times",20,"bold"),bg="#0a3d62",fg="white")
vannila_label.grid(row=0,column=0,sticky='w')

vannila_entry=Entry(Icecream_labelframe, font=("arial",20,"bold"), width=5,bd=5)
vannila_entry.grid(row=0,column=1,pady=10,padx=10)
vannila_entry.insert(0,0)

strawberry_label=Label(Icecream_labelframe,text="Strawberry", font=("times",20,"bold"),bg="#0a3d62",fg="white")
strawberry_label.grid(row=1,column=0,sticky='w')

straberry_entry = Entry(Icecream_labelframe, font=("arial",20,"bold"), width=5,bd=5)
straberry_entry.grid(row=1,column=1,pady=10,padx=10)
straberry_entry.insert(0,0)

choclate_label=Label(Icecream_labelframe,text="choclate", font=("times",20,"bold"),bg="#0a3d62",fg="white")
choclate_label.grid(row=2,column=0,sticky='w')

choclate_entry=Entry(Icecream_labelframe, font=("arial",20,"bold"), width=5,bd=5)
choclate_entry.grid(row=2,column=1,pady=10,padx=10)
choclate_entry.insert(0,0)

butterscotch_label=Label(Icecream_labelframe,text="Butterscotch", font=("times",20,"bold"),bg="#0a3d62",fg="white")
butterscotch_label.grid(row=3,column=0,sticky='w')

butterscotch_entry=Entry(Icecream_labelframe, font=("arial",20,"bold"), width=5,bd=5)
butterscotch_entry.grid(row=3,column=1,pady=10,padx=10)
butterscotch_entry.insert(0,0)

badhampista_label=Label(Icecream_labelframe,text="Badhampista", font=("times",20,"bold"),bg="#0a3d62",fg="white")
badhampista_label.grid(row=4,column=0,sticky='w')

badhampista_entry=Entry(Icecream_labelframe, font=("arial",20,"bold"), width=5,bd=5)
badhampista_entry.grid(row=4,column=1,pady=10,padx=10)
badhampista_entry.insert(0,0)

#billarea

billframe=Frame(foodname_frame1,bd=5,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billarea_label=Label(billframe,text="Bill area", font=("times",20,"bold"),relief=GROOVE)
billarea_label.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

txtarea=Text(billframe, height=18, width=40, yscrollcommand=scrollbar.set)
txtarea.pack()
scrollbar.config(command=txtarea.yview)

#bill menu

bill_labelframe = LabelFrame(window,text="Billmenu", font=("times",20,"bold"), bg="#0a3d62", fg="white", relief=GROOVE)
bill_labelframe.pack()

foodprice_label=Label(bill_labelframe,text="Foodprice", font=("times",15,"bold"),bg="#0a3d62",fg="white")
foodprice_label.grid(row=0,column=0,sticky='w')

foodprice_entry=Entry(bill_labelframe, font=("arial",20,"bold"), width=5,bd=5)
foodprice_entry.grid(row=0,column=1,pady=3,padx=10)

sidedishprice_label=Label(bill_labelframe,text="sidedishpricee", font=("times",15,"bold"),bg="#0a3d62",fg="white")
sidedishprice_label.grid(row=1,column=0,sticky='w')

sidedish_entry=Entry(bill_labelframe, font=("arial",20,"bold"), width=5,bd=5)
sidedish_entry.grid(row=1,column=1,pady=3,padx=10)

icecreamprice_label=Label(bill_labelframe,text="Icecreamprice", font=("times",15,"bold"),bg="#0a3d62",fg="white")
icecreamprice_label.grid(row=2,column=0,sticky='w')

icecreamprice_entry=Entry(bill_labelframe, font=("arial",20,"bold"), width=5,bd=5)
icecreamprice_entry.grid(row=2,column=1,pady=3,padx=10)

#tax

foodtax_label=Label(bill_labelframe,text="Foodtax", font=("times",25,"bold"),bg="#0a3d62",fg="white")
foodtax_label.grid(row=0,column=2,sticky='w')

foodtax_entry=Entry(bill_labelframe, font=("arial",20,"bold"), width=5,bd=5)
foodtax_entry.grid(row=0,column=3,pady=3,padx=20)

sidedishtax_label=Label(bill_labelframe,text="sidedishtax", font=("times",25,"bold"),bg="#0a3d62",fg="white")
sidedishtax_label.grid(row=1,column=2,sticky='w')

sidedishtax_entry=Entry(bill_labelframe, font=("arial",20,"bold"), width=5,bd=5)
sidedishtax_entry.grid(row=1,column=3,pady=3,padx=20)

icecreamtax_label=Label(bill_labelframe,text="Icecreamtax", font=("times",25,"bold"),bg="#0a3d62",fg="white")
icecreamtax_label.grid(row=2,column=2,sticky='w')

icecreamtax_entry=Entry(bill_labelframe, font=("arial",20,"bold"), width=5,bd=5)
icecreamtax_entry.grid(row=2,column=3,pady=3,padx=20)

buttonframe=Frame(bill_labelframe,bd=8,relief=GROOVE)
buttonframe.grid(row=0,column=4,rowspan=3)

totbutton=Button(buttonframe,text="Total",font=("times",15,"bold"),bg="#0a3d62",fg="white",bd=5,width=8,pady=10,command=total)
totbutton.grid(row=0,column=1,pady=20,padx=15)

billbutton=Button(buttonframe,text="Bill",font=("times",15,"bold"),bg="#0a3d62",fg="white",bd=5,width=8,pady=10,command=billarea)
billbutton.grid(row=0,column=2,pady=20,padx=15)

emailbutton=Button(buttonframe,text="Email",font=("times",15,"bold"),bg="#0a3d62",fg="white",bd=5,width=8,pady=10,command=sendmail)
emailbutton.grid(row=0,column=3,pady=20,padx=15)

printbutton=Button(buttonframe,text="Print",font=("times",15,"bold"),bg="#0a3d62",fg="white",bd=5,width=8,pady=10,command=printbill)
printbutton.grid(row=0,column=4,pady=20,padx=15)

clearbutton=Button(buttonframe,text="Clear",font=("times",15,"bold"),bg="#0a3d62",fg="white",bd=5,width=8,pady=10,command=clear)
clearbutton.grid(row=0,column=5,pady=20,padx=15)


window.mainloop()