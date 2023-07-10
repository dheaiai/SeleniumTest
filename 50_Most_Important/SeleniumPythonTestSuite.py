import unittest
import HTMLTestRunner
import os
from test_check_login_page import VerifyloginPage

# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchText and HomePageTest class
VerifyloginPageSuite = unittest.TestLoader().loadTestsFromTestCase(VerifyloginPage)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([VerifyloginPageSuite])

# open the report file
outfile = open(dir + "/test_check_login_page.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests')

# run the suite using HTMLTestRunner
runner.run(test_suite)