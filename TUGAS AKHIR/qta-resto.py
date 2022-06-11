import tkinter
from tkinter import *
import time
import datetime
import random
import tkinter.messagebox

root =Tk()
root.resizable(0,0)
root.geometry("1270x600")
root.iconbitmap(r"QTA.ico")
root.title("Billing System QTA")
root.configure(background='#6B7AA1')

####################################################### NAMA RESTO ###########################################################
Tops=Frame(root,bg='#94B3FD',bd=10,padx=5,pady=5,relief="raise")
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('Robot',40,'bold'),text='RESTO QTA MANAGEMENT',width=38,bd=10,bg='navy',fg='white',justify=CENTER)
lblTitle.grid(row=0)

####################################################### PAGE BUKTI PEMBAYARAN #################################################
ReceiptCal_F=Frame(root,bg='blue',bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F,bg='blue',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Receipt_F=Frame(ReceiptCal_F,bg='powder blue',bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

####################################################### PAGE PEMBAYARAN ##########################################
MenuFrame=Frame(root,bg='blue',bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)

Cost_F=Frame(MenuFrame,padx=40,bg='#94B3FD',bd=4)
Cost_F.pack(side=BOTTOM)

Drinks_F=Frame(MenuFrame,bg='#94DAFF',bd=4,relief=RIDGE)
Drinks_F.pack(side=LEFT)

Food_F=Frame(MenuFrame,bg='#94DAFF',bd=4,relief=RIDGE)
Food_F.pack(side=RIGHT)

################################################### variable ################################################
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

TglOrder      = StringVar()
Receipt_Ref   = StringVar()
Pajak         = StringVar()
TotalHarga    = StringVar()
TotalSemua    = StringVar()
HargaMakanan  = StringVar()
HargaMinuman  = StringVar()
BiayaPelayanan = StringVar()

TglOrder.set(time.strftime("%d/%m/%Y"))

E_Coffee        = StringVar()
E_HotTea        = StringVar()
E_IceTea        = StringVar()
E_Sprite        = StringVar()
E_HotCappuccino = StringVar()
E_IceCappuccino = StringVar()
E_CocaCola      = StringVar()
E_SodaGembira   = StringVar()

E_NasiGoreng    = StringVar()
E_Spagheti      = StringVar()
E_MieRebus      = StringVar()
E_MieGoreng     = StringVar()
E_Sandwich      = StringVar()
E_Burger        = StringVar()
E_SosisBakar    = StringVar()
E_KentangGoreng = StringVar()

E_Coffee.set("0")
E_HotTea.set("0")
E_IceTea.set("0")
E_Sprite.set("0")
E_HotCappuccino.set("0")
E_IceCappuccino.set("0")
E_CocaCola.set("0")
E_SodaGembira.set("0")

E_NasiGoreng.set("0")
E_Spagheti.set("0")
E_MieRebus.set("0")
E_MieGoreng.set("0")
E_Sandwich.set("0")
E_Burger.set("0")
E_SosisBakar.set("0")
E_KentangGoreng.set("0")



########################################## Fungsi Deklarasi ####################################################

def Exit():
    Exit=tkinter.messagebox.askyesno("Exit Billing System QTA","Are You Sure Exit ?")
    if Exit > 0:
        root.destroy()
        return

def Reset():
    Pajak.set("")
    TotalHarga.set("")
    TotalSemua.set("")
    HargaMakanan.set("")
    HargaMinuman.set("")
    BiayaPelayanan.set("")
    txtReceipt.delete("1.0",END)

    E_Coffee.set("0")
    E_HotTea.set("0")
    E_IceTea.set("0")
    E_Sprite.set("0")
    E_HotCappuccino.set("0")
    E_IceCappuccino.set("0")
    E_CocaCola.set("0")
    E_SodaGembira.set("0")

    E_NasiGoreng.set("0")
    E_Spagheti.set("0")
    E_MieRebus.set("0")
    E_MieGoreng.set("0")
    E_Sandwich.set("0")
    E_Burger.set("0")
    E_SosisBakar.set("0")
    E_KentangGoreng.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtCoffee.configure(state=DISABLED)
    txtHotTea.configure(state=DISABLED)
    txtIceTea.configure(state=DISABLED)
    txtSprite.configure(state=DISABLED)
    txtHotCappuccino.configure(state=DISABLED)
    txtIceCappuccino.configure(state=DISABLED)
    txtCocaCola.configure(state=DISABLED)
    txtSodaGembira.configure(state=DISABLED)
    txtNasiGoreng.configure(state=DISABLED)
    txtSpagheti.configure(state=DISABLED)
    txtMieRebus.configure(state=DISABLED)
    txtMieGoreng.configure(state=DISABLED)
    txtSandwich.configure(state=DISABLED)
    txtBurger.configure(state=DISABLED)
    txtSosisBakar.configure(state=DISABLED)
    txtKentangGoreng.configure(state=DISABLED)

def CostofItem():
    Item1=float(E_Coffee.get())
    Item2=float(E_HotTea.get())
    Item3=float(E_IceTea.get())
    Item4=float(E_Sprite.get())
    Item5=float(E_HotCappuccino.get())
    Item6=float(E_IceCappuccino.get())
    Item7=float(E_CocaCola.get())
    Item8=float(E_SodaGembira.get())

    Item9=float(E_NasiGoreng.get())
    Item10=float(E_Spagheti.get())
    Item11=float(E_MieRebus.get())
    Item12=float(E_MieGoreng.get())
    Item13=float(E_Sandwich.get())
    Item14=float(E_Burger.get())
    Item15=float(E_SosisBakar.get())
    Item16=float(E_KentangGoreng.get())

    #SET HARGA
    PriceofDrinks   =(Item1 * 15000) + (Item2 * 7000) + (Item3 * 8000) + (Item4 * 10000) + (Item5 * 16000) + (Item6 * 18000) + (Item7 * 10000) + (Item8 * 20000)
    
    PriceofFood     =(Item9 * 25000) + (Item10 * 30000) + (Item11 * 15000) + (Item12 * 15000) + (Item13 * 12000) + (Item14 * 15000) + (Item15 * 10000) + (Item16 * 12000)

    DrinksPrice = "Rp",str('%.2f'%(PriceofDrinks))
    FoodPrice   =  "Rp",str('%.2f'%(PriceofFood))
    HargaMakanan.set(FoodPrice)
    HargaMinuman.set(DrinksPrice)
    Pelayanan   = "Rp",str('%.2f'%(1500))
    BiayaPelayanan.set(Pelayanan)

    TotalHargaofITEMS = "Rp",str('%.2f'%(PriceofDrinks + PriceofFood))
    TotalHarga.set(TotalHargaofITEMS)

    Tax = "Rp",str('%.2f'%((PriceofDrinks + PriceofFood) * 0.05))
    Pajak.set(Tax)
    
    Gabung = (1500 + (PriceofDrinks + PriceofFood) * 0.05)
    TC  ="Rp",str('%.2f'%(PriceofDrinks + PriceofFood + Gabung))
    TotalSemua.set(TC)


def chk_Coffee():
    if(var1.get() == 1):
        txtCoffee.configure(state = NORMAL)
        txtCoffee.focus()
        txtCoffee.delete('0',END)
        E_Coffee.set("")
    elif(var1.get() == 0):
        txtCoffee.configure(state = DISABLED)
        E_Coffee.set("0")

def chk_HotTea():
    if(var2.get() == 1):
        txtHotTea.configure(state = NORMAL)
        txtHotTea.focus()
        txtHotTea.delete('0',END)
        E_HotTea.set("")
    elif(var2.get() == 0):
        txtHotTea.configure(state = DISABLED)
        E_HotTea.set("0")

def chk_IceTea():
    if(var3.get() == 1):
        txtIceTea.configure(state = NORMAL)
        txtIceTea.delete('0',END)
        txtIceTea.focus()
    elif(var3.get() == 0):
        txtIceTea.configure(state = DISABLED)
        E_IceTea.set("0")

def chk_Sprite():
    if(var4.get() == 1):
        txtFrappe.configure(state = NORMAL)
        txtFrappe.delete('0',END)
        txtFrappe.focus()
    elif(var4.get() == 0):
        txtFrappe.configure(state = DISABLED)
        E_Frappe.set("0")

def chk_HotCappuccino():
    if(var5.get() == 1):
        txtHotCappuccino.configure(state = NORMAL)
        txtHotCappuccino.delete('0',END)
        txtHotCappuccino.focus()
    elif(var5.get() == 0):
        txtHotCappuccino.configure(state = DISABLED)
        E_HotCappuccino.set("0")

def chk_IceCappuccino():
    if(var6.get() == 1):
        txtIceCappuccino.configure(state = NORMAL)
        txtIceCappuccino.delete('0',END)
        txtIceCappuccino.focus()
    elif(var6.get() == 0):
        txtIceCappuccino.configure(state = DISABLED)
        E_IceCappuccino.set("0")

def chk_CocaCola():
    if(var7.get() == 1):
        txtCocaCola.configure(state = NORMAL)
        txtCocaCola.delete('0',END)
        txtCocaCola.focus()
    elif(var7.get() == 0):
        txtCocaCola.configure(state = DISABLED)
        E_CocaCola.set("0")

def chk_SodaGembira():
    if(var8.get() == 1):
        txtSodaGembira.configure(state = NORMAL)
        txtSodaGembira.delete('0',END)
        txtSodaGembira.focus()
    elif(var8.get() == 0):
        txtSodaGembira.configure(state = DISABLED)
        E_SodaGembira.set("0")

def chk_NasiGoreng():
    if(var9.get() == 1):
        txtNasiGoreng.configure(state = NORMAL)
        txtNasiGoreng.delete('0',END)
        txtNasiGoreng.focus()
    elif(var9.get() == 0):
        txtNasiGoreng.configure(state = DISABLED)
        E_NasiGoreng.set("0")

def chk_Spagheti():
    if(var10.get() == 1):
        txtSpagheti.configure(state = NORMAL)
        txtSpagheti.delete('0',END)
        txtSpagheti.focus()
    elif(var10.get() == 0):
        txtSpagheti.configure(state = DISABLED)
        E_Spagheti.set("0")

def chk_MieRebus():
    if(var11.get() == 1):
        txtMieRebus.configure(state = NORMAL)
        txtMieRebus.delete('0',END)
        txtMieRebus.focus()
    elif(var11.get() == 0):
        txtMieRebus.configure(state = DISABLED)
        E_MieRebus.set("0")

def chk_MieGoreng():
    if(var12.get() == 1):
        txtMieGoreng.configure(state = NORMAL)
        txtMieGoreng.delete('0',END)
        txtMieGoreng.focus()
    elif(var12.get() == 0):
        txtMieGoreng.configure(state = DISABLED)
        E_MieGoreng.set("0")

def chk_Sandwich():
    if(var13.get() == 1):
        txtSandwich.configure(state = NORMAL)
        txtSandwich.delete('0',END)
        txtSandwich.focus()
    elif(var13.get() == 0):
        txtSandwich.configure(state = DISABLED)
        E_Sandwich.set("0")

def chk_Burger():
    if(var14.get() == 1):
        txtBurger.configure(state = NORMAL)
        txtBurger.delete('0',END)
        txtBurger.focus()
    elif(var14.get() == 0):
        txtBurger.configure(state = DISABLED)
        E_Burger.set("0")

def chk_SosisBakar():
    if(var15.get() == 1):
        txtSosisBakar.configure(state = NORMAL)
        txtSosisBakar.delete('0',END)
        txtSosisBakar.focus()
    elif(var15.get() == 0):
        txtSosisBakar.configure(state = DISABLED)
        E_SosisBakar.set("0")

def chk_KentangGoreng():
    if(var16.get() == 1):
        txtKentangGoreng.configure(state = NORMAL)
        txtKentangGoreng.delete('0',END)
        txtKentangGoreng.focus()
    elif(var16.get() == 0):
        txtKentangGoreng.configure(state = DISABLED)
        E_KentangGoreng.set("0")

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10908,500876)
    randomRef= str(x)
    Receipt_Ref.set("Bill"+ randomRef)

########################################### TEKS PEMBAYARAN ####################################################################
    txtReceipt.insert(END,'\t\tRESTAURANT QTA \n')
    txtReceipt.insert(END,'============================================== \n')
    txtReceipt.insert(END,'Receipt Reff: '+Receipt_Ref.get()+'\t|| '+TglOrder.get()+'\n')
    txtReceipt.insert(END,'============================================== \n')
    txtReceipt.insert(END,'Items\t\t\t\t'+"Cost of Items \n")
    txtReceipt.insert(END,'============================================== \n')
    txtReceipt.insert(END,'Coffee\t\t\t\t\t' + E_Coffee.get() +'\n')
    txtReceipt.insert(END,'Hot Tea\t\t\t\t\t'+ E_HotTea.get()+'\n')
    txtReceipt.insert(END,'Ice Tea\t\t\t\t\t'+ E_IceTea.get()+'\n')
    txtReceipt.insert(END,'Sprite\t\t\t\t\t'+ E_Sprite.get()+'\n')
    txtReceipt.insert(END,'Hot Cappuccino\t\t\t\t\t'+ E_HotCappuccino.get()+'\n')
    txtReceipt.insert(END,'Ice Cappuccino\t\t\t\t\t'+ E_IceCappuccino.get()+'\n')
    txtReceipt.insert(END,'Coca-Cola\t\t\t\t\t'+ E_CocaCola.get()+'\n')
    txtReceipt.insert(END,'Soda Gembira\t\t\t\t\t'+ E_SodaGembira.get()+'\n')
    txtReceipt.insert(END,'Nasi Goreng\t\t\t\t\t'+ E_NasiGoreng.get()+'\n')
    txtReceipt.insert(END,'Spagheti\t\t\t\t\t'+ E_Spagheti.get()+'\n')
    txtReceipt.insert(END,'Mie Rebus\t\t\t\t\t'+ E_MieRebus.get()+'\n')
    txtReceipt.insert(END,'Mie Goreng\t\t\t\t\t'+ E_MieGoreng.get()+'\n')
    txtReceipt.insert(END,'Sandwich\t\t\t\t\t'+ E_Sandwich.get()+'\n')
    txtReceipt.insert(END,'Burger\t\t\t\t\t'+ E_Burger.get()+'\n')
    txtReceipt.insert(END,'Sosis Bakar\t\t\t\t\t'+ E_SosisBakar.get()+'\n')
    txtReceipt.insert(END,'Kentang Goreng\t\t\t\t\t'+ E_KentangGoreng.get()+'\n')
    txtReceipt.insert(END,'============================================== \n')
    txtReceipt.insert(END,'Harga Minuman\t\t\t\t'+ HargaMinuman.get()+'\nHarga Makanan\t\t\t\t'+str(HargaMakanan.get())+"\n")
    txtReceipt.insert(END,'Pajak\t\t\t\t'+ Pajak.get()+'\nBiaya Pelayanan\t\t\t\t'+str(BiayaPelayanan.get())+"\n")
    txtReceipt.insert(END,'Harga Item\t\t\t\t'+ TotalHarga.get()+"\n")
    txtReceipt.insert(END,'============================================== \n')
    txtReceipt.insert(END,'Total Semua\t\t\t\t'+str(TotalSemua.get())+"\n")
    txtReceipt.insert(END,'\n')

######################################### Drinks ####################################################################

Coffee        =Checkbutton(Drinks_F,text='Coffee\t\t\t',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='#94DAFF',command=chk_Coffee).grid(row=0,sticky=W)
HotTea        =Checkbutton(Drinks_F,text='Hot Tea',variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='#94DAFF',command=chk_HotTea).grid(row=1,sticky=W)
IceTea        =Checkbutton(Drinks_F,text='Ice Tea',variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='#94DAFF',command=chk_IceTea).grid(row=2,sticky=W)
Sprite        =Checkbutton(Drinks_F,text='Sprite',variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='#94DAFF',command=chk_Sprite).grid(row=3,sticky=W)
HotCappuccino =Checkbutton(Drinks_F,text='Hot Cappuccino',variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='#94DAFF',command=chk_HotCappuccino).grid(row=4,sticky=W)
IceCappuccino =Checkbutton(Drinks_F,text='Ice Cappuccino',variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='#94DAFF',command=chk_IceCappuccino).grid(row=5,sticky=W)
CocaCola      =Checkbutton(Drinks_F,text='Coca-Cola',variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='#94DAFF',command=chk_CocaCola).grid(row=6,sticky=W)
SodaGembira   =Checkbutton(Drinks_F,text='Soda Gembira',variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='#94DAFF',command=chk_SodaGembira).grid(row=7,sticky=W)

############################################## Drink Entry ###############################################################

txtCoffee   = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_Coffee)
txtCoffee.grid(row=0,column=1)

