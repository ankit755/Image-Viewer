import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

r=tkinter.Tk()
r.title( "   Image Viewer")
r.iconbitmap('favicon.ico')
r.minsize(150, 150)
r.maxsize(1000, 650)

def nextImg(imgNumber):
    global status
    global imageLabel
    global nextButton
    global backButton
    global bottomFrame
    bottomFrame.forget()
    bottomFrame = tkinter.Frame(r, bg="grey", borderwidth=8, relief=SUNKEN)
    imageLabel.forget()
    imageLabel = Label(imageFrame, image=image_list[imgNumber])

    nextButton = Button(bottomFrame,font= "verdana",text='NEXT',command=lambda: nextImg(imgNumber+1))
    backButton.forget()
    backButton = Button(bottomFrame,font= "verdana", text="BACK",command = lambda: backward(imgNumber-1))
    exitButton = Button(bottomFrame,font= "verdana", text="Exit ", command=r.quit)
    if imgNumber == 4:
        nextButton = Button(bottomFrame, text="Next", state=DISABLED)
    exitButton.pack(ipadx=15,side=BOTTOM,expand = True,fill = BOTH)
    bottomFrame.pack(side=BOTTOM, fill="x")
    backButton.pack(side=LEFT,expand = True, fill = BOTH)
    nextButton.pack(ipadx=18, side=RIGHT,expand = True, fill = BOTH)
    imageLabel.pack()
    status.forget()
    status = Label(imageFrame,font= "family",bg="light green"
                   ,fg="black", text="Image "+str(imgNumber+1) + " of "+
                                     str(len(image_list)) + str("   "), relief=SUNKEN, anchor=E)
    status.pack(side=BOTTOM, expand=True, fill=BOTH)


    return

def backward(x):
    global imageLabel
    global nextButton
    global backButton
    global imgNumber
    global bottomFrame
    global status
    bottomFrame.forget()
    bottomFrame = tkinter.Frame(r, bg="grey", borderwidth=8, relief=SUNKEN)
    imageLabel.forget()
    imageLabel = Label(imageFrame, image=image_list[x])


    nextButton = Button(bottomFrame,font= "verdana", text="NEXT", command=lambda: nextImg(x + 1))
    backButton = Button(bottomFrame,font= "verdana", text="BACK", command=lambda: backward(x - 1))
    exitButton = Button(bottomFrame,font= "verdana", text="Exit ",command=r.quit)
    if x == 0:
        backButton = Button(bottomFrame, text="back", state=DISABLED)
    exitButton.pack(ipadx=15,side=BOTTOM,expand = True,fill = BOTH)
    bottomFrame.pack(side=BOTTOM, fill="x")
    backButton.pack(side=LEFT,expand = True, fill = BOTH)
    nextButton.pack(ipadx=18, side=RIGHT,expand = True, fill = BOTH)
    imageLabel.pack()

    status.forget()
    status = Label(imageFrame,font= "family", bg="light green",fg="black",text="Image " + str(x+1) +
                    "of " + str(len(image_list)) + str("   "),
                   relief=SUNKEN, anchor=E)
    status.pack(side=BOTTOM, expand=True, fill=BOTH)

    return

