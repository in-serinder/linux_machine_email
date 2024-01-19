import json
import datetime
import os
import collectdata
import logmake


file_name_andpath="config.json" #also ist path
json_data={
    "creat date":datetime.datetime.now().isoformat(),
    "img_path":"/mountusb/crm/save",
    "index_mail_viewimg":4,
    "server":"smtp.163.com",
    "port":465,
    "senderemail":"",
    "sender_password":"",
    "imgdelpath":"",
    "receiveremail":"",
    "showstatusmessage":"True",
    "showjsoninfo":"True" #True or False
}


file_data={}
date=collectdata.gettime_only()

#if not os.path.exists(file_name_andpath):
#        with open("config.json","w") as file:
#            json.dump(json_data,file,indent=4)


def get_show_jsoninfo():  #fsc
    try:
        return file_data['showjsoninfo']
    except KeyError:
        logmake.log_json_erro("showjsoninfo","key",date)


def read_json():
    global file_data
    with open(file_name_andpath, "r") as file:
            file_data=json.load(file)
            if get_show_jsoninfo()=="True":
                print(f"jsoninfo{get_show_jsoninfo()}{file_data}")



def base_exjson():
    if not os.path.exists(file_name_andpath):
        with open("config.json","w") as file:
            json.dump(json_data,file,indent=4)
    else:
        try:
            read_json()
        except FileNotFoundError:
            logmake.log_json_erro("Json Config File Not Found","jsonfile")
    #print(file_data)
    return None;







try:
    base_exjson()
except Exception:
    logmake.log_json_erro("base_exjson-create_json","crtjson",date)
#read_json()
def get_html_viewimg_file():
    try:
        return file_data['index_mail_viewimg']
    except KeyError:
        logmake.log_json_erro("html_viewimg_file","key")


def get_img_data_path():
    try:
        return file_data['img_path']
    except KeyError:
        logmake.log_json_erro("img_data_path","key",date)


def get_smtp_server():
    try:
        return file_data['server']
    except KeyError:
        logmake.log_json_erro("smtp_server_address","key",date)

def get_smtp_server_port():
    #print("tesp",file_data)
    try:
        return file_data['port']
    except KeyError:
        logmake.log_json_erro("smtp_server_port","key",date)

def get_sendermail():
    #print("tesp",file_data)
    try:
        return file_data['senderemail']
    except KeyError:
        logmake.log_json_erro("sendermail","key",date)

def get_receiveremail():
    try:
        return file_data['receiveremail']
    except KeyError:
        logmake.log_json_erro("receiveremail","key",date)

def get_sender_password():
    try:
        return file_data['sender_password']
    except KeyError:
        logmake.log_json_erro("sender_password","key",date)

def get_img_delpath():
    try:
        return file_data['imgdelpath']
    except KeyError:
        logmake.log_json_erro("imgdelpath","key",date)

def get_show_statusmessage():  #fsc
    try:
        return file_data['showstatusmessage']
    except KeyError:
        logmake.log_json_erro("showstatusmessage","key",date)
