import cv2
import instaloader
import os
from glob import glob
from PIL import Image 
import tkinter as tk

window=tk.Tk()
window.geometry("500x300")
window.title(" InstaDP ")

user_var=tk.StringVar()

def inputUsername():
    # user = input("Enter username: ")
    user=user_var.get()
    print(user)
    return user

def getIgProfile(user):
    ig = instaloader.Instaloader()
    ig.download_profile(user,profile_pic_only=True)
    # ig.download_profile(user,download_stories_only=True)    #login required ??

def getImgPath(user):
    img_path_list=glob(os.path.join(f"./{user}","*.jpg"))
    for img_path in img_path_list:
        return img_path

def imgQuality(img_path, user):
    # img_src = cv2.imread('D:\Mastercode\InstDp\\thieu.99\\2023-06-01_14-30-42_UTC_profile_pic.jpg', cv2.IMREAD_UNCHANGED)
    img_src = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    scale_percent = 200

    width = int(img_src.shape[1] * scale_percent / 100)
    height = int(img_src.shape[0] * scale_percent / 100)
    dsize = (width, height)
    output = cv2.resize(img_src, dsize, interpolation=cv2.INTER_LINEAR)
    # new_img_name=input()
    cv2.imwrite(f"./{user}\\{user}_profile_pic.jpg",output)

def getProfilePic():
    user=inputUsername()
    getIgProfile(user)
    img_path=getImgPath(user)
    imgQuality(img_path, user)
    img = Image.open(f"./{user}\\{user}_profile_pic.jpg")
    img.show()

user_name=tk.Label(window, text="Username").place(x=40,y=60)
get_img_button=tk.Button(window, text="Get profile pic", command=getProfilePic).place(x=40,y=120)

user_name_input_area=tk.Entry(window, textvariable=user_var, width=35).place(x=120,y=60)

window.mainloop()
