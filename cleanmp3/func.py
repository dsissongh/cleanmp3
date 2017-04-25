
import os

class media(object):
	"""docstring for media"""
	def __init__(self):
		self.item = ''
		self.type = ''	

		return


	def gettype(self,item):

		if os.path.isdir(item):
			self.type = 'dir'
			return 1

		if os.path.isfile(item):
			self.type = 'file'
			return 2

		return 0



def traverse(item):
	basedir = os.path.dirname(item)
	elements = os.listdir(item)
	for element in elements:

		if os.path.isdir(basedir + '/' + element):
			traverse(basedir + '/' + element)

		print(basedir + '/' + element)