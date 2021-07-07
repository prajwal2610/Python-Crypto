from cryptography.fernet import Fernet
import rsa

skey = open('symmetric.key','rb')
key = skey.read()


cipher = Fernet(key)

myfile = open('Screenshot 2021-07-02 000703.png','rb')
myfiledata= myfile.read()

encrypted_data = cipher.encrypt(myfiledata)
edata = open('encrypted_file','wb')
edata.write(encrypted_data)

print(encrypted_data)


pkey = open('publickey.key','rb')
pkdata = pkey.read()


pubkey = rsa.PublicKey.load_pkcs1(pkdata)


encrypted_key = rsa.encrypt(key,pubkey)

ekey = open('encrypted_key','wb')
ekey.write(encrypted_key)
