# auto-zoom-opener
This is a light and effective way of opening a recurrent Zoom meeting or Google meeting that only needs to be accessed on work days. This project is compatible with every operating system with only a few previous configurations that must be done before getting everything started. 
## Pre-configuration
To run the project correctly on your computer a dependency must be installed. regardless of the Operative system. The most important one is Python. 
1. To install in Linux simply type in the terminal `sudo apt update` followed by a `sudo apt install python3`.
To install in Windows or MacOS simply go to [Python Downloads](https://www.python.org/downloads) download your version and be sure to configure the download to .PATH.
2. After this the process is fairly simple. By this point you can clone the project. To allow it to work properly simply clone it in your user folder and type  on the terminal `git clone https://github.com/Delta12348/auto-zoom-opener.git` (or simply type it in the terminal without any previous configuration). 
  * Windows: Win + R then type cmd to open terminal
  * Linux: Super + T
4. After that, open the downloaded folder, three files should be there configuration.py startup.sh and README.my which is this file.
5. We must execute the configuration.py file before doing anything else, to run, you can either use the terminal by typing `cd auto-zoom.opener` and then `python3 configuration.py` or by clicking the configuration.py twice, just be sure you have the Python interpreter as the default opener for .py files.
6. Follow all the instructions that are listed on the terminal. The terminal should ask operative system and meeting link.
7. If on Windows, the process has ended and every time you turn on your computer on a week day, it will open the meeting. If on Linux or MacOS some more steps must be done.  
6. Save the file.
7. Follow the steps depending on your operating system.
## Linux or MacOS
The project has been preloaded with an SH script that facilitates the proccess a lot, the only thing that must be done is to allow the script startup.sh run on startup and that is it. Startup files are mainly on configuration, simply select the startup.sh file on that menu. There you go, every time you boot your computer the meeting will open.
## Windows (If not working)
Unless you have a unix terminal installed, you can follow the process above. If not you can do the following. 
1. Since Windows cannot access shell files, you can delete startup.sh file. 
2. Just copy and paste the zoom_opener.py into the startmenu located in e.g. `C:\Users\Anmol\AppData\Roaming\Microsoft\Windows\Start Menu\Programs`
3. Adjust the properties of the python file to run as a script and not as text 
  * Right Click the zoom-opener.py and select properties
  * Be sure to select to the Python application before any other program. 
