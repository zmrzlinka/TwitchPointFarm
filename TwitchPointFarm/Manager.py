import os
import webbrowser
import subprocess

os.system('python AutoPoints.py')

folders = os.listdir(r'C:\Users\miros\Documents\TwitchPointFarm')

for stuff in folders:
    if(stuff=="Twitch"):
        webbrowser.open('https://www.twitch.tv/yassuo', new=2)
    
subprocess.call([r'C:\Users\miros\Documents\TwitchPointFarm\Cleaning.bat'])
