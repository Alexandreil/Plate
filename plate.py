from tkinter import *
import random

def fon():
	y = 0
	while y < 650:
		x = 0
		while x < 650:
			canvas.create_rectangle(x, y, x+60, y+57, outline="#C69515", fill = "#ECD598")
			x+=60
		y+=57
#Функция начала игры, размещаем плиты
def start_click(event):
	plt0.place(x=181, y=140)
	plt1.place(x=241, y=140)
	plt2.place(x=301, y=140)
	plt3.place(x=361, y=140)
	plt4.place(x=181, y=197)
	plt5.place(x=241, y=197)
	plt6.place(x=301, y=197)
	plt7.place(x=361, y=197)
	plt8.place(x=181, y=254)
	plt9.place(x=241, y=254)
	plt10.place(x=301, y=254)
	plt11.place(x=361, y=254)
	plt12.place(x=181, y=311)
	plt13.place(x=241, y=311)
	plt14.place(x=301, y=311)
	plt15.place(x=361, y=311)
	btn1.destroy()
	fon()

def res_click(event):
	fon()
	btn2.destroy()

#Функции для окрашивания плит в случае правильной последовательности и сброс предыдущих ответов в случае ошибки
def click0(event):
	plt0.configure(bg="green")

def click1(event):
	if plt0["bg"] == "green":
		plt1.configure(bg="green")
	else:
		plt0.configure(bg="#E3E0D5")

def click2(event):
	if plt1["bg"] == "green":
		plt2.configure(bg="green")
	else:
		plt0.configure(bg="#E3E0D5")
		plt1.configure(bg="#E3E0D5")

def click3(event):
	if plt2["bg"] == "green":
		plt3.configure(bg="green")
	else:
		plt0.configure(bg="#E3E0D5")
		plt1.configure(bg="#E3E0D5")
		plt2.configure(bg="#E3E0D5")

def click4(event):
	if plt3["bg"] == "green":
		plt4.configure(bg="green")
	else:
		plt0.configure(bg="#E3E0D5")
		plt1.configure(bg="#E3E0D5")
		plt2.configure(bg="#E3E0D5")
		plt3.configure(bg="#E3E0D5")

def click5(event):
	if plt4["bg"] == "green":
		plt5.configure(bg="green")
	else:
		plt0.configure(bg="#E3E0D5")
		plt1.configure(bg="#E3E0D5")
		plt2.configure(bg="#E3E0D5")
		plt3.configure(bg="#E3E0D5")
		plt4.configure(bg="#E3E0D5")

def click6(event):
	if plt5["bg"] == "green":
		plt6.configure(bg="green")
	else:
		plt0.configure(bg="#E3E0D5")
		plt1.configure(bg="#E3E0D5")
		plt2.configure(bg="#E3E0D5")
		plt3.configure(bg="#E3E0D5")
		plt4.configure(bg="#E3E0D5")
		plt5.configure(bg="#E3E0D5")

def click7(event):
	if plt6["bg"] == "green":
		plt7.configure(bg="green")
	else:
		plt0.configure(bg="#E3E0D5")
		plt1.configure(bg="#E3E0D5")
		plt2.configure(bg="#E3E0D5")
		plt3.configure(bg="#E3E0D5")
		plt4.configure(bg="#E3E0D5")
		plt5.configure(bg="#E3E0D5")
		plt6.configure(bg="#E3E0D5")

def click8(event):
	if plt7["bg"] == "green":
		plt8.configure(bg="green")
	else:
		plt0.configure(bg="#E3E0D5")
		plt1.configure(bg="#E3E0D5")
		plt2.configure(bg="#E3E0D5")
		plt3.configure(bg="#E3E0D5")
		plt4.configure(bg="#E3E0D5")
		plt5.configure(bg="#E3E0D5")
		plt6.configure(bg="#E3E0D5")
		plt7.configure(bg="#E3E0D5")

def click9(event):
	if plt8["bg"] == "green":
		plt9.configure(bg="green")
	else:
		plt0.configure(bg="#E3E0D5")
		plt1.configure(bg="#E3E0D5")
		plt2.configure(bg="#E3E0D5")
		plt3.configure(bg="#E3E0D5")
		plt4.configure(bg="#E3E0D5")
		plt5.configure(bg="#E3E0D5")
		plt6.configure(bg="#E3E0D5")
		plt7.configure(bg="#E3E0D5")
		plt8.configure(bg="#E3E0D5")

