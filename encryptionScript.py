# from textgenrnn import textgenrnn
# import tweepy
from simplecrypt import encrypt, decrypt
from pandas import read_json
import json

api_keys = read_json('api_keys.json', typ="series")

cryptKey = encrypt(api_keys['password'], api_keys['key'])
cryptSecret = encrypt(api_keys['password'], api_keys['secret'])

encrypted_keys = {}
encrypted_keys['key'] = cryptKey
encrypted_keys['secret'] = cryptSecret


file = open('key.key', 'wb')
file.write(cryptKey)
file.close()
file = open('secret.key', 'wb')
file.write(cryptSecret)
file.close()
