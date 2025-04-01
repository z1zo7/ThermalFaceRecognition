from library import *
import Window1
import Window3
from connect import *
from test import *


def window2():
    # Creating Add Windows
    addWindow = Tk()
    addWindow.geometry('%dx%d+%d+%d' % (665, 712, 450, 60))
    addWindow.title("Face Recognition")
    addWindow.resizable(False, False)
    addWindow.configure(bg=BG)
    # Icon
    iWindow = ImageTk.PhotoImage((Image.open(r'_internal\Images\\face-id-30.png')))
    addWindow.iconphoto(False, iWindow)
    Button_mode
    Button_help

    # Command Buttons
    def backAction():
        addWindow.destroy()
        Window1.window1()

#-------------------- Hoveres -----------------------------
    def hoverIconBack(e):
        lblIconBack.config(text="Go Back", bg="#FFFFFF")
        lblIconBack.place(x=0, y=30)

    def leaveIconBack(e):
        lblIconBack.place_forget()
#-------------------- Hoveres -----------------------------

    def helpAction():
        global Button_help
        if Button_help == True:
            lblHelpAddImage.configure(text="If click on this icon adds image but this image\n extension is .bmp",bg="#FFFFFF")
            lblHelpAddImage.place(x=30, y=300)
            lblHelpRecognition.configure(text="If click on this icon recognizes the image that added ", bg="#FFFFFF")
            lblHelpRecognition.place(x=30, y=550)
            Button_help = False
        else:
            lblHelpAddImage.place_forget()
            lblHelpRecognition.place_forget()
            Button_help = True
    #-------------------- Hoveres -----------------------------
    def hoverIconHelp(e):
        lblIconHelp.config(text="Help..?", bg="#FFFFFF")
        lblIconHelp.place(x=30, y=30)

    def leaveIconHelp(e):
        lblIconHelp.place_forget()
# -------------- End --------------

    def forwardAction():
        addWindow.destroy()
        Window3.window3()

#-------------------- Hoveres -----------------------------
    def hoverIconForward(e):
        lblIconForward.config(text="Go Forward", bg="#FFFFFF")
        lblIconForward.place(x=60, y=30)
# -------------- End --------------
    def leaveIconForward(e):
        lblIconForward.place_forget()

    def addImage():
        global myImage
        global imagePath

        for filename in os.listdir("test_images"):
            os.remove(os.path.join("test_images", filename))
            print(f"Deleted image: {filename}")

        for filename in os.listdir("cropped_image"):
            os.remove(os.path.join("cropped_image", filename))
            print(f"Deleted image: {filename}")

        imagePath = filedialog.askopenfilename(initialdir="/", title="Select An Image", filetypes=(
            ("Image Files", "*.bmp"), ("png Images", "*.png"), ("jpg Images", "*.jpg")))

        if imagePath.lower().split(".")[-1] =='bmp' or 'png':
            try:
                myImage = ImageTk.PhotoImage(Image.open(imagePath).resize((299, 250)))
                ImageAdd.config(image=myImage)
                copy_image(imagePath, r"test_images")
            except Exception as e:
                print("Error displaying image:", e)
        else:
            messagebox.showerror("ERROR", "Please Put An Image (.bmp)")
        
#-------------------- Hoveres -----------------------------
    def hoverIconAdd(e):
        lblIconAdd.config(text="Add Image", bg="#FFFFFF")
        lblIconAdd.place(x=30, y=300)

    def leaveIconAdd(e):
        lblIconAdd.place_forget()
