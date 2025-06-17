from kafka import KafkaProducer
import json
import logging

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Kafka broker URL based on docker-compose internal network
KAFKA_BROKER = 'localhost:9092'

# Initialize the producer
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)



def send_trade_message(topic: str, trade_data: dict):
    """
    Publish a trade message to Kafka.
    
    Args:
        topic (str): Kafka topic name.
        trade_data (dict): JSON-serializable dict.
    """
    try:
        future = producer.send(topic, value=trade_data)
        result = future.get(timeout=10)
        logger.info(f"Sent message to {result.topic} partition {result.partition} offset {result.offset}")
    except Exception as e:
        logger.exception(f"Failed to produce message: {e}")

def close_producer():
    """
    Ensure all messages are flushed before shutdown.
    """
    producer.flush()
    logger.info("Kafka producer flushed and closed.")
