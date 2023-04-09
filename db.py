import sqlite3
# Создание базы данных bloggers.db
conn = sqlite3.connect('bloggers.db')
cur = conn.cursor()
# Создание таблицы для Блогера(id, имя, фамилия, никнейм, работа, ссылка на фото)
cur.execute("""CREATE TABLE BLOGGER (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  secname TEXT NOT NULL,
  username TEXT NOT NULL,
  job TEXT NOT NULL,
  photo TEXT NOT NULL
);
""")
conn.commit()
# Создание таблицы для Постов(id, id блогера, название, текст, дата)
# Есть зависимость от id блогера из таблицы BLOGGER
cur.execute('''CREATE TABLE POST
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             blogger_id INTEGER,
             title TEXT NOT NULL,
             description TEXT NOT NULL,
             date TEXT NOT NULL,
             FOREIGN KEY (blogger_id) REFERENCES BLOGER(id))''')

conn.commit()

# Заполнение блогеров
insertBloggers = 'INSERT INTO BLOGGER (id, name, secname, username, job, photo) values(?, ?, ?, ?, ?, ?)'
blogers = [
    (0,'Сантьяго','Дребов','devil2014','Дизайнер','https://photo1'),
    (1,'Антон','Андреев','kwazimodo24','Программист','https://photo2'),
    (2,'Ксения','Владимирова','ksiva84','Системный администратор','https://photo3'),
    (3,'Валентин','Кириешкин','buzzlighter','Администратор баз данных','https://photo4')
]
with conn:
    conn.executemany(insertBloggers, blogers)
# Заполнение постов
insertPosts = 'INSERT INTO POST (id, blogger_id, title, description, date) values(?, ?, ?, ?, ?)'
posts = [
    (0, 0, 'Пост Дребов 1', 'Lorem ipsum dolor sit amet', '2023-04-07T15:16:10+00:00'),
    (1, 0, 'Пост Дребов 2', 'Lorem ipsum dolor sit amet', '2023-04-07T15:16:10+00:00'),
    (2, 1, 'Пост Андреев 1', 'Lorem ipsum dolor sit amet', '2023-04-07T15:16:10+00:00'),
    (3, 1, 'Пост Андреев 2', 'Lorem ipsum dolor sit amet', '2023-04-07T15:16:10+00:00'),
    (4, 2, 'Пост Владиморова 1', 'Lorem ipsum dolor sit amet', '2023-04-07T15:16:10+00:00'),
    (5, 3, 'Пост Кириешкин 1', 'Lorem ipsum dolor sit amet', '2023-04-07T15:16:10+00:00'),
]

with conn:
    conn.executemany(insertPosts, posts)