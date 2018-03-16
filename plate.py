from tkinter import *
import random

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
	btn1.grid_forget()
	y = 0
	while y < 650:
		x = 0
		while x < 650:
			canvas.create_rectangle(x, y, x+60, y+57, outline="#C69515", fill = "#ECD598")
			x+=60
		y+=57

root = Tk()

#Имя проекта
root.title("Порядок")
#Создаем холст
canvas = Canvas(root, width = 600, height = 600, bg = "#E6C67D")
canvas.pack()

#Вступительный текст
text = '''Рад Вас видеть в моей мини игре “Порядок”.

 Смысл игры заключается в том, что необходимо нажать
на плитки в порядке возрастания (от 1 до n-го числа).
Для интереса, Вы будете ограничены во времени.
Замечание: эта игра поможет Вам развить Ваше внимание.

Приятной игры!'''
canvas.create_text(330, 260, text = text, fill = "#EAECFF", font =("Helvetica", "14"))

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

#Создаем кнопку начала игры
btn1 = Button(root, text = "Начать игру", width = 10, height = 1, bg = "#CA9B1E")
btn1.place(x=248, y=542)
btn1.bind("<Button-1>", start_click)

root.mainloop()