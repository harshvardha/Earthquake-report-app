import tkinter
import webbrowser
class scrollableFrame(tkinter.Frame):
    def __init__(self,master,width,height,background):
        super(scrollableFrame,self).__init__()
        self.master = master
        self.canvas = tkinter.Canvas(master = self,width = width,height = height,bg = background)
        self.canvas.pack(side = tkinter.LEFT)
        scrollbar = tkinter.Scrollbar(master = self,orient = tkinter.VERTICAL,command = self.canvas.yview)
        scrollbar.pack(side = tkinter.RIGHT)
        self.canvas.configure(yscrollcommand = scrollbar.set,scrollregion = (0,0,0,400))
        self.canvas.bind_all("<MouseWheel>",self.onMouseWheel)
    
    def onMouseWheel(self,event):
        self.canvas.yview_scroll(-1*(event.delta//120),"units")

class Buttons(tkinter.Button):
    def __init__(self,master,width,height,text,background,command = None,link = None):
        super(Buttons,self).__init__(master = master,width = width,height = height,text = text,bd = 0,bg = background)
        self.link = link
        if(self.link!=None):
            self.configure(command = self.openLinkOnClick)
        else:
            self.configure(command = command)
    
    def openLinkOnClick(self):
        webbrowser.open_new(self.link)

class labels(tkinter.Label):
    def __init__(self,master,width,height,text,background):
        super(labels,self).__init__(master = master,width = width,height = height,text = text,bg = background)