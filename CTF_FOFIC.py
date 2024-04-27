#----------------[SHEBANG AND ENCODING]----------------#
#!/usr/bin/python3
# -*- coding: utf-8 -*-
#------------------------------------------------------#

#-*-*-*-*-*-*-*-*-*-*-*-*-
# Author   : r4im4nn     #
# Date     : 04/2024     #
# Version  : 1.0         #
# OS 	   : Linux       #
# Language : Python 3    #
#-*-*-*-*-*-*-*-*-*-*-*-*-

#----------------------[MODULES]---------------------#
import os,subprocess,string,sys
import netifaces as ni
#------------------------------------------------------#

#-----------[FOLDER/FILE CREATION FUNCTION]------------#
def createFoldersFile(ROOM_NAME:str):
    
    INTERFACE:str = "tun0"

    try:
        IP:str = ni.ifaddresses(INTERFACE)[ni.AF_INET][0]['addr'] # We get the VPN IP (tun0)
    except ValueError:
        print("[!] You must specify a valid interface name or you forgot to activate your OPENVPN !")
        IP = '0.0.0.0'
    
    os.system("mkdir '{0}'".format(ROOM_NAME)) # Folder creation.
    DATE:str = subprocess.Popen('date "+%D | %H:%M"', shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip() # We get the date
        
        # Banner set-up 
    BANNER:str = ("""-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
● DATE : {0}
● ROOM : {1}
● VPN  : {2}
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n""".format(DATE, ROOM_NAME, IP))
    
    # Notes set-up
    NOTE_AREA = """
[ INFO ] - TARGET
	-> IP     : 
	-> DOMAIN :  
    
............................
[ PHASE 1 ] - RECONNAISSANCE
............................

	-> 	
 	
	-> 
			    
	-> FINDINGS | 
		    
    [ ! ] Now that we've got enough information, we can start the exploitation.
		    
..........................
[ PHASE 2 ] - EXPLOITATION
..........................

	-> 

	-> 
		
	-> 	
	         
	[ ! ] We got our initial acces, it's time to elevate privileges

.....................................	
[ PHASE 3 ] - TOTAL CONTROL & EVASION
.....................................

	-> 

	-> 
		
	-> 
.....................................

[ ★ ] - CREDENTIALS
	-> 
	-> 

[ ★ ] - FLAGS
	-> USER : 
    -> ROOT :"""

	# File creation
    with open("{0}/notes_{0}.txt".format(ROOM_NAME),"w") as noteTakingFile: 
        noteTakingFile.write(BANNER)
        noteTakingFile.write(NOTE_AREA)

#----------------------[BANNER]------------------------#


POST = """
 __  ___  ___      ___  __   ___    __  
/  `  |  |__      |__  /  \ |__  | /  ` 
\__,  |  |    ___ |    \__/ |    | \__,                                                                                              
           BY R4IM4NN | V.1.0                                                                                                                                                                                                           """
#------------------------------------------------------#

#----------------------[MAIN]--------------------------#
if __name__ == '__main__':
    try:
        print(POST)
        
        ROOM_NAME:str = input("Enter the ROOM name : ")
        
        # Check if input is blank
        while (ROOM_NAME == ""):
            print("[!] Error : YOU MUST ENTER A NAME !")
            ROOM_NAME:str = input("Enter the CTF's lab name : ")

        ROOM_NAME_WITHOUTSPACES = ROOM_NAME.replace(" ", "_") # Replace spaces by underscores

        # Check if the folder exists
        if os.path.isdir(ROOM_NAME_WITHOUTSPACES):
        	print("[!] This folder already exists")
           
        else:          
            createFoldersFile(ROOM_NAME_WITHOUTSPACES)
            print("[!] Your folder | {0} | is created !".format(ROOM_NAME_WITHOUTSPACES))
    
    except KeyboardInterrupt:
        print("\nEXIT")
    except FileNotFoundError:
        print("[!] You can't use these special characters !")
        sys.exit()
#-----------------------------------------------------#  
