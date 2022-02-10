"""
Class to handle incoming data regarding peoples friends.
"""
from collections import defaultdict
import logging


__author__ = "Evan Fonseka"
logger = logging.getLogger(__name__)


class NewFriend:
    def __init__(self):
        self.name_keeper = defaultdict(set)

    def name_organiser(self, name: str):
        """Name Organiser

        Args:
            name (str): Takes in the string value, gets our key and value to input into the name keeper
        """
        names = name.split(" ")
        name_key = names[0]
        name_value = names[-1]
        self.name_keeper[name_key] |= {name_value}

    def add_friends(self, names: list):
        """Add Initial Friends

        Args:
            names (list): List of names base names
        """
        for n in names:
            self.name_organiser(n)

    def to_json(self) -> dict:
        """Converts our hashset name keeper into a jsonifiable object

        Args:
            self ([hashset]): dict(k, {v})

        Returns:
            [dict(list)]: Makes flask happy
        """
        return dict(zip(self.name_keeper.keys(), map(list, self.name_keeper.values())))

    def add_friend(self, name_key: str, friend_to_add: str):
        """Add a Friend

        Args:
            name_key (str): Takes in the profile name
            friend_to_add (str): Friend that can be added
        """
        if friend_to_add is not None:
            self.name_keeper[name_key] |= {friend_to_add}
        else:
            return logger.error(f"Sorry your {friend_to_add} does not exist, please try again.")

    def remove_friend(self, name_key: str, friend_to_remove: str):
        """Remove a Friend

        Args:
            name_key (str): Takes in the profile name
            friend_to_remove (str): Friend that will be un-friended
        """
        self.name_keeper[name_key].remove(friend_to_remove)

    def list_friends_of_friends(self, name: str) -> list:
        """Find Mutual Friends

        Args:
            name (str): Takes in a name, looks at their friends and finds possible mutual friends.

        Returns:
            list: Possible new friends to add.
        """
        output = []

        input_friends = self.name_keeper[name]
        for i in input_friends:
            output.extend(self.name_keeper[i])

        if len(output) >= 1:
            return output
        else:
            return logger.error(f"Sorry {name} has no potential mutual friends :(")
