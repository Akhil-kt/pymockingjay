from pandas import read_json
from simplecrypt import encrypt, decrypt

api_keys = read_json('api_keys.json', typ="series")
password = api_keys['password']

def getKey():
    file = open('key.key', 'rb')
    key = file.read() # The key will be type bytes
    file.close()
    key = decrypt(password, key)
    return key
 
def getSecret():
    file = open('secret.key', 'rb')
    secret = file.read() # The key will be type bytes
    file.close()
    secret = decrypt(password, secret)
    return secret



