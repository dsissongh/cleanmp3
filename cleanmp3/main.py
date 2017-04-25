import os

from func import media
from func import traverse


test = '/mnt/h/nas/Music/a/Adele/singles/cover.jpg'
test = '/mnt/h/nas/Music/a/Adele/'

myitem = media()
print(myitem.gettype(test))

traverse(test)
