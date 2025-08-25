import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=r'C:\Users\Rahul\PycharmProjects\PageObjectModel_selenium\Log\automation.log',
                            format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%Y-%m-%d %H:%M:%S',force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

