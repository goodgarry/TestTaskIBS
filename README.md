# IBSTestTask
Тестовое задание для стажировки МИП "Интернет-Бизнес-Системы"

Задание:

Необходимо средствами языка Python и одного из фреймворков FastAPI (лучше всего) или
Django реализовать сервис, который возвращает набор данных в json-формате по http(s)
запросу, пригодный для отображения такой страницы:
https://www.figma.com/file/QOHXuTHr6hKChqiTw6KEmY/front-test-task


Сервис развернут на площадке Render: 
- https://ibstask-antonov.onrender.com/docs


Реализация:

1) Для хранения данных была использована база данных SQLite, создание таблиц и их заполнение находится в файле db.py
Было создано две таблицы:

#### Таблица BLOGGER

id|name|secname|username|job|photo
---: | :---: | :---: | :---: | :---:| :---:
0|Сантьяго|Дребов|devil2014|Дизайнер|https://photo1
1|Антон|Андреев|kwazimodo24|Программист|https://photo2
2|Ксения|Владимирова|ksiva84|Системный администратор|https://photo3
3|Валентин|Кириешкин|buzzlighter|Администратор баз данных|https://photo4


#### Таблица POST

id | blogger_id | title | description | date
---: | ---: | :---: | :---: | ---
0| 0| Пост Дребов 1| Lorem ipsum dolor sit amet| 12.01.2002
1| 0| Пост Дребов 2| Lorem ipsum dolor sit amet| 13.01.2002
2| 1| Пост Андреев 1| Lorem ipsum dolor sit amet| 12.02.2002
3| 1| Пост Андреев 2| Lorem ipsum dolor sit amet| 13.02.2002
4| 2| Пост Владиморова 1| Lorem ipsum dolor sit amet| 12.03.2002
5| 3| Пост Кириешкин 1| Lorem ipsum dolor sit amet| 13.04.2002

Есть зависимость между таблицей POST и BLOGER через blogger_id( id в таблице BLOGGER)

База данных представлена в файле bloggers.db

2) Для реализации GET-запроса была использована библиотека FastAPI.
   Извлечение данных происходит с помощью SQL-запросов к базе данных SQLite. 
   Метод для GET-запроса представлен в файле api.py.
   
#### Метод get_blogger(blogLimit, postLimit, orderBy, direction):
 - blogLimit - количество требуемых блогеров(по умолчанию - 2)
 - postLimit - количество требуемых постов(по умолчанию - 2)
 - orderBy - столбец базы данных для сортировки(по умолчанию - никнейм)
 - direction - направление сортировки (ASC - по возрастанию, DESC - по убыванию, по умолчанию - ASC)
  
 #### Примеры запросов:
- Вывести трех блогеров с одним постом у каждого, отсортировать по имени по возрастанию:
http://ibstask-antonov.onrender.com/bloggers/?blogLimit=3&postLimit=1&orderBy=name&direction=ASC
- Вывести двух блогеров с двумя постами у каждого, отсортировать по никнейму по убыванию:
 http://ibstask-antonov.onrender.com/bloggers/?direction=DESC
