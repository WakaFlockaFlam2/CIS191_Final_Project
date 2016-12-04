#! /usr/bin/python

# -*- coding: iso-8859-1 -*-
try:
    import wx
    import os

except ImportError:
    raise ImportError,"The wxPython module is required to run this program"
class simpleapp_wx(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent
        self.initialize()

    def initialize(self):
        sizer = wx.GridBagSizer()

        jpg = wx.Image('ros_install_header.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        wx.StaticBitmap(self, -1, jpg, (0, 0))

        self.label = wx.StaticText(self,-1,label=u'Hello !')
        self.label.SetBackgroundColour(wx.BLUE)
        self.label.SetForegroundColour(wx.WHITE)
        sizer.Add( self.label, (1,0),(1,2), wx.EXPAND )

        self.SetSizerAndFit(sizer)
        self.Show(True)

if __name__ == "__main__":
    os.system("mkdir /home/jake/Desktop/test")
    app = wx.App()
    frame = simpleapp_wx(None,-1,'my application')
    frame.SetSize(wx.Size(1000,700))
    app.MainLoop()

