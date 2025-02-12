import time
import logging
from azure.servicebus import ServiceBusMessage
from servicebus_consumer.processor import Processor

class OrchestratorProcessor(Processor):
    def process(self, message: any, sender: any) -> None:
        logging.info(f"[Orchestrator] Processing message: {message}")
        # Simulate processing delay.
        time.sleep(1)
        # Publish a new message.
        new_message = ServiceBusMessage("Message processed by OrchestratorProcessor.")
        sender.send_messages(new_message)
        logging.info("[Orchestrator] Published a new message.")
