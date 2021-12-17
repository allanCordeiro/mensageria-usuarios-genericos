# encoding: utf-8
import argparse
import json
import logging
import os.path
import traceback

import confluent_kafka

from generate_user_data import GenerateUserData
from confluent_kafka import Producer, KafkaException


class StreamProducer:
    def __init__(self, kafka_config):
        self._config = kafka_config
        self.producer = None

    @staticmethod
    def ack(err, msg):
        delivered_records = 0
        if err is not None:
            print(f"Failed do deliver message {err}")
        else:
            delivered_records += 1
            print(f"Produced record to topic {msg.topic()} partition [{msg.partition()}] @ offset {msg.offset()}")

    def publish(self, topic, user_key, data):
        logger = self.__get_logger()

        try:
            if self.producer is None:
                self.__get_connection()
            logger.debug(f"Sending message to topic [{topic}]")
            self.producer.produce(topic=topic,
                                  key=user_key,
                                  value=json.dumps(data, separators=(',', ':')).encode('utf-8'),
                                  on_delivery=self.ack)
            self.producer.flush()
        except BufferError as be:
            logger.error(f"BufferError trying to publish topic [{topic}]:[{user_key}]")
        except Exception:
            logger.error(f"Error trying to publish data topic [{topic}]:[{user_key}]")
            logger.debug(traceback.format_exc())

    @staticmethod
    def __get_logger():
        return logging.getLogger(os.path.basename(__file__))

    def __get_connection(self):
        logger = self.__get_logger()
        conf = {
            'bootstrap.servers': ','.join(map(str, self._config.get('hosts')))
        }
        try:
            producer = confluent_kafka.Producer(**conf)
            self.producer = producer
        except KafkaException as ke:
            logger.error("Error to estabilsh connection with Kafka")
            logger.debug(traceback.format_exc())
            raise KafkaException(ke)


def main(ciclying=None):
    logging.basicConfig(level=logging.DEBUG)
    hosts = {"hosts": ["kafka1:19091"]}
    stream = StreamProducer(hosts)

    while True:
        user = GenerateUserData()
        user_data = user.get_user_data()

        for i in range(len(user_data)):
            stream.publish("new-customers", "customer_data", user_data[i])
        if ciclying is None or ciclying == 1:
            break
        else:
            ciclying -= 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parameters')
    parser.add_argument('--cicles',
                        '-c',
                        type=int,
                        help='How many cicles to create messages to the topic'
    )
    args = parser.parse_args()

    main(args.cicles)

