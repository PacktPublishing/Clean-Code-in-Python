"""Clean Code in Python - Chapter 6: Descriptors

Test for the examples of descriptors methods.
"""

from unittest import TestCase, main

from descriptors_methods_2 import ClientClass
from descriptors_methods_3 import User


class TestSet(TestCase):
    def setUp(self):
        self.client = ClientClass()

    def test_name(self):
        self.assertEqual(ClientClass.descriptor._name, "descriptor")

    def test_invalid_parameters_not_assigned(self):
        with self.assertRaisesRegex(ValueError, "-1 is not >= 0"):
            self.client.descriptor = -1

        with self.assertRaisesRegex(ValueError, "'something' is not a number"):
            self.client.descriptor = "something"

    def test_assign_valid_data(self):
        for value in (1, 2.71, 0.5):
            with self.subTest(value=value):
                self.client.descriptor = value
                self.assertEqual(self.client.descriptor, value)

    def test_assing_valie_then_invalid(self):
        self.client.descriptor = 3.14
        with self.assertRaisesRegex(ValueError, "-4 is not >= 0"):
            self.client.descriptor = -4
        self.assertAlmostEqual(self.client.descriptor, 3.14)


class TestDelete(TestCase):
    def setUp(self):
        self.admin = User("root", "root@d.com", ["admin"])
        self.user = User("user", "user1@d.com", ["email", "helpdesk"])

    def test_delete_email(self):
        self.assertEqual(self.admin.email, "root@d.com")
        del self.admin.email
        self.assertIsNone(self.admin.email)

    def test_no_set_none(self):
        with self.assertRaisesRegex(ValueError, "email can't be set to None"):
            self.admin.email = None
        with self.assertRaisesRegex(ValueError, "email can't be set to None"):
            self.user.email = None

    def test_cannot_delete(self):
        with self.assertRaisesRegex(
            ValueError, "User \S+ doesn't have \S+ permission"
        ):
            del self.user.email


if __name__ == "__main__":
    main()
