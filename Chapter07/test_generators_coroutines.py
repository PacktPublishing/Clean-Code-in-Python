""""Tests for generators_coroutines_*.py"""
from unittest import TestCase, main, mock

from generators_coroutines_1 import (CustomException, DBHandler, stream_data,
                                     stream_db_records)
from generators_coroutines_2 import auto_stream_db_records
from generators_coroutines_2 import stream_db_records as stream_db_records_2


class BaseTestCase(TestCase):
    def setUp(self):
        self.info = mock.patch("log.logger.info").start()
        self.handler = DBHandler("test")

    def tearDown(self):
        self.info.stop()


class TestClose(BaseTestCase):
    """Tests for generators_coroutines_1"""

    def test_close_called(self):
        streamer = stream_db_records(self.handler)
        rows = next(streamer)
        streamer.close()

        self.assertEqual(len(rows), 10)
        self.assertTrue(self.handler.is_closed)


class TestThrow(BaseTestCase):
    """Tests for generators_coroutines_1"""

    def test_throw_controlled_exception(self):
        streamer = stream_data(self.handler)

        self.assertEqual(len(next(streamer)), 10)
        streamer.throw(CustomException)
        self.assertEqual(len(next(streamer)), 10)

    def test_unhandled_exception(self):
        streamer = stream_data(self.handler)
        self.assertEqual(len(next(streamer)), 10)
        with self.assertRaises(StopIteration):
            streamer.throw(RuntimeError)

        self.assertTrue(self.handler.is_closed)


class TestStreamer(BaseTestCase):
    """Tests for generators_coroutines_2.stream_db_records."""

    def test_default_value(self):
        streamer = stream_db_records_2(self.handler)
        none = next(streamer)
        rows = next(streamer)

        self.assertIsNone(none)
        self.assertEqual(len(rows), 10)

    def test_with_fixed_value(self):
        streamer = stream_db_records_2(self.handler)
        none = next(streamer)
        rows = streamer.send(20)

        self.assertIsNone(none)
        self.assertEqual(len(rows), 20)

    def test_multiple_values(self):
        streamer = stream_db_records_2(self.handler)
        none = next(streamer)
        default_len = next(streamer)

        self.assertIsNone(none)
        self.assertEqual(len(default_len), 10)

        self.assertEqual(len(streamer.send(20)), 20, "provided length of 20")
        self.assertEqual(len(streamer.send(15)), 15, "provided length of 15")
        self.assertEqual(
            len(next(streamer)), 15, "no length provided use previous = 15"
        )
        self.assertEqual(
            len(streamer.send(None)), 15, "nothing sent, use previous"
        )
        self.assertEqual(len(streamer.send(7)), 7, "new provided length")

    def test_first_call_fixed_value(self):
        streamer = stream_db_records_2(self.handler)

        self.assertIsNone(next(streamer))
        self.assertEqual(len(streamer.send(1)), 1)


class TestStreamer2(BaseTestCase):
    """Tests for generators_coroutines_2.auto_stream_db_records."""

    def test_default_value(self):
        streamer = auto_stream_db_records(self.handler)
        rows = next(streamer)
        self.assertEqual(len(rows), 10)

    def test_with_fixed_value(self):
        streamer = auto_stream_db_records(self.handler)
        rows = streamer.send(20)

        self.assertEqual(len(rows), 20)

    def test_multiple_values(self):
        streamer = auto_stream_db_records(self.handler)
        default_len = next(streamer)

        self.assertEqual(len(default_len), 10)

        self.assertEqual(len(streamer.send(20)), 20, "provided length of 20")
        self.assertEqual(len(streamer.send(15)), 15, "provided length of 15")
        self.assertEqual(
            len(next(streamer)), 15, "no length provided use previous = 15"
        )
        self.assertEqual(
            len(streamer.send(None)), 15, "nothing sent, use previous"
        )
        self.assertEqual(len(streamer.send(7)), 7, "new provided length")

    def test_first_call_fixed_value(self):
        streamer = auto_stream_db_records(self.handler)
        self.assertEqual(len(streamer.send(1)), 1)


if __name__ == "__main__":
    main()
