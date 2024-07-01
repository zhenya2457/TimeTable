from tkinter import *
masterWindow = Tk()


screen_width = masterWindow.winfo_screenwidth()
#Main Window min width
self.window_width = screen_width * .01
self.window_height = screen_height * .04

#Window startst in center of screen
self.window_start_x = (screen_width/2)
self.window_start_y = (screen_height/2)
masterWindow.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height, self.window_start_x, self.window_start_y))
self.buttonsFrame.pack(side = TOP)
button_width = 13
button_height = 2

#A simple dict that stores script name strings
for script in SCRIPTS.keys():
    #Remove script extension
    script_name = script.split(".")[0]
    button_width = 13
    button_height = 2
    BUTTONS[script] = Button(self.buttonsFrame, text = script, width = button_width, height = button_height, justify = LEFT, wraplength = 100, command = lambda s = script: self.runScript(s))
    BUTTONS[script].grid(row = self.row, column = self.col)
    self.update()

    #Increment row and col and set new window size
    if self.col == 2:
        self.col = 0
        self.row += 1
        reached_max_width = True
    else:
        self.col += 1
        if not reached_max_width:
            self.window_width += button_width * 13
    self.window_height = self.buttonsFrame.winfo_height() * (self.row*3)
    masterWindow.geometry("%dx%d" % (self.window_width, self.window_height))


def runScript(self, script):
    print(script)