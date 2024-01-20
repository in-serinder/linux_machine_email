# About this program/bash script
- [Required packages](#how-it-operateswhat-is-needed)
- [Configuration](#how-to-configure-it)
- [Execution](#run-it)
- [Effect](#the-displayed-effect)
## How it operates&What is needed
This program utilizes Linux command-line tools and pip third-party libraries during runtime, so if you want to use it, you need to have these dependencies.

**Linux tools used**
```
date
fswebcam
scrot
sensors
awk
arp-scan
grep
df
````

**Required pip third-party libraries**
``````
yagmail==0.15.293
psutil==5.9.7
``````
They function in sending emails and obtaining hardware information
*and* You can use the following commands
``````
pip install -r requirements.txt
``````

## How to configure it
The configuration of the program is divided into two files: `crms.sh` and `config.json`. In `crms.sh`, the program handles input, delay management, and image capture. `config.json` is responsible for configuring SMTP settings, email recipients, and some output information settings.

### `crms.sh`
Due to time constraints, I urgently need a script to help me monitor the system status and surrounding environment. I haven't put much effort into the code, so the execution of this program is delayed and looped. This Bash script will launch the main program after capturing the necessary photos.
``````
sleep 1800    /*It will execute the loop again in half an hour because the main program does not have a loop mechanism*/

source_dir="/mountusb/crm/save" /*This variable specifies a relative path to store the captured file*/

fswebcam /*Camera capture*/
scrot /*To capture the screen of the current execution environment with a graphical desktop, you can remove or comment out the code if you don't need it.*/
``````

### `config.json`
As you can see, it is configured using JSON due to its concise and easily readable nature.
``````

{
    "img_path":"",
    "index_mail_viewimg": 4,
    "server": "smtp.163.com",
    "port": 465,
    "senderemail": "",
    "sender_password": "",
    "imgdelpath": "",
    "receiveremail": "",
    "showstatusmessage":"False",
    "showjsoninfo":"False"
}
``````
#### *About these key values*
- **img_path**:It selects the relative path of the captured photos (including screen captures and camera captures). It will select the latest 'n' photos (determined by the 'index_mail_view' key below) and send them to your specified email as HTML content with attachments.
- **index_mail_viewimg**:The value of this key determines the number of attachments and preview photos you want to display and include in the email.
- **server**：Your SMTP server address
- **port**：Your SMTP server port.The typical server port is 25,265,994, etc
- **senderemail**:The email address of the sender, which is used by your machine
- **sender_password**:This is an authorization code or account password that you need to use the SMTP key provided by the provider to send emails.
- **imgdelpath**:Here, a directory is specified, and it will delete files in the specified path around midnight every week.
- **receiveremail**:Your email/recipient's email address
- **showstatusmessage**:This option takes a bool value of `True` or `False`. When set to `True`, the terminal where you run the script will display the **device's status information**.
- **showjsoninfo**:This option takes a bool value of `True` or `False`. When set to `True`, the terminal where you run the script will display the **Configuration of JSON**

## Run it
+ Clone the program into your directory using the following command.
``````
git clone https://github.com/in-serinder/linux_machine_email.git
``````
+ Perhaps it also requires you to add executable permissions to the script or program
``````
chmod u+x crms.sh
chmod u+x main 
``````

+ Due to the tools and directory permission involved, you need to run it with root privileges.
``````
sudo ./crms.sh
``````

## The displayed effect
- [Mobile](#mobile-email)
- [PC](#pc-email)
### **Mobile email**
![img1](/img-noim/img1.jpg)
![img1](/img-noim/img2.jpg)
![img1](/img-noim/img3.jpg)
![img1](/img-noim/img4.jpg)

### **PC email**
![img1](/img-noim/img5.jpg)
![img1](/img-noim/img6.jpg)


- [Back to Top](#about-this-programbash-script)
