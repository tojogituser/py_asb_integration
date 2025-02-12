import time
import logging
from servicebus_consumer.consumer import ServiceBusConsumer
from TaskXProcessor import TaskXProcessor  # Local import

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(threadName)s] %(levelname)s: %(message)s')

if __name__ == "__main__":
    # Replace with your actual Service Bus details.
    connection_str = "<your_service_bus_connection_string>"
    subscription_topic = "<your_subscription_topic>"
    subscription_name = "<your_subscription_name>"
    publisher_topic = "<your_publisher_topic>"
    
    processor = TaskXProcessor()
    consumer = ServiceBusConsumer(connection_str, subscription_topic, subscription_name, publisher_topic, processor, num_threads=5)
    
    try:
        consumer.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Interrupt received. Shutting down...")
        consumer.stop()
