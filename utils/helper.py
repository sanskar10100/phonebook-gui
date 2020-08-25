"""Provides various helper functions."""

import tkinter as tk
import hashlib

def create_button(frame, button_text, function_to_call):
	"""Returns a new button created according to the style guidelines."""
	return tk.Button(master=frame, text=button_text, fg='#FFFFFF', bg='#009688', command=function_to_call)

def create_label(frame, label_text):
	"""Returns a newly created label according to the style guidlines."""
	return tk.Label(master=frame, text=label_text, fg='#212121', bg='#CFD8DC')

def encrypt_credentials(username, password):
	"""Return the login credential in sha256 encrypted format."""
	encrypt_login_details = list()
	encrypt_login_details.append(hashlib.sha256(username.encode()).hexdigest())
	encrypt_login_details.append(hashlib.sha256(password.encode()).hexdigest())
	return tuple(encrypt_login_details)

def scrub(table_name):
	"""Sanitizes input for database query"""
	return ''.join( chr for chr in table_name if chr.isalnum() or chr == '_' )