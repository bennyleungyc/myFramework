*** Settings ***
Resource         keywords//search_flights_keywords.robot
Test Setup     Open search page
Test Teardown  Close pages

*** Test Cases ***
The user can search for flights
    Select Departure   Paris
    Select Destination    London
    Search Flights
    Flights are found

