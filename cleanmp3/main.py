import os
import sqlite3
from db import datao

from func import media
from func import traverse


test = '/mnt/h/nas/Music/a/Adele/singles/cover.jpg'
test = '/mnt/h/nas/Music/a/Adele/'


myitem = media()
print(myitem.gettype(test))

traverse(test)


dbcon = datao()
print(dbcon.new)

if dbcon.new == 1:
	dbcon.createintentorytables()
	dbcon.new = 0

#conn.commit()
dbcon.close()

