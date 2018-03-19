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
	plt16.configure(bg="#E3E0D5")
	plt17.configure(bg="#E3E0D5")
	plt18.configure(bg="#E3E0D5")
	plt19.configure(bg="#E3E0D5")
	plt20.configure(bg="#E3E0D5")
	plt21.configure(bg="#E3E0D5")
	plt22.configure(bg="#E3E0D5")
	plt23.configure(bg="#E3E0D5")
	plt24.configure(bg="#E3E0D5")
	plt25.configure(bg="#E3E0D5")
	plt26.configure(bg="#E3E0D5")
	plt27.configure(bg="#E3E0D5")
	plt28.configure(bg="#E3E0D5")
	plt29.configure(bg="#E3E0D5")
	plt30.configure(bg="#E3E0D5")
	plt31.configure(bg="#E3E0D5")

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
	if x1 == 61:
		x2 = x1 + 60
		x3 = x2 + 60
		x4 = x3 + 60
		x5 = x4 + 60
		x6 = x5 + 60
		x7 = x6 + 60
		x8 = x7 + 60
	if x1 == 121:
		x2 = x1 - 60
		x3 = x1 + 60
		x4 = x3 + 60
		x5 = x4 + 60
		x6 = x5 + 60
		x7 = x6 + 60
		x8 = x7 + 60
	if x1 == 181:
		x2 = x1 - 60
		x3 = x2 - 60
		x4 = x1 + 60
		x5 = x4 + 60
		x6 = x5 + 60
		x7 = x6 + 60
		x8 = x7 + 60
	if x1 == 241:
		x2 = x1 - 60
		x3 = x2 - 60
		x4 = x3 - 60
		x5 = x1 + 60
		x6 = x5 + 60
		x7 = x6 + 60
		x8 = x7 + 60
	if x1 == 301:
		x2 = x1 - 60
		x3 = x2 - 60
		x4 = x3 - 60
		x5 = x4 - 60
		x6 = x1 + 60
		x7 = x6 + 60
		x8 = x7 + 60
	if x1 == 361:
		x2 = x1 - 60
		x3 = x2 - 60
		x4 = x3 - 60
		x5 = x4 - 60
		x6 = x5 - 60
		x7 = x1 + 60
		x8 = x7 + 60
	if x1 == 421:
		x2 = x1 - 60
		x3 = x2 - 60
		x4 = x3 - 60
		x5 = x4 - 60
		x6 = x5 - 60
		x7 = x6 - 60
		x8 = x1 + 60
	if x1 == 481:
		x2 = x1 - 60
		x3 = x2 - 60
		x4 = x3 - 60
		x5 = x4 - 60
		x6 = x5 - 60
		x7 = x6 - 60
		x8 = x7 - 60 
	if y1 == 36:
		y2 = y1 + 57
		y3 = y2 + 57
		y4 = y3 + 57
		y5 = y4 + 57
		y6 = y5 + 57
		y7 = y6 + 57
		y8 = y7 + 57
	if y1 == 93:
		y2 = y1 - 57
		y3 = y1 + 57
		y4 = y3 + 57
		y5 = y4 + 57
		y6 = y5 + 57
		y7 = y6 + 57
		y8 = y7 + 57  
	if y1 == 140:
		y2 = y1 - 57
		y3 = y2 - 57
		y4 = y1 + 57
		y5 = y4 + 57
		y6 = y5 + 57
		y7 = y6 + 57
		y8 = y7 + 57
	if y1 == 197:
		y2 = y1 - 57
		y3 = y2 - 57
		y4 = y3 - 57
		y5 = y1 + 57
		y6 = y5 + 57
		y7 = y6 + 57
		y8 = y7 + 57
	if y1 == 254:
		y2 = y1 - 57
		y3 = y2 - 57
		y4 = y3 - 57
		y5 = y4 - 57
		y6 = y1 + 57
		y7 = y6 + 57
		y8 = y7 + 57
	if y1 == 311:
		y2 = y1 - 57
		y3 = y2 - 57
		y4 = y3 - 57
		y5 = y4 - 57
		y6 = y5 - 57
		y7 = y1 + 57
		y8 = y7 + 57
	if y1 == 368:
		y2 = y1 - 57
		y3 = y2 - 57
		y4 = y3 - 57
		y5 = y4 - 57
		y6 = y5 - 57
		y7 = y6 - 57
		y8 = y1 + 57
	if y1 == 425:
		y2 = y1 - 57
		y3 = y2 - 57
		y4 = y3 - 57
		y5 = y4 - 57
		y6 = y5 - 57
		y7 = y6 - 57
		y8 = y7 - 57

	
	plt0.place(x=x1, y=y5)
	plt1.place(x=x3, y=y7)
	plt2.place(x=x2, y=y2)
	plt3.place(x=x4, y=y8)

	plt4.place(x=x2, y=y1)
	plt5.place(x=x3, y=y6)
	plt6.place(x=x4, y=y7)
	plt7.place(x=x2, y=y4)

	plt8.place(x=x2, y=y7)
	plt9.place(x=x1, y=y4)
	plt10.place(x=x4, y=y2)
	plt11.place(x=x3, y=y1)

	plt12.place(x=x1, y=y2)
	plt13.place(x=x3, y=y4)
	plt14.place(x=x1, y=y7)
	plt15.place(x=x4, y=y5)

	plt16.place(x=x5, y=y6)
	plt17.place(x=x7, y=y1)
	plt18.place(x=x6, y=y3)
	plt19.place(x=x8, y=y8)

	plt20.place(x=x6, y=y5)
	plt21.place(x=x7, y=y4)
	plt22.place(x=x8, y=y3)
	plt23.place(x=x6, y=y6)

	plt24.place(x=x6, y=y8)
	plt25.place(x=x5, y=y5)
	plt26.place(x=x8, y=y2)
	plt27.place(x=x7, y=y3)

	plt28.place(x=x5, y=y3)
	plt29.place(x=x7, y=y8)
	plt30.place(x=x5, y=y7)
	plt31.place(x=x8, y=y5)

	plt32.place(x=x1, y=y1)
	plt33.place(x=x3, y=y3)
	plt34.place(x=x2, y=y6)
	plt35.place(x=x4, y=y4)

	plt36.place(x=x2, y=y5)
	plt37.place(x=x3, y=y2)
	plt38.place(x=x4, y=y3)
	plt39.place(x=x2, y=y8)

	plt40.place(x=x2, y=y3)
	plt41.place(x=x1, y=y8)
	plt42.place(x=x4, y=y6)
	plt43.place(x=x3, y=y5)

	plt44.place(x=x1, y=y6)
	plt45.place(x=x3, y=y8)
	plt46.place(x=x1, y=y3)
	plt47.place(x=x4, y=y1)

	plt48.place(x=x5, y=y2)
	plt49.place(x=x7, y=y5)
	plt50.place(x=x6, y=y7)
	plt51.place(x=x8, y=y4)

	plt52.place(x=x6, y=y1)
	plt53.place(x=x7, y=y2)
	plt54.place(x=x8, y=y7)
	plt55.place(x=x6, y=y2)

	plt56.place(x=x6, y=y4)
	plt57.place(x=x5, y=y1)
	plt58.place(x=x8, y=y6)
	plt59.place(x=x7, y=y7)

	plt60.place(x=x5, y=y4)
	plt61.place(x=x7, y=y6)
	plt62.place(x=x5, y=y8)
	plt63.place(x=x8, y=y1)
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
		plt15.configure(bg="green")
	else:
		rin()