def PrivateGallery():
    r.iconify()
    global pexitButton
    global pdeleteButton
    global pPublicButton
    global pbottomFrame
    global pimageLabel
    global pnextButton
    global pbackButton


    p = tkinter.Toplevel()
    p.title("   private gallery")
    p.iconbitmap('favicon.ico')
    p.minsize(150, 150)
    p.maxsize(1300, 650)



    def forward(imgPos):
        global currentStatus
        global pimageLabel
        global pnextButton
        global pbackButton
        global pbottomFrame
        global pexitButton

        pbottomFrame.forget()
        pbottomFrame = tkinter.Frame(p, bg="grey", borderwidth=8, relief=SUNKEN)
        pimageLabel.forget()
        pimageLabel = Label(pimageFrame, image=pimage_list[imgPos])

        pnextButton = Button(pbottomFrame,font= "verdana", text='NEXT', command=lambda: forward(imgPos + 1))
        pbackButton.forget()
        pbackButton = Button(pbottomFrame,font= "verdana", text="BACK", command=lambda: back(imgPos - 1))
        pexitButton = Button(pbottomFrame,font= "verdana", text="Exit ", command=p.quit)
        if imgPos == 1:
            pnextButton = Button(pbottomFrame,font= "verdana", text="next", state=DISABLED)




        pexitButton.pack(ipadx=15,side=BOTTOM,expand = True,fill = BOTH)
        pbottomFrame.pack(side=BOTTOM, fill="x")
        pbackButton.pack(side=LEFT,expand = True, fill = BOTH)
        pnextButton.pack(ipadx=18, side=RIGHT,expand = True, fill = BOTH)
        pimageLabel.pack()

        currentStatus.forget()
        currentStatus = Label(pimageFrame, font="family", bg="light green", fg="black", text="Image " + str(imgPos + 1) + " of " + str(len(pimage_list)) + str("   "),
                              relief=SUNKEN, anchor=E)
        currentStatus.pack(side=BOTTOM, expand=True, fill=BOTH)



        return

    def back(imgPos1):
        global currentStatus
        global pimageLabel
        global pnextButton
        global pbackButton
        global pbottomFrame
        global pexitButton

        pbottomFrame.forget()
        pbottomFrame = tkinter.Frame(p, bg="grey", borderwidth=8, relief=SUNKEN)
        pimageLabel.forget()
        pimageLabel = Label(pimageFrame, image=pimage_list[imgPos1])

        pnextButton = Button(pbottomFrame,font= "verdana", text='NEXT', command=lambda: forward(imgPos1 + 1))
        pbackButton.forget()
        pbackButton = Button(pbottomFrame,bd= 5,font= "verdana", text="BACK", command=lambda: back(imgPos1 - 1))
        pexitButton = Button(pbottomFrame,bd= 5,font= "verdana", text="Exit ", command=p.quit)
        if imgPos1 == 0:
            pbackButton = Button(pbottomFrame,font= "verdana", text="back", state=DISABLED)

        pexitButton.pack(ipadx=15,side=BOTTOM,expand = True,fill = BOTH)
        pbottomFrame.pack(side=BOTTOM, fill="x")
        pbackButton.pack(side=LEFT,expand = True, fill = BOTH)
        pnextButton.pack(ipadx=18, side=RIGHT,expand = True, fill = BOTH)
        pimageLabel.pack()

        currentStatus.forget()
        currentStatus = Label(pimageFrame,font= "family",
                        text="Image " + str(imgPos1+1) + "of " + str(len(pimage_list)) + str("   "),
                        relief=SUNKEN, anchor=E)
        currentStatus.pack(side=BOTTOM, expand=True, fill=BOTH)

        return

    def gotoPublic():
        global e1
        e1.delete(0,END)
        p.destroy()
        r.deiconify()
        return
    def about():
        messagebox.showinfo("INFO", "This is a private gallery which is fully secured by strong password")
        return

    pleftFrame = tkinter.Frame(p,bg="#39FF14", borderwidth=6, relief=SUNKEN)
    pleftFrame.pack(side=LEFT, fill="y")
    pPublicButton = Button(pleftFrame,bg="light blue",fg="black",font= "algerian", text="Public Gallery",command = gotoPublic).pack(fill=X)
    pabout = Button(pleftFrame,bg="light blue",font= "family", text="About Private Gallery",command= about).pack(pady=10, fill=X)
    # ------------------------------------- PRIVATE IMAGE FRAME-------------------------------------------------------------------------------------------

    pimageFrame = Frame(p)
    pimageFrame.pack(side=TOP, fill=Y)
    pmy_img1 = ImageTk.PhotoImage(Image.open("P IMG 1.jpg"))
    pmy_img2 = ImageTk.PhotoImage(Image.open("P IMG 2.jpg"))

    pimage_list = [pmy_img1, pmy_img2]

    pimageLabel = Label(pimageFrame, image=pmy_img1)
    pimageLabel.pack()

    currentStatus = Label(pimageFrame, bg="light blue", font="family",
                          text="Image 1 of " + str(len(pimage_list)) + str("   "),
                          relief=SUNKEN, anchor=E)
    currentStatus.pack(side=BOTTOM, expand=True, fill=BOTH)

    # --------------------------------------BOTTOM FRAME-----------------------------------------------------------------------------------------
    pbottomFrame = tkinter.Frame(p, bg="grey", borderwidth=8, relief=SUNKEN)
    pbottomFrame.pack(side=BOTTOM, fill="x")
    pexitButton = Button(pbottomFrame,font= "verdana" ,text="Exit ", command=p.quit)
    pexitButton.pack(ipadx=15,side=BOTTOM,expand = True,fill = BOTH)
    pbackButton = Button(pbottomFrame,font= "verdana", text="BACK", command=back)
    pbackButton.pack(side=LEFT,expand = True, fill = BOTH)
    pnextButton = Button(pbottomFrame,font= "verdana", text="Next", command=lambda : forward(1))
    pnextButton.pack(ipadx=18, side=RIGHT,expand = True, fill = BOTH)
    p.mainloop()
    return

