import base64
import os
from random import shuffle, choices

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__, template_folder=os.getcwd()+"/client", static_folder=os.getcwd()+"/client")
import sqlite3

conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()
images = []
imagesPath = "client/img/"
for image in os.listdir(imagesPath):
    if image != "background.png":
        images.append(imagesPath+image)
print(images)
# cursor.execute('''CREATE TABLE your_table (question TEXT, option1 TEXT, option2 TEXT, option3 TEXT, option4 TEXT, answer TEXT, image BLOB)''')
db = [
["Какого цвета звезды на флаге Новой Зеландии?", "Белый", "Красный", "Синий", "Желтый", "Белый", images[0]],
["В центре какого флага изображено 24-спицевое колесо Ашока Чахра?", "Индия", "Шри-Ланка", "Бангладеш", "Пакистан",
 "Индия", images[1]],
["Как называется культовое здание на камбоджийском флаге?", "Пагода Шве Дагон", "Ангкор-Ват", "Фусими Инари Тайша",
 "Джокьякарта", "Пагода Шве Дагон", images[2]],
["Флаг какой страны содержит самую большую звезду из всех флагов мира?", "Центральноафриканская Республика",
 "Суринам", "Мьянма", "Йемен", "Мьянма", images[3]],
["На каком флаге изображен черный двуглавый орел на красном фоне?", "Албания", "Албания", "Албания", "Албания",
 "Албания", images[4]],
["Флаг какой страны является единственным в мире, кроме прямоугольника или квадрата?", "Непал", "Непал", "Непал",
 "Непал", "Непал", images[5]],
["Какой единственный штат США имеет флаг с изображением Юнион Джек?", "Нью-Гэмпшир", "Род-Айленд", "Массачусетс",
 "Гавайи", "Массачусетс", images[6]],
["Флаг Брунея состоит из желтого, белого, красного и какого другого цвета?", "Чёрный", "Чёрный", "Чёрный", "Чёрный",
 "Чёрный", images[7]]
]

cursor.executemany("INSERT INTO your_table VALUES (?, ?, ?, ?, ?, ?, ?)", db)



@app.route('/', methods=['GET', 'POST'])
def home():
    shuffle(db)
    return render_template('/html/index.html', questions=db)

@app.route('/calc')
def calc():
    return render_template('/html/calculation.html')

@app.route('/calculated')
def calculated():
    result = request.form
    return render_template('/html/calculation.html', result=result)

@app.route('/results', methods=['GET', 'POST'])
def submit_form():
    data = request.form
    return f"Success, with  {data}"

@app.route('/quiz-results', methods=['GET', 'POST'])
def page2():
    answers = []
    counts = 0
    for question in db:
        answers.append(request.form.get(question[0]))
        if request.form.get(question[0]) is not None:
            if request.form.get(question[0]) == question[5]:
                counts += 1
    # return f"Your correct answers is {counts}/{len(db)}"
    return render_template("/html/index2.html", correct=f"{counts}/{len(db)}")


if __name__ == '__main__':
    app.run(port=8888)
