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
from calorie import CounterApp

def main():
    #Set default application with title, window size and icon
    root = Tk()
    root.iconbitmap(default = 'favicon.ico')
    root.title("Calorie Counter")
    root.geometry("440x300")

    app = CounterApp(root)

    initial_menubar = Menu(root)
    menubar = app.makeMenuBar(root, initial_menubar)

    root.mainloop()


if __name__ == '__main__':
    main()
