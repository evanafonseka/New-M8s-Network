from flask import Flask, jsonify, request
from flask_cors import cross_origin
from NewFriend import NewFriend

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True



BASE_DATA = ["Bob knows Alice", "Alice knows Fred", "Fred knows Ganesh", "Julie knows Ganesh"]
new_friends_instance = NewFriend()
new_friends_instance.add_initial_friends(BASE_DATA)


@app.route("/")
@cross_origin()
def index():
    return jsonify(new_friends_instance.json_output())


@app.route("/add_friend")
@cross_origin()
def add_friend():
    current_user = request.args.get("current_user")
    friend_to_add = request.args.get("friend_to_add")
    new_friends_instance.add_friend(name_key=current_user, friend_to_add=friend_to_add)
    return jsonify(new_friends_instance.json_output())


@app.route("/remove_friend")
@cross_origin()
def remove_friend():
    current_user = request.args.get("current_user")
    friend_to_remove = request.args.get("friend_to_remove")
    new_friends_instance.remove_friend(name_key=current_user, friend_to_remove=friend_to_remove)
    return jsonify(new_friends_instance.json_output())


@app.route("/friends_of_friends")
@cross_origin()
def friends_of_friends():
    name = request.args.get("name")
    return jsonify(new_friends_instance.list_friends_of_friends(name=name))
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
