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

#conn.commit()
dbcon.close()

