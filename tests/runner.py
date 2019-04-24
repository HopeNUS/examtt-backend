import sys
import unittest
from HtmlTestRunner import HTMLTestRunner

import tests.database.test_DatabaseController as dbCtrl
import tests.logic.test_StudentLogicController as stuLogicCtrl
import tests.logic.test_WarriorLogicController as warLogicCtrl

loader = unittest.TestLoader()
suite = unittest.TestSuite()

for module in [dbCtrl, stuLogicCtrl, warLogicCtrl]:
    suite.addTests(loader.loadTestsFromModule(module))

runner = unittest.TextTestRunner(verbosity=3)
if len(sys.argv) == 2 and sys.argv[1] == "html":
    runner = HTMLTestRunner(
        output='report',
        report_name="IntegrationTest",
        combine_reports=True)
result = runner.run(suite)
if result.failures:
    exit(-1)
