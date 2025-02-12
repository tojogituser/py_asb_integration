# modules/servicebus_consumer/consumer.py
import time
import threading
import logging
from azure.servicebus import ServiceBusClient
from .processor import Processor

class ServiceBusConsumer:
    def __init__(self, connection_str: str, subscription_topic: str, subscription_name: str,
                 publisher_topic: str, processor: Processor, num_threads: int = 5) -> None:
        """
        Initialize the consumer with Service Bus connection details, topic/subscription info,
        the processor instance, and the number of consumer threads.
        """
        self.connection_str = connection_str
        self.subscription_topic = subscription_topic
        self.subscription_name = subscription_name
        self.publisher_topic = publisher_topic
        self.processor = processor
        self.num_threads = num_threads
        self.servicebus_client = ServiceBusClient.from_connection_string(connection_str, logging_enable=True)
        self.threads = []
        self._stop_event = threading.Event()

    def _consume_loop(self) -> None:
        """
        The consuming loop that each thread runs. It creates its own receiver and sender,
        then continuously polls for messages and processes them until a stop event is set.
        """
        try:
            with self.servicebus_client.get_subscription_receiver(
                topic_name=self.subscription_topic,
                subscription_name=self.subscription_name
            ) as receiver, self.servicebus_client.get_topic_sender(
                topic_name=self.publisher_topic
            ) as sender:
                logging.info("Receiver started and listening...")
                while not self._stop_event.is_set():
                    try:
                        messages = receiver.receive_messages(max_message_count=10, max_wait_time=5)
                        if messages:
                            for message in messages:
                                try:
                                    self.processor.process(message, sender)
                                    receiver.complete_message(message)
                                except Exception as e:
                                    logging.error(f"Error processing message: {e}")
                                    receiver.abandon_message(message)
                        else:
                            time.sleep(1)
                    except Exception as e:
                        logging.error(f"Error in consuming loop: {e}")
                        time.sleep(5)
        except Exception as e:
            logging.error(f"Receiver initialization failed: {e}")

    def start(self) -> None:
        """
        Spawns the configured number of threads, each running its own consuming loop.
        """
        logging.info("Starting consumer threads...")
        for i in range(self.num_threads):
            thread = threading.Thread(
                target=self._consume_loop,
                name=f"ConsumerThread-{i}"
            )
            thread.daemon = True
            thread.start()
            self.threads.append(thread)
        logging.info("All consumer threads started.")

    def stop(self) -> None:
        """
        Signals the consumer threads to stop and waits for them to finish.
        """
        logging.info("Stopping consumer threads...")
        self._stop_event.set()
        for thread in self.threads:
            thread.join(timeout=10)
        self.servicebus_client.close()
        logging.info("Consumer stopped.")
