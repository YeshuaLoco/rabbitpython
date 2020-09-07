#!/usr/bin/new python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

chane = connection.channel()

chane.queue_declare(queue = 'test')

chane.basic_publish(exchange='', routing_key='test', body='This is a test message')

chane.close()

