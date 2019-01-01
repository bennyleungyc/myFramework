*** Settings ***
Library     pages//BasePage.py    Chrome

*** Keywords ***
TestSetup
    Openbrowser

TestTeardown
    Closebrowser
