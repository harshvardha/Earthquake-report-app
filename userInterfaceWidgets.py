import tkinter
import webbrowser
class scrollableFrame(tkinter.Frame):
    def __init__(self,master,width,height,background):
        super(scrollableFrame,self).__init__()
        self.master = master
        self.frame_y = 30
        self.canvas = tkinter.Canvas(master = self,width = width,height = height,bg = background)
        self.canvas.pack(side = tkinter.LEFT)
        scrollbar = tkinter.Scrollbar(master = self,orient = tkinter.VERTICAL,command = self.canvas.yview)
        scrollbar.pack(side = tkinter.RIGHT,fill = tkinter.Y,expand = True)
        self.canvas.configure(yscrollcommand = scrollbar.set)
        self.canvas.bind_all("<MouseWheel>",self.onMouseWheel)
    
    def onMouseWheel(self,event):
        self.canvas.yview_scroll(-1*(event.delta//120),"units")

    def createWindow(self,dataFrame):
        self.canvas.create_window(337,self.frame_y,window = dataFrame,width = 650,height = 50)
        self.frame_y += 50

class Buttons(tkinter.Button):
    def __init__(self,master,text,background,command = None,link = None):
        super(Buttons,self).__init__(master = master,text = text,bd = 0,bg = background)
        self.link = link
        if(self.link!=None):
            self.configure(command = self.openLinkOnClick)
        else:
            self.configure(command = command)
    
    def openLinkOnClick(self):
        webbrowser.open_new(self.link)

class dataFrame(tkinter.Frame):
    def __init__(self,master,text,background,link):
        super(dataFrame,self).__init__(master = master,bg = background,bd = 2,highlightthickness = 2,highlightbackground = "white")
        self.magnitudeLabel = tkinter.Label(
            master = self,text = text[0],bg = background,bd = 0,font = ("SanSerif",11)
        )
        self.magnitudeLabel.place(x = 10,y = 11)
        self.placeLabel = tkinter.Label(
            master = self,text = text[1],bg = background,bd = 0,font = ("SanSerif",11)
        )
        self.placeLabel.place(x = 150,y = 11)
        self.openLinkButton = Buttons(
            master = self,text = "More Information",background = "white",link = link
        )
        self.openLinkButton.place(x = 530,y = 10)

class labels(tkinter.Label):
    def __init__(self,master,width,height,text,background):
        super(labels,self).__init__(master = master,width = width,height = height,text = text,bg = background)
