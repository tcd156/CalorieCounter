# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


from Tkinter import *
import caloriefunctions


class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)
        master.rowconfigure(2, weight=1)


    def setTextBoxState(self, message):
        """
        This sets the default text box state to being read-only after applying
        'message'
        """
        self.textBox_txt.config(state = NORMAL)
        self.textBox_txt.delete(0.0, END)
        self.textBox_txt.insert(0.0, message)
        self.textBox_txt.config(state = DISABLED)


    def checkDogType(self, dog_type, dog_weight, weight_needs):
        """
        Checks against radio buttons for 'neutered' or 'intact' for dog_type
        """
        default_weight_needs = ['Stay current weight', 'Select weight needs:']

        if dog_type == "neutered" and weight_needs in default_weight_needs:
            calories_needed = caloriefunctions.neuteredAdult(dog_weight)
            
            message = "The dog should be eating %d calories per day" %(calories_needed) + " to stay at the current weight."
            self.setTextBoxState(message)

        elif dog_type == "intact" and weight_needs in default_weight_needs:   
            calories_needed = caloriefunctions.intactAdult(dog_weight)
            
            message = "The dog should be eating %d calories per day" %(calories_needed) + " to stay at the current weight."
            self.setTextBoxState(message)

        elif dog_type == 'intact':
            self.checkDogWeightNeeds(dog_type, dog_weight, weight_needs)

        elif dog_type == 'neutered':
            self.checkDogWeightNeeds(dog_type, dog_weight, weight_needs)


    def checkDogWeightNeeds(self, dog_type, dog_weight, weight_needs):
        """
        Checks against option box for weight_needs
        """
        if weight_needs == "Lose weight":
            calories_needed = caloriefunctions.weightLoss(dog_weight)
            message = "The dog should be eating %d calories per day" %(calories_needed) + " to lose weight."

            self.setTextBoxState(message)

        elif weight_needs == "Gain weight" and dog_type == 'intact':
            min_cal, max_cal = caloriefunctions.weightGainIntact(dog_weight)
            message = "The dog should be eating between %d - %d calories per day to gain weight." %(min_cal, max_cal)
            
            self.setTextBoxState(message)

        elif weight_needs == "Gain weight" and dog_type == 'neutered':
            min_cal, max_cal = caloriefunctions.weightGainNeutered(dog_weight)
            message = "The dog should be eating between %d - %d calories per day to gain weight." %(min_cal, max_cal)
            
            self.setTextBoxState(message)


    def findRER(self, *args):
        """
        This calculates the calorie requirements based on input given from 
        the user
        """
        weight = self.rer_ent.get()
        checked_dog_weight = caloriefunctions.convertToFloat(weight)

        dog_type_choice = self.choice.get()

        weight_needs = self.original.get()

        if checked_dog_weight and (weight > 0):
            self.checkDogType(dog_type_choice, checked_dog_weight, weight_needs)
        else:
            message = "Please check your entry."

            self.setTextBoxState(message)


    def createWidgets(self):
        """
        Creates widgets for the frame
        """    
        #Label for text entry for weight
        self.rer_lbl = Label(self, text = "Weight:")
        self.rer_lbl.grid(row = 2, column = 0, sticky = "e")
        
        #Submit button
        self.submit_bttn = Button(self, text = "Submit", command = self.findRER)
        self.submit_bttn.grid(row = 2, column = 2, sticky = "")

        #Entry text box
        self.rer_ent = Entry(self)
        self.rer_ent.grid(row = 2, column = 1, sticky = "nsew", pady = 10)
        self.rer_ent.bind('<Return>', self.findRER)
        self.rer_ent.focus_set()

        #Display Text box
        self.textBox_txt = Text(self, width = 35, height = 4, wrap = WORD)
        self.textBox_txt.grid(row = 4, column = 1, columnspan = 2, sticky = "nsew")

        #set default instructions in text box
        message = "Please enter a weight in pounds, select whether the animal is intact or neutered, and select it's weight needs."

        self.setTextBoxState(message)

        #create variable to hold for radio buttons
        self.choice = StringVar()
        self.choice.set('neutered')

        #radio button for 'intact'
        Radiobutton(self, text = "Intact", variable = self.choice, value = 'intact').grid(row = 1, column = 1, 
            sticky = "w", padx = 0, pady = 10)

        #radio button for 'neutered'
        Radiobutton(self, text = "Neutered", variable = self.choice, value = 'neutered').grid(row = 1, column = 0, 
            sticky = "w", padx = 15)

        #set variable to initialize option box
        self.original = StringVar()
        self.original.set('Select weight needs:')

        #option box for 'weight needs'
        self.option_box = OptionMenu(self, self.original, 
            'Stay current weight',
            'Lose weight', 'Gain weight')
        self.option_box.grid(row = 1, column = 2, sticky = 'e')
        self.option_box.config(height = 1, width = 20)


def aboutPopUp(root):
    """
    Pop up dialog for About menu in menu bar
    """
    about = Toplevel(takefocus = True)
    about.geometry("250x150")
    about.transient(master = root)
    about.title("About Calorie Counter")
    about_message = "\nCalorie Counter - ALPHA - Version: 0.1" + "\nWritten by: Tyler Dennis & Allie Alvey\n" + "\n Contact: tcd156@hotmail.com\n"

    about_msg = Label(about, text=about_message)
    about_msg.pack(side = "top", fill = "both", expand = 1)

    button = Button(about, text = "Dismiss", command = about.destroy, pady = 10)
    button.pack()


    #about.wait_window()

def makeMenuBar(root, menubar):
    """
    Basic menu bar creation
    """
    filemenu = Menu(menubar, tearoff = 0)
    filemenu.add_command(label = "Exit", command = root.quit)
    menubar.add_cascade(label = "File", menu = filemenu)
    
    aboutmenu = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = "About", menu = aboutmenu)
    aboutmenu.add_command(label = "About Calorie Counter", command = lambda: aboutPopUp(root))
    root.config(menu = menubar)


def main():
    #Set default application with title, window size and icon
    root = Tk()
    root.iconbitmap(default = 'favicon.ico')
    root.title("Calorie Counter")
    root.geometry("440x300")

    #Create a menu bar for app

    app = Application(root)

    initial_menubar = Menu(root)
    menubar = makeMenuBar(root, initial_menubar)

    root.mainloop()


if __name__ == '__main__':
    main()
