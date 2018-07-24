import sys
from database import Model

class Main:
	def __init__(self, database):
		self.database = Model(database)
		self.init_app()

	def init_app(self):
		while True:
			data = self.database.read_database()
			for d in data:
				print(d)
			print('____________________________')
			print("""
				What do you want to do? \n 
				1. Write a new todo \n 
				2. Update an item in your list \n 
				3. Delete an item in your list """)
			input_data = input("Choice: ")
			if input_data == "e":
				break
			elif int(input_data) == 1:
				self.write_data()
			elif int(input_data) == 2:
				self.update_data()
			elif int(input_data) == 3:
				self.delete_data()

	def write_data(self):
		user_input = input("Write new todo: ")
		self.database.write_data(str(user_input))

	def update_data(self):
		try:
			row_id, text = input("Input the number in the database and the entry,\nseparated by ':'").split(':')
		except:
			print("Invalid input")
		else:
			self.database.update_data(row_id=row_id, text=text)
if __name__ == '__main__':
	Main(sys.argv[1])