def click16():
	if plt15["bg"] == "green":
		plt16.configure(bg="green")
	else:
		rin()

def click17():
	if plt16["bg"] == "green":
		plt17.configure(bg="green")
	else:
		rin()

def click18():
	if plt17["bg"] == "green":
		plt18.configure(bg="green")
	else:
		rin()

def click19():
	if plt18["bg"] == "green":
		plt19.configure(bg="green")
	else:
		rin()

def click20():
	if plt19["bg"] == "green":
		plt20.configure(bg="green")
	else:
		rin()

def click21():
	if plt20["bg"] == "green":
		plt21.configure(bg="green")
	else:
		rin()

def click22():
	if plt21["bg"] == "green":
		plt22.configure(bg="green")
	else:
		rin()

def click23():
	if plt22["bg"] == "green":
		plt23.configure(bg="green")
	else:
		rin()

def click24():
	if plt23["bg"] == "green":
		plt24.configure(bg="green")
	else:
		rin()

def click25():
	if plt24["bg"] == "green":
		plt25.configure(bg="green")
	else:
		rin()

def click26():
	if plt25["bg"] == "green":
		plt26.configure(bg="green")
	else:
		rin()

def click27():
	if plt26["bg"] == "green":
		plt27.configure(bg="green")
	else:
		rin()

