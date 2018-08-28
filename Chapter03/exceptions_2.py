"""Clean Code in Python - Chapter 3: General Traits of Good Code

> Error Handling - Exceptions
"""
import logging
import time

logger = logging.getLogger(__name__)


class Connector:
    """Abstract the connection to a database."""

    def connect(self):
        """Connect to a data source."""
        return self

    @staticmethod
    def send(data):
        return data


class Event:
    def __init__(self, payload):
        self._payload = payload

    def decode(self):
        return f"decoded {self._payload}"


def connect_with_retry(connector, retry_n_times, retry_threshold=5):
    """Tries to establish the connection of <connector> retrying
    <retry_n_times>.

    If it can connect, returns the connection object.
    If it's not possible after the retries, raises ConnectionError

    :param connector:           An object with a `.connect()` method.
    :param retry_n_times int:   The number of times to try to call
                                ``connector.connect()``.
    :param retry_threshold int: The time lapse between retry calls.

    """
    for _ in range(retry_n_times):
        try:
            return connector.connect()
        except ConnectionError as e:
            logger.info(
                "%s: attempting new connection in %is", e, retry_threshold
            )
            time.sleep(retry_threshold)
    exc = ConnectionError(f"Couldn't connect after {retry_n_times} times")
    logger.exception(exc)
    raise exc


class DataTransport:
    """An example of an object that separates the exception handling by
    abstraction levels.
    """

    retry_threshold: int = 5
    retry_n_times: int = 3

    def __init__(self, connector):
        self._connector = connector
        self.connection = None

    def deliver_event(self, event):
        self.connection = connect_with_retry(
            self._connector, self.retry_n_times, self.retry_threshold
        )
        self.send(event)

    def send(self, event):
        try:
            return self.connection.send(event.decode())
        except ValueError as e:
            logger.error("%r contains incorrect data: %s", event, e)
            raise
