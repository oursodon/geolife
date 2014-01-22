import MySQLdb
from os import listdir
from os.path import isfile, join

def connect_db():
	#MySQLdb.connect("host","user","psswd","base")
	db = MySQLdb.connect("localhost","root","truc","geolife")
	return db

def close_db(db):
	db.close()

def create_user(iduser, db):
	sql = "INSERT INTO USER (id) VALUES ('%d')" % (int(iduser))
	#print sql
	try:
		db.cursor().execute(sql)
		db.commit()
	except Exception, e:
		print e
		db.rollback()

def create_point(iduser, db, row):
	sql = "INSERT INTO POINT (iduser,latitude,longitude,altitude,date) VALUES ('%d','%f','%f','%f','%s')" % \
(int(iduser),float(row[0]),float(row[1]),float(row[3]),row[5]+" "+row[6])
	#print sql
	try:
		db.cursor().execute(sql)
		db.commit()
	except Exception, e:
		print e
		db.rollback()

def create_label(iduser, db, row):
	sql = "INSERT INTO LABEL (iduser,starttime,endtime,mode) VALUES ('%d','%s','%s','%s')" % (int(iduser),row[0].replace('/','-',3),row[1].replace('/','-',3),row[2])
	#print sql
	try:
		error = db.cursor().execute(sql)
		db.commmit()
	except Exception, e:
		print e
		db.rollback()


dossiers = listdir(".")
db = connect_db()
cpt = 1

for dossier in dossiers:
	print "User "+str(cpt)+"/"+str(len(dossiers))
	cpt += 1
	print "Dossier : "+dossier
	create_user(dossier,db)

	onlyfiles = [f for f in listdir("./"+dossier) if isfile(join("./"+dossier,f))]
	if(len(onlyfiles) == 1):
		print "Parsage labels"
		contenulabel = open("./"+dossier+"/labels.txt")
		compteur = 1
		
		for line in contenulabel.readlines():
			if compteur < 2:
				compteur += 1 
			else:
				tuple = line.rstrip('\n\r').split("	")
				create_label(dossier, db, tuple)
		contenulabel.close()
	
	chemin = "./"+dossier+"/Trajectory/"
	fichiers = listdir(chemin)
	
	nbfichiers = len(fichiers)
	cptfichier = 1

	#Parsage des fichiers contenant les points GPS
	for fichier in fichiers:
		print "Parsage fichiers points ("+str(cptfichier)+"/"+str(nbfichiers)+")"
		contenu = open(chemin+fichier,"r")
		cptfichier += 1
		compteur = 1
		for line in contenu.readlines():
			if compteur < 7:
				compteur += 1 
			else:
				tuple = line.rstrip('\n\r').split(",")
				create_point(dossier,db, tuple)
		contenu.close()


