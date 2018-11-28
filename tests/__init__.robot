*** Settings ***
Library         pages//BasePage.py
Suite Setup		My Suite Setup    SuiteSetup
Suite Teardown	My Suite Teardown    SuiteTeardown

*** Variables ***
${MESSAGE}       Hello, world!!!!!
${LINK}    https://google.com

*** Keywords ***
My Suite Setup
	[Arguments]    ${msg}
	suite setup    ${msg}

My Suite Teardown
	[Arguments]    ${msg}
	suite teardown    ${msg}