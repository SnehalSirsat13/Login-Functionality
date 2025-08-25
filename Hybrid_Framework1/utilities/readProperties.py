import configparser

from pytest_html.extras import url

config=configparser.RawConfigParser()
config.read(r"C:\Users\Rahul\PycharmProjects\Hybrid_Framework1\Configurations\config.ini")

class Readconfig:
    @staticmethod
    def getApplicationURL():
        config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        config.get('common info', 'password')
        return password





