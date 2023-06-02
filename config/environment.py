import configparser
import os

config = configparser.ConfigParser()

Current_folder = os.path.dirname(os.path.abspath(__file__))
env_file = os.path.join(Current_folder, 'env.ini')
config.read(env_file)

class ReadConfig:

    @staticmethod
    def getURI():
        uri = config.get('Environment_Details', 'baseURI')
        return str(uri)

    @staticmethod
    def getEmail():
        email = config.get('Login_Creds', 'user_email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('Login_Creds', 'password')
        return password


