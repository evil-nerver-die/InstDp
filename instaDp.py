import cv2
import instaloader
import os
import shutil
import time
import tkinter as tk
import webbrowser

from glob import glob
from instascrape import Reel
from PIL import Image, ImageTk 


window=tk.Tk()
window.geometry("500x300")
window.title(" InstaDP ")
window.iconbitmap('./icon_and_image\\instagram_black_logo_icon_147122.ico')
menu_bar=tk.Menu(window)
bg_img=ImageTk.PhotoImage(Image.open("./icon_and_image\\500x300_1697031-6a047e58-986e-4253-87bd-df2d0f727708.jpg"))
window.config(menu=menu_bar, bg="#2b203b")

# Get profile picture function

user_var=tk.StringVar()
reel_url_var=tk.StringVar()

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
    scale_percent = 250

    width = int(img_src.shape[1] * scale_percent / 100)
    height = int(img_src.shape[0] * scale_percent / 100)
    dsize = (width, height)
    output = cv2.resize(img_src, dsize, interpolation=cv2.INTER_LINEAR)
    # new_img_name=input()
    cv2.imwrite(f"./{user}\\{user}_profile_pic.jpg",output)

def getProfilePic():
    user=inputUsername()
    isExist=os.path.exists(f"./{user}")
    if isExist:
        shutil.rmtree(f"./{user}")
    getIgProfile(user)
    img_path=getImgPath(user)
    imgQuality(img_path, user)
    img = Image.open(f"./{user}\\{user}_profile_pic.jpg")
    img.show()

# Get reel video function

def getReelVideo():
    reel_link=reel_url_var.get()
    SESSIONID = ""
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
        Safari/537.36 Edg/79.0.309.43",
        "cookie": f'sessionid={SESSIONID};'
    }
    insta_reel = Reel(reel_link)

    insta_reel.scrape(headers=headers)

    insta_reel.download(fp=f".\\reel{int(time.time())}.mp4")

    print("Download succcessfully")



# Display function

def go_home():
    hideAllFrames()
    lobby_frame.pack(fill="both",expand=1)
    bg_label=tk.Label(lobby_frame, image=bg_img)
    bg_label.pack()

def openGetProfilePicFrame():
    hideAllFrames()
    get_profile_pic_frame.pack(fill="both", expand=1)
    user_name=tk.Label(get_profile_pic_frame, text="Username", font=('calibre',12, 'bold'), bg="#2b203b").place(x=70,y=60)
    get_img_button=tk.Button(get_profile_pic_frame, text="Get profile pic",font=('calibre',10, 'bold'), bg="#605670", command=getProfilePic).place(x=200,y=120)

    user_name_input_area=tk.Entry(get_profile_pic_frame, textvariable=user_var, width=40).place(x=180,y=60)
    # user_name_input_area.insert(0,'Enter instagram username....')



def openGetReelFrame():
    hideAllFrames()
    get_reel_vid_frame.pack(fill="both",expand=1)
    reel_URL=tk.Label(get_reel_vid_frame, text="Link Reel", font=('calibre',12, 'bold'), bg="#2b203b").place(x=70,y=60)
    download_button=tk.Button(get_reel_vid_frame, text="Download Reel",font=('calibre',10, 'bold'), bg="#605670", command=getReelVideo).place(x=200,y=120)

    url_input_area=tk.Entry(get_reel_vid_frame, textvariable=reel_url_var, width=40).place(x=180,y=60)

def open_help_frame():
    # url="https://www.google.com.vn/?gws_rd=ssl"
    # webbrowser.open(url)
    hideAllFrames()
    help_text = tk.Text(get_help_frame, width=40, height=12, font=('calibre',12))
    help_file=open("./guidle.txt", 'r')
    stuff=help_file.read()
    help_text.insert(tk.END, stuff)
    help_file.close()
    help_text.pack()
    
    

def linkInfor():
    url="https://github.com/evil-nerver-die"
    webbrowser.open(url)

def hideAllFrames():
    lobby_frame.pack_forget()
    get_profile_pic_frame.pack_forget()
    get_reel_vid_frame.pack_forget()
    get_help_frame.pack_forget()
    

tool_menu=tk.Menu(menu_bar)
menu_bar.add_cascade(label="Options", menu=tool_menu)
tool_menu.add_command(label="Home", command=go_home)
tool_menu.add_separator()
tool_menu.add_command(label="Get profile pic", command=openGetProfilePicFrame)
tool_menu.add_separator()
tool_menu.add_command(label="Get reel video", command=openGetReelFrame)

help_menu=tk.Menu(menu_bar)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Help", command=open_help_frame)
help_menu.add_command(label="About Us", command=linkInfor)
help_menu.add_separator()
help_menu.add_command(label="Exit", command=window.quit)

get_profile_pic_frame=tk.Frame(window, width=500, height=300,bg="#2b203b")
get_reel_vid_frame=tk.Frame(window, width=500, height=300,bg="#2b203b")
lobby_frame=tk.Frame(window,width=500, height=300,bg="#2b203b")
lobby_frame.pack(fill="both",expand=1)
get_help_frame=tk.Frame(window,width=500, height=300,bg="#2b203b")

bg_label=tk.Label(lobby_frame, image=bg_img)
bg_label.pack()



window.mainloop()
