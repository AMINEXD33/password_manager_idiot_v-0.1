import os, sys, time
import core
import datetime
import getpass
import string

if __name__ == "__main__":
    #----- vars 
    dict_,reverce_dict_ = None,None
    password = ''
    #-------
    #set up the files in first run 
    def setup_ ():
        print ("Setting up files") 
        #create the directories
        flag = True
        for x in ['password.txt','salt/salt.txt','recovery/salt_rec.txt','recovery/password_rec.txt']:
            try :
                
                file = open(x,'w')
                file.close()
                print(f'[+] {x} file has been created !')
                
            except:
                
                print(f'[x] error creating {x}')
                flag = False
        return flag
    #getting the dicts ready
    def initiate_dicts(password):
        # getting hash from password file
        hash = ''
        with open('password.txt','r') as file:
            hash = file.readline().strip(' ')
        
        print('[!]------> initiating DICTS for encodeing and decoding passwords , plz wait !')
        list, assci = core.IDIOT_Hashing.encode_apassword(password,hash)
        dict_ , reverce_dict_ = core.IDIOT_Hashing.load_hash_table(assci, list)
        return dict_ , reverce_dict_
    # this function checks if files are all in place , and fixthem if they are missing 
    def start_protocol():
        # check if password file exists 
        test1 = core.CHECK_FILES.does_hash_file_exists()
        # check if the password_rec exists 
        test2 = core.CHECK_FILES.does_passw_rec_exists()
        #check if the salt file exists
        test3 = core.CHECK_FILES.does_salt_file_exists()
        #check if the salt_rec exists 
        test4 = core.CHECK_FILES.does_salt_rec_file_exists()
        flag = None
        flag2 = None
        # clear terminal
        if 'linux' in (sys.platform).lower(): 
            try : 
                os.system('clear')
            except:pass
        elif 'win' in (sys.platform).lower():
            try :
                os.system('cls')
            except:pass  
        print('IDIOT \n V-0.1')
        # show progress 
        if test1 : 
            print('[+] password file found ✓')
        elif test1 == False:
            print('[-] password file does not exist X')
            
        if test2 :
            print('[+] password_rec file found ✓')
        elif test2 == False:
            print('[-] password_rec file does not exist X')

        if test3 :
            print('[+] salt file found ✓')
        elif test3 == False:
            print('[-] salt file does not exist X')
        
        if test4 :
            print('[+] salt_rec file found ✓')
        elif test4 == False:
            print('[-] salt_rec file does not exist X')
        
        if test1 ==True and test2 == True and test3 == True and test4 == True:
            flag = True
        #----------password files 
        #if password exists, but password_rec is missing 
        elif test1 == True and test2 == False :
            print('[?] password_rec file does not exist , would you like to copy it from password [yes/no] ?')
            choice = input('> ')
            if 'yes' in choice.lower():
                if core.CHECK_FILES.from_password_fix_pass_rec():
                    print('[!] password_rec has been copied from password ✓')
                    flag = True 
                else: 
                    print('[x] something went wrong !')
                    flag=False
        # if password is missing , but password_rec exists
        elif test1== False and test2 == True:
            print('[?] password file does not exist, would you like to copy it from password_rec [yes/no]?')
            choice = input('> ')
            if 'yes' in choice.lower():
                if core.CHECK_FILES.from_pass_rec_fix_passowd():
                    print('[!] password file has been copied from password_rec ✓')
                    flag = True 
                else: 
                    print('[x] something went wrong!')
                    flag=False
        # if non exist , PANIC ! XD
        elif test1 == False and test2 == False:
            print("""
            [x] password and password_rec files are missing
            [?] would you like to write (password and password_rec) as empty files [1]
            [?] input the hash , then write both files [2]
            """)
        
            while True :
                choice = input('>')
                if choice == '1':
                    core.CHECK_FILES.write_recpass_and_password(False,0)
                    print('[!] DONE ! ')
                    flag = True 
                    break
                elif choice == '2':
                    core.CHECK_FILES.write_recpass_and_password(True,input('?hash >'))
                    print('[!] DONE ! ')
                    flag = True 
                    break
                else:
                    print('[x] invalid choice, try again')
        
        #----------salt files
        #if salt exists , but salt_rec is missing
        if test3 == True and test4 == False:
            print('[?] salt_rec file does not exist, would you like to copy it from salt [yes/no]?')
            choice = input('> ')
            if 'yes' in choice.lower():
                if core.CHECK_FILES.from_salt_fix_salt_rec():
                    print('[!] salt_rec has been copied from salt ✓')
                    flag2 = True
                else: 
                    print('[x] something went wrong !')
                    flag2 = False
        #if salt_rec exists, but salt is missing
        elif test3 == False and test4 == True:
            print('[?] salt file does not exist, would you like to copy it from salt_rec [yes/no]?')
            choice = input('> ')
            if 'yes' in choice.lower():
                if core.CHECK_FILES.from_salt_rec_fix_salt():
                    print('[!] salt_rec has been copied from salt ✓')
                    flag2 = True 
                else: 
                    print('[x] something went wrong !')
                    flag2=False
        # if non exist , PNIC ! XD
        elif test3 == False and test4 == False:
            print("""
            [x] salt and salt_rec files are missing
            [?] would you like to write (salt and salt_rec) as empty files [1]
            [?] input the salt value , then write both files [2]
            """)
        
            while True :
                choice = input('>')
                if choice == '1':
                    core.CHECK_FILES.write_recsalt_and_salt(False,0)
                    print('[!] DONE ! ')
                    flag2 = True
                    break
                elif choice == '2':
                    core.CHECK_FILES.write_recsalt_and_salt(True,input('?hash >'))
                    print('[!] DONE ! ')
                    flag2 = False
                    break
                else:
                    print('[x] invalid choice, try again')
        if flag and flag2  :
            return True
        else:
            return False
    # just help panel for users (manual)
    def help_panel():
        if 'linux' in (sys.platform).lower(): 
            try : 
                os.system('clear')
            except:pass
        elif 'win' in (sys.platform).lower():
            try :
                os.system('cls')
            except:pass    
        print("""
            MANUAL****************************************************************
            |
            --- show all values in all objects --->>>>      > showv
            |
            --- show all values in an object --->>>      > showv object_name
            |
            --- create new object --->>>     > createob object_name
            |
            --- show all objects --->>>     > showob
            |
            --- delete an object --->>>     > deleteob object_name
            |
            --- rename an object --->>>     > renameob object_name new_name
            |
            --- add values (username, password, email) to an object --->>>     > addv object_name username password email
            |
            --- delete a row from an object --->>>     > deleter object_name INDEX
            |
            --- update values of an object --->>>     > updatev object_name username password email INDEX
                |
                |
                -------> too keep old values write same , example >> updatev facebook doom whoisthisghuy same 12
            
        """)
    # this function will take care of authanticating the user , and help if the hash is wrong or missing
    def who_are_you(password):
        
        flag = core.IDIOT_Hashing.password_is_valid(password)
        if flag == False:
            print('[x] wrong password or hash is corrupted !')
            print("""
                ----------------------------------------------------
                    [!] reenter a valid password [1]
                    [!] recover hash from password_recovery [2]
                    [!] exit [anything]
                ----------------------------------------------------
            """)
            choice = input('> ')
            if choice == '1':
                print('[?] Plz Enter your password !')
                password = getpass.getpass("[PASSWORD]")
                
                return who_are_you(password)
            elif choice == '2':
                fixed = core.CHECK_FILES.from_pass_rec_fix_passowd()
                if fixed == True :
                    print('[+] hash recovered !')
                    print('[?] Plz Enter your password !')
                    password = getpass.getpass("[PASSWORD]")
                    return who_are_you(password)
            else:
                sys.exit()
        if flag == True :
            print('[+] Password is valid')
            return True
    # all commands logic 
    def main_prog():
        while True :
            sys.tracebacklimit = 0
            command = core.IDIOT_Input(input('[IDIOT] >'))
            command = command.clean_input()
            
            if command[0] == 'help': help_panel()
            elif command[0] == 'showv':
                if len(command) == 1 :
                    core.IDIOT_CSV_.get_all_values(reverce_dict_)
                elif len(command) == 2:
                    core.IDIOT_CSV_.get_all_values_from_file(command[1],reverce_dict_)
                else:
                    print('[x] huh? \n[!]type help to get manual ')
            elif command[0] == 'createob':
                if len(command) == 2:
                    flag = core.IDIOT_CSV_.create_new_object(command[1])
                    if flag == True:
                        print(f'[+] object {command[1]} has been created successfully !')
                    elif flag == 12 :
                        print('[!] object already exists !')
                    elif flag == False:
                        print('[x] error     see core function (create_new_object)')
                else: 
                    print('[x] huh? \n[!]type help to create')
            elif command[0] == 'showob':
                if len(command) == 1 :
                    flag = core.IDIOT_CSV_.get_all_objects()
                    if flag == False:
                        print('[x] something is wrong with the data_base folder')
                elif len(command) == 2:
                    print("[x] huh? \n[!]type help to get manual ")
            elif command[0] == 'deleteob':
                if len(command) == 2:
                    flag = core.IDIOT_CSV_.delete_object(command[1])
                    if flag == True:
                        print(f'[+] object {command[1]} has been deleted successfully !')
                    elif flag == None :
                        print('[x] object does not exist in data_base ')
                    else:
                        print('[x] error at the function (delete_object)')    
            elif command[0] == 'renameob':
                if len(command) == 3:
                    flag = core.IDIOT_CSV_.change_name(command[1], command[2])
                    if flag == True:
                        print(f'[+] object {command[1]} has been renamed to {command[2]} successfully!')
                    elif flag==None:
                        print('[x] object does not exist in data_base')
                    elif flag == False:
                        print('[x] error in the function (change_name')
            elif command[0] == 'addv':
                
                if len(command) == 5:
                    
                    print(command)
                    try:
                        core.IDIOT_CSV_.create_new_row(command[1],[command[2],command[3],command[4],datetime.date.today().strftime("%d/%m/%Y")],dict_)
                    except:
                        print("[!] plz dont use special characters , reserved for encoding and decoding your passwords !")
                else :
                    print('[x] huh? \n[!]type help to get manual ')
    #----------------------------------------------------------------

    #this flag will indecate if the hash and password are valid 
    flag = None
    # checking if first time runing or not 
    readconfig = None
    with open('config.txt','r') as file:
        txt = file.readline().strip(' ')
        if 'False' in txt:
            readconfig = False
        elif 'True' in txt:
            readconfig = True
        else:
            readconfig = False
    #setup_ = None
    setup_done = None
    if readconfig == True:
       setup_done= setup_()
       time.sleep(5)
    #else:pass
    
    # check files 
    start_protocol()
    
    
    
    #create new password (hash) 
    if readconfig == True :
        
        if setup_done :#setup_ and protocol:
            
            print("[+] saving a random salt !")
            core.IDIOT_Hashing.make_salt()
            print('[+] first time running , lets create a new password !')
            core.IDIOT_Hashing.create_new_password()
            # change the config value 
            with open('config.txt','w') as file:file.write('False')
            
            del readconfig
            # authenticate user
            print('[?] Plz Enter your password !')
            password = getpass.getpass("[PASSWORD]")
            flag = who_are_you(password)
        else:
            print('[error] while setting up EXITING !')
            sys.exit()
            
    # trying to authenticate user
    else:
        # check files 
        print('[?] Plz Enter your password !')
        password = getpass.getpass("[PASSWORD]")
        flag = who_are_you(password)
    
    if flag == True :
        time.sleep(1)
        # initiate dicts if user is authenticated 
        dict_,reverce_dict_ = initiate_dicts(password)
        main_prog()
    


