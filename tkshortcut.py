from tkinter import *
from PIL import Image,ImageTk
import os
from time import *

'''
I HAVE WRITTEN THESE SIMPLE CODE TO USE SHORT CUT FOR MY PERSONAL TKINTER PROJECT

- Here we got one short cut name tkCenter - this is nothing but centerize the window in display
  all we just need to do is pass the root or window class as a parameter of tkCenter.

- Here also we got tkSplash - this is very helpfull to create a splash screen in tkinter. 
  For that we just simply need to a GIF file . If we want to use our personal video 
  than we have to convert that video into GIF file first . I use GIF file Cz splash screen 
  remains for few seconds and a GIF file is enough for that.
  Parameters ==> X exis of GIF, Y exis of GIF, GIF_name.extension (String with upper comma)

'''

def tkCenter(the_window):
    the_window.update_idletasks()
    width = the_window.winfo_width()
    frm_width = the_window.winfo_rootx() - the_window.winfo_x()
    win_width = width + 2 * frm_width
    height = the_window.winfo_height()
    titlebar_height = the_window.winfo_rooty() - the_window.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = the_window.winfo_screenwidth() // 2 - win_width // 2
    y = the_window.winfo_screenheight() // 2 - win_height // 2
    the_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    the_window.deiconify()




def tkSplash(splash_x, splash_y,GIF_name):

    the_window = Tk()
    the_window.geometry(f"{splash_x}x{splash_y}")
    the_window.wm_overrideredirect(True)


    the_window.update_idletasks()
    width = the_window.winfo_width()
    frm_width = the_window.winfo_rootx() - the_window.winfo_x()
    win_width = width + 2 * frm_width
    height = the_window.winfo_height()
    titlebar_height = the_window.winfo_rooty() - the_window.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = the_window.winfo_screenwidth() // 2 - win_width // 2
    y = the_window.winfo_screenheight() // 2 - win_height // 2
    the_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    the_window.deiconify()

    gif = Image.open(GIF_name)
    length_of_frames = gif.n_frames

    try:
        os.mkdir('frame_of_GIF')
        frame_of_GIF = []
        gif = Image.open(GIF_name)
        length_of_frames = gif.n_frames

        for i in range(length_of_frames):
            gif.seek(i)
            gif.save(os.path.join("frame_of_GIF",f"gif{i}.png"))
            frame_of_GIF.append(os.path.join("frame_of_GIF",f"gif{i}.png"))

    except:
        pass

    for i in range(length_of_frames):

# Resize img and use ==>
        img= (Image.open(f"frame_of_GIF/gif{i}.png"))
        resized_image= img.resize((splash_x,splash_y), Image.Resampling.LANCZOS)
        new_image= ImageTk.PhotoImage(resized_image)

# USING THE IMAGES OF GIF AS SPLASH ===============================================>>>
        sample = Label(the_window, image=new_image,bd=0)
        sample.place(x=0,y=0)
        the_window.update_idletasks()
        sleep(0.1)

    the_window.destroy()
    the_window.mainloop()