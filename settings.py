from flask import Flask
from cryptography.fernet import Fernet


app = Flask(__name__)
key = b'xaoOlrrom5pcjTFytdY9pFbTBAuNG95U43qHFXv6gZw='
f = Fernet(key)
path_to_db_file = 'telegraph.db'
