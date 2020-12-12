import subprocess
# import sys
import win32process
import os
from time import sleep

# pid = subprocess.Popen([sys.executable, "longtask.py"],
file_path = os.path.dirname(os.path.realpath(__file__))
print(file_path)
file_path = os.path.join(file_path, "HelloWorld.PS1")
print(file_path)
# creation_flags = win32process.DETACHED_PROCESS
# creation_flags = win32process.CREATE_NEW_CONSOLE
process = subprocess.Popen(["powershell.exe", file_path], shell=False,
                           creationflags=win32process.CREATE_NEW_CONSOLE)
sleep(5)

# уСТАНОВКА OFFLINE-PACKAGES
# pip.exe wheel --wheel-dir "c:\\Work\\offline_packages" -r "C:\\Work\\acvpServer\\backend\\requirements.txt"