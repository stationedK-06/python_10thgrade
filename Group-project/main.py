
import tkinter as tk
from tkinter.ttk import *
from tkinter import font
import csv
# etc
import time
import webbrowser
from PIL import ImageTk, Image
import edit_menu as em
import file_menu as fm




font_setting = {'font_family': 'Helvetica', 'font_size': 12}

def save_font_setting():
    with open('font_setting.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['font_family', 'font_size'])
        writer.writeheader()
        writer.writerow(font_setting)

def load_font_setting():
    try:
        with open('font_setting.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                font_setting['font_family'] = row['font_family']
                font_setting['font_size'] = row['font_size']
    except FileNotFoundError:
      pass
      



def font_window():
    global text
    font_window = tk.Toplevel(wd)
    font_window.title("Choose Font")
    our_font = font.Font(family="Helvetica", size=12)

    our_listbox = tk.Listbox(font_window, selectmode=tk.SINGLE, width=80)
    our_listbox.pack()

    for f in font.families():
        our_listbox.insert("end", f)

    size_var = tk.StringVar(font_window, value=str(our_font.cget("size")))
  
    def apply_font():
        selected_font = our_listbox.get(tk.ACTIVE)
        selected_size = size_var.get()
        text.config(font=(selected_font, int(selected_size)))
        font_setting['font_family'] = selected_font
        font_setting['font_size'] = selected_size
        save_font_setting()
    size_label = tk.Label(font_window, text="Font Size:")
    size_label.pack()

    size_entry = tk.Entry(font_window, textvariable=size_var)
    size_entry.pack()

    apply_button = tk.Button(font_window, text="Apply", command=apply_font)
    apply_button.pack()


def open_help_link():
    url = "https://www.bing.com/search?q=get+help+with+notepad+in+windows&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA"
    webbrowser.open_new_tab(url)

def create_help_window():
    help_window = tk.Toplevel(wd)
    help_window.title("View Help Link")
    help_window.geometry("850x100")

    link_label = tk.Label(help_window, text="https://www.bing.com/search?q=get+help+with+notepad+in+windows&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA", font=('helvetica', 8))
    link_label.pack()

    open_link_button = tk.Button(help_window, text="Open Link", command=open_help_link)
    open_link_button.pack()





def helpimage():
    imgwindow = tk.Toplevel(wd)
    imgwindow.title("About Notepad")

    image_path = "About_Notepad.gif"
    image = ImageTk.PhotoImage(file=image_path)  # Use ImageTk.PhotoImage to load the image

    image_label = tk.Label(imgwindow, image=image)
    image_label.image = image  # Store a reference to the image
    image_label.pack()




load_font_setting()
wd = tk.Tk()
wd.title("Untitled - Notepad")
wd.geometry("640x480")
auto_save_stat = tk.BooleanVar()
save_timer = time.time()
autosave_interval = 60
# global

# Main Window Menus/Bars

# for text box
text = tk.Text(wd, font=(font_setting['font_family'], int(font_setting['font_size'])))
text.pack(expand=True)

menu_bar = tk.Menu(wd)
file_menu = tk.Menu(menu_bar, tearoff=False)
edit_menu = tk.Menu(menu_bar, tearoff = False)
format_menu = tk.Menu(menu_bar, tearoff = False)
setting_menu = tk.Menu(menu_bar, tearoff = False)
help_menu = tk.Menu(menu_bar, tearoff = False)

file_menu.add_command(label="Open", command= lambda: fm.open_file(wd,text))
file_menu.add_command(label="Save as", command=lambda: fm.save_as_file(wd,text))
file_menu.add_command(label="Save", command= lambda: fm.save_file(wd, text))
file_menu.add_command(label="New file", command = lambda: fm.new_file(wd, text))
file_menu.add_separator()
file_menu.add_command(label="Exit", command= wd.quit)


setting_menu.add_command(label = "Auto Save", command = lambda: fm.auto_save_setting(wd,text,auto_save_stat))
#help menu
help_menu.add_command(label = "View help", command = lambda: create_help_window())
help_menu.add_command(label = "About Notepad", command = lambda: helpimage())

# edit_menu
edit_menu.add_command(label = "Copy",command = lambda: em.copy_text(text))
edit_menu.add_command(label = "Paste",command = lambda: em.paste_text(text))
edit_menu.add_command(label = "Select All", command = lambda: em.select_all(text))
edit_menu.add_command(label = "Clear All", command = lambda: em.clear_all(text))
edit_menu.add_command(label = "Delete",command= lambda: em.delete_text(text))

# font formatting window
format_menu=tk.Menu(menu_bar, tearoff=False)
format_menu.add_command(label="Format Notepad", command=font_window)
# format_save.tk.Menu(menu_bar, tearoff = False)
# format_save.add_command(Label = "Save format setting", command = lambda: save_font_setting(font_family, font_size))


menu_bar.add_cascade(label= "Format menu", menu = format_menu)
menu_bar.add_cascade(label="File menu", menu=file_menu)
menu_bar.add_cascade(label="Setting", menu = setting_menu)
menu_bar.add_cascade(label="Help", menu = help_menu)
menu_bar.add_cascade(label = "Edit menu", menu = edit_menu)
# font_menu.add_command(label = "Font", commnad = font_set)
# menu_bar.add_cascade(label = "Font setting", menu = )
wd.config(menu=menu_bar)
wd.mainloop()

