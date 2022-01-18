import tkinter
import userInterfaceWidgets
import apiRequestScript
from datetime import datetime,timedelta
root = tkinter.Tk()
root.geometry("700x500")
root.title("Earthquake Report")

#filter by button
filterByButton = tkinter.Button(
    master = root,text = "Filter by",bd = 0,bg = "grey",font = ("SanSerif",15),
    activebackground = "grey"
)
filterByButton.place(x = 10,y = 10)

#indicator label
indicatorLabel = tkinter.Label(
    master = root,bd = 0,text = "By Magnitude",font = ("SanSerif",20)
)
indicatorLabel.place(x = 500,y = 10)

scrollableFrame = userInterfaceWidgets.scrollableFrame(
    master = root,width = 675,height = 430,background = "white"
)
scrollableFrame.pack(side = tkinter.BOTTOM)
data = apiRequestScript.getEarthQuakeData(
    'most recent',
    starttime = (datetime.now()-timedelta(1)).strftime("%Y-%m-%d"),
    endtime = datetime.today().strftime("%Y-%m-%d")
)
no_of_frames= len(data)
frameId = 0
while(frameId<no_of_frames):
    dataframe = userInterfaceWidgets.dataFrame(
        master = scrollableFrame.canvas,text = [str(data[frameId]['properties']['mag']),data[frameId]['properties']['place']],
        background = "grey",link = data[frameId]['properties']['url']
    )
    no_of_frames -= 1
    frameId += 1
    scrollableFrame.createWindow(dataframe)
scrollableFrame.canvas.configure(scrollregion = (0,0,0,scrollableFrame.frame_y-20))
root.mainloop()