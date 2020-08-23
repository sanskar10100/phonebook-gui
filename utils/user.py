import tkinter as tk
from . import helper

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
			self.username = # Assign hashed username here
			self.password = # Assign hashed password here
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
		btn_submit = # TODO: Generate submit button. Call submit if clicked.
		# Wait until submit button is clicked
		btn_submit.wait_variable(self.clicked) # should be the last line of the function

	def add_user(self):
		self._gen_new_frame()
		# TODO:
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