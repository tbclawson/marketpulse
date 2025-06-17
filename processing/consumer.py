from kafka import KafkaConsumer
import json
import logging

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def start_consumer(topic: str):
    """
    Start a Kafka consumer to listen for trade messages.
    
    Args:
        topic (str): Kafka topic to consume from.
    """
    # Kafka broker address (host machine)
    bootstrap_servers = ['localhost:9092']  # or 'broker:29092' if running inside Docker

    # Initialize the consumer
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset='earliest',  # or 'latest' for new messages only
        enable_auto_commit=True,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        group_id='marketpulse-consumer-group'
    )

    logger.info(f"Consumer started for topic: {topic}")

    try:
        for message in consumer:
            trade_data = message.value
            logger.info(f"Received trade: {trade_data}")

            # TODO: Call indicators engine
            # TODO: Call storage layer
    except KeyboardInterrupt:
        logger.info("Consumer shutdown requested by user.")
    finally:
        consumer.close()
        logger.info("Consumer connection closed.")
