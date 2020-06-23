# File Monitor (in python)
This project utilises the `win32` python library which acts as an intermediate between the python program, and the windows API. The python script uses the `ReadDirectoryChangesW` API function provided by the windows API, and waits for incoming images downloaded while browsing with internet explorer. After acquiring the images it then writes them to a new location in the operating system (it copies them to the `current_directory + "\images"`).

# Installation
Clone the file monitor repository
```
git clone https://github.com/guysudai1/File-Monitor/
```

# Usage
```
python filemon.py
```