def click28():
	if plt27["bg"] == "green":
		plt28.configure(bg="green")
	else:
		rin()

def click29():
	if plt28["bg"] == "green":
		plt29.configure(bg="green")
	else:
		rin()

def click30():
	if plt29["bg"] == "green":
		plt30.configure(bg="green")
	else:
		rin()

def click31():
	if plt30["bg"] == "green":
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
x=[61 ,121 ,181, 241, 301, 361, 421, 481] 
y=[36, 93, 140, 197, 254, 311, 368, 425]
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
plt16 = Button(root, text = "17", width = 7, height = 3, bg = "#E3E0D5", command =  click16)
plt17 = Button(root, text = "18", width = 7, height = 3, bg = "#E3E0D5", command =  click17)
plt18 = Button(root, text = "19", width = 7, height = 3, bg = "#E3E0D5", command =  click18)
plt19 = Button(root, text = "20", width = 7, height = 3, bg = "#E3E0D5", command =  click19)
plt20 = Button(root, text = "21", width = 7, height = 3, bg = "#E3E0D5", command =  click20)
plt21 = Button(root, text = "22", width = 7, height = 3, bg = "#E3E0D5", command =  click21)
plt22 = Button(root, text = "23", width = 7, height = 3, bg = "#E3E0D5", command =  click22)
plt23 = Button(root, text = "24", width = 7, height = 3, bg = "#E3E0D5", command =  click23)
plt24 = Button(root, text = "25", width = 7, height = 3, bg = "#E3E0D5", command =  click24)
plt25 = Button(root, text = "26", width = 7, height = 3, bg = "#E3E0D5", command =  click25)
plt26 = Button(root, text = "27", width = 7, height = 3, bg = "#E3E0D5", command =  click26)
plt27 = Button(root, text = "28", width = 7, height = 3, bg = "#E3E0D5", command =  click27)
plt28 = Button(root, text = "29", width = 7, height = 3, bg = "#E3E0D5", command =  click28)
plt29 = Button(root, text = "30", width = 7, height = 3, bg = "#E3E0D5", command =  click29)
plt30 = Button(root, text = "31", width = 7, height = 3, bg = "#E3E0D5", command =  click30)
plt31 = Button(root, text = "32", width = 7, height = 3, bg = "#E3E0D5", command =  click31)

plt32 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt33 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt34 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt35 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt36 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt37 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt38 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt39 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt40 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt41 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt42 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt43 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt44 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt45 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt46 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt47 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt48 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt49 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt50 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt51 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt52 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt53 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt54 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt55 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt56 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt57 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt58 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt59 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt60 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt61 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt62 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")
plt63 = Button(root, text = "", width = 7, height = 3, bg = "#E3E0D5")


#Создаем кнопку начала игры
btn1 = Button(root, text = "Начать игру", width = 10, height = 1, bg = "#CA9B1E", command = start_click)
btn1.place(x=248, y=542)

root.mainloop()
