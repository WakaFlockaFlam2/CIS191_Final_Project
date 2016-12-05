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
    def onBtn(self, event):
        """"""
        print "First radioBtn = ", self.radio.GetValue()
        print "Second radioBtn = ", self.radio2.GetValue()
    def quit(self, event):
        sys.exit()
    def update(self, event):
        self.progText.SetLabel("System is up to date for ROS...")
        os.system("gnome-terminal -e 'sudo apt-get update'")
        self.g1.SetValue(30)

    def onRadioBox(self,e): 
        print self.box.GetStringSelection(),' is clicked from Radio Box'

    def onClickWorkspace(self, e): 
      cb = e.GetEventObject() 
      print cb.GetLabel(),' is clicked',cb.GetValue()
    def initialize(self):
        jpg = wx.Image('ros_install_header.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        wx.StaticBitmap(self, -1, jpg, (0, 0))
        
        self.box = wx.RadioBox(self, -1, "ROS Distro        ", pos=(200,200), choices=["kinetic", "jade", "indigo", "hydro", "groovy", "fuerte"], style=wx.VERTICAL)
        self.box.Bind(wx.EVT_RADIOBOX,self.onRadioBox)

        self.libs = wx.RadioBox(self, -1, "ROS Version        ", pos=(400,200), choices=["full", "desktop", "base"], style=wx.VERTICAL)
        self.libs.Bind(wx.EVT_RADIOBOX,self.onRadioBox)

        self.workspace = wx.CheckBox(self, -1, label="Initialize workspace", pos=(600, 200))
        self.workspace.SetValue(True)
        self.workspace.Bind(wx.EVT_CHECKBOX, self.onClickWorkspace)

        installbtn = wx.Button(self, label="Install", pos=(900, 650))
        installbtn.Bind(wx.EVT_BUTTON, self.update)
        quitbutton = wx.Button(self, label="Quit", pos=(800, 650))
        quitbutton.Bind(wx.EVT_BUTTON, self.quit)

        self.infoText = wx.StaticText(self, -1, "ROS is a middleware for asynchronous, one-to-many communication between nodes.", (400, 400))
        self.progText = wx.StaticText(self, -1, "Install Progress:", (50, 550))

        self.g1 = wx.Gauge(self, -1, 100, (50, 580), (900, 45))        
        self.g1.SetValue(0)
        self.Show(True)

if __name__ == "__main__":
    app = wx.App()
    frame = simpleapp_wx(None,-1,'ROS Easy Install Tool')
    frame.SetSize(wx.Size(1000,700))
    app.MainLoop()

