import logging

class LogInformation():

	def TEST_INFORMATION(self,namefile="",message=""):
		print(namefile)
		namefile = "/Users/dheerajjain/Documents/Selenium/50_Most_Important/tools/"+namefile+".log"
		logging.basicConfig(filename='namefile.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO)
		logging.info(message)
