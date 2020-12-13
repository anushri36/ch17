###
#
# This program demonstrates using SQLite to manipulate and query a 'books'
# database.
#
# Author: Anushri Kartik-Narayan
# Assignment: Homework 12 - Exercise 17.1
# Class: CIS2532-NET02
# Professor: Sheikh Shamsuddin
# Submitted 12/13/2020
#
###

import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')

pd.options.display.max_columns = 10

# Question 17.1.a
print("\nQuestion 17.1.a")
print("All last names in 'authors' reverse-alphabetically:")
print(pd.read_sql('SELECT last FROM authors ORDER BY last DESC', connection))

# Question 17.1.b
print("\nQuestion 17.1.b")
print("All titles in 'titles' alphabetically:")
print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection))

# Question 17.1.c
print("\nQuestion 17.1.c")
print("For each author, all titles sorted alphabetically:")
print(pd.read_sql("""SELECT first, last, title, titles.isbn, copyright 
                    FROM author_ISBN
                    INNER JOIN titles ON author_ISBN.isbn = titles.isbn
                    INNER JOIN authors ON author_ISBN.id = authors.id
                    ORDER BY last, first, title""", connection))

# Question 17.1.d
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last)
                            VALUES ('Sue', 'Red')""")
print("\nQuestion 17.1.d")
print("Total 'authors' table including new author 'Sue Red':")
print(pd.read_sql('SELECT * FROM authors', connection))
cursor = cursor.execute('DELETE FROM authors WHERE id=6')

# Question 17.1.e
cursor = cursor.execute("""INSERT INTO titles (isbn, title, edition, copyright)
                            VALUES (7382593059, 'Python 101', 1, 2020)""")
cursor = cursor.execute("""INSERT INTO author_ISBN (id, isbn)
                            VALUES (6, 7382593059)""")
print("\nQuestion 17.1.e")
print("Total 'titles' table including new title 'Python 101':")
print(pd.read_sql('SELECT * FROM titles', connection))
print("\nTotal 'authors_ISBN' table including new author's id and new title's ISBN:")
print(pd.read_sql('SELECT * FROM author_ISBN', connection))
cursor = cursor.execute('DELETE FROM titles WHERE isbn=7382593059')
cursor = cursor.execute('DELETE FROM author_ISBN WHERE isbn=7382593059')

connection.close()
