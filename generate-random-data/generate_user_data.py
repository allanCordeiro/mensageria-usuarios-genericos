# encoding: utf-8
import json
from confluent_kafka import Producer, KafkaError, KafkaException
from names import GetNameFromAPI
from cpf import RandomCPF


def generate_user_data(quantity=None):
    data_qty = 10 if quantity is None else quantity
    names_list = GetNameFromAPI(data_qty)
    cpf_list = RandomCPF(data_qty)
    random_data = []

    names = names_list.get_name_list()
    cpfs = cpf_list.get_cpf_list()

    for i in range(0, data_qty):
        user_data = {'cpf': cpfs[i], 'name': names[i]}
        random_data.append(user_data)

    return random_data


def ack(err, msg):
    delivered_records = 0
    if err is not None:
        print(f"Failed do deliver message {err}")
    else:
        delivered_records += 1
        print(f"Produced record to topic {msg.topic()} partition [{msg.partition()}] @ offset {msg.offset()}")


def publisher(user_key,user_data, kafka_producer:Producer):
    p = kafka_producer
    p.produce('new-customers',
              key=user_key,
              value= json.dumps(user_data, separators=(',', ':')).encode('utf-8'),
              on_delivery=ack)
    p.flush(10)


if __name__ == "__main__":
    producer = Producer({'bootstrap.servers': 'kafka1:19091'})
    user_data = generate_user_data()
    for i in range(len(user_data)):
        publisher("customer_data", user_data[i], producer)

