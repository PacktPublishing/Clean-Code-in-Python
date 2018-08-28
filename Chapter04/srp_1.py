"""Clean Code in Python - Chapter 4, The SOLID Principles

> SRP: Single Responsibility Principle
"""


class SystemMonitor:
    def load_activity(self):
        """Get the events from a source, to be processed."""

    def identify_events(self):
        """Parse the source raw data into events (domain objects)."""

    def stream_events(self):
        """Send the parsed events to an external agent."""
