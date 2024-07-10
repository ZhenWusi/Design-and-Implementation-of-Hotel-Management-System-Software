import wx
import sqlite3

#flag == 1 注册到DBM
#flag == 2 注册到Customer

class registered(wx.Frame):
    def __init__(self, parent, id, flag):
        wx.Frame.__init__(self, parent, id, title = "新用户注册", pos = (600, 300), size =(420, 320))
        panel = wx.Panel(self)
        wx.StaticText(panel, label = "请输入相关信息", pos = (170, 20))
        self.flag = flag
        if flag == 1:
            self.label_User = wx.StaticText(panel, label = "用户名:", pos = (50, 70))
            self.label_Password = wx.StaticText(panel, label = "密码:", pos = (50, 110))
            self.User = wx.TextCtrl(panel, pos = (100, 70), size = (235, 25),style =  wx.TE_LEFT)
            self.Password = wx.TextCtrl(panel, pos = (100, 110), size = (235, 25), style = wx.TE_LEFT)
            self.bt1 = wx.Button(panel, label = "确定", pos = (105, 150))
            self.bt2 = wx.Button(panel, label = "退出", pos = (245, 150))
            self.bt1.Bind(wx.EVT_BUTTON, self.bt1_f)
            self.bt2.Bind(wx.EVT_BUTTON, self.bt2_f)
        else:
            self.label_User = wx.StaticText(panel, label = "用户名:", pos = (50, 50))
            self.label_Password = wx.StaticText(panel, label = "密码:", pos = (50, 90))
            self.label_Name = wx.StaticText(panel, label = "姓名:", pos = (50, 130))
            self.label_Telephone = wx.StaticText(panel, label = "电话:", pos = (50, 170))
            self.User = wx.TextCtrl(panel, pos = (100, 50), size = (235, 25),style =  wx.TE_LEFT)
            self.Password = wx.TextCtrl(panel, pos = (100, 90), size = (235, 25), style = wx.TE_LEFT)
            self.UName = wx.TextCtrl(panel, pos = (100,130), size = (235,25), style = wx.TE_LEFT)
            self.Telepone = wx.TextCtrl(panel, pos = (100,170), size = (235,25), style = wx.TE_LEFT)
            self.bt1 = wx.Button(panel, label = "确定", pos = (105, 210))
            self.bt2 = wx.Button(panel, label = "退出", pos = (245, 210))
            self.bt1.Bind(wx.EVT_BUTTON, self.bt1_f)
            self.bt2.Bind(wx.EVT_BUTTON, self.bt2_f)
    
    def bt1_f(self, event):
        con = sqlite3.connect("酒店管理系统.db")
        cur = con.cursor()
        UserName = self.User.GetValue()
        Password = self.Password.GetValue()
        if self.flag == 1:
            cur.execute("SELECT * FROM DBM where 用户名 = '%s'" % UserName)
        elif self.flag == 2 :
            cur.execute("SELECT * FROM Customer where 账号 = '%s'" % UserName)
        else :
            pass
        l_info = cur.fetchall()
        if len(l_info) == 0:
            if self.flag == 1:
                cur.execute("INSERT INTO DBM(用户名, 密码) VALUES(?, ?)", (UserName, Password))
            elif self.flag == 2 :
                U_Name = self.UName.GetValue()
                U_Telephone = self.Telepone.GetValue()
                cur.execute("INSERT INTO Customer(客户ID,账号, 密码, 电话, 名字) VALUES(?, ?)", (UserName, UserName ,Password, U_Telephone, U_Name))
            else :
                pass
            message = "注册成功"
            con.commit()
            self.Destroy()
        else:
            message = "用户名已存在"
        cur.close()
        con.close()
        wx.MessageBox(message)

    def bt2_f(self, event):
        self.Destroy()
        wx.MessageBox("退出成功")

def Registered(f):
    app = wx.App()
    frame = registered(None, -1, f)
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    Registered(1)
