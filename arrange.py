import os
import datetime
from datetime import datetime, timedelta
import collectdata
import jsondeal
import emailkey
import logmake


def cpu_temperatures_ar(temperatures):
    if 'coretemp' in temperatures:
        core_temps=temperatures['coretemp']
        table=""
        for temp in core_temps:
            table="Core:"+temp.label+"Temperatures:"+temp.current

def delete_files_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

def get_latest_file_in_directory(directory):
    files = [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    if not files:
        return None
    latest_file = max(files, key=os.path.getmtime)
    return latest_file

check_time = datetime(2022, 1, 15, 2, 30)

def is_last_day_of_week_delimg():       #闲置
    today = datetime.datetime.now()
    if today.weekday() == 6 and today.hour == 12:
        delete_files_in_directory(emailkey.delpath())
        logmake.log_del(collectdata.gettime())
        return True
    return False

def is_last_day_of_week_delimg2():
    now = datetime.now()
    last_day_of_week = now + timedelta(days=(6 - now.weekday()))
    start_time = last_day_of_week.replace(hour=12, minute=0, second=0)
    end_time = last_day_of_week.replace(hour=3, minute=0, second=0) + timedelta(days=1)
    if start_time <= now <= end_time:
        delete_files_in_directory(emailkey.delpath())
        logmake.log_del(collectdata.gettime())
        return True
    else:
        return False



def get_latest_files_zwei(dirt):
    files = os.listdir(dirt)
    files = [os.path.join(dirt, file) for file in files]
    files = sorted(files, key=os.path.getmtime, reverse=True)
    latest_files = files[:jsondeal.get_html_viewimg_file()]  #pick
    return latest_files