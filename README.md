# New Friends Network

## Requirements:
Design a system for my “New Friend Network”. Given a list of people and their friends in the following format:
- “Bob knows Alice”, - This does not imply that Alice knows Bob too
- “Alice knows Fred”,
- “Fred knows Ganesh”,
- “Julie knows Ganesh”, ...etc

## Solution
- Please see `NewFriend.py` that handles the transformation of the string and returns the output as json
- Data structure used was a hashset for memory purposes, with the assumption that repeated names will be input and therefore will not be useful if a list was used 
- Especially when searching for *friends of friends*
- Please see `NewFriendsNetwork.postman_collection.json` for example requests to speak to the API

## How to Run
### Docker (Preferred)
```
git clone https://github.com/evanafonseka/New-M8s-Network.git
cd NewFriendsNetwork
docker-compose up
```
### Other (Not as Preferred)
```
git clone https://github.com/evanafonseka/New-M8s-Network.git
cd NewFriendsNetwork/app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

