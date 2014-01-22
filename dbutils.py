import MySQLdb

def connect_db():
	#MySQLdb.connect("host","user","psswd","base")
	db = MySQLdb.connect("localhost","root","truc","geolife")
	return db

def close_db(db):
	db.close()