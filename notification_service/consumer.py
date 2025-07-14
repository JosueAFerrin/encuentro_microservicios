# consumer.py
import pika
import json

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"🔔 Notificación: El usuario {data['username']} ha iniciado sesión.")

def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='user.login', durable=True)

    channel.basic_consume(queue='user.login', on_message_callback=callback, auto_ack=True)
    print(" [*] Esperando eventos de login...")
    channel.start_consuming()

if __name__ == "__main__":
    consume()
