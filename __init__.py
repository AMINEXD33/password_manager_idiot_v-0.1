import time , os, sys
import threading
import core



if __name__ == "__main__":
    def start_protocol():
        # check if conf file exists 
        test1 = core.CHECK_FILES.does_hash_file_exists()
        # check if the password_rec exists 
        test2 = core.CHECK_FILES.does_passw_rec_exists()
        flag = None
        
        # checking if files exists 
        if 'linux' in (sys.platform).lower(): 
            try : 
                os.system('clear')
            except:pass
        elif 'win' in (sys.platform).lower():
            try :
                os.system('cls')
            except:pass  
        print('IDIOT \n V-0.1')
        
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
    
    def main_prog():
        help_panel()
    
    
    
    
    
    
    
    
    
    
    main_prog()
    #clear = start_protocol()
    

