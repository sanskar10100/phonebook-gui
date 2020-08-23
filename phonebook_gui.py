"""A tkinter based phonebook application that manages contact lists for individual users.

Emphasis on security, through Object Oriented Methodology and crdential encryption.
Provides a lot of management options for contacts.
Uses sqlite3 database for persistance.
"""
import tkinter as tk
import sqlite3
from utils import user

if __name__ == '__main__':
	"""Makes a root window. Entry point for the application."""
	window = tk.Tk()
	window.title('Phonebook')
	window.geometry('400x400')
	window.configure(bg='#455A64')

	user.UserManagement(window)

	window.mainloop()