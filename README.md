# New Friends Network

## Requirements:
Design a system for my “New Friend Network”. I was given a list of people and their friends in the following format:
- “Bob knows Alice”, - This does not imply that Alice knows Bob too
- “Alice knows Fred”,
- “Fred knows Ganesh”,
- “Julie knows Ganesh”, ...etc

## Solution
- Please see `NewFriend.py` that handles the transformation of the string and returns the output as json
- Data structure used was a hashset for memory purposes, with the assumption that repeated names will be input and therefore will not be useful if a list was used especially when searching *friends of friends*
- Please see `NewFriendsNetwork.postman_collection.json` for example requests to speak to the API

## How to Run
### Docker
```
git clone https://github.com/evanafonseka/New-M8s-Network.git
cd NewFriends
docker-compose up
```

