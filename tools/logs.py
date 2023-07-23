import logging
from datetime import datetime


class LogInformation():
    currFileName = None

    def getCurrentDate(self):
        # datetime object containing current date and time
        now = datetime.now()

        # print("now =", now)

        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d-%m-%Y_%H:%M:%S")
        # print("date and time =", dt_string)
        return dt_string

    def __init__(self, namefile=""):
        self.currFileName = namefile + "_" + self.getCurrentDate() + ".log"
        #print(self.currFileName)

    def TEST_INFORMATION(self, namefile="", message=""):
        #print(message)
        logging.basicConfig(filename=self.currFileName, filemode='w', format='%(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info(message)
