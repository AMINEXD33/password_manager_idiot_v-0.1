import os , csv ,sys
import pandas as pd
import hashlib
import getpass
import string
import bcrypt



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
    # check if salt file exits
    def does_salt_file_exists():
        full_path = str(os.getcwd())+'/salt'
        files_in_directory = os.listdir(full_path)
        for x in files_in_directory:
            if x == "salt.txt" :
                return True
        return False
    #check if salt_rec exists
    def does_salt_rec_file_exists():
        full_path = str(os.getcwd())+'/recovery'
        files_in_directory = os.listdir(full_path)
        for x in files_in_directory:
            if x == "salt_rec.txt" :
                return True
        return False

    # copy the password to new recovery/password_rec
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
    # write empty recovery/password_rec and password or write with hash
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
    # copy the salt to salt_rec
    def from_salt_fix_salt_rec():
        data = ''
        with open('salt/salt.txt','r') as file :
            data = file.readline()
        with open('recovery/salt_rec.txt','w') as file:
            file.write(data)
        return True
    # copy the recovery salt to salt
    def from_salt_rec_fix_salt():
        data = ''
        with open('recovery/salt_rec.txt','r') as file :
            data = file.readline()
        with open('salt/salt.txt','w') as file:
            file.write(data)
        return True
    def write_recsalt_and_salt(flag,salt):
        # if flag write hash to files
        if flag :
            with open('recovery/salt_rec.txt','w') as file:
                file.write(str(hash))
            with open('salt/salt.txt','w') as file:
                file.write(str(hash))
            return True
        # if not flag write empty files
        elif not flag :
            with open('recovery/salt_rec.txt','w') as file:
                file.write('')
            with open('salt/salt.txt','w') as file:
                file.write('')
            return True
class IDIOT_CSV_ :
    #get header
    def get_header(opened_file):
        header = next(opened_file)
        return header.split(',')
    # createnew object
    def create_new_object(object_name):

        object_name = object_name+'.csv'
        files_in_database = os.listdir('data_base') # get all files in directory
        if object_name in files_in_database:
            return 12  # dont want it to get mixed up as an error at the __init__file
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
    def update_rowX_with(file , index_row ,values, dict):
        values[0]= IDIOT_Hashing.encode(dict , values[0])
        values[1]= IDIOT_Hashing.encode(dict , values[1])


        try :
            data= pd.read_csv(f"data_base/{file}.csv")
            try :
                data.iloc[int(index_row), [0,1,2,3]] = values
                data.to_csv(f"data_base/{file}.csv", index=False)
            except:
                print('[x] index out of range !')
            return True
        except:
            print('[x] object does not exist !')
    def delete_rowX(file , index_row):
        try :
            data= pd.read_csv(f"data_base/{file}.csv")
            try :
                data = data.drop(int(index_row), axis=0)
                data.to_csv(f"data_base/{file}.csv", index=False)
            except:
                print('[x] index is out of range !')
            return True
        except:
            print('[x] object does not exist !')
    # create a row (username , password , email , and date )
    def create_new_row(file ,values, dict ):
        values[0]= IDIOT_Hashing.encode(dict , values[0])
        values[1]= IDIOT_Hashing.encode(dict , values[1])

        try :
            data= pd.read_csv(f"data_base/{file}.csv")

            # Create values for the new row
            new_row_values = {'username': values[0],'password': values[1],'email': values[2],'date_joined': values[3]}

            # Add the new row to the DataFrame
            data.loc[len(data)] = new_row_values
            data.to_csv(f"data_base/{file}.csv", index=False)
            return True
        except:
            print('[x] object does not exist !')
            return False
    # get all values from csv files
    def get_all_values(reverce_dicr):

        #---------------------------------------------
        output = ""
        files_in_directory = os.listdir('data_base/')
        for x in files_in_directory:
            if 'csv' in x :
                output+= f"_________________{x}___________________\n"

                data = pd.read_csv(f'data_base/{x}')
                for index, row in data.iterrows():
                # Access and modify column values for the current row
                    try:
                        #getting the value of eatch password in eatch row decoded
                        data.loc[index, 'password'] = IDIOT_Hashing.decode(reverce_dicr, data.loc[index, 'password'])
                        data.loc[index, 'username'] = IDIOT_Hashing.decode(reverce_dicr, data.loc[index, 'username'])
                    except:
                        data.loc[index, 'password'] = "(can't decode)"
                        data.loc[index, 'username'] = "(can't decode)"


                output+= data.to_string() + '\n'
        print(output)
    # get all values from a specific csv file
    def get_all_values_from_file(file , reverce_dict):
        output = ''
        try :
            data = pd.read_csv(f'data_base/{file}.csv')
            output+= f'-------------{file}------------\n'
            for index, row in data.iterrows():
            # Access and modify column values for the current row
                try:
                    #getting the value of eatch password in eatch row decoded
                    data.loc[index, 'password'] = IDIOT_Hashing.decode(reverce_dict, data.loc[index, 'password'])
                    data.loc[index, 'username'] = IDIOT_Hashing.decode(reverce_dict, data.loc[index, 'username'])
                except:
                    data.loc[index, 'password'] = "(can't decode)"
                    data.loc[index, 'username'] = "(can't decode)"
        except:
            print('[x]object does not exist')
            return

        output+= data.to_string() + '\n'
        print(output)
    #show all objects
    def get_all_objects():
        try :
            files_in_directory = os.listdir('data_base/')
            for x in files_in_directory:
                if ".csv" in x :
                    print(f'==obj===>{x}'.strip('.csv'))
        except:
            return False
        return True
    # delete an object
    def delete_object(filename):
        try :
            files_in_directory = os.listdir('data_base/')

            for x in files_in_directory:
                if ".csv" in x :
                    if x == filename+'.csv' :
                        os.remove(f'data_base/{x}')

                        return True
            return None
        except:
            return False
    # change the name of an object
    def change_name(filename, new_name):
        files_in_directory = os.listdir('data_base/')
        if filename+'.csv' not in files_in_directory:
            return None
        else:
            try:
                os.rename(f'data_base/{filename}.csv',f'data_base/{new_name}.csv')
                return True
            except:
                return False



