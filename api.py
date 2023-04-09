from fastapi import FastAPI
import fastapi
from fastapi.responses import JSONResponse
import sqlite3

app = FastAPI()

# Хранение данных происходит с помощью базы данных SQLite,
# создание таблиц и заполнение находится в файле db.py

# Метод get_blogger(blogLimit, postLimit, orderBy, direction):
# blogLimit - количество требуемых блогеров(по умолчанию - 2)
# postLimit - количество требуемых постов(по умолчанию - 2)
# orderBy - столбец для сортировки(по умолчанию - никнейм)
# direction - направление сортировки (ASC - по возрастанию, DESC - по убыванию, по умолчанию - ASC)

# Примеры запросов:
# Вывести трех блогеров с одним постом у каждого, отсортировать по имени по возрастанию
# http://127.0.0.1:8000/bloggers/?blogLimit=3&postLimit=1&orderBy=name&direction=ASC
# Вывести двух блогеров с двумя постами у каждого, отсортировать по никнейму по убыванию
# http://127.0.0.1:8000/bloggers/?direction=DESC


@app.get("/bloggers/")
def get_blogger(blogLimit: int = fastapi.Query(default=2, description='Количество блогеров'),
                postLimit: int = fastapi.Query(default=2, description='Количество постов'),
                orderBy: str = fastapi.Query(default="username", description='Название столбца для сортировки'),
                direction: str = fastapi.Query(default="ASC", description='Направление сортировки(ASC/DESC)')):
    # Подключение к базе данных
    conn = sqlite3.connect('bloggers.db')
    cur = conn.cursor()
    # Запрос в таблицу BLOGGER
    cur.execute(f"SELECT id, name, secname, username, job, photo FROM BLOGGER ORDER BY {orderBy} {direction} LIMIT {blogLimit} ")
    bloggers = []
    for row in cur.fetchall():
        # Запрос в таблицу POST
        id, name, secname, username, job, photo = row
        cur.execute(f"SELECT id, blogger_id, title, description, date FROM POST WHERE blogger_id={id} LIMIT {postLimit}")
        posts = []
        for row in cur.fetchall():
            id, blogger_id, title, description, date = row
            posts.append({"title": title, "description": description, "date": date})
        blogger = {"id": id, "name": name, "secname":secname, "username": username, "job": job, "photo": photo, "posts":posts}
        bloggers.append(blogger)
    conn.close()
    # Вывод информации в формате JSON
    return JSONResponse(content=bloggers)
