import os

logpath="log/dlog.lg"



def log_del(date):
    logdir = os.path.dirname(logpath)
    if not os.path.exists(logdir):
        os.makedirs(logdir)
    with open(logpath, "a") as file:
        file.write("------->Delete temporary directory Time: " + date + "\n")


def log_crm(date,file_name):
    logdir = os.path.dirname(logpath)
    if not os.path.exists(logdir):
        os.makedirs(logdir)
    with open(logpath, "a") as file:
        file.write("Create photo files :-"+file_name[0]+"\n-"+file_name[1]+"\n-"+file_name[2]+"\n-"+file_name[3]+"\tTime:"+date+"\n")


def log_email_send(date):
    logdir = os.path.dirname(logpath)
    if not os.path.exists(logdir):
        os.makedirs(logdir)
    with open(logpath, "a") as file:
        file.write("Email Send \tTime:" + date + "\n")



def log_json_erro(error_contents,type,date):
    #date=str(date)
    logdir = os.path.dirname(logpath)
    if not os.path.exists(logdir):
        os.makedirs(logdir)
    with open(logpath, "a") as file:
        if type=="key" :
            file.write("Json erro-Key erro:"+error_contents+"\t Check Json Config File \t Date:"+date+"\n")
            print("ke") #log有重复异常抛出
        elif type=="jsonfile":
            file.write("Json file erro:"+error_contents+"\t Rest Json Or Recreate \t Date:"+date+"\n")
        elif type=="crtjson":
            file.write("Json Error creating file\t"+date+"\n")
        else:
            file.write("Json Unknown Error\t"+date+"\n")