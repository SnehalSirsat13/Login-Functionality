import configparser
config = configparser.RawConfigParser()
config.read(r"C:\Users\Rahul\PycharmProjects\PageObjectModel_selenium\configuration\config.ini")

class Readconfig:

    @staticmethod
    def getApplicationURL():
        url = config.get("common info","base_Url")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common info","userName")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info","password")
        return password