def click10(event):
	if plt9["bg"] == "green":
		plt10.configure(bg="green")
	else:
		plt0.configure(bg="#E3E0D5")
		plt1.configure(bg="#E3E0D5")
		plt2.configure(bg="#E3E0D5")
		plt3.configure(bg="#E3E0D5")
		plt4.configure(bg="#E3E0D5")
		plt5.configure(bg="#E3E0D5")
		plt6.configure(bg="#E3E0D5")
		plt7.configure(bg="#E3E0D5")
		plt8.configure(bg="#E3E0D5")
		plt9.configure(bg="#E3E0D5")

def click11(event):
	if plt10["bg"] == "green":
		plt11.configure(bg="green")
	else:
		plt0.configure(bg="#E3E0D5")
		plt1.configure(bg="#E3E0D5")
		plt2.configure(bg="#E3E0D5")
		plt3.configure(bg="#E3E0D5")
		plt4.configure(bg="#E3E0D5")
		plt5.configure(bg="#E3E0D5")
		plt6.configure(bg="#E3E0D5")
		plt7.configure(bg="#E3E0D5")
		plt8.configure(bg="#E3E0D5")
		plt9.configure(bg="#E3E0D5")
		plt10.configure(bg="#E3E0D5")

def click12(event):
	if plt11["bg"] == "green":
		plt12.configure(bg="green")
	else:
		plt0.configure(bg="#E3E0D5")
		plt1.configure(bg="#E3E0D5")
		plt2.configure(bg="#E3E0D5")
		plt3.configure(bg="#E3E0D5")
		plt4.configure(bg="#E3E0D5")
		plt5.configure(bg="#E3E0D5")
		plt6.configure(bg="#E3E0D5")
		plt7.configure(bg="#E3E0D5")
		plt8.configure(bg="#E3E0D5")
		plt9.configure(bg="#E3E0D5")
		plt10.configure(bg="#E3E0D5")
		plt11.configure(bg="#E3E0D5")

def click13(event):
	if plt12["bg"] == "green":
		plt13.configure(bg="green")
	else:
		plt0.configure(bg="#E3E0D5")
		plt1.configure(bg="#E3E0D5")
		plt2.configure(bg="#E3E0D5")
		plt3.configure(bg="#E3E0D5")
		plt4.configure(bg="#E3E0D5")
		plt5.configure(bg="#E3E0D5")
		plt6.configure(bg="#E3E0D5")
		plt7.configure(bg="#E3E0D5")
		plt8.configure(bg="#E3E0D5")
		plt9.configure(bg="#E3E0D5")
		plt10.configure(bg="#E3E0D5")
		plt11.configure(bg="#E3E0D5")
		plt12.configure(bg="#E3E0D5")

def click14(event):
	if plt13["bg"] == "green":
		plt14.configure(bg="green")
	else:
		plt0.configure(bg="#E3E0D5")
		plt1.configure(bg="#E3E0D5")
		plt2.configure(bg="#E3E0D5")
		plt3.configure(bg="#E3E0D5")
		plt4.configure(bg="#E3E0D5")
		plt5.configure(bg="#E3E0D5")
		plt6.configure(bg="#E3E0D5")
		plt7.configure(bg="#E3E0D5")
		plt8.configure(bg="#E3E0D5")
		plt9.configure(bg="#E3E0D5")
		plt10.configure(bg="#E3E0D5")
		plt11.configure(bg="#E3E0D5")
		plt12.configure(bg="#E3E0D5")
		plt13.configure(bg="#E3E0D5")

