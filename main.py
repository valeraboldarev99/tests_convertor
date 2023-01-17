import csv;
import numpy as np;
import re;
from tkinter import *;
import time;

def find_answer():											#поиск ответов
	file = list(csv.reader(open("test_csv.csv")));			#файл с вопросами
	questions_list = [];
	for row in file:										#пройти по файлу вопросов и добавлени е их в массив
		questions_list.append(row);

	answer_num = 1;
	for i in range(0, len(questions_list)):
		quest = questions_list[i][0].split(";");			#разделяем по ;, запятые нужно убрать
		itere = 0;
		file_answers = open("test_answers.csv", "a");		#файл с ответами
		for j in quest:										#пройдем по вопросам
			if(str(j).find('+**') != -1):					#правильный ответ (в конце варианта +**), проверить чтобы внутри вопросов не было +
				file_answers.write(str(itere) + '; \n');	#запись ответов в файл

			itere = itere + 1;								#номер варианта
		answer_num = answer_num + 1;						#номер вопроса
	status_list.insert(END, 'Готово - Записано - ' + str(answer_num - 1) + ' ответов');

def convert_to_csv():										#из txt в csv
	file = open("test_csv.csv", "a");						#файл для записи
	txt = open('test_txt.txt', 'r', encoding='utf-8');		#файл для чтения вопросов

	with open('test_txt.txt', 'r', encoding='utf-8') as txt:	#считываем вопросы и записываем в questions
		questions = txt.readlines();

	splits = np.array_split(questions, len(questions));		#порезать на кол-во вопросов, в конце списка не должно быть пустых строк
	str_num = 1;
	for split in splits:									#проходим по вопросам
		for spp in split:									#проход внутри вопроса по самому вопросу и вариантам ответов
			try:
				file.write(str(spp));						#запись в файл
			except Exception as e:
				status_list.insert(END, 'Ошибка при конвертировании строки - ' + str(str_num));
			str_num = str_num + 1;																	#номер строки
	status_list.insert(END, 'Готово - Записано - ' + str(str_num - 1) + ' вопросов');
	file.close();

def clear_label():											#очистить облать
	status_list.delete(0, END);

def clear_file_questions():									#очистить файл вопросов
	file_questions = open("test_csv.csv", "w");
	file_questions.write('');
	file_questions.close();
	status_list.insert(END, 'Готово - файл очищен');

def clear_file_answers():									#очистить файл ответов
	file_questions = open("test_answers.csv", "w");
	file_questions.write('');
	file_questions.close();
	status_list.insert(END, 'Готово - файл очищен');

window = Tk();
window.geometry("640x270");
window.title("Test convertor txt-to-csv")
window.configure(bg='orange');
button1 = Button(text = "Найти ответы", command = find_answer);
button1.place(x = 30, y = 10, width = 90, height = 25);
button2 = Button(text = "Конвертировать", command = convert_to_csv);
button2.place(x = 150, y = 10, width = 100, height = 25);
button3 = Button(text = "Очистить окно", command = clear_label);
button3.place(x = 280, y = 10, width = 100, height = 25);
button4 = Button(text = "Очистить файл вопросов", command = clear_file_questions);
button4.place(x = 410, y = 10, width = 160, height = 25);
button5 = Button(text = "Очистить файл ответов", command = clear_file_answers);
button5.place(x = 410, y = 45, width = 160, height = 25);
label3 = Label(text = "File: ");
label3.configure(bg='orange');
label3.place(x = 30, y = 60);
status_list = Listbox();
status_list.place(x = 30, y = 80, width = 570, height = 150);
window.mainloop();

