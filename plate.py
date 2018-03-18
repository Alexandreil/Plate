from tkinter import *
import random

def rin():
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
	plt15.configure(bg="#E3E0D5")

def fon():
	y = 0
	while y < 650:
		x = 0
		while x < 650:
			canvas.create_rectangle(x, y, x+60, y+57, outline="#C69515", fill = "#ECD598")
			x+=60
		y+=57
#Функция начала игры, рандомно размещаем плиты
def start_click():
	x1=random.choice(x)
	y1=random.choice(y)
	if x1 == 181:
		x2 = x1 + 60
		x3 = x2 + 60
		x4 = x3 + 60
	if x1 == 241:
		x2 = x1 - 60
		x3 = x1 + 60
		x4 = x3 + 60
	if x1 == 301:
		x2 = x1 - 60
		x3 = x2 - 60
		x4 = x1 + 60
	if x1 == 361:
		x3 = x1 - 60
		x2 = x3 - 60
		x4 = x2 - 60
	if y1 == 140:
		y2 = y1 + 57
		y3 = y2 + 57
		y4 = y3 + 57
	if y1 == 197:
		y2 = y1 - 57
		y3 = y1 + 57
		y4 = y3 + 57
	if y1 == 254:
		y2 = y1 - 57
		y3 = y2 - 57
		y4 = y1 + 57
	if y1 == 311:
		y3 = y1 - 60
		y2 = y3 - 60
		y4 = y2 - 60
	plt0.place(x=x1, y=y1)
	plt1.place(x=x3, y=y3)
	plt2.place(x=x2, y=y2)
	plt3.place(x=x4, y=y4) 
	plt4.place(x=x2, y=y1)
	plt5.place(x=x3, y=y2)
	plt6.place(x=x4, y=y3)
	plt7.place(x=x2, y=y4)
	plt8.place(x=x2, y=y3)
	plt9.place(x=x1, y=y4)
	plt10.place(x=x4, y=y2)
	plt11.place(x=x3, y=y1)
	plt12.place(x=x1, y=y2)
	plt13.place(x=x3, y=y4)
	plt14.place(x=x1, y=y3)
	plt15.place(x=x4, y=y1)
	btn1.destroy()

	fon()

#Функции для окрашивания плит в случае правильной последовательности и сброс предыдущих ответов в случае ошибки
def click0():
	plt0.configure(bg="green")

def click1():
	if plt0["bg"] == "green":
		plt1.configure(bg="green")
	else:
		plt0.configure(bg="#E3E0D5")

def click2():
	if plt1["bg"] == "green":
		plt2.configure(bg="green")
	else:
		rin()

def click3():
	if plt2["bg"] == "green":
		plt3.configure(bg="green")
	else:
		rin()

def click4():
	if plt3["bg"] == "green":
		plt4.configure(bg="green")
	else:
		rin()

def click5():
	if plt4["bg"] == "green":
		plt5.configure(bg="green")
	else:
		rin()

def click6():
	if plt5["bg"] == "green":
		plt6.configure(bg="green")
	else:
		rin()

def click7():
	if plt6["bg"] == "green":
		plt7.configure(bg="green")
	else:
		rin()

def click8():
	if plt7["bg"] == "green":
		plt8.configure(bg="green")
	else:
		rin()

def click9():
	if plt8["bg"] == "green":
		plt9.configure(bg="green")
	else:
		rin()

def click10():
	if plt9["bg"] == "green":
		plt10.configure(bg="green")
	else:
		rin()

def click11():
	if plt10["bg"] == "green":
		plt11.configure(bg="green")
	else:
		rin()

def click12():
	if plt11["bg"] == "green":
		plt12.configure(bg="green")
	else:
		rin()

def click13():
	if plt12["bg"] == "green":
		plt13.configure(bg="green")
	else:
		rin()

def click14():
	if plt13["bg"] == "green":
		plt14.configure(bg="green")
	else:
		rin()

def click15():
	if plt14["bg"] == "green":
		start_click()
		rin()
	else:
		rin()

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
canvas.create_text(330, 260, text = text, fill = "black", font =("Helvetica", "14"))

#Необходимые координаты
x=[181, 241, 301, 361]
y=[140, 197, 254, 311]
#Создаем плитки с номерами 
plt0 = Button(root, text = "1", width = 7, height = 3, bg = "#E3E0D5", command =  click0)
plt1 = Button(root, text = "2", width = 7, height = 3, bg = "#E3E0D5", command =  click1)
plt2 = Button(root, text = "3", width = 7, height = 3, bg = "#E3E0D5", command =  click2)
plt3 = Button(root, text = "4", width = 7, height = 3, bg = "#E3E0D5", command =  click3)
plt4 = Button(root, text = "5", width = 7, height = 3, bg = "#E3E0D5", command =  click4)
plt5 = Button(root, text = "6", width = 7, height = 3, bg = "#E3E0D5", command =  click5)
plt6 = Button(root, text = "7", width = 7, height = 3, bg = "#E3E0D5", command =  click6)
plt7 = Button(root, text = "8", width = 7, height = 3, bg = "#E3E0D5", command =  click7)
plt8 = Button(root, text = "9", width = 7, height = 3, bg = "#E3E0D5", command =  click8)
plt9 = Button(root, text = "10", width = 7, height = 3, bg = "#E3E0D5", command =  click9)
plt10 = Button(root, text = "11", width = 7, height = 3, bg = "#E3E0D5", command =  click10)
plt11 = Button(root, text = "12", width = 7, height = 3, bg = "#E3E0D5", command =  click11)
plt12 = Button(root, text = "13", width = 7, height = 3, bg = "#E3E0D5", command =  click12)
plt13 = Button(root, text = "14", width = 7, height = 3, bg = "#E3E0D5", command =  click13)
plt14 = Button(root, text = "15", width = 7, height = 3, bg = "#E3E0D5", command =  click14)
plt15 = Button(root, text = "16", width = 7, height = 3, bg = "#E3E0D5", command =  click15)


#Создаем кнопку начала игры
btn1 = Button(root, text = "Начать игру", width = 10, height = 1, bg = "#CA9B1E", command = start_click)
btn1.place(x=248, y=542)

root.mainloop()
