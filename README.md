# New Friends Network

## Requirements:
Design a system for my “New Friend Network”. Given a list of people and their friends in the following format:
- “Bob knows Alice”, - This does not imply that Alice knows Bob too
- “Alice knows Fred”,
- “Fred knows Ganesh”,
- “Julie knows Ganesh”, ...etc

Designed an API to include:
- Adding friends
- Removing friends
- Listing Friends of friends. eg Bob  “friend of a friend” is `[“Fred”]`

## Solution
- Please see `NewFriend.py` that handles the transformation of the string and returns the output as json
- Data structure used is a hashset: `name_keeper` for memory purposes, with the assumption that more names will be input 
- Therefore, a list would not be efffective especially when searching for *friends of friends*
- Please see `NewFriendsNetwork.postman_collection.json` for example requests to speak to the API

## How to Run
### Docker (Preferred)
```
git clone https://github.com/evanafonseka/New-M8s-Network.git
docker-compose build
docker-compose up
```
### Other (Not as Preferred)
```
git clone https://github.com/evanafonseka/New-M8s-Network.git
pip3 install -r requirements.txt
python3 main.py
```

Open up `http://localhost:4000/` on your browser (or the postman collection)


## API Endpoints
### Default
- Loads initial data
```
{
  "Alice": [
    "Fred"
  ], 
  "Bob": [
    "Alice"
  ], 
  "Fred": [
    "Ganesh"
  ], 
  "Julie": [
    "Ganesh"
  ]
}
```

### /add_friend
- Parameters:
  - current_user
  - friend_to_add

E.G.
```
http://localhost:4000/add_friend?current_user={Fred}&friend_to_add={Scooby}
```

### /remove_friend
- Parameters:
  - current_user
  - friend_to_remove


E.G.
```
http://localhost:4000/remove_friend?current_user={Fred}&friend_to_remove={Ganesh}
```

### /friends_of_friends
- Parameter:
  - name

E.G.
```
http://localhost:4000/friends_of_friends?name={Alice}
```

