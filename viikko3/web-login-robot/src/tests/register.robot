*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  tee
    Set Password  teesken123
    Set Password Confirmation  teesken123
    Submit Credentials
    
Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  teesken123  
    Set Password Confirmation  teesken123
    Submit Credentials
    Register Should Fail With Message  Username should only contain letters and be atleast 3 characters long

Register With Valid Username And Too Short Password
    Set Username  tee
    Set Password  teeske1
    Set Password Confirmation  teeske1
    Submit Credentials 
    Register Should Fail With Message  Password needs to be atleast 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  tee
    Set Password  teesken123  
    Set Password Confirmation  teesken12
    Submit Credentials
    Register Should Fail With Message  Passwords do not match 

*** Keywords ***
Create User And Go To Register Page
    Create User  testi  testi123
    Go To Register Page
    Register Page Should Be Open

Register Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}
    
Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register
