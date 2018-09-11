import sqlite3
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import string

class sqlite_conn:
	def __init__(self):
		self.conn = sqlite3.connect("test.db")
		self.c = self.conn.cursor()
	
	def Operation(self,sql):
		try:
			self.c.execute(sql)
			self.conn.commit()
		except:
			return False
		return True
		
	def query(self,sql):
		self.cursor = self.c.execute(sql)
		self.output = []
		for cur in self.cursor:
			self.output.append(cur)
		self.conn.commit()
		return self.output
		
LARGE_FONT = ("Verdana", 20)
class Application(tk.Tk):
	  def __init__(self):
           super().__init__()
           self.wm_title("超市现存管理系统")
           container = tk.Frame(self)
           container.pack(side="top", fill="both", expand = True)
           container.grid_rowconfigure(0, weight=1)
           container.grid_columnconfigure(0, weight=1)
           self.frames = {}
           for F in (StartPage,ShowAll,ShowOne):
                frame = F(container, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky="nsew")
           self.show_frame(StartPage)
			
	  def show_frame(self, cont):
           frame = self.frames[cont]
           frame.tkraise() 
		
class StartPage(tk.Frame):
	def __init__(self,parent,root):
		super().__init__(parent)
		label = tk.Label(self, text="超市现存管理系统\n(普通用户)", font=LARGE_FONT)
		label.pack(pady=100)
		ft2=tkFont.Font(size=16)
		tk.Button(self, text="显示所有商品",font=ft2,command=lambda: root.show_frame(ShowAll),width=30,height=2,).pack()
		tk.Button(self, text="查询某一商品",font=ft2,command=lambda: root.show_frame(ShowOne),width=30,height=2,).pack()
		tk.Button(self, text="统 计 商 品",font=ft2,command=lambda: root.show_frame(ShowAll),width=30,height=2,).pack()
		tk.Button(self, text="切 换 用 户",font=ft2,command=lambda: root.show_frame(ShowAll),width=30,height=2,).pack()
		tk.Button(self,text='退 出 系 统',height=2,font=ft2,width=30,command=root.destroy,).pack()
		
class ShowAll(tk.Frame):
	def __init__(self,parent,root):
		super().__init__(parent)
		label = tk.Label(self, text="显示所有商品", font=LARGE_FONT)
		label.pack(pady=100)
		ft2=tkFont.Font(size=16)
		tk.Label(self,text="查询到的所有商品信息如下:",font=ft2).pack()
		tk.Label(self,text="货号 货名 型号 送货价 库存量 经办人",font=ft2).pack()
		display = self.query_All()
		for dis in display:
			tk.Label(self,text=dis,font=ft2).pack()
		tk.Button(self, text="返回首页",width=8,font=ft2,command=lambda: root.show_frame(StartPage)).pack(pady=20)
				
	def query_All(self):
		sql = '''SELECT * FROM SHOP'''
		request = sqlite_conn()
		out = request.query(sql)
		return out

class ShowOne(tk.Frame):
	def __init__(self,parent,root):
		super().__init__(parent)
		label = tk.Label(self, text="显示所有商品", font=LARGE_FONT)
		label.pack(pady=100)
		ft2=tkFont.Font(size=16)
		
		tk.Label(self,text="请输入想要查找的属性:\n(1-货号，2-货名，3-型号，4-送货价，5-库存量，6-经办人)",font=ft2).pack()
		self.v1 = tk.StringVar()
		tk.Entry(self,width=30,textvariable=v1,font=ft2,bg='Ivory').pack()
		tk.Label(self,text="请输入该属性的内容:",font=ft2).pack()
		self.v2 = tk.StringVar()
		tk.Entry(self,width=30,textvariable=v2,font=ft2,bg='Ivory').pack()
		tk.Button(self, text="返回首页",width=8,font=ft2,command=lambda: root.show_frame(StartPage)).pack(pady=20)
		#tk.Button(self, text="确定查找",width=8,font=ft2,command=self.query_one(self.v1,self.v2)).pack()
		
	def query_one(self,choice,content):
		print(choice," ",content)
		if choice == "1":
			choice = "NUMBER"
		elif choice == "2":
			choice = "GOODS_NAME"
		elif choice == "3":
			choice = "TYPE"
		elif choice == "4":
			choice = "PRICE"
		elif choice == "5":
			choice = "AMOUNT"
		elif choice == "6":
			choice = "PERSON_NAME"
		sql = SELECT * FROM SHOP WHERE "{}"={}.format(choice,content)
		print(sql)
		request = sqlite_conn()
		out = request.query(sql)
		display = ""
		for o in out:
			display += o + "\n"
		messagebox.showinfo("查找某一商品信息",display)
		'''
	

app = Application()
app.mainloop()
