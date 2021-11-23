from cryptography.fernet import Fernet

key = Fernet.generate_key()
key2 = Fernet.generate_key()

crypter = Fernet(key)
crypter2 = Fernet(key2)

dyn_id = crypter.encrypt(b'audiovideonerds@yahoo.com')
dyn_pw = crypter2.encrypt(b'Michoaca1')

decrypt_string = crypter.decrypt(dyn_id)
decrypt_string2 = crypter2.decrypt(dyn_pw)

USER_ID = (str(decrypt_string, 'utf8'))
USER_PW = (str(decrypt_string2, 'utf8'))
