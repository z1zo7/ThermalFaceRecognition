import Window1
import Window2
from connect import *


def window3():
    historyWindow = Tk()
    historyWindow.geometry('%dx%d+%d+%d' % (665, 712, 450, 60))
    historyWindow.title("Face Recognition")
    historyWindow.resizable(False, False)
    historyWindow.configure(bg=BG)
    # Icon

    iWindow = ImageTk.PhotoImage((Image.open(r'_internal\Images\\face-id-30.png')))
    historyWindow.iconphoto(False, iWindow)

    # Icon
    iWindow = ImageTk.PhotoImage(Image.open(r'_internal\\Images\\face-id-30.png'))
    historyWindow.iconphoto(False, iWindow)

    # Create Frames
    fTitle = Frame(historyWindow, width=665, height=68, bg="#478CF3")
    fTitle.pack(side=TOP, fill=X)

    # Create Labels
    lblTitle = Label(fTitle, text="History", justify=CENTER, font=("Arial", 20), bg="#478CF3", fg=FC)
    lblTitle.place(relx=0.5, rely=0.5, anchor="center")

    def backAction():
        historyWindow.destroy()
        Window2.window2()

#-------------------- Hoveres -----------------------------
    def hoverIconBack(e):
        lblIconBack.config(text="Go Back", bg="#FFFFFF")
        lblIconBack.place(x=0, y=49)

    def leaveIconBack(e):
        lblIconBack.place_forget()
# -------------- End --------------

    def homeAction():
        historyWindow.destroy()
        Window1.window1()

#-------------------- Hoveres -----------------------------
    def hoverIconHome(e):
        lblIconHome.config(text="Home", bg="#FFFFFF")
        lblIconHome.place(x=30, y=49)

    def leaveIconHome(e):
        lblIconHome.place_forget()
# -------------- End --------------

    def forwardAction():
        return

#-------------------- Hoveres -----------------------------
    def hoverIconForward(e):
        lblIconForward.config(text="Go Forward", bg="#FFFFFF")
        lblIconForward.place(x=60, y=49)

    def leaveIconForward(e):
        lblIconForward.place_forget()
# -------------- End --------------

    # Create Buttons
    iconImageBack = ImageTk.PhotoImage(Image.open(r'_internal\\Images\W-back-30.png'))
    iconBack = Button(fTitle, image=iconImageBack, borderwidth=0, cursor="hand2", bg="#478CF3", command=backAction,activebackground='#5294f7')
    iconBack.place(x=0)
    iconBack.bind("<Enter>", hoverIconBack)
    iconBack.bind("<Leave>", leaveIconBack)

    iconImageHome = ImageTk.PhotoImage(Image.open(r'_internal\\Images\W-home-30.png'))
    iconhome = Button(fTitle, image=iconImageHome, borderwidth=0, cursor="hand2", bg="#478CF3", command=homeAction,activebackground='#5294f7')
    iconhome.place(x=30)
    iconhome.bind("<Enter>", hoverIconHome)
    iconhome.bind("<Leave>", leaveIconHome)

    iIconForward = ImageTk.PhotoImage(Image.open(r'_internal\Images\off-forward-30.png'))
    iconForward = Button(fTitle, image=iIconForward, bg="#478CF3", borderwidth=0, cursor="hand2", command=forwardAction,activebackground="#478CF3")
    iconForward.place(x=60)
    iconForward.bind("<Enter>", hoverIconForward)
    iconForward.bind("<Leave>", leaveIconForward)
# -------------- End --------------
    # ------ Create Labels ------
    lblIconBack = Label(historyWindow, text="", bg="#478CF3")
    lblIconHome = Label(historyWindow, text="", bg="#478CF3")
    lblIconForward = Label(historyWindow, text="", bg="#478CF3")

    # Frame for the table
    table_frame_container = Frame(historyWindow, bg=BG, bd=2, relief=SOLID, width="665")
    table_frame_container.pack(fill=BOTH, expand=True)

    # Table
    table_frame = Frame(table_frame_container, bg=BG)
    table_frame.pack(fill=BOTH, expand=True)

    canvas = Canvas(table_frame, bg=BG)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar_y = Scrollbar(table_frame, orient=VERTICAL, command=canvas.yview, bg=BG)
    scrollbar_y.pack(side=RIGHT, fill=Y)

    scrollbar_x = Scrollbar(table_frame_container, orient=HORIZONTAL, command=canvas.xview, bg=BG)
    scrollbar_x.pack(side=BOTTOM, fill=X)

    canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    image_table_frame = Frame(canvas, bg=BG)
    canvas.create_window((0, 0), window=image_table_frame, anchor=NW)

    # Variables to keep track of images and count
    image_info = []
    image_count = 0

    add_image(image_table_frame, canvas, image_info, image_count)

    historyWindow.mainloop()


# Function to add images to the table
def add_image(imageTableFrame, canvas, imageInfo, imageCount):
    # Establish the database connection
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()

    # Execute SQL query

    query = f'SELECT * FROM {tableName}'
    cursor.execute(query)

    # Fetch the results
    rows = cursor.fetchall()

    for row in rows:
        image = row.Images
        image = io.BytesIO(image)           # Convert Byte Array To ByteIO
        photo = ImageTk.PhotoImage(Image.open(image).resize((270, 250)))
        label = Label(imageTableFrame, image=photo)
        label.imageR = photo  # Keep a reference to the image object

        # -----------------------------------
        name = row.Name
        nameLabel = Label(imageTableFrame, text=name, bg=BG, fg=FC)
        # -----------------------------------
        date = row.Date
        DateLabel = Label(imageTableFrame, text=date, bg=BG, fg=FC)

        imageCount += 1
        indexLabel = Label(imageTableFrame, text=str(imageCount), bg=BG, fg=FC)

        imageInfo.insert(0, (indexLabel, label, nameLabel, DateLabel))

    # Update the GUI
    updateImagePositions(imageInfo)
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Close cursor and connection
    cursor.close()
    conn.close()


# Function to update the positions of images in the table
def updateImagePositions(imageInfo):
    for widgetRow in imageInfo:
        for widget in widgetRow:
            widget.grid_forget()

    for i, (indexLabel, label, nameLabel, timeLabel) in enumerate(imageInfo, start=1):
        indexLabel.grid(row=i, column=0, columnspan=4, padx=25, pady=5, sticky=W)
        label.grid(row=i, column=4, padx=25, columnspan=4, pady=5, sticky=W)
        nameLabel.grid(row=i, column=8, columnspan=4, padx=25, pady=5, sticky=W)
        timeLabel.grid(row=i, column=12, columnspan=4, padx=25, pady=5, sticky=W)

# window3()

