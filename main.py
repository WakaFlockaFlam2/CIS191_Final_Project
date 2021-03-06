#! /usr/bin/python

#these are system libs no install required
import os
import sys
import lsb_release
try:
    import wx
except ImportError:
    raise ImportError,"Need GUI Library. Run $sudo apt-get install python-wxgtk2.8on"
class simpleapp_wx(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent
        self.initialize()
    #quit button calls this function
    def quit(self, event):
        sys.exit()
    #update() is called when install is clicked to install ROS
    def update(self, event): 
        print
        self.progText.SetLabel("Install Progress:")
        if self.box.GetStringSelection() == "hydro" or self.box.GetStringSelection() == "groovy" or self.box.GetStringSelection() == "fuerte":
            self.progText.SetLabel("This is an old, deprecated version of ROS. Please select a newer version for install.")
        elif self.box.GetStringSelection() == "kinetic" and (lsb_release.get_lsb_information().get('RELEASE') != "15.10" and lsb_release.get_lsb_information().get('RELEASE') != "16.04"):
            self.progText.SetLabel("You must be on Ubuntu 15.10 or 16.04 for this distro")
        elif self.box.GetStringSelection() == "jade" and (lsb_release.get_lsb_information().get('RELEASE') != "14.04" and lsb_release.get_lsb_information().get('RELEASE') != "14.10" or lsb_release.get_lsb_information().get('RELEASE') != "15.10"):
            self.progText.SetLabel("You must be on Ubuntu 14.04 or 14.10 or 15.10 for this distro")
        elif self.box.GetStringSelection() == "indigo" and (lsb_release.get_lsb_information().get('RELEASE') != "13.10" and lsb_release.get_lsb_information().get('RELEASE') != "14.04"):
            self.progText.SetLabel("You must be on Ubuntu 13.10 or 14.04 for this distro")
        else:
            self.progText.SetLabel("System is up to date for ROS...")
            os.system("gnome-terminal -e 'sudo apt-get update'")
            self.g1.SetValue(30)
            os.system("sudo apt-get install ros-" + self.box.GetStringSelection() + "-" + self.libs.GetStringSelection() + " && sudo rosdep init && rosdep update && echo 'source /opt/ros/indigo/setup.bash' >> ~/.bashrc && source ~/.bashrc && sudo apt-get install python-rosinstall && mkdir -p ~/catkin_ws/src && cd ~/catkin_ws/src && catkin_init_workspace")
            self.g1.SetValue(60)
            if self.tuts.GetLabel():
                os.system("gnome-terminal -e 'sudo apt-get install ros-" + self.box.GetStringSelection() + "-ros-tutorials'")
            self.g1.SetValue(100)
            self.progText.SetLabel("Complete!")

    #some functions for testing radio box implementation
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
        #add all the gui componends
        jpg = wx.Image('ros_install_header.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        wx.StaticBitmap(self, -1, jpg, (0, 0))
        #open software image
        osi = wx.Image('osilogo.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        wx.StaticBitmap(self, -1, osi, (600, 462), size=(100,100))
        #xkcd image
        xkcd = wx.Image('xkcd.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        wx.StaticText(self, -1, "Obligatory  xkcd", (762, 308))
        wx.StaticBitmap(self, -1, xkcd, (725, 325))
        #distro selection
        self.box = wx.RadioBox(self, -1, "ROS Distro        ", pos=(55,225), choices=["kinetic", "jade", "indigo", "hydro", "groovy", "fuerte"], style=wx.VERTICAL)
        self.box.Bind(wx.EVT_RADIOBOX,self.onRadioBox)
        wx.StaticText(self, -1, "ROS releases are called\ndistributions.The distros are\nordered from newest to oldest.\nChoose the default option if\nunsure.", (13, 415))
        #library install selection
        self.libs = wx.RadioBox(self, -1, "ROS Version        ", pos=(280,225), choices=["desktop-full", "desktop", "ros-base"], style=wx.VERTICAL)
        self.libs.Bind(wx.EVT_RADIOBOX,self.onLibsBox)
        wx.StaticText(self, -1, "Choose 'full-desktop' unless\nyou are short on storage.", (280, 350))
        #workspace initialization checkbox
        self.workspace = wx.CheckBox(self, -1, label="Initialize workspace", pos=(505, 225))
        self.workspace.SetValue(True)
        self.workspace.Bind(wx.EVT_CHECKBOX, self.onClickWorkspace)
        wx.StaticText(self, -1, "If selected a ROS workspace\n will be initialized.", (505, 275))
        #install tutorial libs checkbox
        self.tuts = wx.CheckBox(self, -1, label="Install ROS Tutorials Package", pos=(730, 225))
        self.tuts.SetValue(True)
        self.tuts.Bind(wx.EVT_CHECKBOX, self.onClickTuts)
        wx.StaticText(self, -1, "", (13, 160))
        #install button which calls the update() function
        installbtn = wx.Button(self, label="Install", pos=(900, 650))
        installbtn.Bind(wx.EVT_BUTTON, self.update)
        quitbutton = wx.Button(self, label="Quit", pos=(800, 650))
        quitbutton.Bind(wx.EVT_BUTTON, self.quit)
        #progress bar and info text
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

