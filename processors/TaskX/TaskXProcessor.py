import time
import logging
from azure.servicebus import ServiceBusMessage
from servicebus_consumer.processor import Processor

class TaskXProcessor(Processor):
    def process(self, message: any, sender: any) -> None:
        logging.info(f"[TaskX] Processing message: {message}")
        # Simulate processing delay.
        time.sleep(1)
        # Publish a new message.
        new_message = ServiceBusMessage("Message processed by TaskXProcessor.")
        sender.send_messages(new_message)
        logging.info("[TaskX] Published a new message.")
