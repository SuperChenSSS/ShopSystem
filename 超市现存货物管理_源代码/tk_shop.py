from main_v3 import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

class Application(tk.Frame):
	def __init__(self, master=None):
		global f
		super().__init__(master)
		master.title("超市现存管理系统")
		self.pack()
		self.create_widgets()
		
	def add_goods_func(self):
		if not self.f:
			tk.messagebox.showerror("错误","权限不足！")
			return
		Add_SQL()
		#tk.messagebox.askokcancel("测试",message_callback)
	
	def show_all_func(self):
		if not self.f:
			tk.messagebox.showerror("错误","权限不足！")
			return
		query_All_SQL()
		
	def del_goods_func(self):
		if not self.f:
			tk.messagebox.showerror("错误","权限不足！")
			return
		del_SQL()
		
	def modify_goods_func(self):
		if not self.f:
			tk.messagebox.showerror("错误","权限不足！")
			return
		Modify_SQL()
		
	def query_one_goods_func(self):
		query_One_SQL()
		
	def count_goods_func(self):
		Count()
	
	def change_user_func(self):
		self.f = check_user(self.f)
		
	def add_user_func(self):
		if not self.f:
			tk.messagebox.showerror("错误","权限不足！")
			return
		Add_User()
		
	def query_user_func(self):
		if not self.f:
			tk.messagebox.showerror("错误","权限不足！")
			return
		query_User()
		
	def quit_user_func(self):
		if not self.f:
			tk.messagebox.showerror("错误","权限不足！")
			return
		tk.messagebox.askokcancel("提示","已切换为普通用户模式！")
		self.f = False
	
	def create_widgets(self):
		self.f = False
		conn = sqlite3.connect('test.db')
		print("成功打开数据库")
		self.add_goods = tk.Button(self)
		self.add_goods["text"] = "增 加 商 品"
		self.add_goods["command"] = self.add_goods_func
		self.add_goods.pack(side="top")
		
		self.show_all = tk.Button(self)
		self.show_all["text"] = "显示所有商品"
		self.show_all["command"] = self.show_all_func
		self.show_all.pack(side="top")
		
		self.del_goods = tk.Button(self)
		self.del_goods["text"] = "删 除 商 品"
		self.del_goods["command"] = self.del_goods_func
		self.del_goods.pack(side="top")
		
		self.modify_goods = tk.Button(self)
		self.modify_goods["text"] = "修 改 商 品"
		self.modify_goods["command"] = self.modify_goods_func
		self.modify_goods.pack(side="top")
		
		self.query_one_goods = tk.Button(self)
		self.query_one_goods["text"] = "查询某一商品"
		self.query_one_goods["command"] = self.query_one_goods_func
		self.query_one_goods.pack(side="top")
		
		self.count_goods = tk.Button(self)
		self.count_goods["text"] = "统 计 商 品"
		self.count_goods["command"] = self.count_goods_func
		self.count_goods.pack(side="top")
		
		self.change_user = tk.Button(self)
		self.change_user["text"] = "切 换 用 户"
		self.change_user["command"] = self.change_user_func
		self.change_user.pack(side="top")
		
		self.add_user = tk.Button(self)
		self.add_user["text"] = "添 加 用 户"
		self.add_user["command"] = self.add_user_func
		self.add_user.pack(side="top")
		
		self.query_user = tk.Button(self)
		self.query_user["text"] = "查询总用户信息"
		self.query_user["command"] = self.query_user_func
		self.query_user.pack(side="top")
		
		self.quit_user = tk.Button(self)
		self.quit_user["text"] = "退出管理权限"
		self.quit_user["command"] = self.quit_user_func
		self.quit_user.pack(side="top")
		
		self.quit = tk.Button(self, text="退 出 系 统", fg="black",command=root.destroy)
		self.quit.pack(side="bottom")

root = tk.Tk()
root.geometry("200x250")
app = Application(master=root)
app.mainloop()