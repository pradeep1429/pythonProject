import inspect
import logging
from datetime import datetime
from pathlib import Path

import pytest


# @pytest.mark.usefixtures("setup")
class Base:
    ROOT_PATH = str(Path(__file__).parent.parent)
    @staticmethod
    def getLogger():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        logFilePath = Base.ROOT_PATH + "/logs/" + 'logfile_'+ datetime.now().strftime("%Y%m%d") +'.log'
        #logFilePath = self.ROOT_PATH + "/logs/" + 'logfile.log'
        fileHandler = logging.FileHandler(logFilePath, mode='w')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger



