import inspect
import logging
class BaseClass:
    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        logger.addHandler(fileHandler)

        formatter = logging.Formatter("%(asctime)s: %(levelname)s:%(name)s: %(message)s")
        fileHandler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        return logger
