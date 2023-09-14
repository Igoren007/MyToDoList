import pika, sys, os, logging


logger = logging.basicConfig(level=logging.INFO, filename="rabbit_receiver.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    log.debug("Established connection to rabbitmq")
    channel.queue_declare(queue='tg_notify')

    def callback(ch, method, properties, body):
        print(f"Received:{body}", type(body))
        log.debug(f"Received:{body}")
        mes = body.split(b'_')
        for m in mes:
            print(m.decode('utf-8'))
            print("-*-*-*-*-*-*-*-*-*-*-*-*")

    channel.basic_consume(queue='tg_notify', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        log = logging.getLogger(__name__)
        log.setLevel(logging.DEBUG)
        handler2 = logging.FileHandler("/var/log/container/receiver.log", mode='w')
        formatter2 = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        handler2.setFormatter(formatter2)
        log.addHandler(handler2)
        log.debug("App started.....")
        print("App started.....")
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
