import wx
import sqlite3

path = "酒店管理系统.db"

class Function(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title = "Customer", size =(800, 600))
        panel = wx.Panel(self)
        wx.StaticText(panel, label = "*客户ID", pos = (100,50))
        wx.StaticText(panel, label = "名字", pos = (100,100))
        wx.StaticText(panel, label = "电话", pos = (100,150))
        wx.StaticText(panel, label = "密码", pos = (100,200))

        wx.StaticText(panel, label = "*客户ID", pos = (100,300))
        wx.StaticText(panel, label = "名字", pos = (160,300))
        wx.StaticText(panel, label = "电话", pos = (220,300))
        wx.StaticText(panel, label = "密码", pos = (320,300))

        self.Com_ID =  wx.TextCtrl(panel, pos = (200, 50), size = (235, 25),style =  wx.TE_LEFT)
        self.Com_name =  wx.TextCtrl(panel, pos = (200, 100), size = (235, 25),style =  wx.TE_LEFT)
        self.Com_telephone =  wx.TextCtrl(panel, pos = (200,150), size = (235, 25),style =  wx.TE_LEFT)
        self.Com_password =  wx.TextCtrl(panel, pos = (200,200), size = (235, 25),style =  wx.TE_LEFT)
        self.bt1 = wx.Button(panel, label = "查询所有信息", pos = (100,250))
        self.bt2 = wx.Button(panel, label = "查询", pos = (210,250))
        self.bt3 = wx.Button(panel, label = "录入", pos = (300,250))
        self.bt4 = wx.Button(panel, label = "删除", pos = (400,250))
        self.bt5 = wx.Button(panel, label = "修改", pos = (500,250))
        self.bt1.Bind(wx.EVT_BUTTON, self.bt1_f)
        self.bt2.Bind(wx.EVT_BUTTON, self.bt2_f)
        self.bt3.Bind(wx.EVT_BUTTON, self.bt3_f)
        self.bt4.Bind(wx.EVT_BUTTON, self.bt4_f)
        self.bt5.Bind(wx.EVT_BUTTON, self.bt5_f)
        self.Text = wx.TextCtrl(panel, pos = (100,320), size = (550, 200),style =  wx.TE_MULTILINE)

    def bt1_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT * FROM Customer")
        inf = cur.fetchall() 
        string = ""
        for i in inf:
            string = string+i[0] + "\t" + i[1] + "\t" + i[2] + "\t" + i[4] + "\t\n"
        self.Text.SetValue(string)
        cur.close()

    def bt2_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Com_ID.GetValue()
        Name = self.Com_name.GetValue()
        Telephone = self.Com_telephone.GetValue()
        if ID == "":
            message = "请输入客户ID"
            wx.MessageBox(message)
        else:
            cur.execute("SELECT * FROM Customer WHERE 客户ID = ?",(ID,))
            inf = cur.fetchall()
            if inf == []:
                message = "信息不存在"
                wx.MessageBox(message)
            else :
                string = ""
                string =inf[0][0] + "\t" + inf[0][1] + "\t" + inf[0][2] + "\t" + inf[0][4] + "\t"
                self.Text.SetValue(string)
        cur.close()

    def bt3_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Com_ID.GetValue()
        Name = self.Com_name.GetValue()
        Telephone = self.Com_telephone.GetValue()
        Password = self.Com_password.GetValue()

        if ID == "" or Name == "" or Telephone == "":
            message = "信息不完整"
            wx.MessageBox(message)
        else:
            message = "信息录入成功"
            cur.execute("INSERT INTO Customer(客户ID,名字,电话,账号,密码) VALUES(?,?,?,?,?)",(ID,Name,Telephone,ID,Password))
            wx.MessageBox(message)
        con.commit()
        cur.close()

    def bt4_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Com_ID.GetValue()
        Name = self.Com_name.GetValue()
        Telephone = self.Com_telephone.GetValue()
        Password = self.Com_password.GetValue()
        if ID == "":
            message = "所需删除的数据不明确"
            wx.MessageBox(message)
        else:
            cur.execute("SELECT * FROM Customer WHERE 客户ID = ?",(ID,))
            inf = cur.fetchall()
            if inf == []:
                message = "信息不存在"
                wx.MessageBox(message)
            else:
                message = "信息删除成功"
                cur.execute("DELETE FROM Customer WHERE 客户ID = ?",(ID,))
                wx.MessageBox(message)
                con.commit()
            cur.close()

    def bt5_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Com_ID.GetValue()
        Name = self.Com_name.GetValue()
        Telephone = self.Com_telephone.GetValue()
        Password = self.Com_password.GetValue()
        if ID == "":
            message = "所需更改的数据不明确"
            wx.MessageBox(message)
        else:
            cur.execute("SELECT * FROM Customer WHERE 客户ID = ?",(ID,))
            inf = cur.fetchall()
            if inf == []:
                message = "信息不存在"
                wx.MessageBox(message)
            else: 
                message = "请输入需要修改的信息"
                if Name != "":
                    message = "信息修改成功"
                    cur.execute("UPDATE Customer SET 名字 = ? WHERE 客户ID = ?",(Name,ID))
                if Telephone != "":
                    message = "信息修改成功"
                    cur.execute("UPDATE Customer SET 电话 = ? WHERE 客户ID = ?",(Telephone,ID))
                if Password != "":
                    message = "信息修改成功"
                    cur.execute("UPDATE Customer SET 密码 = ? WHERE 客户ID = ?",(Password,ID))
                wx.MessageBox(message)
            con.commit()
        cur.close()

def customer():
    app = wx.App()
    frame = Function(None, -1)
    frame.Centre()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    app = wx.App()
    frame = Function(None, -1)
    frame.Centre()
    frame.Show()
    app.MainLoop()