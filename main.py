import string
import random

password = str(input('Password to encrypt: '))

# Create list of each char in password.
ind_password = [i for i in password]

ind_password = list(ind_password)

# Create list of every character. Other than spaces.
chr_list = [chr(33+i) for i in range(90)]

# Static key
key = 77
# A random key could be used for higher security, but the decrypter would be much more
# advanced and complex.

print(ind_password)

def encrypt(ind_password, chr_list, key):
    for id, letter in enumerate(ind_password):
        for idc, char in enumerate(chr_list):
            if letter == char:
                try:
                    # Just takes the current position and adds key to the index. 
                    # Shifting it up ultimatly.
                    ind_password[id] = chr_list[idc+key]
                except:
                    # If the index + key is greater than the amount of chars in the list,
                    # you minus the length of the char list (90) form the sum, to create
                    # a treadmill affect.
                    r_key = abs(abs(idc+key) - 90)
                    ind_password[id] = chr_list[r_key]
                    
def decrypt(ind_password, chr_list, key):
    for id, letter in enumerate(ind_password):
        for idc, char in enumerate(chr_list):
            if letter == char:
                try:
                    # Just minus the key from the index to reset position.
                    ind_password[id] = chr_list[idc-key]
                except:
                    # If the index - key is below 0, you must add the length of the list
                    # to the index and minus the key to reset the position.
                    t_key = abs(abs(90+idc) - key)
                    ind_password[id] = chr_list[t_key]
        
encrypt(ind_password, chr_list, key)
print(f'Encrypted: {ind_password}')

decrypt(ind_password, chr_list, key)
print(f'Decrypted: {ind_password}')
