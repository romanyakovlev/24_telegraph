from cryptography.fernet import Fernet
from flask import Flask
import psycopg2
import urllib.parse
import os


app = Flask(__name__)
key = b'xaoOlrrom5pcjTFytdY9pFbTBAuNG95U43qHFXv6gZw='
f = Fernet(key)

urllib.parse.uses_netloc.append("postgres")
url = urllib.parse.urlparse(os.environ["DATABASE_URL"])
