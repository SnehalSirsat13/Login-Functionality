import configparser

config=configparser.RawConfigParser()
config.read(r"C:\Users\Rahul\PycharmProjects\Hybrid_Bank_Framework\Configurations\config.ini")


class ReadConfig():
    @staticmethod
    def getApplicationURL(self):
       url = config.get('common info','baseURL')
       return url

    @staticmethod
    def getUseremail(self):
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword(self):
        username = config.get('common info', 'password')
        return password



