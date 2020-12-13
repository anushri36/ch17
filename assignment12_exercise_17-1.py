import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')

pd.options.display.max_columns = 10

# flip direction; only the last names
print(pd.read_sql('SELECT last FROM authors', connection))

print(pd.read_sql('SELECT title FROM titles', connection))
