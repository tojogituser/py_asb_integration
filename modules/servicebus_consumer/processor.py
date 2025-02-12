# modules/servicebus_consumer/processor.py
from typing import Any

class Processor:
    def process(self, message: Any, sender: Any) -> None:
        """
        Process a message and optionally publish another message using the provided sender.
        Override this method in subclasses.
        """
        raise NotImplementedError("Subclasses must implement the process method.")
