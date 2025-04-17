import sqlite3

def write_to_db(data):
    conn = sqlite3.connect('messages.db') 
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS messages (content TEXT)')
    c.execute('INSERT INTO messages (content) VALUES (?)', (data,))
    conn.commit()
    conn.close()
