import os
import random

def change_wallpaper():
    wallpaper_path = '/media/indrajeet/Inderjit/wallpapers'
    wallpapers = os.listdir(wallpaper_path)
    
    wallpaper = random.choice(wallpapers)
    command = 'gsettings set org.gnome.desktop.background picture-uri file:///'+ wallpaper_path +"/" + wallpaper
    os.system(command)

    return "wallpaper changed"
