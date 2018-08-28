"""Clean Code in Python - Chapter 8: Unit Testing

> Unit Testing and Software Design
"""
import logging
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MetricsClient:
    """3rd-party metrics client"""

    def send(self, metric_name, metric_value):
        if not isinstance(metric_name, str):
            raise TypeError("expected type str for metric_name")

        if not isinstance(metric_value, str):
            raise TypeError("expected type str for metric_value")

        logger.info("sending %s = %s", metric_name, metric_value)


class WrappedClient:
    """An object under our control that wraps the 3rd party one."""

    def __init__(self):
        self.client = MetricsClient()

    def send(self, metric_name, metric_value):
        return self.client.send(str(metric_name), str(metric_value))


class Process:
    """Same process, now using a wrapper object."""

    def __init__(self):
        self.client = WrappedClient()

    def process_iterations(self, n_iterations):
        for i in range(n_iterations):
            result = self.run_process()
            self.client.send("iteration.{}".format(i), result)

    def run_process(self):
        return random.randint(1, 100)


if __name__ == "__main__":
    Process().process_iterations(10)
