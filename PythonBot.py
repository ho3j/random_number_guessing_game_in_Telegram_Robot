"""
Hossein Jalili
feb-15-2022
version 1.0.0
Implement a random_number_guessing_game in Telegram Robot with Python

"""
from gettext import textdomain
import json                                 # importing the JSON library
from urllib.request import urlopen          # importing the urlopen attribute from the request method in urllib library
from urllib.parse import quote, unquote     # importing the quote/unquote attributes from the parse method in urllib library
# import time                                 # importing the time library
# import os
import random
from colorama import Fore
from datetime import datetime


# clear=lambda : os.system("cls")


####################### Functions #######################
def aux_dec2utf8(resp):                     # a function for decoding HTML content to utf-8 format
    decoded = ''
    for line in resp:
        decoded += line.decode('utf-8')
    return decoded
#----------------------------------

def choice_n():
    global n
    n = random.randrange(0,10)
    # print("goal is :",n)

def write_operation(x):
    file_name = "save_time_login.txt"
    file = open( file_name, "a+" )
    file.write(x+"\n")
    file.close()


    

######################### START #########################
TOKEN = '5149849190:AAFsEAN8evbyXbCquzLj5mAUVqFCNXXXBts'

# TOKEN = input(" Enter Your token bot :") 
      # define the access token
URL   = 'https://api.telegram.org/bot{}/'.format(TOKEN)       # Telegram bot API url + TOKEN

cmd   = 'getme'                                               # Auxiliary variable for defining commands


resp  = urlopen(URL + cmd)                                     # reading the url
line  = aux_dec2utf8(resp)                                     # converting the content to utf-8
gtm   = json.loads(line)                                       # converting the content to JSON


# clear()
choice_n()
status = True                                                  # define a status variable for the while loop
while status:                                                  # interring the while loop
 
    cmd = 'getUpdates'                                         # Auxiliary variable for defining commands

    resp = urlopen(URL + cmd)                                  # reading the url to get the current updates
    line = aux_dec2utf8(resp)                                  # converting the content to utf-8
    upds = json.loads(line)                                    # converting the content to JSON
    try:
        s1=upds["result"][0]['message']['from']
        inf0=("===========================")
        inf1=("update_id : \t"+str(upds["result"][0]['update_id']))
        inf2=("text : \t\t"+str(upds["result"][0]['message']["text"]))
        inf3=("date : \t\t"+str(upds["result"][0]['message']["date"]))
        inf4=("message_id : \t"+str(upds["result"][0]['message']['message_id']))
        inf5=("id : \t\t"+str(s1['id']))
        inf6=("is_bot : \t"+str(s1['is_bot']))
        inf7=("first_name : \t"+str(s1['first_name']))
        inf8=("username : \t"+str(s1['username']))
        inf9=("language_code : " +str(s1["language_code"]))
        inf10=("--------------------")
        #print("\n\n\n\n")
        # print(s1)

        # print(inf0)
        # print(inf1)
        # print(inf2)
        # print(inf3)
        # print(inf4)
        # print(inf5)
        # print(inf6)
        # print(inf7)
        # print(inf8)
        # print(inf9)
        # print(inf10)

        write_operation("\n"+str(inf0)+"\n"+str(inf1)+"\n"+str(inf2)+"\n"+str(inf3)+"\n"+str(inf4)+"\n"+str(inf5)+"\n"+str(inf6)+"\n"+str(inf7)+"\n"+str(inf8)+"\n"+str(inf9)+"\n"+str(inf10))
        

    except:
        pass

    NoM  = len(upds['result'])                                 # Number of New Messages Received

    if NoM != 0:                                               # if updates are available

        msg  = upds['result'][0]['message']                    # make the current message ready for processing
        chid = str(msg['chat']['id'])                          # read the chat id

        if 'text' in msg:
            txt  = quote(msg['text'].encode('utf-8'))  
            # txt= msg['text'] 
            

            # print("number input : ",txt)
            write_operation("number input : "+str(txt))
            # list_bot.append(msg['text'])          # encoding the text to utf-8 then quoting it to url
            # print(msg['text'])

            if txt.isalpha() or not txt.isdigit(): 
                # print(n)
                # print('string_input')
                write_operation("string_input\n")
                # print("goal is :",n)
                write_operation("goal is : "+str(n)+"\n")
                txt='enter_english_number'
                cmd  = 'sendMessage'                                  
                resp = urlopen(URL + cmd +f'?chat_id={chid}&text={txt}')        
                line = aux_dec2utf8(resp)                              
                chck = json.loads(line) 
                
            if txt.isdigit() and int(txt) > n :
                # print("goal is :",n)
                write_operation("goal is : "+str(n))
                # print('goal_is_smaller')
                write_operation("goal_is_smaller\n")
                txt='goal_is_smaller'
                cmd  = 'sendMessage'                                  
                resp = urlopen(URL + cmd +f'?chat_id={chid}&text={txt}')        
                line = aux_dec2utf8(resp)                              
                chck = json.loads(line)  
            elif txt.isdigit() and int(txt) < n :
                # print(n)
                # print("goal is :",n)
                write_operation("goal is : "+str(n))
                # print('goal_is_bigger')
                write_operation("goal_is_bigger\n")
                txt='goal_is_bigger'
                cmd  = 'sendMessage'                                  
                resp = urlopen(URL + cmd +f'?chat_id={chid}&text={txt}')        
                line = aux_dec2utf8(resp)                              
                chck = json.loads(line) 
            if txt.isdigit() and int(txt) == n :
                # print(n)
                # print("goal is :",n)
                write_operation("goal is : "+str(n))
                # print('correct')
                write_operation("correct")
                txt='correct'
                cmd  = 'sendMessage'                                  
                resp = urlopen(URL + cmd +f'?chat_id={chid}&text={txt}')        
                line = aux_dec2utf8(resp)                              
                chck = json.loads(line)

                choice_n()
                # print("new goal is :",n)
                write_operation("new goal is : "+str(n))
                txt='new_goal'
                resp = urlopen(URL + cmd +f'?chat_id={chid}&text={txt}')        
                line = aux_dec2utf8(resp)                              
                chck = json.loads(line)                 

            # print("===========================")
            write_operation("===========================\n")
            if chck['ok']:                                         # If sending was successfull

                uid = upds['result'][0]['update_id']               # Read the update id
                cmd = 'getUpdates'                                 # Auxilary variable for defining commands
                urlopen(URL + cmd + '?offset={}'.format(uid + 1))  # Giving the offset Telegram forgets all those messages before this update id

            # if txt == "exit"  :
            #     break
        
        else:
            uid = upds['result'][0]['update_id']                   # Read the update id
            cmd = 'getUpdates'                                     # Auxilary variable for defining commands
            urlopen(URL + cmd + '?offset={}'.format(uid + 1))      # Giving the offset Telegram forgets all those messages before this update id
    # print('.')
    # time.sleep(2)
