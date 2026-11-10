import sqlite3

DBNAME = "MovieData.db"

def init_db():
    conn = sqlite3.connect(DBNAME)
    conn.close()

#init_db()

# =========================================

def create_table():
    query = '''
    CREATE TABLE IF NOT EXISTS movies
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    year TEXT,
    country TEXT,
    imdb_rate REAL
    )
    '''
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

#create_table()

# =========================================

def insert_record(title, year, country, imdb_rate):
    title = title.title()
    country = country.title()
    query = '''
        INSERT INTO movies(title, year, country, imdb_rate)
        VALUES(?, ?, ?, ?)

        '''
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query, (title, year, country, imdb_rate))
    conn.commit()
    conn.close()

#insert_record("Fight Club", "2002", "USA", 8.8)
#insert_record("City Of God", "2001", "Brazil", 8.4)

# =========================================

def select_all_records():
    #query = 'SELECT title, year FROM movies'
    query = 'SELECT * FROM movies'

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    rows = cursor.execute(query).fetchall()
    conn.close()
    return rows

#print(select_all_records())

# =========================================

def select_records_by_id(id):
    query = 'SELECT * FROM movies WHERE id = ?'

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    row = cursor.execute(query, (id,)).fetchone()
    conn.close()
    return row

#print(select_records_by_id(1))

# =========================================

def select_records_by_name(name):
    query = 'SELECT * FROM movies WHERE LOWER(REPLACE(title, " ", ""))=LOWER(REPLACE(?, " ", ""))'

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    rows = cursor.execute(query, (name,)).fetchall()
    conn.close()
    return rows

# =========================================

def select_records_by_rate(rate):
    query = 'SELECT * FROM movies WHERE imdb_rate = ?'

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    rows = cursor.execute(query, (rate,)).fetchall()
    conn.close()
    return rows

# =========================================

def delete_records_by_id(id):
    query = 'DELETE FROM movies WHERE id = ?'

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM movies WHERE id = ?', (id,))
    movie = cursor.fetchone()

    if movie:
        cursor.execute(query, (id,))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False
    

#print(delete_records_by_id(5))

# =========================================

def delete_records_by_name(name):
    query = '''
        DELETE FROM movies
        WHERE LOWER(REPLACE(title, " ", "")) = LOWER(REPLACE(?, " ", ""))
    '''

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    cursor.execute(query, (name,))
    conn.commit()
    conn.close()

# =========================================

def update_records_by_id(id, title, year, country, imdb_rate):

    title = title.title()
    country = country.title()

    query = '''
        UPDATE movies
        SET title=?, year=?, country=?, imdb_rate=?
        WHERE id = ?
        '''

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM movies WHERE id = ?', (id,))
    movie = cursor.fetchone()

    if movie:
        cursor.execute(query, (title, year, country, imdb_rate, id))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False
    
#print(update_records_by_id(2, 2019, 9.8))

# =========================================

def update_records_by_name(name, year, country, imdb_rate):

    country = country.title()

    query = '''
        UPDATE movies
        SET year=?, country=?, imdb_rate=?
        WHERE id = ?
        '''

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    cursor.execute(
        'SELECT * FROM movies WHERE LOWER(REPLACE(title, " ", "")) = LOWER(REPLACE(?, " ", ""))',
        (name,)
    )

    movie = cursor.fetchone()

    if movie:
        cursor.execute(query, (year, country, imdb_rate, movie[0]))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False