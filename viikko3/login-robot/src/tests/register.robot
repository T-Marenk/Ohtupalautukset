*** Settings ***
Resource  resource.robot
Test Setup  Input New Command and Create User


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  tee  teesken123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  testi  teesken123
    Output Should Contain  User with username testi already exists

Register With Too Short Username And Valid Password
    Input Credentials  te  teesken123
    Output Should Contain  Username has to be atleast 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  tee  teeske1
    Output Should Contain  Password needs to be atleast 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  tee  teeskentel
    Output Should Contain  Password needs to contain numbers and letters
  
*** Keywords ***
Input New Command and Create User
    Input New Command
    Input Credentials  testi  testi123 
    Input New Command
