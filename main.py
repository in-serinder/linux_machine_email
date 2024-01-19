import arrange
import emailcontent
import collectdata
import emailkey
import logmake
import jsondeal
import smtpsend

if __name__ == '__main__':
    smtpsend.send_mail(emailkey.sendemail(),emailkey.sender_password(),emailkey.receiveremail(),emailcontent.message())
    logmake.log_crm(collectdata.gettime_only(),arrange.get_latest_files_zwei(jsondeal.get_img_data_path()))
    jsondeal.base_exjson()
    arrange.is_last_day_of_week_delimg2()
    if jsondeal.get_show_statusmessage()=="True":
        print(emailcontent.message())
    else:
        print(f"Send Successful Date:{collectdata.gettime_only()}")

