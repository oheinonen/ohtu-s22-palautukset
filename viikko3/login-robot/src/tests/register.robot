*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  oskari  oskari123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  oskari123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  oskari123
    Output Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  kalle123  os
    Output Should Contain  Password must be at least 3 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle123  oskarioskari
    Output Should Contain  Password can't contain only characters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123