txtHotTea   = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_HotTea)
txtHotTea.grid(row=1,column=1)

txtIceTea   = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_IceTea)
txtIceTea.grid(row=2,column=1)

txtSprite   = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_Sprite)
txtSprite.grid(row=3,column=1)

txtHotCappuccino = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_HotCappuccino)
txtHotCappuccino.grid(row=4,column=1)

txtIceCappuccino  = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_IceCappuccino)
txtIceCappuccino.grid(row=5,column=1)

txtCocaCola      = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_CocaCola)
txtCocaCola.grid(row=6,column=1)

txtSodaGembira   = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_SodaGembira)
txtSodaGembira.grid(row=7,column=1)

############################################# Foods ######################################################################

NasiGoreng    = Checkbutton(Food_F,text="Nasi Goreng\t\t",variable=var9,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='#94DAFF',command=chk_NasiGoreng).grid(row=0,sticky=W)
Spagheti      = Checkbutton(Food_F,text="Spagheti",variable=var10,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='#94DAFF',command=chk_Spagheti).grid(row=1,sticky=W)
MieRebus      = Checkbutton(Food_F,text="Mie Rebus ",variable=var11,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='#94DAFF',command=chk_MieRebus).grid(row=2,sticky=W)
MieGoreng     = Checkbutton(Food_F,text="Mie Goreng ",variable=var12,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='#94DAFF',command=chk_MieGoreng).grid(row=3,sticky=W)
Sandwich      = Checkbutton(Food_F,text="Sandwich ",variable=var13,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='#94DAFF',command=chk_Sandwich).grid(row=4,sticky=W)
Burger        = Checkbutton(Food_F,text="Burger ",variable=var14,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='#94DAFF',command=chk_Burger).grid(row=5,sticky=W)
SosisBakar    = Checkbutton(Food_F,text="Sosis Bakar ",variable=var15,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='#94DAFF',command=chk_SosisBakar).grid(row=6,sticky=W)
KentangGoreng = Checkbutton(Food_F,text="Kentang Goreng ",variable=var16,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='#94DAFF',command=chk_KentangGoreng).grid(row=7,sticky=W)

