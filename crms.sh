while true;do
    source_dir="/mountusb/crm/save" #Prepare the source folder for storing images

    #Here, a photo with a resolution of 1280x720 will be generated. You can modify it and generate its name through the date command
    #This is the file captured by the camera
    fswebcam -r 1280x720 -d /dev/video0 $source_dir/image-"$(date +"%a %b %e %T %Z %Y")".jpg
    sleep 3 #The interval time between each camera capture
    fswebcam -r 1280x720 -d /dev/video0 $source_dir/image-"$(date +"%a %b %e %T %Z %Y")".jpg
    sleep 3
    fswebcam -r 1280x720 -d /dev/video0 $source_dir/image-"$(date +"%a %b %e %T %Z %Y")".jpg
    sleep 2
    #Captured a screenshot of the desktop. To enable this capture, the bash must run the script in a desktop environment such as X window.
    #Its selection priority is 3, and you can discard it by commenting the code with "#"
    scrot $source_dir/image-DeskTopshort"$(date +"%a %b %e %T %Z %Y")".jpg

    ./main  #Starting from here, execute the Python program
    sleep 1800      #Delay execution time (or timer interval)
done