import sys
import platform
import os
# pip install py-cpuinfo
import cpuinfo 

print("************************************************************")

print("sys.platform:  ", sys.platform)
# ver =  sys.getwindowsversion()
# print("sys.getwindowsversion():  ", ver)
# i = 0
# for cur in ver:
#     print("sys.getwindowsversion()[{}]:  {}".format(i, cur))
#     i += 1
print("************************************************************")

print("platform.version():  ", platform.version())

print("platform.architecture():  ", platform.architecture())

print("platform.architecture()[0]:  ", platform.architecture()[0])

print("platform.architecture()[1]:  ", platform.architecture()[1])

print("************************************************************")

print("platform.uname():  ", platform.uname())
print("platform.uname()[0]:  ", platform.uname()[0])
print("platform.uname()[1]:  ", platform.uname()[1])
print("platform.uname()[5]:  ", platform.uname()[5])

print("platform.uname():  in cycle 'for'.")
current_os = platform.uname()
i = 0
for cur in current_os:
    print("platform.uname()[{}]:  {}".format(i, cur))
    i += 1
print("platform.processor():  ", platform.processor())
print("platform.platform():  ", platform.platform())
print("platform.machine():  ", platform.machine())
print("platform.version():  ", platform.version())
print("platform.release():  ", platform.release())
print("platform.system():  ", platform.system())
print("************************************************************")

print("os.getlogin():  ", os.getlogin())

print("os.name:  ", os.name)

print("os.environ:  ", os.environ)
env = os.environ
s_env = sorted(env.items())
for k, v in s_env:
    print("    ", k, " -> ", v)
# print("os.environ['OS']:  ", os.environ['OS'])
# print("os.environ['PLATFORM']:  ", os.environ['PLATFORM'])
# print("os.environ['PROCESSOR_ARCHITECTURE']:  ", os.environ['PROCESSOR_ARCHITECTURE'])
# print("os.environ['PROCESSOR_IDENTIFIER']:  ", os.environ['PROCESSOR_IDENTIFIER'])
# print("os.environ['PROCESSOR_LEVEL']:  ", os.environ['PROCESSOR_LEVEL'])
# print("os.environ['PROCESSOR_REVISION']:  ", os.environ['PROCESSOR_REVISION'])
# print("os.environ['NUMBER_OF_PROCESSORS']:  ", os.environ['NUMBER_OF_PROCESSORS'])

# print("os.environ['USERNAME']:  ", os.environ['USERNAME'])
# print("os.environ['USERPROFILE']:  ", os.environ['USERPROFILE'])
# print("************************************************************")

print("************************************************************")
cpu = cpuinfo.get_cpu_info()
print("cpuinfo.get_cpu_info():  ", cpu)

print("cpuinfo.get_cpu_info(['brand_raw']):  ", cpu['brand_raw'])
print("cpuinfo.get_cpu_info() by sorted list")
s_cpu = sorted(cpu.items())
for k, v in s_cpu:
    print("    ", k, " -> ", v)
print("************************************************************")
