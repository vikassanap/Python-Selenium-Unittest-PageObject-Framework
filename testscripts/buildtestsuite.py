import unittest
import managetenantstests
import logintests
import uploadapplicationtests
import createformtests
import xmlrunner
from main import *

suite = unittest.TestSuite()
if(config['test_suit_name'] == "smoke_test_suite"):
    suite1 = managetenantstests.suite()
    suite2 = logintests.smoke_suite()
    suite.addTest(suite1)
    suite.addTest(suite2)

if(config['test_suit_name'] == "all"):
    suite1 = managetenantstests.suite()
    suite2 = logintests.suite()
    suite3 = uploadapplicationtests.suite()
    suite4 = createformtests.suite()
    suite.addTest(suite1)
    suite.addTest(suite2)
    suite.addTest(suite3)
    suite.addTest(suite4)

if(config['test_suit_name'] == "upload"):
    suite1 = uploadapplicationtests.suite() 
    suite.addTest(suite1)

if(config['test_suit_name'] == "logintests"):
    suite1 = logintests.suite()
    suite.addTest(suite1)

path =  os.path.dirname(os.path.realpath(__file__))
time_stamp = datetime.now().isoformat()
report_file_name = path +"/../test-reports/history_reports/"+time_stamp+".html"
mail_file_name = path +"/../test-reports/report/mail_Report.html"

outfile = open(mail_file_name, "w")
outfile1 = open(report_file_name, "w")
runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                stream1=outfile1,
                verbosity=2,
                title= config['project_title'],
                description=config['project_description']
                 )
runner.run(suite)
outfile.close()
time.sleep(5)


