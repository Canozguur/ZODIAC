import time as tm
from tkinter import *

import requests
from bs4 import BeautifulSoup
from PIL import ImageTk,Image

from tkinter.ttk import Combobox
def About_zodiac(zodiac):

    translate = {"aries": "koc",
                 "taurus": "boga",
                 "gemini": "ikizler",
                 "cancer": "yengec",
                 "leo": "aslan",
                 "virgo": "basak",
                 "libra": "terazi",
                 "scorpio": "akrep",
                 "sagitarius": "yay",
                 "capricorn": "oglak",
                 "aquarius": "kova",
                 "pisces": "balik",
                 }
    print(zodiac)
    root.geometry("1040x700")
    for i in root.winfo_children():
        i.destroy()
    zodiac = zodiac.lower()
    zodiac = translate[zodiac]
    print(zodiac)
    url = "https://www.gunlukburc.net/gunluk-burc-yorumlari/" + zodiac + ".html"
    r = requests.get(url)
    print(r.headers["Date"])

    soup = BeautifulSoup(r.content, "html.parser")
    veri = soup.find_all(class_="yildiz-fali ask")
    oran = soup.find_all(class_="percentage")
    veri1 = soup.find_all(class_="single-chart")
    paragraf_genel = soup.find(class_="d-block order-1")
    baslik= paragraf_genel.find_next(class_="d-block")
    a = paragraf_genel.find_next("p").get_text()
    l_baslık = Label(text=baslik.get_text(),font="Arial 15",fg="purple")
    w = Text(root, height=9, borderwidth=0,font="Verdana 14")
    w.insert(1.0,a)
    w.place(x=40,y=80)

    l_baslık.place(x=40,y=40)

    w.configure(state="disabled")
    info = []
    for i in range(0, 5):

        yazı = veri1[i].get_text()
        yazı = str(yazı).replace("%", " \n %")
        info.append(yazı)


    l_genel = Label(text=info[0],font="ARIAL 18",)
    l_ask = Label(text=info[1],font="ARIAL 18",)
    l_para = Label(text=info[2],font="ARIAL 18",)
    l_Saglik = Label(text=info[3],font="ARIAL 18",)
    l_is = Label(text=info[4],font="ARIAL 18",)
    l_genel.place(x=100,y=500)
    l_ask.place(x=250,y=500)
    l_para.place(x=400,y=500)
    l_Saglik.place(x=550,y=500)
    l_is.place(x=700,y=500)
    value = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagitarius", "capricorn",
             "aquarius", "pisces", ]

    c_secim = Combobox(values=value,)
    b_ara = Button(text="Search" )
    if c_secim.get() == []:
        b_ara.config(state=DISABLED)

    b_ara.config( command=lambda: About_zodiac(c_secim.get()))


    b_ara.place(x=800, y=540)
    c_secim.place(x=800, y=500)
#defim():


def time():

    import time as tm


    zaman = tm.strftime("%H:%M:%S")
    l_time["text"]= zaman
    root.after(1000,time)

def konum(event):
    print(event.x,event.y)


root = Tk()
root.title("Burç Yorumu")
root.geometry("1050x1000")



aries  = Image.open("ARİES.jpg")
taurus = Image.open(r"TAURUS.jpg")
gemini = Image.open(r"GEMİNİ.jpg")
cancer = Image.open(r"CANCER.jpg")
leo = Image.open(r"LEO.jpg")
virgo = Image.open(r"VIRGO.jpg")
libra = Image.open(r"LIBRA.jpg")
scorpio = Image.open(r"SCORPIO.jpg")
sagitairus = Image.open(r"SAGITARIUS.jpg")
capricorn = Image.open(r"CAPRICORN.jpg")
aquarius = Image.open(r"AQUARIUS.jpg")
pisces = Image.open(r"PISCES.jpg")
imagearies = aries.resize((160, 160), Image.ANTIALIAS)
imagetaurus = taurus.resize((160, 160), Image.ANTIALIAS)
imagegemini = gemini.resize((160, 160), Image.ANTIALIAS)
imagecancer = cancer.resize((160, 160), Image.ANTIALIAS)
imageleo = leo.resize((160, 160), Image.ANTIALIAS)
imagevirgo = virgo.resize((160, 160), Image.ANTIALIAS)
imagelibra = libra.resize((160, 160), Image.ANTIALIAS)
imagescorpio = scorpio.resize((160, 160), Image.ANTIALIAS)
imagesagitairus = sagitairus.resize((160, 160), Image.ANTIALIAS)
imagecapricorn = capricorn.resize((160, 160), Image.ANTIALIAS)
imageaquarius = aquarius.resize((160, 160), Image.ANTIALIAS)
imagepisces = pisces.resize((160, 160), Image.ANTIALIAS)

imagearies = ImageTk.PhotoImage(imagearies)
imagetaurus = ImageTk.PhotoImage(imagetaurus)
imagegemini = ImageTk.PhotoImage(imagegemini)
imagecancer = ImageTk.PhotoImage(imagecancer)
imageleo = ImageTk.PhotoImage(imageleo)
imagevirgo = ImageTk.PhotoImage(imagevirgo)
imagelibra = ImageTk.PhotoImage(imagelibra)
imagescorpio = ImageTk.PhotoImage(imagescorpio)
imagesagitairus = ImageTk.PhotoImage(imagesagitairus)
imagecapricorn = ImageTk.PhotoImage(imagecapricorn)
imageaquarius = ImageTk.PhotoImage(imageaquarius)
imagepisces = ImageTk.PhotoImage(imagepisces)
fm = Frame(root)
fm1 = Frame(root)
fm2 = Frame(root)
fm3 = Frame(root)




