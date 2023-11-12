
# EasyMC Token Bruteforcer

Bruteforces EasyMC Alt tokens and redeems them and gives you the session id.

## FAQ

#### Is it safe?

Yes, you can check the source code.

#### How do i login with a Session ID?

Use an Session ID login mod, one i recommend is: https://github.com/Schubilegend/SchubiAuthV2

#### How does it work?

It generates a random 20 letter string, then sends a request to the EasyMC Token Redeem API, and if its valid, it redeems it and gives you the info about the account. (Minecraft Username, UUID, Session ID) 


## Screenshots

![App Screenshot](https://cdn.discordapp.com/attachments/1160238803735285833/1173258697032613948/hello__-_py_bruteforcer.py_1_b1.png?ex=65634d4f&is=6550d84f&hm=0067037319c7062c0290d3aa0f11f809aca69c44750be7145c30afccc135fcb8&)


## Installation
```bash
  git clone https://github.com/chleba124/easymc-bruteforcer.git
  cd easymc-bruteforcer
  bash install_requirements.sh or install_requirements.bat (If your on Windows)
  python3 bruteforcer.py or python bruteforcer.py (Use python3 if you use linux.)
```
    
