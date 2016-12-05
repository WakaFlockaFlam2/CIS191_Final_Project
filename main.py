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

    def initialize(self):
        jpg = wx.Image('ros_install_header.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        wx.StaticBitmap(self, -1, jpg, (0, 0))

        self.radio = wx.RadioButton(self, label="Test", style = wx.RB_GROUP, pos=(200,200))
        self.radio2 = wx.RadioButton(self, label="Test2", pos=(200,220))
        installbtn = wx.Button(self, label="Install", pos=(900, 650))
        installbtn.Bind(wx.EVT_BUTTON, self.onBtn)
        quitbutton = wx.Button(self, label="Quit", pos=(800, 650))
        quitbutton.Bind(wx.EVT_BUTTON, self.quit)
        

        self.Show(True)

if __name__ == "__main__":
    app = wx.App()
    frame = simpleapp_wx(None,-1,'ROS Easy Install Tool')
    frame.SetSize(wx.Size(1000,700))
    app.MainLoop()

