from unittest import TestCase, main
from unittest.mock import Mock

from ut_design_2 import WrappedClient


class TestWrappedClient(TestCase):
    def test_send_converts_types(self):
        wrapped_client = WrappedClient()
        wrapped_client.client = Mock()
        wrapped_client.send("value", 1)

        wrapped_client.client.send.assert_called_with("value", "1")


if __name__ == "__main__":
    main()
