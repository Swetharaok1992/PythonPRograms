import tkinter as tk
import tkinter.messagebox as msg
import tkinter.colorchooser as clr
from tkinter import Toplevel

# This program implements the concept of MSPaint using Python tkinter (GUI programming)
class GetPointsDialog:
    DEFAULT_COLOR = 'black'
    v = 0

    def __init__(self, master, Wid_type):
        """
        This method opens coefficients window to get coefficients for Circle, Line and Rectangle and passes it to main window.
        """
        # Intialize all the variables needed for the coefficients window.
        self.X1cord = None
        self.X2cord = None
        self.Y1cord = None
        self.Y2cord = None
        self.radius = None
        self.wid = Wid_type
        self.rb1 = None
        self.rb2 = None
        self.v = tk.IntVar()
        self.coordinates_window = None
        self.color = None
        self.dashed = None

        if Wid_type is not None:
            # Design the labels and textboxes and radio buttons for the coefficients window.
            self.coordinates_window = Toplevel(master)
            self.coordinates_window.title("Enter Co-ordinate Points")
            self.coordinates_window.geometry("500x100")
            self.coordinates_window.transient(master)
            self.coordinates_window.grab_set()
            lb1 = tk.Label(self.coordinates_window, text='                 X1')
            lb1.grid(row=0)
            self.X1cord = tk.Entry(self.coordinates_window)
            self.X1cord.grid(row=0, column=1)
            lb2 = tk.Label(self.coordinates_window, text='                 Y1')
            lb2.grid(row=0, column=2)
            self.Y1cord = tk.Entry(self.coordinates_window)
            self.Y1cord.grid(row=0, column=3)
            self.rb1 = tk.Radiobutton(self.coordinates_window, text="Dashed", variable=self.v, value=1)
            self.rb1.grid(row=2, column=0)
            self.rb2 = tk.Radiobutton(self.coordinates_window, text="Un Dashed", variable=self.v, value=2)
            self.rb2.grid(row=2, column=1)
            color = tk.Button(self.coordinates_window, text="Color", command=self.choose_color)
            color.grid(row=2, column=2)
            submit = tk.Button(self.coordinates_window, text="Submit", command=self.submit)
            submit.grid(row=3, column=1)
            reset = tk.Button(self.coordinates_window, text="Reset", command=self.reset)
            reset.grid(row=3, column=6)
            # when window type is 'Circle' then display a different design and different window for line and rectangle
            if Wid_type == "circle":
                rad_la = tk.Label(self.coordinates_window, text='    Enter Radius')
                rad_la.grid(row=1)
                self.radius = tk.Entry(self.coordinates_window)
                self.radius.grid(row=1, column=1)
            elif Wid_type == "line" or Wid_type == "rec":
                lb3 = tk.Label(self.coordinates_window, text='                 X2')
                lb3.grid(row=1, column=0)
                self.X2cord = tk.Entry(self.coordinates_window)
                self.X2cord.grid(row=1, column=1)
                lb4 = tk.Label(self.coordinates_window, text='                 Y2')
                lb4.grid(row=1, column=2)
                self.Y2cord = tk.Entry(self.coordinates_window)
                self.Y2cord.grid(row=1, column=3)

    def choose_color(self):
        """
        SELECT THE COLOR FROM LIST OF COLOR'S AVAILABLE AND PASS THE COLOR TO MAIN WINDOW
        """
        global DEFAULT_COLOR
        self.get_color = clr.askcolor()
        # If color is not selected then set a default value to the color.
        if self.get_color[1] != "":
            self.color = self.get_color[1]
        else:
            self.color = DEFAULT_COLOR

    def submit(self):
        """
        IT SHOULD GET THE INPUT FROM USER AND SHOULD CHECK ALL THE CONDITIONS GIVEN FROM USER AND VALIDATE, ONCE VALUES ARE GOOD SEND VALUES TO MAIN CLASS ELSE RESET THE VALUES.
        """
        value = None
        #  Display error if there are no sufficient data.
        try:
            value = "X1"
            new_val = int(self.X1cord.get())
            value = "Y1"
            new_val = int(self.Y1cord.get())
            if self.v.get() == 0:
                msg.showinfo("Error", "Please select either dashed or un dashed", parent=self.coordinates_window)
            if self.wid == 'circle':
                value = "radius"
                new_val = int(self.radius.get())
                self.radius = int(self.radius.get())
            elif self.wid == "line" or self.wid == "rec":
                value = "X2"
                new_val = int(self.X2cord.get())
                value = "Y2"
                new_val = int(self.Y2cord.get())
                if int(self.X1cord.get()) < 50 or int(self.X2cord.get()) < 50 or int(self.X1cord.get()) > int(self.X2cord.get()) or int(self.Y1cord.get()) > int(self.Y2cord.get()):
                    raise ArithmeticError
                self.X2cord = int(self.X2cord.get())
                self.Y2cord = int(self.Y2cord.get())

            self.X1cord = int(self.X1cord.get())
            self.Y1cord = int(self.Y1cord.get())
            self.dashed = self.v.get()
            self.color = self.color
            self.coordinates_window.destroy()

        except ValueError:
            msg.showinfo("ValueError", "Coefficient's of " + str(value)+" can't be character or a Null", parent=self.coordinates_window )

        except ArithmeticError:
            msg.showinfo("Error", "Coefficient's of X1 or X2 can't be less than 50 or X1 < X2 or Y1< Y2", parent=self.coordinates_window )

    # Reset the values entered to empty on click of this buttom
    def reset(self):
        global v
        """
        SHOULD RESET THE VALUES IN THE ENTRY BOXES IF THERE ARE ANY ALPHANUMERIC ERRORS
        """
        self.v.set(0)
        self.X1cord.delete("0", tk.END)
        self.Y1cord.delete("0", tk.END)
        if self.wid == "circle":
            self.radius.delete("0", tk.END)
        elif self.wid == "line" or self.wid == "rec":
            self.X2cord.delete("0", tk.END)
            self.Y2cord.delete("0", tk.END)


