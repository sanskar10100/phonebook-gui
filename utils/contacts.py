"""Provides code for manipulating contact data in the database.

Also provides various methods for verification.
"""

import tkinter as tk
from tkinter import messagebox
from . import user
from . import helper


class ContactsManagement:
	"""Provides contact management methods, like addition, deletion, view, modify, search.

	Attributes:-
	"""

	def __init__(self, window, frame, tablename):
		self.tablename = tablename
		self.window = window
		self.frame = frame
		self.draw_contacts_menu()

	def _gen_new_frame(self):
		"""Destroys any existing frame and generates a new one."""
		if self.frame:
			self.frame.destroy()
		self.frame = tk.Frame(master=self.window, bg='#455A64')
		self.frame.pack(expand='True', fill='both')

	def draw_contacts_menu(self):
		"""Draws buttons for calling different methods on screen."""
		self._gen_new_frame()
		helper.create_button(self.frame, text='Show All Contacts', command=self.show_all_contacts).grid()
		helper.create_button(self.frame, text='Add Contact', command=self.add_contact).grid()
		helper.create_button(self.frame, text='Remove Contact', command=self.remove_contact).grid()
		helper.create_button(self.frame, text='Modify Contact', command=self.modify_contact).grid()
		helper.create_button(self.frame, text='Search Contact', command=self.search_contact).grid()

	def show_all_contacts(self):
		pass

	def add_contact(self):
		pass

	def remove_contact(self):
		pass

	def modify_contact(self):
		pass

	def search_contact(self):
		pass