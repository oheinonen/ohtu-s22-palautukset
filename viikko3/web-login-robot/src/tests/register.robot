*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Register With Valid Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  oskari123
    Set Password Confirmation  oskari123
    Submit Register Credentials
    Register Should Fail With Message  Username must be at least 3 characters long
    
Register With Valid Username And Too Short Password
    Set Username  oskari
    Set Password  ka
    Set Password Confirmation  oskari123
    Submit Register Credentials
    Register Should Fail With Message  Password must be at least 3 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  oskari
    Set Password  oskari123
    Set Password Confirmation  oskari1233
    Submit Register Credentials
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Register With Valid Credentials
    Go To Login Page
    Set Username  oskari
    Set Password  oskari123
    Submit Login Credentials
    Login Should Succeed



Login After Failed Registration
    Register With Invalid Credentials
    Go To Login Page
    Set Username  o
    Set Password  o
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password



*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register With Valid Credentials
    Set Username  oskari
    Set Password  oskari123
    Set Password Confirmation  oskari123
    Submit Register Credentials

Register With Invalid Credentials
    Set Username  o
    Set Password  o
    Set Password Confirmation  o
    Submit Register Credentials