b_aries = Button(fm,image=imagearies,fg='green', bg='white',text="KOC",compound=BOTTOM,command=lambda : About_zodiac("ARIES") )
b_taurus = Button(fm1,image=imagetaurus,fg='green', bg='white',text="BOGA",compound=BOTTOM,command=lambda : About_zodiac("TAURUS"))
b_gemini = Button(fm2,image=imagegemini,fg='green', bg='white',text="IKIZLER",compound=BOTTOM,command=lambda : About_zodiac("GEMINI"))
b_cancer = Button(fm,image=imagecancer,fg='green', bg='white',text="YENGEC",compound=BOTTOM,command=lambda : About_zodiac("CANCER"))
b_leo = Button(fm1,image=imageleo,fg='green', bg='white',text="ASLAN",compound=BOTTOM,command=lambda : About_zodiac("LEO"))
b_virgo = Button(fm2,image=imagevirgo,fg='green', bg='white',text="BASAK",compound=BOTTOM,command=lambda : About_zodiac("VIRGO"))
b_libra = Button(fm,image=imagelibra,fg='green', bg='white',text="TERAZI",compound=BOTTOM,command=lambda : About_zodiac("LIBRA"))
b_scorpio = Button(fm1,image=imagescorpio,fg='green', bg='white',text="AKREP",compound=BOTTOM,command=lambda : About_zodiac("SCORPIO"))
b_sagitairus = Button(fm2,image=imagesagitairus,fg='green', bg='white',text="YAY",compound=BOTTOM,command=lambda : About_zodiac("SAGITARIUS"))
b_capricorn = Button(fm,image=imagecapricorn,fg='green', bg='white',text="OGLAK",compound=BOTTOM,command=lambda : About_zodiac("CAPRICORN"))
b_aquarius = Button(fm1,image=imageaquarius,fg='green', bg='white',text="KOVA",compound=BOTTOM,command=lambda : About_zodiac("AQUARIUS"))
b_pisces = Button(fm2,image=imagepisces,fg='green', bg='white',text="BALIK",compound=BOTTOM,command=lambda : About_zodiac("PISCES"))
l_aries = Label(fm,text = "21 March-20 April")
l_taurus = Label(fm1,text = "21 April-21 May")
l_gemini = Label(fm2,text = "22 May-21 June")
l_cancer = Label(fm,text = "22 june-22 July")
l_leo = Label(fm1,text = "23 july-23 August")
l_libra = Label(fm,text = "24 August-22 September")
l_virgo = Label(fm2,text = "23 September-23 October")
l_scorpio = Label(fm1,text = "24 October-22 November")
l_sagitairus = Label(fm2,text = "23 November-21 December")
l_capricorn = Label(fm,text = "22 December-20 January")
l_aquarius = Label(fm1,text = "21 January-18 February")
l_pisces = Label(fm2,text = "19 February-20 March")

b_aries.pack(padx=40,pady=15,side=TOP, anchor=W)
l_aries.pack(padx=80,side=TOP,anchor=W)
b_taurus.pack(padx=40,pady=15,side=TOP, anchor=W)
l_taurus.pack(padx=80,anchor=W)
b_gemini.pack(padx=40,pady=15,side=TOP, anchor=W)
l_gemini.pack(padx=80,anchor=W)
b_cancer.pack(padx=40,pady=15,side=TOP, anchor=W)
l_cancer.pack(padx=80,anchor=W)
b_leo.pack(padx=40,pady=15,side=TOP, anchor=W)
l_leo.pack(padx=80,anchor=W)
b_virgo.pack(padx=40,pady=15, side=TOP, anchor=W)
l_virgo.pack(padx=70,anchor=W)
b_libra.pack(padx=40,pady=15,side=TOP, anchor=W)
l_libra.pack(padx=70,anchor=W)
b_scorpio.pack(padx=40,pady=15,side=TOP, anchor=W)
l_scorpio.pack(padx=70,anchor=W)
b_sagitairus.pack(padx=40,pady=15,side=TOP, anchor=W)
l_sagitairus.pack(padx=70,anchor=W)
b_capricorn.pack(padx=40,pady=15,side=TOP, anchor=W)
l_capricorn.pack(padx=70,anchor=W)
b_aquarius.pack(padx=40,pady=15,side=TOP, anchor=W)
l_aquarius.pack(padx=70,anchor=W)
b_pisces.pack(padx=40,pady=15,side=TOP, anchor=W)
l_pisces.pack(padx=75,anchor=W)











fm.pack(side=LEFT)
fm1.pack(side=LEFT)
fm2.pack(side=LEFT)

root.bind("<Button-1>",konum)

l_time = Label(root, font="Verdana 20", relief=RAISED)
l_time.pack(anchor=NE, padx=20, pady=20)
time()


root.mainloop()
