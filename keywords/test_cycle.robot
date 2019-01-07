*** Settings ***
Library     pages//BasePage.py    Chrome
Library     Selenium2Library

*** Keywords ***
TestSetup
    Opentestbrowser

TestTeardown
    Capture Page Screenshot
    closetestbrowser
