import datetime
from playsound import playsound
hour=int(input("enter hour:"))
min=int(input("enter minutes:"))
meridiem=input("enter meridiem:")

if meridiem=="pm":
    hour+=12
    
while True:
    if hour==datetime.datetime.now().hour and min==datetime.datetime.now().minute:
        print("playing song...")
        playsound("D:\sampledata\[iSongs.info] 01 - Bhoom Bhaddhal.mp3")
        break

