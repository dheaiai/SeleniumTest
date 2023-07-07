import logging
from datetime import datetime

class LogInformation():

	def TEST_INFORMATION(self,namefile="",message=""):
		#now = datetime.now()
		#namefile = namefile+"-"+now.strftime("%d/%m/%Y-%H:%M:%S")+".log"
		#print(namefile)
		logging.basicConfig(filename=namefile+'.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO)
		logging.info(message)
