import sys
import platform
import os

print("************************************************************")
print("sys.platform:  ", sys.platform)
print("************************************************************")

print("platform.architecture():  ", platform.architecture())
print("platform.architecture():  in cycle 'for'.")
current_arch = platform.architecture()
i = 0
for cur in current_arch:
    print("platform.architecture()[{}]:  {}".format(i, cur))
    i += 1

print("************************************************************")
print("platform.uname():  ", platform.uname())
print("platform.uname():  in cycle 'for'.")
current_os = platform.uname()
i = 0
for cur in current_os:
    print("platform.uname()[{}]:  {}".format(i, cur))
    i += 1
print("************************************************************")

print("platform.system():  ", platform.system())
print("platform.node():  ", platform.node())
print("platform.release():  ", platform.release())
print("platform.version():  ", platform.version())
print("platform.machine():  ", platform.machine())
print("platform.processor():  ", platform.processor())
print("platform.platform():  ", platform.platform())
print("************************************************************")
try:
    print("platform.mac_ver():  ", platform.mac_ver())
except Exception as e:
    print(e)

print("************************************************************")

try:
    print("platform.linux_distribution():  ", platform.linux_distribution())
except Exception as e:
    print(e)

print("************************************************************")

try:
    print("platform.win32_ver():  ", platform.win32_ver())
except Exception as e:
    print(e)

print("************************************************************")

print("os.getlogin():  ", os.getlogin())

print("os.name:  ", os.name)

print("os.environ:  ", os.environ)
env = os.environ
s_env = sorted(env.items())
for k, v in s_env:
    print("    ", k, " -> ", v)

print("************************************************************")