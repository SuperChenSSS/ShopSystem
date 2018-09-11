import pymysql
import getpass

def Create_Table_User():
	c = conn.cursor()
	c.execute('''CREATE TABLE USER
			(NAME STRING PRIMARY KEY NOT NULL,
			PASSWORD STRING NOT NULL);''')
	print("用户建表成功")
	conn.commit()

def query_User():
	c = conn.cursor()
	print("现有的User信息为:")
	print("用户名\t  密码")
	c.execute("SELECT NAME,PASSWORD FROM USER")
	cursor = c.fetchall()
	for cur in cursor:
		print(cur[0],'\t',cur[1])
	print("查询完毕！")

def Add_User():
	c = conn.cursor()
	query_User()
	username = input("请输入你想要添加的用户名:")
	password = getpass.getpass("请输入你想要附带的密码:")
	c.execute('''INSERT INTO USER(NAME,PASSWORD)
			VALUES ("{NAME}","{PASS}")'''.format(NAME=username,PASS=password))
	conn.commit()
	print("已经成功插入该用户信息!")

def Match_User():
	c = conn.cursor()
	username = input("请输入用户名:")
	password = getpass.getpass("请输入密码:")
	c.execute('''SELECT PASSWORD FROM USER 
			WHERE NAME="{NAME}"'''.format(NAME=username))
	data = c.fetchall()
	for d in data:
		if str(d[0]) == password:
			print("{NAME},欢迎登陆系统！将切换为管理员模式！".format(NAME=username))
			return True
	return False

def check_user(flag=False):
	if flag:
		print("已经是管理员用户，无需切换！")
		return True
	if Match_User() == True:
		print("验证正确，已切换为管理员用户！")
		return  True
	else:
		print("验证错误，保持原有用户状态！")
	return False
	
def Create_Table():
	c = conn.cursor()
	c.execute('''CREATE TABLE SHOP
			(NUMBER INT PRIMARY KEY NOT NULL,
			GOODS_NAME           STRING    NOT NULL,
			TYPE            STRING     NOT NULL,
			PRICE          INT	NOT NULL,
			AMOUNT         INT	NOT NULL,
			PERSON_NAME	STRING    NOT NULL);''')
	print ("超市建表成功");
	conn.commit()
	
def Add_SQL():
	c = conn.cursor()
	print("请输入新增商品信息：")
	goods_number = input("货号:")
	goods_name = input("货名:")
	Type = input("型号:")
	price = input("进货价:")
	amount = input("库存量:")
	person_name = input("经办人:")
	sql_insert = "INSERT INTO SHOP(NUMBER,GOODS_NAME,TYPE,PRICE,AMOUNT,PERSON_NAME) \
			VALUES (" + goods_number + ",\"" + goods_name + "\",\"" + Type + "\"," + price + "," + amount + ",\"" + person_name + "\")"
	#print(sql_insert)
	c.execute(sql_insert);
	conn.commit()
	print ("已成功记录本条信息")

def query_All_SQL(attributes="",value=""):
	print("表中全部信息如下：")
	c = conn.cursor()
	if attributes == "" and value == "":
		c.execute("SELECT * FROM SHOP")
		cursor = c.fetchall()
	elif attributes == "SUM":
		print("商品名称\t商品总价格")
		c.execute("SELECT GOODS_NAME,SUM(PRICE * AMOUNT) FROM SHOP GROUP BY GOODS_NAME")
		cursor = c.fetchall()
		for row in cursor:
			print(row[0],end='\t')
			print(row[1])
		return
	elif attributes == "PERSON":
		print("经办人\t总数量")
		c.execute("SELECT PERSON_NAME,SUM(AMOUNT) FROM SHOP GROUP BY PERSON_NAME")
		cursor = c.fetchall()
		for row in cursor:
			print(row[0],end='\t')
			print(row[1])
		return
	else:
		c.execute("SELECT * from SHOP WHERE " + attributes + "=\"" + value + "\";")
		cursor = c.fetchall()
	if attributes != "SUM" and attributes != "PERSON":
		print("货号\t货名\t型号\t送货价\t库存量\t经办人")
	for row in cursor:
		print (row[0],end='\t')
		print (row[1],end='\t')
		print (row[2],end='\t')
		print (row[3],end='\t')
		print (row[4],end='\t')
		print (row[5])
	print("全部信息查询完毕")

def del_SQL():
	query_All_SQL()
	target_goods = input("请输入想删除的目标货名:")
	c = conn.cursor()
	c.execute("DELETE from SHOP where GOODS_NAME=\"" + target_goods + "\";")
	conn.commit()
	print("该货物已成功删除")
	
