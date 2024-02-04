
# EasyMC Token Bruteforcer

Bruteforces EasyMC Alt tokens and redeems them and gives you the session id.

## FAQ

#### Is it safe?

Yes, you can check the source code.

#### How do i login with a Session ID?

Use an Session ID login mod, one i recommend is: https://github.com/Schubilegend/SchubiAuthV2

#### How does it work?

It generates a random 20 letter string, then sends a request to the EasyMC Token Redeem API, and if its valid, it redeems it and gives you the info about the account. (Minecraft Username, UUID, Session ID) 




## Installation
```bash
  git clone https://github.com/chleba124/easymc-bruteforcer.git
  cd easymc-bruteforcer
  bash install_requirements.sh or install_requirements.bat (If your on Windows)
  python3 bruteforcer.py or python bruteforcer.py (Use python3 if you use linux.)
```
    
