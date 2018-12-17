*** Settings ***
Library         pages//SearchFlightPage.py    Chrome

*** Keywords ***
Open search page
    Open

Close pages
    Close

Select departure
    [Arguments]  ${city}
    select departure city  ${city}

select destination
    [Arguments]  ${city}
    select destination city  ${city}

select departure and destination
    [Arguments]  ${fromcity}  ${tocity}
    select departure city  ${fromcity}
    select destination city  ${tocity}
    search for flights
    @{flights}=     Get Found Flights
    set test variable  ${flights}

Search Flights
    search for flights
    @{flights}=     Get Found Flights
    set test variable  ${flights}

Flights are found
    Should Not Be Empty     ${flights}