import tkinter as tk
from . import helper
from tkinter import messagebox

### Important
### Important
### Important
### See helper's create_button and create_label functions. Use them.
### Write all the extra functions in helper module too.
### Important
### Important
### Important

class UserManagement:
	"""Provides UserManagement functionality: add, remove and select user.

	Attributes:-
	"""

	def __init__(self, window):
		self.frame = None
		self.window = window
		self.username = None
		self.password = None
		self.clicked = tk.IntVar()
		self.clicked.set(0)
		self.draw_user_menu()

	def _gen_new_frame(self):
		"""Destroys any existing frame and generates and configure a new frame."""
		if self.frame:
			self.frame.destroy()
		self.frame = tk.Frame(master=self.window, bg='#455A64')
		self.frame.pack(expand=True, fill='both')

	def draw_user_menu(self):
		"""Draws User Management menu with 3 options on the screen."""
		self._gen_new_frame()
		btn_add_user = helper.create_button(self.frame, 'Add User', self.add_user)
		btn_add_user.grid(sticky='w')
		btn_remove_user = helper.create_button(self.frame, 'Remove User', self.remove_user)
		btn_add_user.grid(sticky='w')
		btn_select_user = helper.create_button(self.frame, 'Select User', self.select_user)
		btn_select_user.grid(sticky='w')

	def _create_input_credentials(self):
		"""Inputs First Time User's credentials and sets username and password."""
		def submit():
			if u_pass == c_pass
				credentials = helper._encryption([u_name, u_pass])
				self.username =  credentials[0]# Assign hashed username here
				self.password = credentials[1]# Assign hashed password here
				self.clicked.set(1)

		#TODO: 
		# 3 text lables, username, password and confirm password.
		# 3 Entry widgets. 
		# One submit button. Data from entry widget should be checked for criteria matching
		# then hashed and then stored.
		# Program should wait until submit button is clicked before returning.
		# If password criteria doesn't match, display a messagebox saying so
		# and clear the entry fields.
		self._gen_new_frame()
		# variable to store the value of the entry boxes.
		u_name = str(tk.StringVar())
		u_pass = str(tk.StringVar())
		c_pass = str(tk.StringVar())
		# labels of username and password and confirm password.
		lbl_username = helper.create_label(self.frame, 'Username')
		lbl_username.grid(row=0, column=0, sticky='w')
		lbl_Password = helper.create_label(self.frame, 'Password')
		lbl_Password.grid(row=0, column=0, sticky='w')
		lbl_confirm_password = helper.create_label(self.frame, 'Confirm Password')
		lbl_confirm_password.grid(row=0, column=0, sticky='w')
		# creating entry boxes for above labels.
		entry_username = helper.create_entry(self.frame, width=16, textvariable=u_name)
		entry_username.grid(row=0, column=1, sticky='w')
		entry_password = helper.create_entry(self.frame, width = 16, textvariable=u_pass)
		entry_password.grid(row=1, column=1, sticky='w')
		entry_confirm_password = helper.create_entry(self.frame, width = 16, textvariable=c_pass)
		entry_confirm_password.grid(row=2, column=1, sticky='w')
		# TODO: Generate submit button. Call submit if clicked.
		# Creating submit button to add the user
		btn_submit = tk.Button(master=self.frame, text='Submit', fg='#FFFFFF', bg='#009688', command=submit)
		btn_add_user.grid(row=3, column=1, sticky='w')
		# Wait until submit button is clicked
		btn_submit.wait_variable(self.clicked) # should be the last line of the function

	def add_user(self):
		self._gen_new_frame()
		# TODO:
		if  _create_input_credentials():
			c.execute("""CREATE TABLE IF NOT EXISTS users( 
			username VARCHAR(40) NOT NULL,
			password VARCHAR(40) NOT NULL);
			""")
			c.execute("INSERT INTO users VALUES (?,?);", (self.username, self.password, ))
			conn.commit()

			tablename = helper.scrub('contacts_' + self.username)
			c.execute(f"""CREATE TABLE {tablename} (
			name VARCHAR(255) NOT NULL,
			phno VARCHAR(20) NOT NULL,
			email VARCHAR(255) NOT NULL);
			""")
			conn.commit()
			tk.messagebox.showinfo(title='Phonebook', message='User Added in the Phonebook')

		else:
			tk.messagebox.showerror(title='Invalid Credentials', message='Credentials do no match the requirements.')
		# Call create_input_credentials. If everything goes smoothly, show a messagebox saying user successfully added.
		# Create a table if not exists in database, called users with the following fields:
		# username varchar(40) NOT NULL, password VARCHAR(40) NOT NULL
		# Add username and password to the table.

	def _input_credentials(self):
		"""Inputs and sets user credentials."""
		def submit():
			# TODO
			self.clicked.set(1)
		self._gen_new_frame()

		# TODO:
		# Two labels, username and password. 2 entry widgets.
		# One submit button.
		# set self.username and self.password
		btn_submit = # TODO
		btn_submit.wait_variable(self.clicked) # should be the last line of the function

	def remove_user(self):
		# TODO: You know what to do. Display a messgaebox showing status.

	def select_user(self):
		# TODO: You know what to do. Display a messagebox showing status.