# -------------- End --------------

    def recognitionAction():

        if imagePath.lower().split(".")[-1] =='bmp':
        # ---------------- Model ------------------
            faceName = testImages()
            lblRecognition.config(text=faceName)
            try:
                newImage = r"cropped_image\\newImage.bmp"
                image = Image.open(newImage)
                image = image.resize((299, 210))  # Resize if necessary
                photo = ImageTk.PhotoImage(image)
                labelImageRecognition.config(image=photo)
                labelImageRecognition.image = photo  # Keep a reference to avoid garbage collection
            except Exception as e:
                print("Error displaying cropped image:", e)

        # ----------- Database ------------------
            currentDate = datetime.now().strftime("%Y-%m-%d")
            updateDatabase(newImage, faceName, currentDate)
            delete_images(r"test_images")
        else:
            messagebox.showerror("ERROR", "Please Click On Add Image To Select Your Face Image")

    #-------------------- Hoveres -----------------------------
    def hoverIconRecognition(e):
        lblIconRecognition.config(text="Recognition", bg="#FFFFFF")
        lblIconRecognition.place(x=50, y=550)

    def leaveIconRecognition(e):
        lblIconRecognition.place_forget()

    # -------------- End --------------

    # Creating Widgets
    # Create Images
    image1 = Image.open('_internal\Images\image1.png')
    image1 = image1.resize((299, 250))
    imageAdd = ImageTk.PhotoImage(image1)

    image2 = Image.open('_internal\Images\image2.jpg')
    image2 = image2.resize((299, 210))
    ImageRecognition = ImageTk.PhotoImage(image2)

    # ---------- END -----------

    # Create Labels
    ImageAdd = Label(addWindow, image=imageAdd)
    ImageAdd.place(x=320, y=130)

    labelImageRecognition = Label(addWindow, image=ImageRecognition)
    labelImageRecognition.place(x=320, y=400)

    lblRecognition = Label(addWindow, text="------", font=10, bg=FC, width=20, borderwidth=0)
    lblRecognition.place(x=359, y=630)

    lblIconHelp = Label(addWindow, text="")
    lblIconAdd = Label(addWindow, text="")
    lblIconRecognition = Label(addWindow, text="")
    lblIconBack = Label(addWindow, text="")
    lblIconForward = Label(addWindow, text="")
    lblHelpRecognition = Label(addWindow)
    lblHelpAddImage = Label(addWindow)

    # -------------- End --------------

    # Create Buttons 
    iIconBack = ImageTk.PhotoImage(Image.open(r'_internal\Images\back-30.png'))
    iconBack = Button(addWindow, image=iIconBack, bg=BG, borderwidth=0, cursor="hand2", command=backAction,activebackground='#61677a')
    iconBack.place(x=0)
    iconBack.bind("<Enter>", hoverIconBack)
    iconBack.bind("<Leave>", leaveIconBack)

    iIconHelp = ImageTk.PhotoImage(Image.open(r'_internal\Images\help-30.png'))
    iconHelp = Button(addWindow, image=iIconHelp, bg=BG, borderwidth=0, cursor="hand2", command=helpAction,activebackground='#61677a')
    iconHelp.place(x=30)
    iconHelp.bind("<Enter>", hoverIconHelp)
    iconHelp.bind("<Leave>", leaveIconHelp)

    iIconForward = ImageTk.PhotoImage(Image.open(r'_internal\Images\forward-30.png'))
    iconForward = Button(addWindow, image=iIconForward, bg=BG, borderwidth=0, cursor="hand2", command=forwardAction,activebackground='#61677a')
    iconForward.place(x=60)
    iconForward.bind("<Enter>", hoverIconForward)
    iconForward.bind("<Leave>", leaveIconForward)

    iIconAdd = ImageTk.PhotoImage(Image.open(r'_internal\Images\imageAdd.png'))
    iconAdd = Button(addWindow, image=iIconAdd, bg=BG, cursor="hand2", command=addImage, borderwidth=0,activebackground='#61677a')
    iconAdd.place(x=30, y=200)
    iconAdd.bind("<Enter>", hoverIconAdd)
    iconAdd.bind("<Leave>", leaveIconAdd)

    btnStart = Button(addWindow, text="Start", bg='#61677a', fg=FC, width=10, font=16, cursor="hand2",command=recognitionAction, activebackground="#478CF3")
    btnStart.place(x=30, y=500)
    btnStart.bind("<Enter>", hoverIconRecognition)
    btnStart.bind("<Leave>", leaveIconRecognition)
    # ---------- END -----------



    # Super Loop
    addWindow.mainloop()

# window2()


