from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from PIL import ImageTk, Image
from operations import detectText, getImagePath, copyText, saveFile, toDoc

def showGUI():
    root = Tk()

    # Centering
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width/2) - (800/2)
    y = (screen_height/2) - (600/2)

    # Root window customization
    favicon= PhotoImage(file='D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\Images\ocrfavicon.png')

    root.iconphoto(False,favicon)
    root.title("OCR to Document")
    root.geometry(f'800x600+{int(x)}+{int(y)}')
    root.resizable(False,False)

    detectedText = StringVar()
    bgImage = Image.open('D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\GUI\\background.png')
    background = ImageTk.PhotoImage(bgImage)

    # Canvas
    canvas = Canvas(
        root,
        bg = "#d1b342",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge",
    )
    canvas.place(x=0,y=0)

    canvas.create_image(0,0,image=background,anchor=NW)



    # Image Selector Field
    imagePathText = StringVar()
    imagePathText.set("")
    imagePath = Entry(font=("Tahoma",14),relief="groove",borderwidth=0,highlightthickness=0,bg="#eeeeee",textvariable=imagePathText)
    imagePath.place(x=50,y=310,width=460,height=32)

    # Image Selector Button
    chooseImgIcon = PhotoImage(file=f"D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\GUI\img0.png")
    def chooseImage():
        imagePathText.set(getImagePath())

    imageSelector = Button(
        image=chooseImgIcon,
        borderwidth=0,
        highlightthickness=0,
        relief="groove",
        border=0,
        cursor="hand2",
        command=chooseImage
    )
    imageSelector.place(
        x=530,
        y=310,
        width=100,
        height=32
    )


    # Scan
    def scan():
        if imagePathText.get() == "":
            messagebox.showerror("Error","Invalid path! Please enter a correct path of an image.")
            return
        try:
            detectedText.set(detectText(imagePathText.get()))
        except:
            messagebox.showerror("Error","Invalid path! Please enter a correct path of an image.")
            return

        messagebox.showinfo("Success","Text successfully detected!")


    scanImageIcon = PhotoImage(file=f"D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\GUI\img1.png")
    scanButton = Button(
        image=scanImageIcon,
        borderwidth=0,
        highlightthickness=0,
        relief="groove",
        cursor="hand2",
        command=scan
    )
    scanButton.place(
        x=650,
        y=310,
        width=100,
        height=32
    )


    # Copy Text
    def copyToClipboard():
        copyText(detectedText.get())


    copyTextImageIcon = PhotoImage(file=f"D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\GUI\img2.png")
    copyTextImageIconHover = PhotoImage(file=f"D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\GUI\img2hover.png")

    copyTextButton = Button(
        image=copyTextImageIcon,
        borderwidth=0,
        highlightthickness=0,
        relief="groove",
        cursor="hand2",
        command=copyToClipboard
    )
    copyTextButton.place(
        x=50,
        y=414,
        width=205.88,
        height=65.88
    )

    #Hover Effects
    def Copyon_enter(e):
        copyTextButton['image'] = copyTextImageIconHover

    def Copyon_leave(e):
        copyTextButton['image'] = copyTextImageIcon

    copyTextButton.bind("<Enter>",Copyon_enter)
    copyTextButton.bind("<Leave>",Copyon_leave)



    # Save Text
    def saveTextFile():
        saveFile(detectedText.get())


    saveTextImageIcon= PhotoImage(file=f"D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\GUI\img3.png")
    saveTextImageIconHover= PhotoImage(file=f"D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\GUI\img3hover.png")

    saveTextButton = Button(
        image=saveTextImageIcon,
        borderwidth=0,
        highlightthickness=0,
        relief="groove",
        cursor="hand2",
        command=saveTextFile
    )
    saveTextButton.place(
        x=297,
        y=414,
        width=205.88,
        height=65.88
    )

    #Hover Effects
    def Saveon_enter(e):
        saveTextButton['image'] = saveTextImageIconHover

    def Saveon_leave(e):
        saveTextButton['image'] = saveTextImageIcon

    saveTextButton.bind("<Enter>",Saveon_enter)
    saveTextButton.bind("<Leave>",Saveon_leave)


    # to Doc
    def toDocument():
        toDoc(detectedText.get())

    toDocImageIcon = PhotoImage(file=f"D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\GUI\img4.png")
    toDocImageIconHover = PhotoImage(file=f"D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\GUI\img4hover.png")


    toDocButton = Button(
        image=toDocImageIcon,
        borderwidth=0,
        highlightthickness=0,
        relief="groove",
        cursor="hand2",
        command=toDocument
    )
    toDocButton.place(
        x=544,
        y=414,
        width=205.88,
        height=65.88
    )

    #Hover Effects
    def toDocon_enter(e):
        toDocButton['image'] = toDocImageIconHover

    def ToDocon_leave(e):
        toDocButton['image'] = toDocImageIcon

    toDocButton.bind("<Enter>",toDocon_enter)
    toDocButton.bind("<Leave>",ToDocon_leave)

    root.mainloop()