"""Provides various helper functions."""

import tkinter as tk

def create_button(frame, button_text, function_to_call):
	return tk.Button(master=frame, text=button_text, fg='#FFFFFF', bg='#009688', command=function_to_call)

def create_label(frame, label_text):
	return tk.Label(master=frame, text=label_text, fg='#212121', bg='#CFD8DC')