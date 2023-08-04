import tkinter as tk
import webbrowser
from PIL import ImageTk, Image


def open_help_link():
  url = "https://www.bing.com/search?q=get+help+with+notepad+in+windows&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA"
  webbrowser.open_new_tab(url)


def create_help_window(wd):
  help_window = tk.Toplevel(wd)
  help_window.title("View Help Link")
  help_window.geometry("850x100")

  link_label = tk.Label(
    help_window,
    text=
    "https://www.bing.com/search?q=get+help+with+notepad+in+windows&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA",
    font=('helvetica', 8))
  link_label.pack()

  open_link_button = tk.Button(help_window,
                               text="Open Link",
                               command=open_help_link)
  open_link_button.pack()


def helpimage(wd):
  imgwindow = tk.Toplevel(wd)
  imgwindow.title("About Notepad")

  image_path = "About_Notepad.gif"
  image = ImageTk.PhotoImage(
    file=image_path)  # Use ImageTk.PhotoImage to load the image

  image_label = tk.Label(imgwindow, image=image)
  image_label.image = image  # Store a reference to the image
  image_label.pack()
