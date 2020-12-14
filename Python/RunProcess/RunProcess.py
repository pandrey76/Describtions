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

# Запуск процесса который будет работать после того как
# породимвший его процесс закончит работу, но при этом создаётся
# ещё один экземпляр консоли
##########################################################

# process = subprocess.Popen(["powershell.exe", file_path], shell=False,
#                            creationflags=win32process.CREATE_NEW_CONSOLE)

##########################################################


# RunProcess with DETACHED_PROCESS
# Всё работает как с флагом CREATE_NEW_CONSOLE, только
# без создания экземпляра консоли
##########################################################

file_path = "c:\\Work\\WindowsRemoteManeger\\PS\\Update.ps1"
subprocess.Popen(["powershell.exe", file_path], close_fds=True)
sleep(10)
##########################################################

# уСТАНОВКА OFFLINE-PACKAGES
# pip.exe wheel --wheel-dir "c:\\Work\\offline_packages" -r "C:\\Work\\acvpServer\\backend\\requirements.txt"