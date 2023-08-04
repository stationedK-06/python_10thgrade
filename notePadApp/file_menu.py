import tkinter as tk
import time
from tkinter.filedialog import asksaveasfilename, askopenfilename
import os
import json
from tkinter import ttk
from tkinter import messagebox
filepath = None
split_tup = ()

# Functions
def new_file(wd, text):
  global filepath
  text.delete("1.0", tk.END)
  wd.title("Untitled - Notepad")
  filepath = None
  
def open_file(wd, text):
  global filepath
  global split_tup
  filepath = askopenfilename(defaultextension="*.*",
                             filetypes=[("All Files", "*.*"),
                                        ("text Files", "*.txt"),
                                        ("Json files", "*.json")])
  if not filepath:
    return
  split_tup = os.path.splitext(filepath)
  if split_tup[1] != '.txt' and split_tup[1] != '.json':
    messagebox.showinfo(wd,"This note pad only support txt and json")
    return
  text.delete("1.0", tk.END)
  if split_tup[1] == ".json":
    with open(filepath, "r") as f:
      data = json.load(f)
      text.insert(tk.END, data["text"])
  elif split_tup[1] == ".txt":
    with open(filepath, 'r') as f:
      data = f.read()
      text.insert(tk.END, data)
  wd.title(f"{filepath} - Notepad")


def save_file(wd, text):
  global split_tup
  global filepath
  if not filepath:
    save_as_file(wd, text)
    return
  with open(filepath, "w") as f:
    if split_tup[1] == ".json":
      data = {"text": text.get("1.0", tk.END)}
      json.dump(data, f, indent=4)
    elif split_tup[1] == ".txt":
      data = text.get("1.0", tk.END)
      f.write(data)
    else:
      return

  wd.title(f"{filepath} -Notepad")
  print("saved")


def save_as_file(wd, text):
  global filepath
  global split_tup
  filepath = asksaveasfilename(defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),
                                          ("text files", "*.txt"),
                                          ("Json Files", "*.json")])
  print(split_tup)

  if not filepath:
    return
  split_tup = os.path.splitext(filepath)
  data = {"text": text.get("1.0", tk.END)}
  with open(filepath, "w") as f:
    if split_tup[1] == ".json":
      data = {"text": text.get("1.0", tk.END)}
      json.dump(data, f, indent=4)
    elif split_tup[1] == ".txt":
      data = text.get("1.0", tk.END)
      f.write(data)
    else:
      return
  wd.title(f"{filepath} -Notepad")


def auto_save_setting(wd, text, auto_save_stat):
  new_window = tk.Toplevel(wd)
  new_window.title("Autosave-Setting")
  new_window.geometry("200x200")
  # tk.Label(new_window, text = 'setting').pack()
  tk.Checkbutton(new_window,
                 text="Enable Autosave",
                 variable=auto_save_stat,
                 onvalue=True,
                 offvalue=False,
                 command=lambda: auto_save(wd, text, auto_save_stat)).pack()


def start_timer(wd, text, auto_save_stat):
  global save_timer
  save_timer = time.time()
  wd.after(1000, lambda: check_autosave_timer(wd, text, auto_save_stat))
  print(time.asctime())
  print('processing')


def check_autosave_timer(wd, text, auto_save_stat):
  if auto_save_stat.get() == True:
    global save_timer
    global filepath
    if not filepath:
      alert_tap = tk.Toplevel(wd)
      alert_tap.title("Alert")
      ttk.Label(alert_tap,
                text="You have to save a file",
                font=('helveticabold', 14)).pack()
      auto_save_stat.set(False)
      save_as_file(wd, text)
      if not filepath:
        alert_tap.destroy()
        return
      elif filepath:
        auto_save(wd,text,auto_save_stat)
      alert_tap.mainloop()
      return

    current_time = time.time()
    save_file(wd, text)
    save_timer = current_time
    print(time.asctime())
    print('processing')
    wd.after(1000, lambda: check_autosave_timer(wd, text, auto_save_stat))
  elif auto_save_stat.get() == False:
    return
    
def auto_save(wd, text, auto_save_stat):
  if auto_save_stat.get() == True:
    start_timer(wd, text, auto_save_stat)
