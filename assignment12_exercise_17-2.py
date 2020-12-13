###
#
# This program demonstrates using SQLite cursor objects to return metadata
# of a table and table data in tuple format.
#
# Author: Anushri Kartik-Narayan
# Assignment: Homework 12 - Exercise 17.2
# Class: CIS2532-NET02
# Professor: Sheikh Shamsuddin
# Submitted 12/13/2020
#
###

import sqlite3

connection = sqlite3.connect('books.db')
cursor = connection.cursor()

cursor = cursor.execute('SELECT * FROM titles')

print("\nCursor description attribute for 'titles' table:")
for each in cursor.description:
    print(each)

print("\nCursor fetchall method for 'titles' table:")
for each in cursor.fetchall():
    print(each)

connection.close()
