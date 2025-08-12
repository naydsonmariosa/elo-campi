# main.py
from lab.message_handler import MessageHandler
from engine.broker_client import BrokerClient


servicebus_conn_str = "Endpoint=sb://omnichain-dev.servicebus.windows.net/;SharedAccessKeyName=puc;SharedAccessKey=UBF0OYTTB0ktbDir/IS/hlKMQWuv5mOiB+ASbBbPx6s="
input_queue_name  = "sc-puc-entrypoint"
output_queue_name = "sc-puc-output"
dlq_queue_name    = "sc-puc-dlq"


def main():
    
    messageProcessor = MessageHandler()

    brokerClient = BrokerClient(
        message_processor    = messageProcessor,
        servicebus_conn_str  = servicebus_conn_str,
        input_queue_name     = input_queue_name,
        output_queue_name    = output_queue_name,
        dlq_queue_name       = dlq_queue_name
    )

    brokerClient.listenForNewMessages()


if __name__ == "__main__":
    main()
