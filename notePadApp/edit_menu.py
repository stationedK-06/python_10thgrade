# Module functioning 
import tkinter as tk


def delete_text(text): 
  text.event_generate(("<<Cut>>"))
def paste_text(text):
  text.event_generate(("<<Paste>>"))
def copy_text(text):
  text.event_generate(("<<Copy>>"))
def select_all(text):
  text.tag_add('sel','1.0','end')
def clear_all(text):
  text.delete(1.0, tk.END)

