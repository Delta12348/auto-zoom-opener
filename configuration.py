import os

zoomLink = input("Please copy and paste the link of the Zoom or Google meeting: ")

openerMainCode = """import datetime
import webbrowser
zoomLink = "%s"
today = datetime.date.today().weekday()
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
todayDay = week_days[today]
if todayDay in working_days:
    webbrowser.open(zoomLink)
else:
    exit()""" % zoomLink
print("Hello, welcome to the configuration menu")

print("select your operating system")

userInput = int(input("Type 0 if Linux or Mac Type 1 if Windows: "))

if userInput == 0:
    zoomOpener = open("zoom_opener.py", "w+")
    
    zoomOpener.writelines(openerMainCode)
elif userInput == 1:
    dir_fd = os.open("C:/Users/current_user/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup", os.O_RDONLY)
    def opener(path, flags):
        return os.open(path, flags, dir_fd=dir_fd)
    with open("zoom_opener.py", "w+", opener=opener) as f:
        f.writelines(openerMainCode)    



