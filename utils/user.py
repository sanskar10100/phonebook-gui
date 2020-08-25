import tkinter as tk
from . import helper
from tkinter import messagebox
import sqlite3

### Important
### Important
### Important
### See helper's create_button and create_label functions. Use them.
### Write all the extra functions in helper module too.
### Important
### Important
### Important

conn = sqlite3.connect('material.db')
c = conn.cursor()

class UserManagement:
	"""Provides UserManagement functionality: add, remove and select user.

	Attributes:-
	frame: Currently active background frame.
	window: Currently active main program window. Parent of frame
	username: username in plaintext
	password: password in plaintext
	clicked: indicates status of submit buttons. Uses for local looping
	status: status flag, shows status of the most recently called method
	"""

	def __init__(self, window):
		self.frame = None
		self.window = window
		self.username = None
		self.password = None
		self.clicked = tk.IntVar()
		self.clicked.set(0)
		self.status = False
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
		btn_remove_user.grid(sticky='w')
		btn_select_user = helper.create_button(self.frame, 'Select User', self.select_user)
		btn_select_user.grid(sticky='w')

	def _create_input_credentials(self):
		"""Inputs First Time User's credentials and sets username and password."""
		def submit():
			username = entry_username.get()
			password = entry_password.get()
			confirm_password = entry_confirm_password.get()
			if password != confirm_password:
				tk.messagebox.showerror(title='Password Mismatch', message='Both input passwords are not same!')
				self.status = False
			else:
				self.username = username
				self.password = password
				self.status = True
			self.clicked.set(1)

		self._gen_new_frame()

		# labels of username and password and confirm password.
		lbl_username = helper.create_label(self.frame, 'Username')
		lbl_username.grid(row=0, column=0, sticky='w')
		lbl_Password = helper.create_label(self.frame, 'Password')
		lbl_Password.grid(row=1, column=0, sticky='w')
		lbl_confirm_password = helper.create_label(self.frame, 'Confirm Password')
		lbl_confirm_password.grid(row=2, column=0, sticky='w')

		# creating entry boxes for above labels.
		entry_username = tk.Entry(master=self.frame, width=16)
		entry_username.grid(row=0, column=1, sticky='w')
		entry_password = tk.Entry(master=self.frame, width = 16, show='*')
		entry_password.grid(row=1, column=1, sticky='w')
		entry_confirm_password = tk.Entry(master=self.frame, width = 16, show='*')
		entry_confirm_password.grid(row=2, column=1, sticky='w')

		# Creating submit button to add the user
		btn_submit = helper.create_button(self.frame, 'Submit', submit)
		btn_submit.grid(row=3, column=1, sticky='w')
		# Wait until submit button is clicked
		btn_submit.wait_variable(self.clicked)

	def add_user(self):
		self._gen_new_frame()
		self._create_input_credentials()
	
		if self.status is True:		
			tablename = helper.scrub('contacts_' + self.username.lower())
			# Create contacts table for the user
			c.execute(f"""CREATE TABLE {tablename} (
							name VARCHAR(255) NOT NULL,
							number VARCHAR(20) NOT NULL,
							email VARCHAR(255) NOT NULL);""")

			# Encrypt username and password for storage
			encrypted_credentials = helper.encrypt_credentials(self.username, self.password)

			# Create users table (if program is being run for the first time)
			c.execute("""CREATE TABLE IF NOT EXISTS users( 
							username VARCHAR(40) NOT NULL,
							password VARCHAR(40) NOT NULL);""")
			# Insert encrypted user data into users table
			c.execute("INSERT INTO users VALUES (?, ?);", encrypted_credentials)
			conn.commit()
		self.draw_user_menu()

	def _input_credentials(self):
		"""Inputs and sets user credentials."""

		def submit():
			self.username = ent_username.get()
			self.password = ent_password.get()
			self.clicked.set(1)

		self._gen_new_frame()
		# lable and entry for username
		lbl_username = helper.create_label(self.frame, 'Username:').grid(row=0, column=0, sticky='w')
		ent_username = tk.Entry(self.frame, bd=7)
		ent_username.grid(row=0, column=1, sticky='w')
		# lable and entry for password
		lbl_password = helper.create_label(self.frame, 'Password:').grid(row=1, column=0, sticky='w')
		ent_password = tk.Entry(self.frame, bd=7, show='*')
		ent_password.grid(row=1, column=1, sticky='w')
		# Submit button, when clicked registers input		
		btn_submit = helper.create_button(self.frame, 'Login', submit)
		btn_submit.grid(row = 4, column = 1, sticky = 'w')
		btn_submit.wait_variable(self.clicked) # should be the last line of the function

	def remove_user(self):
		pass

	def select_user(self):
		self._input_credentials()

