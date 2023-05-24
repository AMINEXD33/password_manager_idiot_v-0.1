import os, sys, time
import core
import datetime
import getpass


if __name__ == "__main__":
    # this function checks if files are all in place , and fixthem if they are missing 
    def start_protocol():
        # check if conf file exists 
        test1 = core.CHECK_FILES.does_hash_file_exists()
        # check if the password_rec exists 
        test2 = core.CHECK_FILES.does_passw_rec_exists()
        flag = None
        
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
        # everything is fine , exit 
        # addend counte>=10 just to for apperence :)
        if test1 ==True and test2 == True :
            flag = True
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
                    break
                elif choice == '2':
                    core.CHECK_FILES.write_recpass_and_password(True,input('?hash >'))
                    print('[!] DONE ! ')
                    break
                else:
                    print('[x] invalid choice, try again')
        if flag :
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
    def who_are_you():
        print('[?] Plz Enter that password !')
        password = getpass.getpass("[PASSWORD]")
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
                who_are_you()
            elif choice == '2':
                fixed = core.CHECK_FILES.from_pass_rec_fix_passowd()
                if fixed == True :
                    print('[+] hash recovered !')
                    who_are_you()
            else:
                sys.exit()
        if flag == True :
            print('[+] Password is valid')
            return True
    # all commands logic 
    def main_prog():
        while True :
            command = core.IDIOT_Input(input('[IDIOT] >'))
            command = command.clean_input()
            if command[0] == 'help': help_panel()
            elif command[0] == 'show':### decode passwords
                if len(command) == 1 :
                    core.IDIOT_CSV_.get_all_values()
                elif len(command) == 2:
                    core.IDIOT_CSV_.get_all_values_from_file(command[1])
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
                pass
    
    #----------------------------------------------------------------

    #this flag will indecate if the hash and password are valid 
    flag = None
    # checking if first time runing or not 
    readconfig = None
    with open('config.txt','r') as file:
        txt = file.readline()
        if txt == 'False':
            readconfig = False
        elif txt == 'True':
            readconfig = True
    # check files 
    start_protocol()

    #create new password (hash) 
    if readconfig == True :
        print('[+] first time running , lets create a new password !')
        core.IDIOT_Hashing.create_new_password()
        # change the config value 
        with open('config.txt','w') as file:file.write('False')
        
        del readconfig
        # authenticate user
        flag = who_are_you()
    # trying to authenticate user
    else:
        flag = who_are_you()
    
    if flag == True :
        time.sleep(1)
        main_prog()
    


