*** Settings ***
Library         pages//PurchaseTicketPage.py    Chrome

*** Keywords ***

Input Username
    [Arguments]  ${name}
    input name  ${name}
