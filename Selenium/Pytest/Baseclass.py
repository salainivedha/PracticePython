import logging
class BaseClass:
    def getlogger(self):
        logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler("logfile.log")
        logger.addHandler(fileHandler)

        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
        fileHandler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        return logger
