import yagmail
import base64
import arrange
import collectdata
import emailkey
import jsondeal
import logmake

l0=0

def send_mail(sender_email,sender_password,receiver_email,message):
    print(emailkey.server())
    mail_server=yagmail.SMTP(user=sender_email,password=sender_password,host=emailkey.server(),port=jsondeal.get_smtp_server_port())

    Subject= "Machine Work status"
    img_att_file=arrange.get_latest_files_zwei(jsondeal.get_img_data_path())

#图片处理
    img_base64_list = []
    for img_path in img_att_file:
        with open(img_path, "rb") as img_file:
            img_data = img_file.read()
            img_base64 = base64.b64encode(img_data).decode("utf-8")
            img_base64_list.append(img_base64)
        
    html_content = f"""
 <html>
    <body>
        <h2>{Subject}</h2>
        <p>{message}</p>
        {''.join([f'<img src="data:image/png;base64,{img_base64_list[i]}" alt="Machine Work Image">' for i in range(len(img_base64_list))])}
    </body>
</html>
    """
    #<img src="data:image/png;base64,{img_base64_list[0]}" alt="Machine Work Image">
      #      <img src="data:image/png;base64,{img_base64_list[1]}" alt="Machine Work Image">
       #     <img src="data:image/png;base64,{img_base64_list[2]}" alt="Machine Work Image">

    #,attachments=arrange.get_latest_file_in_directory("/mountusb/crm/save")
    mail_server.send(to=receiver_email,subject=Subject,contents=html_content,attachments=img_att_file) #尾项附件listarry
    logmake.log_email_send(collectdata.gettime_only())
    mail_server.close()