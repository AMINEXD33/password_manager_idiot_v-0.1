import os , csv ,sys
import pandas as pd
import hashlib
import getpass
import string

class CHECK_FILES():
    # check if hash file exists 
    def does_hash_file_exists():
        full_path = str(os.getcwd())
        files_in_directory = os.listdir(full_path)
        for x in files_in_directory:
            if x == "password.txt":
                return True
        return False
    # check if recovery file exists
    def does_passw_rec_exists():
        full_path = str(os.getcwd())+'/recovery'
        files_in_directory = os.listdir(full_path)
        for x in files_in_directory:
            if x == "password_rec.txt" :
                return True 
        return False   
    # copy the config to new recovery/password_rec
    def from_password_fix_pass_rec():
        data = ''
        with open('password.txt','r') as file :
            data = file.readline()
        with open('recovery/password_rec.txt','w') as file:
            file.write(data)
        return True     
    # copy the recovery from recovery/password_rec
    def from_pass_rec_fix_passowd():
        data = ''
        with open('recovery/password_rec.txt','r') as file :
            data = file.readline()
        with open('password.txt','w') as file:
            file.write(data)
        return True  
    # write empty recovery/password_rec and config or write with hash 
    def write_recpass_and_password(flag,hash):
        # if flag write hash to files 
        if flag :
            with open('recovery/password_rec.txt','w') as file:
                file.write(str(hash))
            with open('password.txt','w') as file:
                file.write(str(hash))
            return True 
        # if not flag write empty files 
        elif not flag :
            with open('recovery/password_rec.txt','w') as file:
                file.write('')
            with open('password.txt','w') as file:
                file.write('')
            return True 
            
class IDIOT_CSV_ :
    #get header 
    def get_header(opened_file):
        header = next(opened_file)
        return header.split(',')
    # createnew object 
    def create_new_object():
        print('+ enter the object name')
        object_name = input('> ')
        object_name = object_name+'.csv'
        files_in_database = os.listdir('data_base') # get all files in directory 
        if object_name in files_in_database:
            print('+ object already exists')
            return False
        else : pass
        ### creating the new object ####
        try :
            with open(f'data_base/{object_name}', 'w', newline="") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(['username','password','email','date_joined'])
        except:
            return False
        return True
    def get_from_headerX_value_eq_to( file ,header, value):
        try :
            data= pd.read_csv(f"data_base/{file}")
            #print(data)
            found = data[data[header] == value]
            return found.index[0] 
        except:
            return False  
    def update_rowX_with(file , index_row, columns_indexs,value):
        try :
            data= pd.read_csv(f"data_base/{file}")
            data.iloc[index_row, columns_indexs ] = value
            data.to_csv(f"data_base/{file}", index=False)
            
            return True
        except:
            return False
    def delete_rowX(file , index_row):
        try :
            data= pd.read_csv(f"data_base/{file}")
            data = data.drop(index_row, axis=0)
            data.to_csv(f"data_base/{file}", index=False)
            
            return True
        except:
            return False
    def create_new_row(file ,values):
        try :
            data= pd.read_csv(f"data_base/{file}")
            # Create values for the new row
            new_row_values = {'username': values[0],'password': values[1],'email': values[2],'date_joined': values[3]}

            # Add the new row to the DataFrame
            data.loc[len(data)] = new_row_values
            data.to_csv(f"data_base/{file}", index=False)
            return True
        except:
            return False
    # get all values from csv files
    def get_all_values():
        output = ""
        files_in_directory = os.listdir('data_base/')
        for x in files_in_directory:
            if 'csv' in x :
                output+= f"_________________{x}___________________\n"
                data = pd.read_csv(f'data_base/{x}')
                output+= data.to_string() + '\n'
        print(output)
    # get all values from a specific csv file
    def get_all_values_from_file(file):
        output = ""
        try :
            data = pd.read_csv(f'data_base/{file}.csv')
            output+= data.to_string() + '\n'
            print(output)
        except:
            print('[x] object does not exist !')
        



