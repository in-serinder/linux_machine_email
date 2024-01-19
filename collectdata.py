import datetime
import psutil
import arrange
import subprocess
import os

import time

def gettime():
    current_time=datetime.datetime.now()
    #current_time=os.system("date")
    unix_time=int(time.time())

    return "Date:"+str(current_time)+"\nFor Unix:"+str(unix_time)


def gettime_only():
    current_time=datetime.datetime.now()
    #current_time=os.system("date")
    return str(current_time)

def hardinfo():
    cpu_prenct=psutil.cpu_percent()
    cpu_info=psutil.cpu_freq().current/1000
    cpu_core=psutil.cpu_count()
    cpu_hardles=psutil.cpu_count(logical=False)

    memory=psutil.virtual_memory()
    total_memory =memory.total
    avaiable_memory=memory.available
    used_memory=memory.used
    memory_percent=memory.percent

    swap=psutil.swap_memory()
    total_swap=swap.total
    swap_avaiable_used=swap.used
    free_swap=swap.free
    swap_percent=swap.percent


    temperature = subprocess.check_output("sensors", shell=True, text=True)
    progs = subprocess.check_output("ps -eo pid,comm,%cpu --sort=-%cpu | head -n 21", shell=True, text=True)
    localhost = subprocess.check_output("arp-scan --localnet", shell=True, text=True)
    cpuname = subprocess.check_output("lscpu | grep 'Model name' | awk -F: '{print $2}' | sed 's/^[ \t]*//'",shell=True,text=True)
    #cpu_temperatures=Cpu(monitoring_latency=1)
    #cpu_temps=cpu_temperatures.temperature arp-scan --localnet




    cpu= f"-----------------CPU-------------------\nCPU:{cpuname}Freq:{cpu_info:.3f}GHz\nCores: {cpu_core}\nThread: {cpu_hardles}\nUsed Percent: {cpu_prenct}%\n" #+"\nCPU Temps:"+cpu_temps
    memorytable = f"-----------------RAM-------------------\nTotal memory:{total_memory/1024/1024:.2f}MB\nAvailable memory:{avaiable_memory/1024/1024:.2f}MB\nUsed Memory:{used_memory/1024/1024:.2f}MB\nMemory Percent:{memory_percent}%\n"
    swaptable = f"-----------------Swap-------------------\nTotal Swap:{total_swap/1024/1024:.2f}MB\nAvailable Swap:{swap_avaiable_used/1024/1024:.2f}MB\nFree Swap:{free_swap/1024/1024:.2f}MB\nSwap Percent:{swap_percent}%\n"
    temperaturetable = "-----------------Temperature-------------------\n" +temperature
    diskusetable = "-----------------Disk-------------------\n" +subprocess.check_output("df", shell=True, text=True)
    procgresstable = "-----------------Process-------------------\n" +progs
    localhosttable="-----------------LocalHost-------------------\n"+localhost
    return cpu+memorytable+swaptable+temperaturetable+diskusetable+procgresstable+localhosttable

