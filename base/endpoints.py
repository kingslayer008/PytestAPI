import configparser
import os

config = configparser.ConfigParser()

Current_folder = os.path.dirname(os.path.abspath(__file__))
endpoints_file = os.path.join(Current_folder, 'endpoints.ini')
config.read(endpoints_file)

class ReadEndpoint:

    @staticmethod
    def fetch_endpoint(class_name, endpoint_name):
        uri = config.get(class_name, endpoint_name)
        return str(uri)



