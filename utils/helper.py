"""Provides various helper functions."""

import tkinter as tk
import hashlib
import re

credential_criteria = '''Username must be at least 4 characters long. May contain alphabets or numbers

Password Specifications:
At least 8 characters
At least one lowercase alphabet [a-z]
At least one uppercase alphabet [A-Z]
At least one digit [0-9]
At least one special character [@, #, $, &, +, -, *, ?, ., :, /, ;]'''


def create_button(master=None, text=None, command=None):
	"""Returns a new button created according to the style guidelines."""
	return tk.Button(master=master, text=text, fg='#FFFFFF', bg='#009688', command=command, relief=tk.GROOVE)


def create_label(master=None, text=None):
	"""Returns a newly created label according to the style guidlines."""
	return tk.Label(master=master, text=text, fg='#212121', bg='#CFD8DC')


def create_entry(master=None, width=16, show=None):
	"""Returns a newly created entry according to the style guide."""
	return tk.Entry(master=master, width=width, show=show)


def encrypt_credentials(username, password):
	"""Return the login credential in sha256 encrypted format."""
	encrypt_login_details = list()
	encrypt_login_details.append(hashlib.sha256(username.encode()).hexdigest())
	encrypt_login_details.append(hashlib.sha256(password.encode()).hexdigest())
	return tuple(encrypt_login_details)


def scrub(table_name):
	"""Sanitizes input for database query"""
	return ''.join( chr for chr in table_name if chr.isalnum() or chr == '_' )


def verify_credential_criteria(username, password):
	"""Returns true if both username and password match the credential criteria or requirements."""
	if len(username) < 4 or not username.isalnum():
		return False

	status = True
	# Checking the password strength
	if len(password) < 8:
		status = False
	elif not re.search('[a-z]', password):
		status = False
	elif not re.search('[A-Z]', password):
		status = False
	elif not re.search('[0-9]', password):
		status = False
	elif not re.search('[_:@#$&+-?.*;/]', password):
		status = False

	return status


def _verify_contact_name(name):
	"""Fails if contact name isn't valid."""
	if re.fullmatch('[a-zA-Z ]*', name) is None:
		return False


def _verify_contact_num(num):
	"""Fails if contact number isn't valid."""
	if re.fullmatch('''[+]?\d{0,3}[ ]?\d{10}''', num) is None:
			return False


def _verify_contact_email(email):
	"""Fails if contact email is not valid."""
	if re.search('''^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$''', email) is None:
		return False