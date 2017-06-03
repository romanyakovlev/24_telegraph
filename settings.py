from cryptography.fernet import Fernet
from flask import Flask
import psycopg2
from urllib.parse import urlparse


app = Flask(__name__)
key = b'xaoOlrrom5pcjTFytdY9pFbTBAuNG95U43qHFXv6gZw='
f = Fernet(key)

urlparse.uses_netloc.append("postgres")
url = urlparse(os.environ["DATABASE_URL"])
