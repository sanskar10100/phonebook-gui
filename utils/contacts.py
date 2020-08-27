"""Provides code for manipulating contact data in the database.

Also provides various methods for verification.
"""

import tkinter as tk
from tkinter import messagebox
from . import user
from . import helper
import sqlite3


conn = sqlite3.connect('material.db')
c = conn.cursor()


class ContactsManagement:
	"""Provides contact management methods, like addition, deletion, view, modify, search.

	Attributes:-
	"""

	def __init__(self, window, frame, tablename):
		self.tablename = tablename
		self.window = window
		self.frame = frame
		self.clicked = tk.IntVar()
		self.clicked.set(0)
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
		"""Shows all contacts for a user, along with the contact count."""
		# The 0th entry in the tuple returned by fetchone contains the count
		self._gen_new_frame()
		contact_count = c.execute(f'SELECT COUNT(*) FROM {self.tablename}').fetchone()[0]
		# First print the contact count
		textbox = tk.Text(self.frame, bg='#455A64', fg='#FFFFFF', height=1)
		textbox.insert(tk.END, f'Contacts count: {contact_count}')
		textbox.grid()
		# Make a textbox for each row
		for name, number, email in c.execute(f'SELECT * FROM {self.tablename}'):
			textbox = tk.Text(master=self.frame, bg='#455A64', fg='#FFFFFF', height=1)
			textbox.insert(tk.END, f'{name} | {number} | {email}')
			textbox.grid()
		else:
			# Go back when button pressed
			btn_go_back = helper.create_button(self.frame, 'Go Back', command=lambda: self.clicked.set(1))
			btn_go_back.grid(column=0, sticky='w')
			btn_go_back.wait_variable(self.clicked)
			self.draw_contacts_menu()


	def add_contact(self):
		def submit():
			name = entry_name.get()
			number = entry_phno.get()
			email = entry_email.get()
			if email == '':
				email = 'NULL'
			if (helper._verify_contact_name(name) is False) or (helper._verify_contact_num(number) is False):
				pass
			else :
				contact_tuple = (name, number, email)
				c.execute(f'''INSERT INTO {self.tablename} 
							VALUES (?, ?, ?);''', contact_tuple)
				conn.commit()
			self.clicked.set(1)

		self._gen_new_frame()
		# adding name, phno and email label.
		lbl_name = helper.create_label(self.frame, 'Contact Name')
		lbl_name.grid(row=0, column=0, sticky='w')
		lbl_phno = helper.create_label(self.frame, 'Contact Number')
		lbl_phno.grid(row=1, column=0, sticky='w')
		lbl_email = helper.create_label(self.frame, 'Contact Email')
		lbl_email.grid(row=2, column=0, sticky='w')
		
		# adding entry boxes for name, phno and email labels.

		entry_name = tk.Entry(master=self.frame, width=16)
		entry_name.grid(row=0, column=1, sticky='w')
		entry_phno = tk.Entry(master=self.frame, width=16)
		entry_phno.grid(row=1, column=1, sticky='w')
		entry_email = tk.Entry(master=self.frame, width=16)
		entry_email.grid(row=2, column=1, sticky='w')

		# adding button to submit the all the user enter details into the contact_+username table.
		btn_submit = helper.create_button(self.frame, 'Submit', submit)
		btn_submit.grid(row=3, column=1, sticky='w')
		# adding button to go back to the previous menu i.e, draw_contacts_menu.
		btn_go_back = helper.create_button(self.frame, 'Go Back', command=lambda: self.clicked.set(1))
		btn_go_back.grid(row=3, column=0, sticky='w')

		# adding clicking mechanism
		btn_submit.wait_variable(self.clicked)
		self.draw_contacts_menu()

	def remove_contact(self):
		pass

	def modify_contact(self):
		pass

	def search_contact(self):
		pass