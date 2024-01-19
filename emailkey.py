import arrange
import jsondeal


def server():
    account=jsondeal.get_smtp_server()
    return account

def sendemail():        #发送者
    senderemail=jsondeal.get_sendermail()
    return senderemail

def sender_password():      #授权
    password=jsondeal.get_sender_password()
    return password

def receiveremail():        #接受者
    remail=jsondeal.get_receiveremail()
    return remail


#other

def imgpath():
    path=arrange.get_latest_file_in_directory()
    return path

def delpath():
    path=jsondeal.get_img_delpath()
    return path