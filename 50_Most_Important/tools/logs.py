import logging
from datetime import datetime

class LogInformation():

	def TEST_INFORMATION(self,namefile="",message=""):
		logging.basicConfig(filename=namefile+'.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO)
		logging.info(message)
