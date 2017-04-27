import sqlite3

class datao(object):

	def __init__(self):
		self.connection = ''
		self.new = 1
		self.database = 'dat.db'
		self.dbconnection()
		self.firstruncheck()


	def dbconnection(self):
		self.connection = sqlite3.connect(self.database)
		return

	def firstruncheck(self):
		sql = "SELECT count(*) from inventory1;"
		print(self.connection)
		try:
			conn = self.connection
			c = conn.cursor()
			c.execute(sql)
			returndata = c.fetchall()
			#print('1):', returndata)
			self.new = 0
		except:
			self.new = 1
			#print("non")

	def createintentorytables(self):
		sql = "create table inventory ('ID' integer, 'name' string, \
			'location' string)";
			

	def close(self):
		self.connection.close()
