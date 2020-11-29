import sqlite3

def connect():
    conn = sqlite3.connect('rout.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY , date text , waketime text , GRE text , Majorproject text , UniSearch text , Ieltof text )")  
    conn.commit()
    conn.close()

def insert(date ,waketime ,GRE ,Majorproject ,UniSearch ,Ieltof):
    conn = sqlite3.connect('rout.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL , ?,?,?,?,?,?)" , (date ,waketime ,GRE ,Majorproject ,UniSearch ,Ieltof))  
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('rout.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")  
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect('rout.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE Id=? ",(id,))  
    conn.commit()
    conn.close()

def search(date='' ,waketime='' ,GRE='' ,Majorproject='' ,UniSearch='' ,Ieltof=''):
    conn = sqlite3.connect('rout.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=? OR waketime=? OR GRE=? OR Majorproject=? OR UniSearch=? OR Ieltof=?" , (date ,waketime ,GRE ,Majorproject ,UniSearch ,Ieltof) )  
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


connect()

