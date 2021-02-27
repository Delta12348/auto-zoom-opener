# auto-zoom-opener
This is a light and effective way of opening a recurrent Zoom meeting or Google meeting that only needs to be accesed on work days. This project is compatible with every operating system with only a few previous configurations that must be done before getting everything started. 
## Pre-configuration
To run the project correctly on your computer a dependency must be installed. regardless of the Operative system. The most important one is Python. 
1. To install in Linux simply type in the terminal `sudo apt update` followed by a `sudo apt install python3`.
To install in Windows or MacOS simply go to [Python Downloads](https://www.python.org/downloads) download your version and be sure to configure the download to .PATH.
2. After this the process is fairly simple. By this point you can clone the project. To allow it to work properly simply clone it in your user folder and type  on the terminal `git clone https://github.com/Delta12348/auto-zoom-opener.git` (or simply type it in the terminal without any previous configuration). 
  * Windows: Win + R then type cmd to open terminal
  * Linux: Super + T
4. After that, open the downloaded folder, three files should be there zoom-opener.py startup.sh and README.my which is this file.
5. We must do a series of modifications to the zoom-opener file before doing anything else. As you can see, the code in this one is quite simple and it should look like this  
```Python
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
```
The only thing that needs to be configured is the `zoomLink = ""` line. Just type the zoom link you want to access when you access your computer e.g. `zoomLink = "https://us02web.zoom.us/j/insert the rest of session ID here"` You can also change, working_days if you like, to adjust you working days.  
6. Save the file.
7. Follow the steps depending on your operating system.
## Linux or MacOS
The project has been preloaded with an SH script that facilitates the proccess a lot, the only thing that must be done is to allow the script startup.sh run on startup and that is it. Startup files are mainly on configuration, simply select the startup.sh file on that menu. There you go, every time you boot your computer. 
## Windows
Unless you have a unix terminal installed, you can follow the process above. If not you can do the following. 
1. Since Windows cannot access shell files, you can delete startup.sh file. 
2. Just copy and paste the zoom-opener.py into the startmenu located in e.g. `C:\Users\Anmol\AppData\Roaming\Microsoft\Windows\Start Menu\Programs`
3. Adjust the properties of the python file to run as a script and not as text 
  * Right Click the zoom-opener.py and select properties
  * Be sure to select to the Python application before any other program. 
