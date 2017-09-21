#### CURRENT PROBLEM -- LINES 40 AND 52 - LIST ITEMS, NOT SURE HOW TO PULL THE TITLES!!!!!!

import random, md5
from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import sqlalchemy
app = Flask(__name__)
app.secret_key = "secret"
mysql = MySQLConnector(app, 'bookdb')

# def collection():
#     select_query = "SELECT * from books"
#     books = mysql.query_db(select_query)
#     return books


@app.route('/', methods=["get", "post"])
def index():
    select_query = "SELECT * from books"
    books = mysql.query_db(select_query)
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add():
    return render_template('add.html')

@app.route('/addbook', methods=['POST'])
def addbook():
    form_data = request.form
    insert_query = "INSERT INTO books (title, author, year_published, created_at, updated_at) VALUES (:title, :author, :year_published, NOW(), NOW())"
    query_data = {"title": request.form['title'], 'author': request.form['author'], "year_published": request.form['year_published']}
    mysql.query_db(insert_query, query_data)
    return redirect ('/')

@app.route('/update/<idbooks>', methods=['POST'])
def update(idbooks):
    select_query = "SELECT * from books where idbooks = :idbooks"
    query_data = {"idbooks": idbooks}
    book = mysql.query_db(select_query, query_data)
    idbooks = book[0]['idbooks']
    title = book[0]['title']
    author = book[0]['author']
    year_published = book[0]['year_published']
    return render_template("update.html", title=title, author=author, year_published=year_published, idbooks=idbooks)

@app.route('/updateconfirm/<idbooks>', methods=['POST'])
def updateconfirm(idbooks):
    idbooks = int(idbooks)
    update_query = "UPDATE books SET title= :title, author= :author, year_published= :year_published WHERE idbooks= :idbooks"
    query_data = {"title": request.form['title'], 'author': request.form['author'], "year_published": int(request.form['year_published']), "idbooks": idbooks}
    mysql.query_db(update_query, query_data)
    return redirect('/')

@app.route('/delete/<idbooks>', methods=['POST'])
def delete(idbooks):
    select_query = "SELECT * from books where idbooks = :idbooks"
    query_data = {"idbooks": idbooks}
    book = mysql.query_db(select_query, query_data)
    idbooks = book[0]['idbooks']
    if len(book) > 0 :
        title = book[0]['title']
        return render_template("delete.html", idbooks=idbooks, title=title)
    else :
        return redirect ('/')

@app.route('/deleteconfirm/<idbooks>', methods=['POST'])
def deleteconfirm(idbooks):
    idbooks = int(idbooks)
    delete_query = "DELETE from books where idbooks = :idbooks"
    query_data = {"idbooks": idbooks}
    mysql.query_db(delete_query, query_data)

    return redirect ('/')

@app.route('/cancel', methods=['POST'])
def cancel():
    return redirect ('/')

app.run(debug=True)
