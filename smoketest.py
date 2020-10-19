from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from path import HomePageTest

assertion_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(HomePageTest)

smoke_test = TestSuite([assertion_test, search_test])


# this dictionary is used to the declare the output file of the test
kwargs = {
    "output": 'smoke-report'
}

# we pass the TestRunner with the arguments to generate the report.
runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)