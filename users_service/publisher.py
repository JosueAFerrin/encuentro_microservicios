# publisher.py
import pika
import json

def send_login_event(username: str):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        channel = connection.channel()
        channel.queue_declare(queue='user.login', durable=True)

        message = json.dumps({"username": username})
        channel.basic_publish(
            exchange='',
            routing_key='user.login',
            body=message,
            properties=pika.BasicProperties(delivery_mode=2)
        )
        connection.close()
    except Exception as e:
        print(f"Error al enviar evento a RabbitMQ: {e}")
