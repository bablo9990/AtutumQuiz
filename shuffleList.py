import os
from random import choices, shuffle

images = []
imagesPath = "client/img/"
for image in os.listdir(imagesPath):
    if image != "background.png":
        images.append(imagesPath+image)
print(images)
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