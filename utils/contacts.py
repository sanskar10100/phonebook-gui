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
	tablename: sanitized name of the currently active table
	window: parent or root phonebook window
	frame: currently active frame or screen
	clicked: indicates whether a buttton has been clicked. Useful for creating local loops
	status: returns status and occasionally data from the last method, if needed
	"""

	def __init__(self, window, frame, tablename):
		self.tablename = tablename
		self.window = window
		self.frame = frame
		self.clicked = tk.IntVar()
		self.clicked.set(0)
		self.status = None
		self.draw_contacts_menu()

	def _gen_new_frame(self):
		"""Destroys any existing frame and generates a new one."""
		if self.frame:
			self.frame.destroy()
		self.frame = tk.Frame(master=self.window, bg='#455A64')
		self.frame.pack(expand='True', fill='both')

	def draw_contacts_menu(self):
		"""Draws buttons for calling different methods on screen."""
		def return_to_user():
			"""Returns control to user management module."""
			self.frame.destroy()
			self.clicked.set(1)

		self.window.title('Contacts Management')
		self._gen_new_frame()
		self.clicked.set(0)
		btn_1 = helper.create_button(self.frame, text='Show All Contacts', command=self.show_all_contacts)
		helper.grid_button(btn_1)
		btn_2 = helper.create_button(self.frame, text='Add Contact', command=self.add_contact)
		helper.grid_button(btn_2)
		btn_3 = helper.create_button(self.frame, text='Remove Contact', command=self.remove_contact)
		helper.grid_button(btn_3)
		btn_4 = helper.create_button(self.frame, text='Modify Contact', command=self.modify_contact)
		helper.grid_button(btn_4)
		btn_5 = helper.create_button(self.frame, text='Search Contact', command=self.search_contact)
		helper.grid_button(btn_5)
		btn_user = helper.create_button(self.frame, text='Switch to User Management Menu', command=return_to_user, width=30)
		helper.grid_button(btn_user)
		btn_user.wait_variable(self.clicked)

	def show_all_contacts(self):
		"""Shows all contacts for a user, along with the contact count."""
		# The 0th entry in the tuple returned by fetchone contains the count
		self.window.title('Show All Contacts')
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
			helper.grid_button(btn_go_back, column=0, sticky='w')
			btn_go_back.wait_variable(self.clicked)
			self.draw_contacts_menu()


	def add_contact(self):
		"""Adds a contact to the user's contacts table iff the input details are valid."""
		def submit():
			name = entry_name.get()
			number = entry_phno.get()
			email = entry_email.get()
			# Input Validation is done in three stages
			if helper._verify_contact_name(name) is False:
				tk.messagebox.showerror(title='Invalid Name', message='Please make sure that you have entered the correct name')
			elif helper._verify_contact_num(number) is False:
				tk.messagebox.showerror(title='Invalid Number', message='Please make sure that you have entered the correct number')
			else:
				if email == '':
				# If no email is provided, email is assumed to be null
					tk.messagebox.showinfo(title='Addition Successful', message='Contact Successfully Modified')
					c.execute(f'INSERT INTO {self.tablename} VALUES (?, ?, ?)', (name, number, 'NULL', ))
					conn.commit()
				else:
					if helper._verify_contact_email(email) is False:
						tk.messagebox.showerror(title='Invalid Email', message='Please make sure that you have entered the correct email')				
					else:
						tk.messagebox.showinfo(title='Addition Successful', message='Contact Successfully Modified')
						c.execute(f'INSERT INTO {self.tablename} VALUES (?, ?, ?)', (name, number, email, ))
						conn.commit()
			self.clicked.set(1)

		self.window.title('Add Contacts')
		self._gen_new_frame()
		# adding name, phno and email label.
		lbl_name = helper.create_label(self.frame, 'Contact Name')
		lbl_name.grid(row=0, column=0, sticky='w')
		lbl_phno = helper.create_label(self.frame, 'Contact Number')
		lbl_phno.grid(row=1, column=0, sticky='w')
		lbl_email = helper.create_label(self.frame, 'Contact Email')
		lbl_email.grid(row=2, column=0, sticky='w')
		
		# adding entry boxes for name, phno and email labels.
		entry_name = helper.create_entry(master=self.frame, width=16)
		entry_name.grid(row=0, column=1, sticky='w')
		entry_phno = helper.create_entry(master=self.frame, width=16)
		entry_phno.grid(row=1, column=1, sticky='w')
		entry_email = helper.create_entry(master=self.frame, width=16)
		entry_email.grid(row=2, column=1, sticky='w')

		# adding button to submit the all the user enter details into the self.tablename table.
		btn_submit = helper.create_button(self.frame, 'Submit', submit)
		helper.grid_button(btn_submit, row=3, column=1)
		# adding button to go back to the previous menu i.e, draw_contacts_menu.
		btn_go_back = helper.create_button(self.frame, 'Go Back', command=lambda: self.clicked.set(1))
		helper.grid_button(btn_go_back, row=3, column=0)
		# Wait until button is clicked and self.clicked changes
		btn_submit.wait_variable(self.clicked)
		self.draw_contacts_menu()

	def remove_contact(self):
		"""Removes all matches from the database, matching based on name (case insensitive)."""
		def submit():
			name = entry_name.get()
			# If at least one matching record present, delete, else raise error
			if c.execute(f'''SELECT * FROM {self.tablename} WHERE LOWER(name) = ?''', (name.lower(), )).fetchone() is not None:
				query = c.execute(f'''DELETE FROM {self.tablename}
							WHERE LOWER(name) = ?''', (name.lower(), ))
				conn.commit()
				self.clicked.set(1)
			else:
				tk.messagebox.showerror(title='No matches found', message='Contact Name does not exist')
		
		self.window.title('Remove Contacts')
		self._gen_new_frame()
		# taking name to remove the contact from the self.tablename table.
		lbl_name = helper.create_label(self.frame, 'Contact Name')
		lbl_name.grid(row=0, column=0, sticky='w')
		# entry box to take name of the contact to remove.
		entry_name = helper.create_entry(master=self.frame, width=16)
		entry_name.grid(row=0, column=1, sticky='w')
		# button to remove the user.
		btn_remove = helper.create_button(self.frame, 'Delete', submit)
		helper.grid_button(btn_remove, row=1, column=1)
		# adding button to go back to the previous menu i.e, draw_contacts_menu.
		btn_go_back = helper.create_button(self.frame, 'Go Back', command=lambda: self.clicked.set(1))
		helper.grid_button(btn_go_back, row=1, column=0)

		btn_remove.wait_variable(self.clicked)
		self.draw_contacts_menu()

	def modify_contact(self):
		"""Modifies all the occurences of an existing contact based on the contact name."""
		def submit():
			name = ent_name.get()
			number = ent_number.get()
			email = ent_email.get()
			if helper._verify_contact_name(name) is False:
				tk.messagebox.showerror(title='Invalid Name', message='Please make sure that you have entered the correct name')
			elif helper._verify_contact_num(number) is False:
				tk.messagebox.showerror(title='Invalid Number', message='Please make sure that you have entered the correct number')
			else:
				if email == '':
				# If no email is provided, email is assumed to be null
					tk.messagebox.showinfo(title='Modification Successful', message='Contact Successfully Modified')
					c.execute(f'''UPDATE {self.tablename}
									SET name = ?,
										number = ?,
										email = ?
									WHERE LOWER(name) = ?''', (name, number, 'NULL', name_key, ))
					conn.commit()
				else:
					if helper._verify_contact_email(email) is False:
						tk.messagebox.showerror(title='Invalid Email', message='Please make sure that you have entered the correct email')				
					else:
						tk.messagebox.showinfo(title='Modification Successful', message='Contact Successfully Modified')
						c.execute(f'''UPDATE {self.tablename}
										SET name = ?,
											number = ?,
											email = ?
										WHERE LOWER(name) = ?''', (name, number, email, name_key, ))
						conn.commit()
			self.clicked.set(1)

		self.window.title('Modify Contacts')
		self._get_contact_name()
		self.clicked.set(0)
		if self.status[0] is True:
			name_key = self.status[1]
			self._gen_new_frame()
			name = c.execute(f'SELECT name FROM {self.tablename} WHERE LOWER(name) = ?',  (name_key, )).fetchone()[0]
			number = c.execute(f'SELECT number FROM {self.tablename} WHERE LOWER(name) = ?', (name_key, )).fetchone()[0]
			email = c.execute(f'SELECT email FROM {self.tablename} WHERE LOWER(name) = ?', (name_key, )).fetchone()[0]
			# From Tenet: Don't try to understand it; Feel it!
			formatted = lambda email: '' if email is None else email
			helper.create_label(self.frame, 'Name:').grid(row=0, column=0)
			helper.create_label(self.frame, 'Number:').grid(row=1, column=0)
			helper.create_label(self.frame, 'Email:').grid(row=2, column=0)
			ent_name = helper.create_entry(self.frame)
			ent_name.insert(0, name)
			ent_name.grid(row=0, column=1)
			ent_number = helper.create_entry(self.frame)
			ent_number.insert(0, number)
			ent_number.grid(row=1, column=1)
			ent_email = helper.create_entry(self.frame)
			ent_email.insert(0, formatted(email))
			ent_email.grid(row=2, column=1)
			btn_submit = helper.create_button(self.frame, text='Submit', command=submit)
			helper.grid_button(btn_submit, row=3, column=1)
			btn_go_back = helper.create_button(self.frame, text='Go Back', command=lambda: self.clicked.set(1))
			helper.grid_button(btn_go_back, row=3, column=0)
			btn_go_back.wait_variable(self.clicked)
		self.draw_contacts_menu()	

	def _get_contact_name(self):
		"""Used by modify_contact to get a contact name that matches at least one field."""
		def submit():
			contact_name = ent_contact_name.get().lower()
			if c.execute(f'SELECT * FROM {self.tablename} WHERE LOWER(name) = ?', (contact_name, )).fetchone() is None:
				tk.messagebox.showerror(title='No matches', message='Could not find any contacts matching the name')
				self.status = (False, 0, )
			else:
				self.status = (True, contact_name, )
			self.clicked.set(1)

		def go_back():
			self.clicked.set(1)
			self.status = (False, 0, )

		self._gen_new_frame()
		self.clicked.set(0)
		helper.create_label(master=self.frame, text='Contact Name to modify:').grid(row=0, column=0)
		ent_contact_name = helper.create_entry(master=self.frame)
		ent_contact_name.grid(row=0, column=1)
		btn_submit = helper.create_button(self.frame, text='Submit', command=submit)
		helper.grid_button(btn_submit, row=1, column=1)
		btn_go_back = helper.create_button(master=self.frame, text='Go Back', command=go_back)
		helper.grid_button(btn_go_back, row=1, column=0)
		btn_go_back.wait_variable(self.clicked)

	def search_contact(self):
		"""Matches contacts based on name (case insensitive) and prints all matching results."""
		def submit():
			name_key = ent_name_key.get().lower()
			# If no matches are found, raise error and return
			if c.execute(f'SELECT * FROM {self.tablename} WHERE LOWER(name) = ?', (name_key, )).fetchone() is None:
				tk.messagebox.showerror(title='No matches found', message='No matching contacts were found')
			else:
				self._display_matched_contacts(name_key)

		self.window.title('Search Contacts')
		self._gen_new_frame()
		self.clicked.set(0)
		helper.create_label(self.frame, 'Name to be searched: ').grid(row=0, column=0)
		ent_name_key = helper.create_entry(master=self.frame)
		ent_name_key.grid(row=0, column=1)
		btn_go_back = helper.create_button(self.frame, 'Go Back', command=lambda: self.clicked.set(1))
		helper.grid_button(btn_go_back, row=1, column=0)
		btn_submit = helper.create_button(self.frame, text='Submit', command=submit)
		helper.grid_button(btn_submit, row=1, column=1)
		# wait until the submit button is clicked to perform match
		btn_submit.wait_variable(self.clicked)
		self.draw_contacts_menu()
			
	def _display_matched_contacts(self, name_key):
		"""Displays all matched contacts for a particular name key."""
		self._gen_new_frame()
		self.clicked.set(0)
		# Print details for every matching contact name
		for name, number, email in c.execute(f'SELECT * FROM {self.tablename} WHERE LOWER(name) = ?', (name_key, )):
			textbox = tk.Text(master=self.frame, bg='#455A64', fg='#FFFFFF', height=1)
			textbox.insert(tk.END, f'{name} | {number} | {email}')
			textbox.grid()
		else:
			# Go back when button pressed
			btn_go_back = helper.create_button(self.frame, 'Go Back', command=lambda: self.clicked.set(1))
			helper.grid_button(btn_go_back, column=0, sticky='w')
			btn_go_back.wait_variable(self.clicked)