def Modify_SQL():
	c = conn.cursor()
	#NUMBER,GOODS_NAME,TYPE,PERSON_NAME,PRICE,AMOUNT
	print("修改前，表中数据为:")
	query_All_SQL()
	target_goods = input("请输入想修改的目标货名:")
	target_aim = input("请输入你要修改的属性:(1-货号，2-货名，3-型号，4-送货价，5-库存量，6-经办人)")
	if target_aim == "1":
		data = input("请输入新货号:")
		c.execute("UPDATE SHOP set NUMBER = " + data + " where GOODS_NAME=\"" + target_goods + "\";")
	elif target_aim == "2":
		data = input("请输入新货名:")
		c.execute("UPDATE SHOP set GOODS_NAME=\"" + data + "\" where GOODS_NAME=\"" + target_goods + "\";")
	elif target_aim == "3":
		data = input("请输入新型号:")
		c.execute("UPDATE SHOP set TYPE=\"" + data + "\" where GOODS_NAME=\"" + target_goods + "\";")
	elif target_aim == "4":
		data = input("请输入新送货价:")
		c.execute("UPDATE SHOP set PRICE=" + data + " where GOODS_NAME=\"" + target_goods + "\";")
	elif target_aim == "5":
		data = input("请输入新库存量:")
		c.execute("UPDATE SHOP set AMOUNT=" + data + " where GOODS_NAME=\"" + target_goods + "\";")
	elif target_aim == "6":
		data = input("请输入新经办人:")
		c.execute("UPDATE SHOP set PERSON_NAME=\"" + data + "\" where GOODS_NAME=\"" + target_goods + "\";")
	else:
		print("输入错误")
	conn.commit()
	print("已成功修改数据")

def query_One_SQL():
	c = conn.cursor()
	#NUMBER,GOODS_NAME,TYPE,PERSON_NAME,PRICE,AMOUNT
	target = input("请输入你要查找的属性:(1-货号，2-货名，3-型号，4-送货价，5-库存量，6-经办人):")
	#print(target)
	if target == "1":
		data = input("请输入你想查找的货号名称:")
		query_All_SQL("NUMBER",data)
	elif target == "2":
		data = input("请输入你想查找的货物名称:")
		query_All_SQL("GOODS_NAME",data)
	elif target == "3":
		data = input("请输入你想查找的型号:")
		query_All_SQL("TYPE",data)
	elif target == "4":
		data = input("请输入你想查找的送货价:")
		query_All_SQL("PRICE",data)
	elif target == "5":
		data = input("请输入你想查找的库存量:")
		query_All_SQL("AMOUNT",data)
	elif target == "6":
		data = input("请输入你想查找的经办人:")
		query_All_SQL("PERSON_NAME",data)
	else:
		print("输入错误")
	
def Count():
	c = conn.cursor()
	choice = input("1.统计每种货物的总价值 2.计算某经办人的货物总数")
	if choice == "1":
		print("总价值\t商品名称")
		query_All_SQL("SUM")
	elif choice == "2":
		print("货号\t货名\t型号\t送货价\t库存量\t经办人")
		query_All_SQL("PERSON")
	print("统计完毕！")

def menu(flag=False):	
	print("---------------------------------------------------------")
	print("----------------------超市商品管理系统----------------------")
	if flag == True:
		print("\t您当前处于管理员模式，可进行所有操作")
	else:
		print("\t您当前处于普通用户模式，仅允许查询和统计操作")
	if flag:
		print("\t\t1— 增 加 商 品")
	print("\t\t2— 显示所有商品")
	if flag:
		print("\t\t3— 删 除 商 品")
		print("\t\t4— 修 改 商 品")
	print("\t\t5— 查询某一商品")
	print("\t\t6— 统 计 商 品")
	print("\t\t7- 切 换 用 户")
	if flag:
		print("\t\t8- 添 加 用 户")
	if flag:
		print("\t\t9- 查询总用户信息")
	if flag:
		print("\t\t10-退出管理权限")
	print("\t\t0- 退 出 系 统")
	print("\t\t   选 择（0-8）")

if __name__ == "__main__":
	try:
		conn = pymysql.connect(host="47.107.43.27",user="root",password="rootpasswd",db="LEARNSQL",port=3306,charset="UTF8")
	except:
		print("连接出现问题，请检查服务器设置！")
		exit(0)
	print("已经成功远程连接到服务器数据库！")
	print("IP=47.107.43.27")
	#Add_User()
	try:	
		Create_Table_User()
		Create_Table()
	except:
		print("已经创建过表！")
	choice = ""
	flag = False
	while choice != "0":
		menu(flag)
		choice = input("请选择:")
		if choice == "1":
			if not flag:
				print("无法执行该操作！")
				continue
			Add_SQL()
		elif choice == "2":
			query_All_SQL()
		elif choice == "3":
			if not flag:
				print("无法执行该操作！")
				continue
			del_SQL()
		elif choice == "4":
			if not flag:
				print("无法执行该操作！")
				continue
			Modify_SQL()
		elif choice == "5":
			query_One_SQL()
		elif choice == "6":
			Count()
		elif choice == "7":
			flag = check_user(flag)
		elif choice == "8":
			if not flag:
				print("无法执行该操作！")
				continue
			Add_User()
		elif choice == "9":
			if not flag:
				print("无法执行该操作！")
				continue
			query_User()
		elif choice == "10":
			if not flag:
				print("您已经是普通用户权限，无法操作！")
				continue
			flag = False
			print("您已成功退出管理用户！")
		else:
			break
	conn.close()
	print("谢谢您的使用，再见👋")
	
