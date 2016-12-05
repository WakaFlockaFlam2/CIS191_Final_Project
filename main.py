#! /usr/bin/python

# -*- coding: iso-8859-1 -*-
try:
    import wx
    import os
    import sys
except ImportError:
    raise ImportError,"The wxPython module is required to run this program"
class simpleapp_wx(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent
        self.initialize()
    def quit(self, event):
        sys.exit()
    def update(self, event):
        self.progText.SetLabel("System is up to date for ROS...")
        os.system("gnome-terminal -e 'sudo apt-get update'")
        self.g1.SetValue(30)
        os.system("gnome-terminal -e 'sudo apt-get install ros-" + self.box.GetStringSelection() + "-" + self.libs.GetStringSelection() + " && sudo rosdep init && rosdep update && echo \"source /opt/ros/indigo/setup.bash\" >> ~/.bashrc && source ~/.bashrc && sudo apt-get install python-rosinstall'")
        self.g1.SetValue(60)

    def onRadioBox(self,e): 
        print self.box.GetStringSelection()
    def onLibsBox(self,e): 
        print self.libs.GetStringSelection()
    def onClickWorkspace(self, e): 
      cb = e.GetEventObject() 
      print cb.GetLabel(),' is clicked',cb.GetValue()

    def onClickTuts(self, e): 
      cb = e.GetEventObject() 
      print cb.GetLabel(),' is clicked',cb.GetValue()

    def initialize(self):
        jpg = wx.Image('ros_install_header.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        wx.StaticBitmap(self, -1, jpg, (0, 0))
        
        self.box = wx.RadioBox(self, -1, "ROS Distro        ", pos=(55,225), choices=["kinetic", "jade", "indigo", "hydro", "groovy", "fuerte"], style=wx.VERTICAL)
        self.box.Bind(wx.EVT_RADIOBOX,self.onRadioBox)
        wx.StaticText(self, -1, "ROS releases are called\ndistributions.The distros are\nordered from newest to oldest.\nChoose the default option if\nunsure.", (13, 415))


        self.libs = wx.RadioBox(self, -1, "ROS Version        ", pos=(280,225), choices=["desktop-full", "desktop", "ros-base"], style=wx.VERTICAL)
        self.libs.Bind(wx.EVT_RADIOBOX,self.onLibsBox)
        wx.StaticText(self, -1, "Choose 'full-desktop' unless you\nare short on storage.", (280, 350))

        self.workspace = wx.CheckBox(self, -1, label="Initialize workspace", pos=(505, 225))
        self.workspace.SetValue(True)
        self.workspace.Bind(wx.EVT_CHECKBOX, self.onClickWorkspace)
        wx.StaticText(self, -1, "If selected a ROS workspace\n will be initialized.", (505, 275))

        self.tuts = wx.CheckBox(self, -1, label="Install ROS Tutorials Package", pos=(730, 225))
        self.tuts.SetValue(True)
        self.tuts.Bind(wx.EVT_CHECKBOX, self.onClickTuts)
        wx.StaticText(self, -1, "", (13, 160))

        installbtn = wx.Button(self, label="Install", pos=(900, 650))
        installbtn.Bind(wx.EVT_BUTTON, self.update)
        quitbutton = wx.Button(self, label="Quit", pos=(800, 650))
        quitbutton.Bind(wx.EVT_BUTTON, self.quit)

        self.infoText = wx.StaticText(self, -1, "ROS is a middleware for asynchronous, one-to-many communication between nodes. This ROS installer is made to simplify the process of installing\nROS on Ubuntu. It may work with some other Linux distros, but this has not been tested.", (13, 160))
        self.progText = wx.StaticText(self, -1, "Install Progress:", (50, 550))

        self.g1 = wx.Gauge(self, -1, 100, (50, 580), (900, 45))        
        self.g1.SetValue(0)
        self.Show(True)

if __name__ == "__main__":
    app = wx.App()
    frame = simpleapp_wx(None,-1,'ROS Easy Install Tool')
    frame.SetMaxSize(wx.Size(1000,700))
    frame.SetMinSize(wx.Size(1000,700))
    frame.SetSize(wx.Size(1000,700))
    app.MainLoop()

