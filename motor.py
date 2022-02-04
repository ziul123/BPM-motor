import sqlite3 as sql

def create():
	with open("create.sql", "r") as f:
		con = sql.connect("bpm.db")
		cur = con.cursor()
		cur.executescript(f.read())
		con.commit()
		con.close()
	print("BD criado")


def insert():
	op = input()