def click15(event):
	if plt14["bg"] == "green":
		plt15.configure(bg="green")
	else:
		plt0.configure(bg="#E3E0D5")
		plt1.configure(bg="#E3E0D5")
		plt2.configure(bg="#E3E0D5")
		plt3.configure(bg="#E3E0D5")
		plt4.configure(bg="#E3E0D5")
		plt5.configure(bg="#E3E0D5")
		plt6.configure(bg="#E3E0D5")
		plt7.configure(bg="#E3E0D5")
		plt8.configure(bg="#E3E0D5")
		plt9.configure(bg="#E3E0D5")
		plt10.configure(bg="#E3E0D5")
		plt11.configure(bg="#E3E0D5")
		plt12.configure(bg="#E3E0D5")
		plt13.configure(bg="#E3E0D5")
		plt14.configure(bg="#E3E0D5")
	if plt15["bg"] == "green":
		plt0.destroy()
		plt1.destroy()
		plt2.destroy()
		plt3.destroy()
		plt4.destroy()
		plt5.destroy()
		plt6.destroy()
		plt7.destroy()
		plt8.destroy()
		plt9.destroy()
		plt10.destroy()
		plt11.destroy()
		plt12.destroy()
		plt13.destroy()
		plt14.destroy()
		plt15.destroy()
		canvas.create_text(303, 260, text = win, fill = "black", font =("Helvetica", "28"))
		btn2.place(x=216, y=342)

root = Tk()

#Имя проекта
root.title("Порядок")
#Создаем холст
canvas = Canvas(root, width = 600, height = 600, bg = "#E6C67D")
canvas.pack()

#Вступительный текст и конечный
text = '''Рад Вас видеть в моей мини игре “Порядок”.

 Смысл игры заключается в том, что необходимо нажать
на плитки в порядке возрастания (от 1 до n-го числа).
Для интереса, Вы будете ограничены во времени.
Замечание: эта игра поможет Вам развить Ваше внимание.

Приятной игры!'''
win = '''Ты победил!'''
canvas.create_text(330, 260, text = text, fill = "black", font =("Helvetica", "14"))

#Создаем плитки с номерами 
plt0 = Button(root, text = "1", width = 7, height = 3, bg = "#E3E0D5")
plt1 = Button(root, text = "2", width = 7, height = 3, bg = "#E3E0D5")
plt2 = Button(root, text = "3", width = 7, height = 3, bg = "#E3E0D5")
plt3 = Button(root, text = "4", width = 7, height = 3, bg = "#E3E0D5")
plt4 = Button(root, text = "5", width = 7, height = 3, bg = "#E3E0D5")
plt5 = Button(root, text = "6", width = 7, height = 3, bg = "#E3E0D5")
plt6 = Button(root, text = "7", width = 7, height = 3, bg = "#E3E0D5")
plt7 = Button(root, text = "8", width = 7, height = 3, bg = "#E3E0D5")
plt8 = Button(root, text = "9", width = 7, height = 3, bg = "#E3E0D5")
plt9 = Button(root, text = "10", width = 7, height = 3, bg = "#E3E0D5")
plt10 = Button(root, text = "11", width = 7, height = 3, bg = "#E3E0D5")
plt11 = Button(root, text = "12", width = 7, height = 3, bg = "#E3E0D5")
plt12 = Button(root, text = "13", width = 7, height = 3, bg = "#E3E0D5")
plt13 = Button(root, text = "14", width = 7, height = 3, bg = "#E3E0D5")
plt14 = Button(root, text = "15", width = 7, height = 3, bg = "#E3E0D5")
plt15 = Button(root, text = "16", width = 7, height = 3, bg = "#E3E0D5")

#В случае нажатия на плитку вызываем функцию
plt0.bind("<Button-1>", click0)
plt1.bind("<Button-1>", click1)
plt2.bind("<Button-1>", click2)
plt3.bind("<Button-1>", click3)
plt4.bind("<Button-1>", click4)
plt5.bind("<Button-1>", click5)
plt6.bind("<Button-1>", click6)
plt7.bind("<Button-1>", click7)
plt8.bind("<Button-1>", click8)
plt9.bind("<Button-1>", click9)
plt10.bind("<Button-1>", click10)
plt11.bind("<Button-1>", click11)
plt12.bind("<Button-1>", click12)
plt13.bind("<Button-1>", click13)
plt14.bind("<Button-1>", click14)
plt15.bind("<Button-1>", click15)

#Создаем кнопку начала игры
btn1 = Button(root, text = "Начать игру", width = 10, height = 1, bg = "#CA9B1E")
btn1.place(x=248, y=542)
btn1.bind("<Button-1>", start_click)

btn2 = Button(root, width = 10, height = 1, bg = "#CA9B1E", text = "Повторить", font =("Helvetica", "20"))
btn2.bind("<Button-1>", res_click)

root.mainloop()