class Painter:
    def __init__(self):
        """
        SHOULD INITIALISE ALL THE ROOT ATTRIBUTES FOR BASE WINDOW.
        CAN ADD ANY NUMBER OF ATTRIBUTES REQUIRED FOR THE PROGRAM
        """
        # Variables needed for the main window.
        self.start = None
        self.root = tk.Tk()
        self.root.title("Python Paint")
        self.root.geometry("800x800")
        self.enabled = False
        self.X1_CORD = 0
        self.Y1_CORD = 0
        self.radius = 0
        self.X2_CORD = 0
        self.Y2_CORD = 0
        self.color = None
        self.dashed = 0
        self.frm1 = None
        self.cnvs = None
        self.pen = None
        self.line = None
        self.circle = None
        self.call = None
        self.old_x = None
        self.old_y = None
        self.paint_Menu = tk.Menu(self.root)
        self.x = None
        self.y = None
        self.init_widgets()
        self.btn_type = None

    def init_widgets(self):
        """
        SHOULD DO THE BELOW LISTED OPERATIONS.
        """
        file = tk.Menu(self.paint_Menu, tearoff=0)
        options = tk.Menu(self.paint_Menu, tearoff=0)
        help_about = tk.Menu(self.paint_Menu, tearoff=0)
        self.paint_Menu.add_cascade(label="File", menu=file)
        self.paint_Menu.add_cascade(label="Options", menu=options)
        self.paint_Menu.add_cascade(label="Help", menu=help_about)
        file.add_command(label="New", command=self.create_New_Canvas)
        file.add_command(label="Save", command=self.save_canvas)
        file.add_separator()
        file.add_command(label="Exit", command=self.exit)
        options.add_command(label="Circle", command=lambda: self.Get_Cordinate_Points("circle"))
        options.add_command(label="Line", command=lambda: self.Get_Cordinate_Points("line"))
        options.add_command(label="Rectangle", command=lambda: self.Get_Cordinate_Points("rec"))
        options.add_separator()
        options.add_command(label="Clear All", command=self.clear_canvas)
        self.paint_Menu.entryconfig(2, state="disabled")
        help_about.add_command(label="About", command=self.show_help_about)
        self.root.config(menu=self.paint_Menu)
        self.pen = tk.Button(self.root, text='PEN', command=lambda: self.activate_button("PEN"))
        self.line = tk.Button(self.root, text='LINE', command=lambda: self.activate_button("LINE"))
        self.circle = tk.Button(self.root, text='CIRCLE', command=lambda: self.activate_button("CIRCLE"))
        self.pen.grid(row=0, column=0)
        self.line.grid(row=0, column=1)
        self.circle.grid(row=0, column=2)
        self.pen.config(state="disabled")
        self.line.config(state="disabled")
        self.circle.config(state="disabled")
        self.root.mainloop()
        # Adding Menu Bar TO BASE WINDOW

        # CREATE ALL MENUBAR'S

        # CREATE ALL SUB MENUS FOR MAIN MENU AND ACTIVATING DYNAMICALLY.

        # ADD BUTTONS TO THE MAIN WINDOW AND ACTIVATE THEM DYNAMICALLY

    def create_New_Canvas(self):
        """
        CREATE A NEW CANVAS OF SIZE 600x600 TO THE MAIN FRAME
        """
        self.frm1 = tk.Frame(self.root)
        self.frm1.grid(row=2, column=4, sticky=tk.S)
        self.cnvs = tk.Canvas(self.frm1, width=600, height=600, bg='white')
        self.cnvs.pack()
        self.enabled = True
        self.line.config(state='normal')
        self.pen.config(state='normal')
        self.circle.config(state='normal')
        self.enable_menu()

    def activate_button(self, Btn_Typ):
        """
        HANDLE THE BUTTONS ADDED ON THE FRAME FOR FREE PAINT BUTTONS
        """
        self.old_x = None
        self.old_y = None
        if Btn_Typ == "LINE":
            self.btn_type = "LINE"
            self.cnvs.bind('<Button-1>', self.line_click)
            self.cnvs.bind('<ButtonRelease-1>', self.button_released)
        elif Btn_Typ == "CIRCLE":
            self.btn_type = "CIRCLE"
            self.cnvs.bind("<ButtonPress-1>", self.Circle_Click)
            self.cnvs.bind("<ButtonRelease-1>", self.button_released)
        elif Btn_Typ == "PEN":
            self.btn_type = "PEN"
            self.cnvs.bind('<B1-Motion>', self.Brush)
            self.cnvs.bind('<ButtonRelease-1>', self.button_released)
        else:
            self.btn_type = None

    def button_released(self, event):
        """
        WHEN THE MOUSE BUTTON IS RELEASED SHOULD RESET THE CO-ORDINATES OF THE PREVIOUS BINDED VALUES.
        """
        if self.btn_type == "LINE":
            if self.start is not None:
                x = self.start[0]
                y = self.start[1]
                self.cnvs.create_line(x, y, event.x, event.y, fill="black", width=2)
                self.start = None
        elif self.btn_type == "PEN":
            self.old_x = None
            self.old_y = None
        elif self.btn_type == "CIRCLE":
            x0, y0 = (self.x, self.y)
            x1, y1 = (event.x, event.y)
            self.cnvs.create_oval(x0, y0, x1, y1, outline="black")

    def Brush(self, event):
        """
        CAN USE THE BELOW GIVEN CODE FOR BRUSH OR CAN MODIFY ACCORDING TO YOUR INITIASED ATTRIBUTES.
        """
        if self.btn_type == "PEN":
            if self.old_x is not None and self.old_y is not None:
                self.cnvs.create_line(self.old_x, self.old_y, event.x, event.y, width=2, capstyle=tk.BUTT, fill='black', splinesteps=50)
            self.old_x = event.x
            self.old_y = event.y

    def redraw(self):
        """
        SHOULD ABLE TO SAVE ALL THE PREVIOUS CO-ORDINATE VALUES FOR OVAL(CIRCLE), LINE
        """

    def line_click(self, event):
        """
        SHOULD ABLE TO HANDLE THE MOUSE CLICK EVENT AND PASS CO-ORDINATES TO THE CREATE_LINE EVENT FOR THE CANVASE AND PASS THE FILL COLOR AND SET WIDTH PROPERTIES AND SHOULD ABLE TO CLEAR THE PREVIOUS VALUES
        """
        self.start = (event.x, event.y)

    def Circle_Click(self, event):
        """
        SAME AS THE LINE-CLICK METHOD BUT SHOULD CREATE A OVAL HERE
        """
        self.x = event.x
        self.y = event.y

    def enable_menu(self):
        """
        THIS METHOD SHOULD BE ABLE TO HANDLE THE MENUBAR STATUS AND CONFIGURE TO NORMAL STATUS WHEN NEW BUTTON IS SELECTED
        """
        if self.enabled:
            self.enabled = False
            self.paint_Menu.entryconfigure(2, state="normal")
        else:
            self.enabled = False
            self.paint_Menu.entryconfigure(2, state=tk.DISABLED)
        pass

    def Get_Cordinate_Points(self, wid_typ):
        """
        CALL THE TOPLEVEL WINDOW FROM THIS METHOD, SHOULD GET THE CO-ORDINATES AND COLOR AND STRIKE/UNSTRIKE PROPERTIES AND DECIDE TO CALL THE Create_Circle OR Create_OR Create_Rect Line METHODS
        """
        self.call = GetPointsDialog(self.root, wid_typ)
        self.root.wait_window(self.call.coordinates_window)

        if wid_typ == "circle":
            self.Create_Circle(self.call.X1cord, self.call.Y1cord, self.call.radius, self.call.dashed, self.call.color)
        elif wid_typ == "line":
            self.Create_Line(self.call.X1cord, self.call.Y1cord, self.call.X2cord, self.call.Y2cord, self.call.dashed, self.call.color)
        else:
            self.Create_Rect(self.call.X1cord, self.call.Y1cord, self.call.X2cord, self.call.Y2cord, self.call.dashed, self.call.color)

    def Create_Circle(self, x1, y1, rad, Da_or_UDa, Colo):
        """
        CREATE CIRCLE ON THE CANVAS WITH THE CORDINATES AND VALUES RECEIVED FROM THE USER INPUT
        """
        if Da_or_UDa == 1:
            self.cnvs.create_oval(x1-rad, y1-rad, x1+rad, y1+rad, dash=(4, 2), outline=Colo)
        elif Da_or_UDa == 2:
            self.cnvs.create_oval(x1-rad, y1-rad, x1+rad, y1+rad, outline=Colo)

    def Create_Line(self, x1, y1, x2, y2, Da_or_UDa, Colo):
        """
        CREATE LINE ON THE CANVAS WITH THE CORDINATES AND VALUES RECEIVED FROM THE USER INPUT
        """
        if Da_or_UDa == 1:
            self.cnvs.create_line(x1, y1, x2, y2, dash=(4, 2), fill=Colo)
        elif Da_or_UDa == 2:
            self.cnvs.create_line(x1, y1, x2, y2, fill=Colo)

    def Create_Rect(self, x1, y1, x2, y2, Da_or_UDa, Colo):
        """
        CREATE RECTANGE ON THE CANVAS WITH THE CORDINATES AND VALUES RECEIVED FROM THE USER INPUT
        """
        if Da_or_UDa == 1:
            self.cnvs.create_rectangle(x1, y1, x2, y2, dash=(4, 2), outline=Colo)
        elif Da_or_UDa == 2:
            self.cnvs.create_rectangle(x1, y1, x2, y2, outline=Colo)

    def clear_canvas(self):
        """
        triggered when the menu command 'Clear' is clicked
        delete everything from the canvas and set the coefficients to 0's
        """
        try:
            self.call.X1cord = None
            self.call.Y1cord = None
            self.call.dashed = None
            self.call.color = None
            self.call.radius = None
            self.call.X2cord = None
            self.call.Y2cord = None
            self.call = None
            self.cnvs.delete(tk.ALL)
        except AttributeError:
            self.cnvs.delete(tk.ALL)

    def save_canvas(self):
        """
        triggered when the menu command 'Save plot as .PS' is clicked
        save the graph as '{your_student_id_number}.ps'
        """
        try:
            if self.cnvs.find_all() != ():
                self.cnvs.postscript(file="1004265.ps")
                msg.showinfo("Saved", "Canvas saved.")
            else:
                msg.showinfo("Not Saved", "Canvas is Empty. There is nothing to save.")
        except AttributeError:
            msg.showinfo("Not Saved", "Nothing to save. Create new canvas.")

    def show_help_about(self):
        """
        triggered when the menu command 'About' is clicked
        Show an information dialog displaying your name on one line and id number on the second
        """
        msg.showinfo("About PY Paint", "Created by: Swetha Krishnamurthy Rao \n ID: 1004265")
        pass

    def exit(self):
        """
        triggered when the menu command 'Exit' is clicked
        Ask if the user is sure about exiting the application and if the answer is yes then quit the main window
        """
        button_chosen = msg.askquestion("Exit", "Are you sure?", icon='warning')
        if button_chosen == 'yes':
            self.root.destroy()
        else:
            return

p = Painter()
