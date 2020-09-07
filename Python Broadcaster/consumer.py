#!/usr/bin/new python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

chane = connection.channel()


def callbackFunc(ch, method, properties, message):
    print("message received: %r" % message)


chane.basic_consume(
    queue='test', on_message_callback=callbackFunc, auto_ack=True)

print('Waiting message.....')

chane.start_consuming()