class IDIOT_Hashing:
    # make salt
    def make_salt():
        salt = bcrypt.gensalt(16)

        # stor salt
        try:
            with open('salt/salt.txt','w') as file:
                file.write(salt.decode('utf-8'))
            with open('recovery/salt_rec.txt','w') as file:
                file.write(salt.decode('utf-8'))
            return True
        except:
            return False

    # check if hashed password eq to the hash value
    def password_is_valid(password):
        salt = ''
        try :
            with open('salt/salt.txt','r') as file:
                salt = file.readline().strip(' ')
        except:
            print('[x] something went wrong while reading salt value')
        print("[!] checking the password plz wait !")
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8'))
        with open('password.txt','r') as file :
            if hashed_password.decode('utf-8') == file.readline().strip(' '):
                return True
            else:
                return False
    # to create new password
    def create_new_password():
        print("[*] Enter a stong password !")
        inp1 = ''
        # get and make sure the password is what user want
        while True :
            inp1 = getpass.getpass('> ').strip(' ')
            print("Re Enter the password")
            inp2 = getpass.getpass('> ').strip(' ')
            if inp1 == inp2 :
                if len(inp1) <= 10 :
                    #clean and print error message
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
        #get salt
        salt = ''
        try :
            with open('salt/salt.txt','r') as file :
                salt = (file.readline().strip(' ')).encode('utf-8')

        except:
            print('[x] reading salt failed ')
            return False
        # hash password with bcrypt
        print('[!] hashing the password plz wait !')
        hashed = bcrypt.hashpw(inp1.encode('utf-8'), salt)

        # save the hash to the password and password_rec files
        with open(f"recovery/password_rec.txt",'w') as file:
            file.write(hashed.decode('utf-8'))
        with open(f"password.txt",'w') as file:
            file.write(hashed.decode('utf-8'))
        if 'linux' in (sys.platform).lower():
            try :
                os.system('clear')
            except:pass
        elif 'win' in (sys.platform).lower():
            try :
                os.system('cls')
            except:pass
        print(f"""

                Copy this value and store it with root permission so no one has access to it
                in case the password.txt and password_rec.txt got corupted !
                ==============================================================================
                |   [+]HASHED PASSWORD = {hashed.decode('utf8')}
                ==============================================================================

            """)
    # with the password  and hash > create a new hash > get a list of characters of len = 26
    def encode_apassword(password, hash):

        mix = (hash+password).strip(' ')# mix the password and the hash
        hashed = hashlib.sha256() # initiat a sha256
        hashed.update(mix.encode('utf-8')) # update the inctence
        hashed = hashed.hexdigest() # get the hashed result
        punct_lisst = [] #> this will be a variation of string.punctuation
        password_distinct=[]#> this will be a set of distinct password characters
        hash_distinct=[]#> this will be all a variation of [a,b,c,d,e,f]
        other_distinct = []# a variation that depends on the value of the password
        lisst = []


        # loop the lenght of the sha256 == 64 and try to get distinct characters
        # the distict characters are stored in the "hash_distinct" list
        for x in range(64):
            if hashed[x].isalpha():
                if hashed[x] not in password_distinct:
                    if hashed[x] not in hash_distinct:
                        hash_distinct.append(hashed[x])
        # loop the minimum lenght of password and try to get distinct characters
        # the distict characters are stored in the "password_distinct" list
        for x in range(10):
            if password[x].isalpha():
                if password[x] not in password_distinct:
                    if password[x] not in string.digits:
                        if password[x] not in hash_distinct:
                            password_distinct.append(password[x])


        # sum all lists
        len_=len(password_distinct)+len(hash_distinct)+len(punct_lisst)+len(other_distinct)

        # loop through the punctuation list to get what ever is left to complete len = 36
        # were garanted to get the same 25 characters if the password and hash are correct
        # the len of all lists are not enough
        if len_ < 36:
            # for in the unicode-8 table , 128 to 174
            for character in [chr(code_point) for code_point in range(128, 175)]:
                if len_ < 36:
                    if character not in punct_lisst:
                        if character!='*' and character!=',' and character!='"':
                            punct_lisst.append(character)
                            len_+=1
                elif len == 36 : break
                else: pass
            # for in the unicode-8 table , 174 to 191
            for character in [chr(code_point) for code_point in range(174, 192)]:
                if len_ < 36 :
                    if character not in password_distinct:
                        if character not in hash_distinct and character.isalpha():
                            other_distinct.append(character)
                elif len == 36 : break

        # generate the final list
        for x  in [password_distinct, hash_distinct, punct_lisst,other_distinct]:
            for xx in x:
                lisst.append(xx)
        return lisst , string.ascii_lowercase

    # load DICT , that maps every letter to its encoded value
    def load_hash_table(assci_list , encoding_lisst):
        map_dict = {}
        reverce_dict = {}
        # |0_0|
        # generating a dict {'a':'x', 'b':'x',.....,'z':'x'}
        for x in range(len(assci_list)) :
            map_dict[assci_list[x]] = encoding_lisst[x].strip(' ')
        # adding {'0':'x', '1':'x', '2':'x ,.....,'9':'x'}
        for x in range(10):
            map_dict[string.digits[x]] = encoding_lisst[26+x]
        # revercing the map_dict {'x':'a','x':'b',.......,'x':'z'}
        for x in range(len(assci_list)) :
            reverce_dict[encoding_lisst[x].strip(' ')] = assci_list[x]
        # adding the digits also to the reverse dictionary
        for x in range(10):
            reverce_dict[encoding_lisst[x+26]] = string.digits[x]
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
                    encoded_value+=f'{DICT[x.lower()]}'
            else:
                encoded_value+=DICT[x] # using numbers in this case will be a bad idea
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
                decoded_value += REVERCE_DICT[encoded_password[tracker]].upper()



            else:
                if  encoded_password[tracker].isnumeric():
                    decoded_value+= REVERCE_DICT[tracker]
                else:
                    decoded_value+= REVERCE_DICT[encoded_password[tracker]]

        return decoded_value

#input
class IDIOT_Input:
    def __init__(self, input_):
        self.input_ = input_
    # clean the input out / and
    def clean_input(self):
        self.input_ = self.input_.lstrip().rstrip().split()
        return self.input_



