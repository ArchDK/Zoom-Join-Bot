import tkinter as tk
from tkinter import Listbox, Scrollbar, Tk, ttk
from tkinter.constants import CENTER
import joinZoom
from threading import Thread, Event 
class zoomInfo(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)

        self.rowconfigure([0,1,2], weight=0,minsize=40)
        self.columnconfigure([0,1,2], weight=1,minsize=100)
        
        self.widget()

    def widget(self):
        logoLabel = tk.Label(text="ZOOM BOT", width=10)
        logoLabel.grid(column=0,row=0,sticky=tk.N,pady=10)
        
        titleLabel = ttk.Label(self, text="Title")
        titleLabel.grid(column=0, row=1, padx=5, pady=5)
        
        self.title = tk.StringVar()
        titleEntry = ttk.Entry(self,textvariable=self.title)
        titleEntry.grid(column=0, row=2, padx=5)
        
        idLabel = ttk.Label(self, text="ID*")
        idLabel.grid(column=1, row=1, padx=5, pady=5)

        self.id = tk.StringVar()
        idEntry = ttk.Entry(self, textvariable=self.id)
        idEntry.grid(column=1, row=2, padx=5)

        passwordLabel = ttk.Label(self, text="Password*")
        passwordLabel.grid(column=2, row=1, padx=5, pady=5)

        self.password = tk.StringVar()
        passwordEntry = ttk.Entry(self, textvariable=self.password)
        passwordEntry.grid(column=2, row=2, padx=5)
    
    def getZoomInfo(self):
        if self.title == None:
            return "None",self.id.get(),self.password.get()
        return self.title.get(),self.id.get(),self.password.get()
        
    def resetZoomInfo(self):
        self.title = ""
        self.id = ""
        self.password = ""
    
class zoomTime(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        
        self.columnconfigure([0,1,2,3], weight=1,minsize=50)
        
        self.widget()
    def widget(self):
        startLabel = ttk.Label(self, text="Start*")
        startLabel.grid(column=0, row=0, padx=5, pady=5)

        self.start = tk.StringVar()
        startEntry = ttk.Entry(self, text="HH-MM", textvariable=self.start)
        startEntry.grid(column=1, row=0, padx=5, pady=5)

        endLabel = ttk.Label(self, text="End")
        endLabel.grid(column=2, row=0, padx=5, pady=5)

        self.end = tk.StringVar()
        endEntry = ttk.Entry(self, textvariable=self.end)
        endEntry.grid(column=3, row=0, padx=5, pady=5)

    def getZoomTime(self):
        if(self.end.get()==None):
            return self.start.get(),"None"
        return self.start.get(),self.end.get()
    
    
class listZoom(ttk.Frame):
    def __init__(self,container, zoomInfo, zoomTime,zoom):
        super().__init__(container)
        self.rowconfigure([0,1,2,3,4], weight=0,minsize=60)
        self.rowconfigure(5,weight=0,minsize=10)
        self.columnconfigure([0,1,2], weight=1,minsize=50)
        
        self.list = []
        self.zoomInfos = zoomInfo
        self.zoomTimes = zoomTime
        self.zoom = zoom
        self.value = 0

        self.widgetButton()
        self.widgetHeader()


    def widgetButton(self):
        login_button = ttk.Button(self, text="Insert",command=lambda : self.getData())
        login_button.grid(column=2, row=0, padx=5, pady=5)
        
    def widgetHeader(self):
        startLabel = ttk.Label(self, text="Title",borderwidth=2, relief="groove", anchor=CENTER)
        startLabel.grid(column=0, row=1, padx=5, pady=5,ipadx=25)

        startLabel = ttk.Label(self, text="ID",borderwidth=2, relief="groove",anchor=CENTER)
        startLabel.grid(column=1, row=1, padx=5, pady=5,ipadx=35)

        startLabel = ttk.Label(self, text="Password",borderwidth=2, relief="groove", anchor=CENTER)
        startLabel.grid(column=2, row=1, padx=5, pady=5,ipadx=15)

        startLabel = ttk.Label(self, text="Start",borderwidth=2, relief="groove", anchor=CENTER)
        startLabel.grid(column=3, row=1, padx=5, pady=5,ipadx=25)

        startLabel = ttk.Label(self, text="End",borderwidth=2, relief="groove", anchor=CENTER)
        startLabel.grid(column=4, row=1, padx=5, pady=5,ipadx=30)

        self.scrollbar = Scrollbar()
        self.scrollbar.grid(column=5,row=2,padx=5)
        self.listBox = Listbox(self,yscrollcommand=self.scrollbar.set,width=70)
        self.listBox.grid(column=0,row=3,columnspan=6,padx=5)
#           
    def widgetList(self):
        text = ""
        text = [str(x) for x in self.list[self.value]]
        print(self.list)
        output = f"   {self.stringFormat(text[0][:10],11)}   |   {self.stringFormat(text[1][:10],12)}   |   {self.stringFormat(text[2][:12],12)}   |    {self.stringFormat(text[3][:5],10)}   |    {self.stringFormat(text[4][:5],7)}   "
        self.listBox.insert("end",output)
        self.value+=1

    def stringFormat(self,string,spaceValue):
        x = str( " "* (spaceValue-(len(string))) + string + " "* (spaceValue-(len(string))) )
        return x

    def getData(self):
       zoomData = []
       zoomData += self.zoomInfos.getZoomInfo()
       zoomData += self.zoomTimes.getZoomTime()
       print(zoomData[3][:5])
       self.list.append(zoomData)
    #    thread = Thread(target=self.zoom.main(self.list[self.value]))
    #    thread.start()
       self.after(100,self.zoom.main(self.list[self.value]))
       self.widgetList()

class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.zooms = joinZoom.joinZoom()
        self.title("Join Zoom Bot")
        self.minsize(400,300)
        self.rowconfigure([0,1,2], weight=0,minsize=80)
        self.resizable(0,0)

        self.insertFrame()
    def insertFrame(self):
        zoomInfoFrame = zoomInfo(self)
        zoomInfoFrame.grid(column=0,row=0)

        zoomTimeFrame = zoomTime(self)
        zoomTimeFrame.grid(column=0,row=1)
        
        listZoomFrame = listZoom(self,zoomInfoFrame,zoomTimeFrame,self.zooms)
        listZoomFrame.grid(column=0,row=2)




if __name__ == "__main__":
    apps = app()
    apps.mainloop()   