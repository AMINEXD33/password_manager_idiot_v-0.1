import core
import string
#----- get the list and assci > create a mapdict and a reverce_dict 
#----- this is how idiot encode and decode passwords 
#----- disclaimer : the first line is not gonna work if password does't match the hash

# getting hash from password file

print(string.punctuation)
exit()
hash = ''
with open('password.txt','r') as file:
    hash = file.readline().strip(' ')

print('[!]------> initiating DICTS for encodeing and decoding passwords , plz wait !')
list, assci = core.IDIOT_Hashing.encode_apassword('aminemeftah22144',hash)
mapdict , reverce_dict = core.IDIOT_Hashing.load_hash_table(assci, list)
encoded_password = core.IDIOT_Hashing.encode(mapdict, '123321a@#$@!mine0tothe0amine')
decoded_password = core.IDIOT_Hashing.decode(reverce_dict, encoded_password)
print(list , ascii)

print(f'-------------\n {mapdict}{reverce_dict}')
print(f'encoded : {encoded_password}')
print(f'decoded : {decoded_password}')