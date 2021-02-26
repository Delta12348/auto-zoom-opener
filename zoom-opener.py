import datetime
import webbrowser

zoomLink = ""
today = datetime.date.today().weekday()
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
todayDay = week_days[today]

if todayDay in working_days:
    webbrowser.open(zoomLink)
else: 
    print("It is not a working day. Enjoy!!!!")
