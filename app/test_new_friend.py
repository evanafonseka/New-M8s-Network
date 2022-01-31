import  unittest as ut
from NewFriend import NewFriend


class TestNewFriend(ut.TestCase):
    def setUp(self) -> None:
        self.instance = NewFriend()
        self.test_data = ["Bob knows Alice", "Alice knows Fred", "Fred knows Ganesh",
                          "Julie knows Ganesh", "Alice knows Ganesh"]
        self.single_entry = "Bob knows Alice"

    def test_split_names(self):
        """
        Test to see whether the names are split properly and added to the name keeper.
        """
        expected = {"Bob": {"Alice"}}
        self.instance.name_organiser(self.single_entry)
        self.assertEqual(self.instance.name_keeper, expected)

    def test_add_initial_data(self):
        """
        Test for 2 Keys that are the same
        Alice knows Fred and Ganesh,
            hence the second friendship should be appended and not replaced.
        """
        expected = {
            "Bob": {"Alice"},
            "Alice": {"Fred", "Ganesh"},
            "Fred": {"Ganesh"},
            "Julie": {"Ganesh"}
        }
        self.instance.add_initial_friends(self.test_data)
        self.assertEqual(self.instance.name_keeper, expected)

    def test_json_output(self):
        self.instance.add_initial_friends(self.test_data)
        output = self.instance.json_output()
        self.assertTrue(type(output) is dict)


    def test_add_friend(self):
        """
        Test adding a friend. Case where Fred adds Evan as a friend
        """
        self.instance.add_initial_friends(self.test_data)
        self.instance.add_friend("Fred", "Evan")
        self.assertTrue("Evan" in self.instance.name_keeper["Fred"])

    def test_remove_friend(self):
        """
        Test removing friends. Case where Bobs friend is Alice,
            hence Bob once removing Alice will be pointing to an empty list.
        """
        self.instance.add_initial_friends(self.test_data)
        self.instance.remove_friend(name_key="Bob", friend_to_remove="Alice")
        self.assertEqual(self.instance.name_keeper["Bob"], set())

    def test_friends_of_friends(self):
        """
        Test finding friends of friends. Case where we are given a name and return a list response.
            E.g. Bob -> Alice -> [Fred and Ganesh]
        :return:
        """
        self.instance.add_initial_friends(self.test_data)
        friends_of_friends = self.instance.list_friends_of_friends(name="Bob")
        self.assertListEqual(friends_of_friends, ["Ganesh", "Fred"])