################################################ Food Entry ##########################################################

txtNasiGoreng=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_NasiGoreng)
txtNasiGoreng.grid(row=0,column=1)

txtSpagheti=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_Spagheti)
txtSpagheti.grid(row=1,column=1)

txtMieRebus=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_MieRebus)
txtMieRebus.grid(row=2,column=1)

txtMieGoreng=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_MieGoreng)
txtMieGoreng.grid(row=3,column=1)

txtSandwich=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_Sandwich)
txtSandwich.grid(row=4,column=1)

txtBurger=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_Burger)
txtBurger.grid(row=5,column=1)

txtSosisBakar=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_SosisBakar)
txtSosisBakar.grid(row=6,column=1)

txtKentangGoreng=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_KentangGoreng)
txtKentangGoreng.grid(row=7,column=1)

########################################### Informasi Pembayaran ##################################################################

lblHargaMinuman=Label(Cost_F,font=('arial',14,'bold'),text='Harga Minuman\t',bg='#94B3FD',fg='black',justify=CENTER)
lblHargaMinuman.grid(row=0,column=0,sticky=W)
txtHargaMinuman=Entry(Cost_F,width=13,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=3,justify=RIGHT,textvariable=HargaMinuman)
txtHargaMinuman.grid(row=0,column=1)

