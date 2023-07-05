import instaloader
import cv2
from tkinter import *
from tkinter import filedialog

def browserFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)

def getIgProfile():
    ig = instaloader.Instaloader()
    # print(cv2.__version__)
    user = input("Enter username: ")
    ig.download_profile(user,profile_pic_only=True)
    # ig.download_profile(user,download_stories_only=True)    #login required ??

def imgQuality(img_path):
    # img_src = cv2.imread('D:\Mastercode\InstDp\\thieu.99\\2023-06-01_14-30-42_UTC_profile_pic.jpg', cv2.IMREAD_UNCHANGED)
    img_src = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    scale_percent = 200

    width = int(img_src.shape[1] * scale_percent / 100)
    height = int(img_src.shape[0] * scale_percent / 100)
    dsize = (width, height)
    output = cv2.resize(img_src, dsize, interpolation=cv2.INTER_LINEAR)
    new_img_name=input()
    cv2.imwrite(f"D:\Mastercode\InstDp\\thieu.99\\{new_img_name}.jpg",output)

window=Tk()

window.title('INSTDP')

window.geometry("500x500")

window.config(background = "white")

label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")
  
      
button_explore = Button(window,
                        text = "Browse Files",
                        command = browserFiles)

button_exit = Button(window,
                     text = "Exit",
                     command = exit)

label_file_explorer.grid(column = 1, row = 1)
  
button_explore.grid(column = 1, row = 2)
  
button_exit.grid(column = 1,row = 3)

window.mainloop()