#IDIOT_CSV_.get_all_values()
IDIOT_CSV_.get_all_values_from_file('youtube')
class IDIOT_Hashing:
    # check if hashed password eq to the hash value
    def password_is_valid(password):
        hashed_password = hashlib.sha256()
        hashed_password.update(password.encode('utf-8'))
        hashed_password = hashed_password.hexdigest()
        print(hashed_password)
        with open('password.txt','r') as file :
            if hashed_password == file.readline().strip(' '):
                return True 
            else: 
                return False
    # to create new password
    def create_new_password():
        print("[*] Enter a stong password !")
        inp1 = ''
        while True :
            inp1 = getpass.getpass('> ')
            print("Re Enter the password")
            inp2 = getpass.getpass('> ')
            if inp1 == inp2 :
                if len(inp1) <= 10 : 
                    if 'linux' in (sys.platform).lower(): 
                        try : 
                            os.system('clear')
                        except:pass
                    elif 'win' in (sys.platform).lower():
                        try :
                            os.system('cls')
                        except:pass    
                    print('[*] enter a longer password')
                else:
                    break
            else:
                print('[*] Passwords do not match , re enter the password')
        m = hashlib.sha256()
        m.update(inp1.encode('utf-8'))
        hashed = m.hexdigest()
        with open(f"recovery/password_rec.txt",'w') as file:
            file.write(hashed)
        with open(f"password.txt",'w') as file:
            file.write(hashed)
        if 'linux' in (sys.platform).lower(): 
            try : 
                os.system('clear')
            except:pass
        elif 'win' in (sys.platform).lower():
            try :
                os.system('cls')
            except:pass 
        print(f"""
        
                PLZ COPY THIS HASHED PASSWORD AND STOR IT IN A PLACE OF YOUR CHOICE ,
                IF YOU LOSE THIS HASH , AND SOMEHOW THE FILES (password.txt , password_rec.txt) GOT CORUPTED IDIOT CAN'T DECODE THE  PASSWORDS ANYMORE !
                ==============================================================================    
                |   [+]HASHED PASSWORD = {hashed}  |
                ==============================================================================
            """)
    # with the password and hash > create a new hash  and from that hash > get a list of characters of len = 26 
    def encode_apassword(user_password, hash):
        
        Flag = IDIOT_Hashing.password_is_valid(user_password)
        if Flag :
            mix = hash+user_password
            hashed = hashlib.sha256()
            hashed.update(mix.encode('utf-8'))
            hashed = hashed.hexdigest()
            lisst = []
            # loop two times to try and get distinct 16 character from hash and 10 from password
            for loop in range(2):
                if loop == 0 :
                    for x in range(16):
                        flag = True
                        for y in lisst:
                            if hashed[x] == y :
                                flag= False
                            else:pass
                        if flag :
                            lisst.append(hashed[x])
                        else: flag = True
                if loop == 1 :
                    for x in range(10):
                        flag = True 
                        for y in lisst:
                            if user_password[x] == y:
                                flag = False
                            else:pass
                        if flag:
                            lisst.append(user_password[x])
            
            
            # if the len of the lisst is not 25 yet #
            len_=len(lisst)
            punctuation_list = string.punctuation
            
            # loop through the punctuation list to get what ever is left to complete len = 26 
            # were garanted to get the same 25 characters if the password and hash are correct 
            if len_ != 26:
                for x in punctuation_list:
                    flag = True
                    if len_ == 26 : break
                    for y in lisst :
                        if x == y:
                            flag = False
                        else:pass
                    if flag :
                        if x == '*':pass # saving this special character for future use (*x*)= X  
                        else:
                            lisst.append(x)
                            len_+=1
                    else: flag = True
            ascci_list = []
            
            for x in string.ascii_lowercase:
                ascci_list.append(x)   
            return lisst , ascci_list
        else: 
            # wrong password 
            return False
    # load DICT , that maps every letter to its encoded value
    def load_hash_table(assci_list , encoding_lisst):
        map_dict = {}
        reverce_dict = {}
        # |0_0|
        for x in range(len(asscilist)) :
            map_dict[asscilist[x]] = encoding_lisst[x]
        for x in range(len(asscilist)) :
            reverce_dict[encoding_lisst[x]] = asscilist[x]
        return map_dict , reverce_dict
    # encode the password with the DICT 
    # note we're talking about the password that will be stored in the csv files 
    def encode(DICT, password):
        encoded_value = ""
        for x in password:
            if x.isalpha():# if its alphanumeric then 
                if x.isupper():# if it's upper add special characters to identify the uppercase from lowwer case characters
                    encoded_value+=f'*{DICT[x.lower()]}'
                else:
                    encoded_value+=f'{DICT[x.upper()]}'
            else:
                encoded_value+=x # using numbers in this case will be a bad idea 
        return encoded_value     
    # decode a password by using the reverce dict and the encoded_password
    def decode(REVERCE_DICT, encoded_password):
        decoded_value = ""
        tracker = -1
        while True :
            tracker+=1
            if tracker == len(encoded_password):
                break
            if encoded_password[tracker] == '*':
                tracker+=1
                decoded_value += REVERCE_DICT[encoded_password[tracker]]

            
            
            else:
                decoded_value+= REVERCE_DICT[encoded_password[tracker]]
                
        return decoded_value    