def passwdCheck():
    passwd=e1.get()
    z='123456'
    if passwd==z:
        PrivateGallery()
    else:
        e1.delete(0,END)
        messagebox.showerror("INFO","Incorrect Password !")
    return

def aboutus():
    a = tkinter.Tk()
    a.title("   Image Viewer")
    a.iconbitmap('favicon.ico')
    a.minsize(200,200)

    line1Label = Label(a,font= "algerian",text= " IMAGE VIEWER ").pack(


    )
    line2Label = Label(a,font= "algerian", text=" version 2.20.195.15 ").pack()
    line3Label = Label(a,font= "algerian",text=" copyright 2019-2020 Massive Dynamics Inc"
                                               ".").pack()
    return

def contactus():
    messagebox.showinfo("CONTACT US", "QUESTIONS ? NEED HELP ?"
                                      "Connect to us through Email:-technical.support@imageviewer.com call us:- 7470935655"
                        )
    return
#--------------------------------------LEFT FRAME------------------------------------------------------------------------------------------
leftFrame=tkinter.Frame(r,bg="light blue",borderwidth=6,relief = SUNKEN)
leftFrame.pack(side=LEFT,fill="y")
label=Label(leftFrame,bd= 5,font= "ALGERIAN",text="Private Gallery").pack(fill=X)
label1=Label(leftFrame,bd= 5,font= "family",text="Enter Password").pack(pady=2,fill=X)
e1= Entry(leftFrame,width=15,borderwidth=5)
e1.pack(pady=5,)
privateButton = Button(leftFrame,bd= 5,font= "verdana "
                       ,bg="white",text="submit",command=passwdCheck).pack(pady=0,fill=X)
aboutButton =  Button(leftFrame,bd= 5,bg="white",font= "Verdana",text="About",command=aboutus).pack(pady=10,fill=X)
contactUsButton =  Button(leftFrame,bg="white",bd= 5,font= "Verdana",text="Contact Us",command=contactus).pack(pady=5,fill=X)
#-------------------------------------IMAGE FRAME-------------------------------------------------------------------------------------------

imageFrame=Frame(r,bg="Moccasin")
imageFrame.pack(side=TOP,fill=Y)
my_img1 = ImageTk.PhotoImage(Image.open("IMG 1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("IMG 2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("IMG 3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("IMG 4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("IMG 5.jpg"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

status = Label(imageFrame,bg="#33FF00",fg="black",font= "family", text= "Image 1 of " +str(len(image_list))+str("   "),
               relief = SUNKEN,anchor=E)
status.pack(side = BOTTOM, expand = True, fill = BOTH)
imageLabel=Label(imageFrame,image=my_img1)
imageLabel.pack()

#--------------------------------------BOTTOM FRAME-----------------------------------------------------------------------------------------
bottomFrame = tkinter.Frame(r,bg="Moccasin",borderwidth=8,relief=SUNKEN)
bottomFrame.pack(side=BOTTOM,fill="x")
exitButton: None = Button(bottomFrame,bg="white",font= "Verdana",text= "Exit ",command = r.quit).pack(ipadx=15,side=BOTTOM,expand = True, fill = BOTH)
backButton = Button(bottomFrame,font= "Verdana",bg="white",text= "BACK",command=backward)
backButton.pack(side=LEFT ,expand = True, fill = BOTH)
nextButton = Button(bottomFrame,bg="white",font= "Verdana",text= "Next",command = lambda:nextImg(1))
nextButton.pack(ipadx=18,side=RIGHT, expand = True, fill = BOTH)

r.mainloop()