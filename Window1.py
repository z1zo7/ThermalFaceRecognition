# --------- Libraries ---------
from library import *
import Window2
import Window3

# # Creating Windows
def window1():
    dashboardWindow = Tk()
    dashboardWindow.geometry('%dx%d+%d+%d' % (665, 712, 450, 60))
    dashboardWindow.title("Face Recognition")
    dashboardWindow.resizable(False, False)
    dashboardWindow.configure(bg=BG)
    # Icon

    iWindow = ImageTk.PhotoImage((Image.open(r'_internal\Images\\face-id-30.png')))
    dashboardWindow.iconphoto(False, iWindow)
    Button_help = True

    # Comand Buttons
    def helpAction():
        global Button_help
        if Button_help:

            lblImageAdd.config(image=iconImageAdd, bg=BG)
            lblImageAdd.grid(row=3, column=0)
            lblAdd.configure(text="---> Add Image To Recognize ", font=20, bg=BG, fg=FC)
            lblAdd.grid(row=3, column=1)

            lblImageHistory.config(image=iconImageHistory, bg=BG)
            lblImageHistory.grid(row=4, column=0)
            lblHistory.configure(text="---> Check Recognition History ", font=20, bg=BG, fg=FC)
            lblHistory.grid(row=4, column=1)
            Button_help = False

        else:
            lblImageAdd.grid_remove()
            lblAdd.grid_remove()
            lblImageHistory.grid_remove()
            lblHistory.grid_remove()

            Button_help = True

    #-------------------- Hoveres -----------------------------
    def hoverIconHelp(e):
        lblIconHelp.config(text="Help..?", bg="#FFFFFF")
        lblIconHelp.place(x=100, y=480)

    def leaveIconHelp(e):
        lblIconHelp.place_forget()
# -------------- End --------------

    def addAction():
        dashboardWindow.destroy()
        Window2.window2()
    #-------------------- Hoveres -----------------------------
    def hoverIconAdd(e):
        lblIconAdd.config(text="Add Image", bg="#FFFFFF")
        lblIconAdd.place(x=300, y=480)

    def leaveIconAdd(e):
        lblIconAdd.place_forget()
# -------------- End --------------
    def historyAction():
        dashboardWindow.destroy()
        Window3.window3()
    #-------------------- Hoveres -----------------------------
    def hoverIconHistory(e):
        lblIconHistory.config(text="History", bg="#FFFFFF")
        lblIconHistory.place(x=525, y=480)

    def leaveIconHistory(e):
        lblIconHistory.place_forget()
# -------------- End --------------

    # Creating Widgets
    # Create Images
    iDashboard = Image.open('_internal\Images\Dashboard.jpg')
    iDashboard = iDashboard.resize((626, 353))
    iDashboard = ImageTk.PhotoImage(iDashboard)

    iHelp = Image.open('_internal\Images\help-50.png')
    iconImageHelp = ImageTk.PhotoImage(iHelp)

    iAdd = Image.open('_internal\Images\\add-50.png')
    iconImageAdd = ImageTk.PhotoImage(iAdd)

    iHistory = Image.open('_internal\Images\database-50.png')
    iconImageHistory = ImageTk.PhotoImage(iHistory)
    # ---------- END -----------

    # Create Labels
    lblImageDashboard = Label(image=iDashboard)
    lblIconAdd = Label(dashboardWindow, text="")
    lblIconHistory = Label(dashboardWindow, text="")
    lblIconHelp = Label(dashboardWindow, text="")

    lblAdd = Label(dashboardWindow)
    lblImageAdd = Label(dashboardWindow)
    lblHistory = Label(dashboardWindow)
    lblImageHistory = Label(dashboardWindow)

    # ---------- END -----------

    # Create Buttons

    iconHelp = Button(dashboardWindow, image=iconImageHelp, bg=BG, borderwidth=0, cursor="hand2", command=helpAction, activebackground='#61677a')
    iconHelp.bind("<Enter>", hoverIconHelp)
    iconHelp.bind("<Leave>", leaveIconHelp)

    iconAdd = Button(dashboardWindow, image=iconImageAdd, bg=BG, borderwidth=0, cursor="hand2", command=addAction, activebackground='#61677a')
    iconAdd.bind("<Enter>", hoverIconAdd)
    iconAdd.bind("<Leave>", leaveIconAdd)

    iconHistory = Button(dashboardWindow, image=iconImageHistory, bg=BG, borderwidth=0, cursor="hand2",command=historyAction, activebackground='#61677a')
    iconHistory.bind("<Enter>", hoverIconHistory)
    iconHistory.bind("<Leave>", leaveIconHistory)

    # ---------- END -----------
    # Placing Widgets On Screen
    lblImageDashboard.grid(row=0, column=0, columnspan=3, padx=15, pady=20)
    iconHelp.grid(row=1, column=0, pady=20)
    iconAdd.grid(row=1, column=1)
    iconHistory.grid(row=1, column=2)
    # ---------- END -----------

    # Super Loop
    dashboardWindow.mainloop()

# window1()

