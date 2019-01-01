*** Settings ***
Library     pages//BasePage.py    Chrome
Suite Setup      SuiteSetup
Suite Teardown    SuiteTeardown

*** Keywords ***
SuiteSetup
    Log     FunctionA SuiteSetup

SuiteTeardown
    Log     FunctionA SuiteTeardown