lblHargaMakanan=Label(Cost_F,font=('arial',14,'bold'),text='Harga Makanan',bg='#94B3FD',fg='black',justify=CENTER)
lblHargaMakanan.grid(row=1,column=0,sticky=W)
txtHargaMakanan=Entry(Cost_F,width=13,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=3,justify=RIGHT,textvariable=HargaMakanan)
txtHargaMakanan.grid(row=1,column=1)

lblBiayaPelayanan=Label(Cost_F,font=('arial',14,'bold'),text='Biaya Pelayanan',bg='#94B3FD',fg='black',justify=CENTER)
lblBiayaPelayanan.grid(row=2,column=0,sticky=W)
txtBiayaPelayanan=Entry(Cost_F,width=13,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=3,justify=RIGHT,textvariable=BiayaPelayanan)
txtBiayaPelayanan.grid(row=2,column=1)

lblPajak=Label(Cost_F,font=('arial',14,'bold'),text='\tPajak',bg='#94B3FD',bd=7,fg='black',justify=CENTER)
lblPajak.grid(row=0,column=2,sticky=W)
txtPajak=Entry(Cost_F,width=15,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=3,justify=RIGHT,textvariable=Pajak)
txtPajak.grid(row=0,column=3)

lblTotalHarga=Label(Cost_F,font=('arial',14,'bold'),text='\tHarga Item',bg='#94B3FD',bd=7, fg='black',justify=CENTER)
lblTotalHarga.grid(row=1,column=2,sticky=W)
txtTotalHarga=Entry(Cost_F,width=15,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=3,justify=RIGHT,textvariable=TotalHarga)
txtTotalHarga.grid(row=1,column=3)

lblTotalSemua=Label(Cost_F,font=('arial',14,'bold'),text='\tTotal Semua',bg='#94B3FD',bd=7,fg='black',justify=CENTER)
lblTotalSemua.grid(row=2,column=2,sticky=W)
txtTotalSemua=Entry(Cost_F,width=15,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=3,justify=RIGHT,textvariable=TotalSemua)
txtTotalSemua.grid(row=2,column=3)

############################################# RECEIPT/Tanda Terima ###############################################################################

txtReceipt=Text(Receipt_F,width=52,height=22,bg='white',bd=4,font=('Times New Roman',12,'bold'))
txtReceipt.grid(row=0,column=0)

########################################### BUTTONS ################################################################################

btnTotal    =Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=5,text='Total',bg='cornsilk2',command=CostofItem).grid(row=0,column=0)
btnReceipt  =Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Receipt',bg='cornsilk2',command=Receipt).grid(row=0,column=1)
btnReset    =Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Reset',bg='cornsilk2',command=Reset).grid(row=0,column=2)
btnExit     =Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=5,text='Exit',bg='cornsilk2',command=Exit).grid(row=0,column=3)

root.mainloop()
