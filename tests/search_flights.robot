*** Settings ***
Resource         keywords//search_flights_keywords.robot
Resource         keywords//flight_result_keywords.robot
Resource         keywords//purchase_ticket_keywords.robot
Test Setup     Open search page
Test Teardown  Close pages

*** Variables ***
${Departure}    Paris
${Destination}    London
${Username}    Peter

*** Test Cases ***
The user can search for flights
    select departure and destination    ${Departure}    ${Destination}
    Choose Flights
    Input Username    ${Username}
